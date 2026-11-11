"""Students REST API built with Flask.

The students are kept in memory in a ``StudentStore``. Every application
created by ``create_app()`` has its own store.
"""

import copy
import os
from datetime import datetime, timezone
from http import HTTPStatus

from flask import Blueprint, Flask, current_app, json, request, url_for
from werkzeug.exceptions import HTTPException

API_PREFIX = "/api/v1.0"
STORE_KEY = "student_store"
DEFAULT_PORT = 5000
MIN_PORT = 1
MAX_PORT = 65535
MIN_BIRTHYEAR = 1900
TEXT_FIELDS = ("name", "country", "city")
REQUIRED_FIELDS = (*TEXT_FIELDS, "birthyear", "skills")
ALLOWED_FIELDS = (*REQUIRED_FIELDS, "bio")
READ_ONLY_FIELDS = ("id", "created_at", "updated_at")

DEFAULT_STUDENTS = [
    {
        "name": "Anna",
        "country": "Finland",
        "city": "Helsinki",
        "birthyear": 1985,
        "skills": ["HTML", "CSS", "JavaScript", "Python"],
        "bio": "Loves automating boring tasks.",
    },
    {
        "name": "David",
        "country": "UK",
        "city": "London",
        "birthyear": 1990,
        "skills": ["Python", "MongoDB"],
        "bio": "Builds data pipelines.",
    },
    {
        "name": "John",
        "country": "Sweden",
        "city": "Stockholm",
        "birthyear": 1995,
        "skills": ["Java", "C#"],
        "bio": "Writes backend services.",
    },
]

api = Blueprint("api", __name__, url_prefix=API_PREFIX)


class ValidationError(ValueError):
    """Raised when student data or a request parameter is invalid."""


class StudentNotFoundError(LookupError):
    """Raised when there is no student with the requested id.

    Attributes:
        student_id: The id that was not found.
    """

    def __init__(self, student_id):
        """Build the error message from the missing id.

        Args:
            student_id: The id that was not found.
        """
        super().__init__(f"Student {student_id} not found")
        self.student_id = student_id


def _clean_text(field, value):
    """Return a stripped non-empty string or raise ValidationError."""
    if not isinstance(value, str) or not value.strip():
        raise ValidationError(
            f"'{field}' must be a non-empty string, got {value!r}"
        )
    return value.strip()


def _clean_birthyear(value):
    """Return a valid birth year or raise ValidationError."""
    current_year = datetime.now(timezone.utc).year
    if (
        isinstance(value, bool)
        or not isinstance(value, int)
        or not MIN_BIRTHYEAR <= value <= current_year
    ):
        raise ValidationError(
            f"'birthyear' must be an integer between {MIN_BIRTHYEAR} "
            f"and {current_year}, got {value!r}"
        )
    return value


def _clean_skills(value):
    """Return stripped skills without case-insensitive duplicates."""
    if not isinstance(value, list):
        raise ValidationError(f"'skills' must be a list, got {value!r}")
    skills = []
    seen = set()
    for skill in value:
        if not isinstance(skill, str) or not skill.strip():
            raise ValidationError(
                f"'skills' must contain non-empty strings, got {skill!r}"
            )
        skill = skill.strip()
        if skill.casefold() not in seen:
            seen.add(skill.casefold())
            skills.append(skill)
    return skills


def _clean_bio(value):
    """Return a stripped bio or raise ValidationError."""
    if not isinstance(value, str):
        raise ValidationError(f"'bio' must be a string, got {value!r}")
    return value.strip()


def _clean_field(field, value):
    """Validate and clean the value of one known field."""
    if field in TEXT_FIELDS:
        return _clean_text(field, value)
    if field == "birthyear":
        return _clean_birthyear(value)
    if field == "skills":
        return _clean_skills(value)
    return _clean_bio(value)


def validate_student(data, partial=False):
    """Validate student data and return a new, cleaned dict.

    Args:
        data: Untrusted student data, normally a parsed JSON body.
        partial: If True, missing fields are allowed (``PATCH``), but the
            data must contain at least one field and ``bio`` gets no
            default.

    Returns:
        A new dict with stripped strings and de-duplicated skills. The
        input is not changed.

    Raises:
        ValidationError: If ``data`` is not a dict, is empty in partial
            mode, has unknown or missing fields, or a field is invalid.
    """
    if not isinstance(data, dict):
        received = "no valid JSON" if data is None else type(data).__name__
        raise ValidationError(
            f"student data must be a JSON object, got {received}"
        )
    unknown = sorted(set(data) - set(ALLOWED_FIELDS))
    if unknown:
        raise ValidationError(f"unknown field(s): {', '.join(unknown)}")
    if partial and not data:
        raise ValidationError("student data must contain at least one field")
    missing = [field for field in REQUIRED_FIELDS if field not in data]
    if missing and not partial:
        raise ValidationError(
            f"missing required field(s): {', '.join(missing)}"
        )
    cleaned = {
        field: _clean_field(field, value) for field, value in data.items()
    }
    if not partial:
        cleaned.setdefault("bio", "")
    return cleaned


