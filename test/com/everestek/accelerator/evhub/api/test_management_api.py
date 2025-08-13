# coding: utf-8

from fastapi.testclient import TestClient




def test_get_version(client: TestClient):
    """Test case for get_version

    Get the current version of the API
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/version",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_health_check(client: TestClient):
    """Test case for health_check

    Check the health of the application
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/healthcheck",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

