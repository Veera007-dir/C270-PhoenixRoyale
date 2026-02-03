import requests

# Use your live Render URL
BASE_URL = "https://c270-phoenixroyale-devops.onrender.com"

# Test home page
def test_home_page():
    response = requests.get(BASE_URL + "/")
    assert response.status_code == 200
    assert "html" in response.text.lower()  # basic check for HTML content

# Test login page
def test_login_page():
    response = requests.get(BASE_URL + "/login")
    assert response.status_code == 200
    assert "login" in response.text.lower()

# Test register page
def test_register_page():
    response = requests.get(BASE_URL + "/register")
    assert response.status_code == 200
    assert "register" in response.text.lower()

# Test a route that requires authentication
def test_browsing_requires_login():
    response = requests.get(BASE_URL + "/browsing", allow_redirects=False)
    # Hosted server redirects unauthenticated users to login
    assert response.status_code == 302
    assert "/login" in response.headers["Location"]

# Test non-existent movie (without login)
def test_invalid_movie_redirects_to_login():
    response = requests.get(BASE_URL + "/movie/999999", allow_redirects=False)
    # Should redirect to login because we're not authenticated
    assert response.status_code == 302
    assert "/login" in response.headers["Location"]

# Test health endpoint
def test_health_endpoint():
    response = requests.get(BASE_URL + "/health")
    assert response.status_code == 200
    assert "ok" in response.text.lower()
