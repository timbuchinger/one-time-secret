"""
This file (test_secrets.py) contains the functional tests for the `secrets` blueprint.

These tests use GETs and POSTs to different URLs to check for the proper behavior
of the `secrets` blueprint.
"""


def test_home_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Securely create a one-time secret" in response.data


def test_home_page_post(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is is posted to (POST)
    THEN check that a '405' status code is returned
    """
    response = test_client.post('/')
    assert response.status_code == 405
    assert b"Securely create a one-time secret" not in response.data


def test_delete_expired(test_client):
    """
    GIVEN
    WHEN
    THEN
    """
    response = test_client.delete('/cleanup')
    assert response.status_code == 204
    # TODO: Add assertions
