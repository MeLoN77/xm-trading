import os


def get_test_environment_urls():
    """
    Fundtion is defining where test is running OS or Docker
    :return:
    """
    if os.path.exists('/.dockerenv'):
        base_url = "http://api:8000"
        web_socket_uri = "ws://api:8000/ws"
    else:
        base_url = "http://localhost:8000"
        web_socket_uri = "ws://localhost:8000/ws"

    return base_url, web_socket_uri


BASE_URL, WEB_SOCKET_URI = get_test_environment_urls()
