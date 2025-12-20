# Simple web app with security headers - protects against common attacks!
# To run: Use a WSGI server like gunicorn: uv run gunicorn secure_wsgi_app:app

from secure import Secure

secure_headers = Secure()


def app(environ, start_response):
    status = "200 OK"
    headers = [("Content-type", "text/plain")]

    # Add security headers to the response
    # The Secure library automatically adds headers like:
    # - Strict-Transport-Security: Enforces HTTPS connections
    # - X-Content-Type-Options: Prevents MIME sniffing attacks
    # - X-Frame-Options: Prevents clickjacking attacks
    # - Content-Security-Policy: Prevents XSS and injection attacks
    # - Referrer-Policy: Controls referrer information
    # - Permissions-Policy: Controls browser features
    headers.extend(secure_headers.headers.items())

    start_response(status, headers)
    return [b"Welcome to the secure app!"]


if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    with make_server("", 8000, app) as httpd:
        print("Serving on port 8000...")
        httpd.serve_forever()