def _utc_now():
    """Return the current UTC time in ISO format with seconds."""
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


class StudentStore:
    """In-memory storage of students that knows nothing about HTTP.

    Every method returns copies, so changing a returned dict does not
    change the stored data. Ids start at 1 and are never reused.
    """

    def __init__(self, students=None):
        """Create a store and add the given students.

        Args:
            students: Optional iterable of already valid student dicts.

        Raises:
            TypeError: If ``students`` is not iterable.
        """
        try:
            initial_students = iter([] if students is None else students)
        except TypeError as error:
            raise TypeError(
                "students must be an iterable of dicts, "
                f"got {type(students).__name__}"
            ) from error
        self._students = {}
        self._next_id = 1
        for student in initial_students:
            self.add(student)

    def __len__(self):
        """Return the number of stored students.

        Returns:
            The number of students.
        """
        return len(self._students)

    def _find(self, student_id):
        """Return the stored student or raise StudentNotFoundError."""
        if student_id not in self._students:
            raise StudentNotFoundError(student_id)
        return self._students[student_id]

    def add(self, data):
        """Store a new student with the next id and timestamps.

        Args:
            data: Valid student data.

        Returns:
            A copy of the stored student.
        """
        now = _utc_now()
        student = {
            "id": self._next_id,
            **copy.deepcopy(data),
            "created_at": now,
            "updated_at": now,
        }
        self._students[self._next_id] = student
        self._next_id += 1
        return copy.deepcopy(student)

    def get(self, student_id):
        """Return one student.

        Args:
            student_id: Id of the student.

        Returns:
            A copy of the student.

        Raises:
            StudentNotFoundError: If there is no student with this id.
        """
        return copy.deepcopy(self._find(student_id))

    def list(self, country=None, skill=None):
        """Return the students sorted by id, optionally filtered.

        Ids only grow, so the insertion order of the store is the id
        order. Both filters are case-insensitive exact matches.

        Args:
            country: Keep only students from this country.
            skill: Keep only students with this skill.

        Returns:
            A list of student copies.
        """
        return [
            copy.deepcopy(student)
            for student in self._students.values()
            if _matches(student, country, skill)
        ]

    def update(self, student_id, data, partial=False):
        """Replace or merge the data of a student.

        ``id`` and ``created_at`` never change, ``updated_at`` is
        refreshed.

        Args:
            student_id: Id of the student.
            data: Valid student data.
            partial: If True, merge ``data`` into the stored student
                (``PATCH``). Otherwise replace it (``PUT``).

        Returns:
            A copy of the updated student.

        Raises:
            StudentNotFoundError: If there is no student with this id.
            ValueError: If ``data`` contains ``id``, ``created_at`` or
                ``updated_at``. The store is not changed.
        """
        current = self._find(student_id)
        read_only = sorted(set(data) & set(READ_ONLY_FIELDS))
        if read_only:
            raise ValueError(
                f"cannot change read-only field(s): {', '.join(read_only)}"
            )
        kept = {}
        if partial:
            kept = {
                field: value
                for field, value in current.items()
                if field not in READ_ONLY_FIELDS
            }
        self._students[student_id] = {
            "id": student_id,
            **kept,
            **copy.deepcopy(data),
            "created_at": current["created_at"],
            "updated_at": _utc_now(),
        }
        return copy.deepcopy(self._students[student_id])

    def delete(self, student_id):
        """Remove a student.

        Args:
            student_id: Id of the student.

        Raises:
            StudentNotFoundError: If there is no student with this id.
        """
        self._find(student_id)
        del self._students[student_id]


def _matches(student, country, skill):
    """Check a student against the optional country and skill filters."""
    if country is not None and (
        student["country"].casefold() != country.casefold()
    ):
        return False
    return skill is None or skill.casefold() in {
        known.casefold() for known in student["skills"]
    }


def _store():
    """Return the student store of the current application."""
    return current_app.extensions[STORE_KEY]


def _read_filter(name):
    """Return a stripped query filter, or None when it is not set.

    Raises:
        ValidationError: If the filter contains only spaces.
    """
    value = request.args.get(name, "")
    if not value:
        return None
    if not value.strip():
        raise ValidationError(f"'{name}' filter must not be blank")
    return value.strip()


@api.get("/health")
def health():
    """Report that the service is running.

    Returns:
        ``{"status": "ok"}``.
    """
    return {"status": "ok"}


