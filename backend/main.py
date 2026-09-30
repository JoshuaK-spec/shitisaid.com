"""Backend API for shitisaid.com.

Talks to the PostgreSQL database and serves JSON to the frontend.
"""

import os
from typing import TypedDict

import psycopg
from flask import Flask
from psycopg.rows import TupleRow

app = Flask(__name__)


def get_db() -> psycopg.Connection[TupleRow]:
    """Open a new connection to the PostgreSQL database.

    Returns:
        An open connection. Use it in a `with` block so it is closed
        automatically.

    Raises:
        KeyError: If .env variables are not set.
        psycopg.OperationalError: If the database cannot be reached.
    """
    return psycopg.connect(
        host=os.environ.get("POSTGRES_HOST", "db"),
        port=os.environ.get("POSTGRES_PORT", "5432"),
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
        dbname=os.environ["POSTGRES_DB"],
    )


class StandardResponse(TypedDict):
    """Standard JSON body returned."""

    message: str


### ROUTING
@app.route("/health", methods=["GET"])
def health() -> tuple[StandardResponse, int]:
    """Check that the API is running and can reach the database.

    Returns:
        A status message and either HTTP code:
        200 if the database responds or
        503 if it cannot be reached.
    """
    try:
        with get_db() as conn, conn.cursor() as cur:
            cur.execute("SELECT 1")

        return {"message": "the database is online!"}, 200
    except psycopg.OperationalError:
        app.logger.exception("db health check failed")
        return {"message": "the database is unreachable"}, 503


@app.route("/login", methods=["POST"])
def login() -> tuple[StandardResponse, int]:
    """The login endpoint, will be used later."""
    return {"message": "this is the placeholder login endpoint"}, 501


@app.route("/register", methods=["POST"])
def register() -> tuple[StandardResponse, int]:
    """The register endpoint, may be used later."""
    return {"message": "this is the placeholder register endpoint"}, 501


### =================== REFERENCES ===================
# https://flask.palletsprojects.com/en/stable/quickstart/#apis-with-json
# https://www.psycopg.org/psycopg3/docs/basic/usage.html
# https://docs.python.org/3/library/typing.html#typing.TypedDict
# https://peps.python.org/pep-0257/
# https://google.github.io/styleguide/pyguide.html

### =================== AUTHOR ===================
# Luke Mitchell, 2026
