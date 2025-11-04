# Simple web app with security headers - protects against common attacks!
# To run: Use a WSGI server like gunicorn: uv run gunicorn secure_wsgi_app:app

from secure import Secure

secure_headers = Secure()


def app(environ, start_response):
    status = "200 OK"
    headers = [("Content-type", "text/plain")]
    headers.extend(
        secure_headers.headers.items()
    )  # Add security headers to the response
    start_response(status, headers)
    return [b"Welcome to the secure app!"]


if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    with make_server("", 8000, app) as httpd:
        print("Serving on port 8000...")
        httpd.serve_forever()
