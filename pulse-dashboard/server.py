"""Pulse Dashboard - a tiny sales dashboard with zero dependencies.

Run:  python3 server.py
Then open http://localhost:8000

Workshop note: routing, JSON handling and HTML rendering are all mixed
together in this file on purpose. There are no filters, no tests for the
API layer, and errors are not handled. Plenty to improve.
"""

import json
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

from app.data_loader import summary

PORT = 8000
STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")


class DashboardHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=STATIC_DIR, **kwargs)

    def do_GET(self):
        if self.path == "/api/summary":
            data = summary()
            body = json.dumps(data).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        if self.path == "/":
            self.path = "/index.html"

        return super().do_GET()

    def log_message(self, fmt, *args):
        print("[pulse] " + fmt % args)


def main():
    server = HTTPServer(("127.0.0.1", PORT), DashboardHandler)
    print("Pulse Dashboard running on http://localhost:%d" % PORT)
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
