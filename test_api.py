
import requests

BASE_URL = "http://127.0.0.1:8000"

# Test 1: GET /
response = requests.get(f"{BASE_URL}/", timeout=30)
print("TEST 1 - HOME")
print(response.status_code)
print(response.json())

# Test 2: GET /health
response = requests.get(f"{BASE_URL}/health", timeout=30)
print("\nTEST 2 - HEALTH")
print(response.status_code)
print(response.json())

# Test 3: POST /predict - Positive
response = requests.post(
    f"{BASE_URL}/predict",
    json={"text": "I love learning Python!"},
    timeout=60
)
print("\nTEST 3 - POSITIVE")
print(response.status_code)
print(response.json())

# Test 4: POST /predict - Negative
response = requests.post(
    f"{BASE_URL}/predict",
    json={"text": "This movie is terrible!"},
    timeout=60
)
print("\nTEST 4 - NEGATIVE")
print(response.status_code)
print(response.json())

# Test 5: POST /predict - Empty text
response = requests.post(
    f"{BASE_URL}/predict",
    json={"text": ""},
    timeout=30
)
print("\nTEST 5 - EMPTY TEXT")
print(response.status_code)
print(response.json())

# Test 6: POST /predict - Missing text
response = requests.post(
    f"{BASE_URL}/predict",
    json={},
    timeout=30
)
print("\nTEST 6 - MISSING TEXT")
print(response.status_code)
print(response.json())
