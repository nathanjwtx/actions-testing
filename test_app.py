import json

import pytest
from app import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_env_variable_prints_develop(client):
    resp = client.get("/")

    assert json.loads(resp.data) == "develop"


def test_env_variable_prints_docker(client):
    resp = client.get("/")

    assert json.loads(resp.data) == "docker"


def test_env_variable_prints_github_action(client):
    resp = client.get("/")

    assert json.loads(resp.data) == "github-action"