@api.get("/students")
def list_students():
    """Return the students, filtered by ``country`` and ``skill``.

    Returns:
        A JSON list of students.

    Raises:
        ValidationError: If a filter contains only spaces.
    """
    return _store().list(
        country=_read_filter("country"), skill=_read_filter("skill")
    )


@api.get("/students/<int:student_id>")
def get_student(student_id):
    """Return one student.

    Args:
        student_id: Id from the URL.

    Returns:
        The student as JSON.

    Raises:
        StudentNotFoundError: If there is no student with this id.
    """
    return _store().get(student_id)


@api.post("/students")
def create_student():
    """Create a student from the JSON body.

    Returns:
        The created student, status 201 and a ``Location`` header.

    Raises:
        ValidationError: If the JSON body is invalid.
    """
    student = _store().add(validate_student(request.get_json(silent=True)))
    location = url_for(".get_student", student_id=student["id"])
    return student, HTTPStatus.CREATED, {"Location": location}


@api.put("/students/<int:student_id>")
def replace_student(student_id):
    """Replace all data of a student with the JSON body.

    Args:
        student_id: Id from the URL.

    Returns:
        The updated student as JSON.

    Raises:
        ValidationError: If the JSON body is invalid.
        StudentNotFoundError: If there is no student with this id.
    """
    data = validate_student(request.get_json(silent=True))
    return _store().update(student_id, data)


@api.patch("/students/<int:student_id>")
def patch_student(student_id):
    """Change only the fields given in the JSON body.

    Args:
        student_id: Id from the URL.

    Returns:
        The updated student as JSON.

    Raises:
        ValidationError: If the JSON body is invalid.
        StudentNotFoundError: If there is no student with this id.
    """
    data = validate_student(request.get_json(silent=True), partial=True)
    return _store().update(student_id, data, partial=True)


@api.delete("/students/<int:student_id>")
def delete_student(student_id):
    """Delete a student.

    Args:
        student_id: Id from the URL.

    Returns:
        An empty body with status 204.

    Raises:
        StudentNotFoundError: If there is no student with this id.
    """
    _store().delete(student_id)
    return "", HTTPStatus.NO_CONTENT


def _error_response(error, status):
    """Return the JSON body and status of an API error."""
    return {"error": str(error)}, status


def _handle_validation_error(error):
    """Convert ValidationError to a 400 JSON response."""
    return _error_response(error, HTTPStatus.BAD_REQUEST)


def _handle_not_found_error(error):
    """Convert StudentNotFoundError to a 404 JSON response."""
    return _error_response(error, HTTPStatus.NOT_FOUND)


def _handle_http_error(error):
    """Convert a Werkzeug HTTP error to JSON and keep its headers."""
    response = error.get_response()
    response.data = json.dumps({"error": error.description})
    response.content_type = "application/json"
    return response


def create_app(config=None):
    """Create a Flask application with its own student store.

    Args:
        config: Optional dict that is applied to ``app.config`` after the
            defaults, e.g. ``{"SEED_DATA": []}``.

    Returns:
        The configured Flask application.

    Raises:
        TypeError: If ``config`` is not a dict.
    """
    if config is not None and not isinstance(config, dict):
        raise TypeError(f"config must be a dict, got {type(config).__name__}")
    app = Flask(__name__)
    app.config["SEED_DATA"] = DEFAULT_STUDENTS
    app.config.update(config or {})
    app.extensions[STORE_KEY] = StudentStore(app.config["SEED_DATA"])
    app.register_blueprint(api)
    app.register_error_handler(ValidationError, _handle_validation_error)
    app.register_error_handler(StudentNotFoundError, _handle_not_found_error)
    app.register_error_handler(HTTPException, _handle_http_error)
    return app


def read_port():
    """Read the server port from the ``PORT`` environment variable.

    Returns:
        The port number, ``DEFAULT_PORT`` when ``PORT`` is not set.

    Raises:
        ValueError: If ``PORT`` is not an integer or is out of range.
    """
    raw_port = os.environ.get("PORT", str(DEFAULT_PORT))
    try:
        port = int(raw_port)
    except ValueError as error:
        raise ValueError(
            f"PORT must be an integer, got {raw_port!r}"
        ) from error
    if not MIN_PORT <= port <= MAX_PORT:
        raise ValueError(
            f"PORT must be between {MIN_PORT} and {MAX_PORT}, got {port}"
        )
    return port


def main():
    """Run the development server on the port from ``PORT``."""
    try:
        port = read_port()
    except ValueError as error:
        print(f"{error}. Using the default port {DEFAULT_PORT}.")
        port = DEFAULT_PORT
    create_app().run(port=port)


if __name__ == "__main__":
    main()
