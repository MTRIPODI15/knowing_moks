import responses  # Library to mock HTTP requests
import requests   # Used to send HTTP requests

# Base URL of the simulated banking API
BASE_URL = "https://api.mockbank.com"

# Test: Valid transfer between two accounts
@responses.activate
def test_valid_transfer():
    # We mock the POST request to /transfer with a successful response
    responses.add(
        responses.POST,
        f"{BASE_URL}/transfer",
        json={"status": "success", "message": "Transfer completed"},
        status=200
    )

    # Simulated payload for a valid transfer
    payload = {
        "from_account": "123456",
        "to_account": "654321",
        "amount": 100
    }

    # Send the request (it will be intercepted by responses)
    response = requests.post(f"{BASE_URL}/transfer", json=payload)

    # Assertions to validate the mocked response
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "Transfer completed" in response.json()["message"]

# Test: Transfer with insufficient balance
@responses.activate
def test_insufficient_balance():
    # Mocking a failed transfer due to low balance
    responses.add(
        responses.POST,
        f"{BASE_URL}/transfer",
        json={"status": "error", "message": "Insufficient balance"},
        status=400
    )

    # Payload with a very high amount to trigger the error
    payload = {
        "from_account": "123456",
        "to_account": "654321",
        "amount": 1000000
    }

    response = requests.post(f"{BASE_URL}/transfer", json=payload)

    # Assertions to check error handling
    assert response.status_code == 400
    assert response.json()["status"] == "error"
    assert "Insufficient balance" in response.json()["message"]

# Test: Transfer with invalid account number
@responses.activate
def test_invalid_account():
    # Mocking a failed transfer due to invalid account
    responses.add(
        responses.POST,
        f"{BASE_URL}/transfer",
        json={"status": "error", "message": "Invalid account number"},
        status=404
    )

    # Payload with a fake account number
    payload = {
        "from_account": "000000",
        "to_account": "654321",
        "amount": 50
    }

    response = requests.post(f"{BASE_URL}/transfer", json=payload)

    # Assertions to check error message and status
    assert response.status_code == 404
    assert response.json()["status"] == "error"
    assert "Invalid account number" in response.json()["message"]