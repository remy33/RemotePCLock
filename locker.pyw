# Simple http server that lock PC on api call
from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess
from socketserver import ThreadingMixIn


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # add route for heartbeat
        if self.path == "/lock":
            subprocess.run("Rundll32.exe user32.dll,LockWorkStation", shell=True)
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"locked!")

        elif self.path == "/heartbeat":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_error(404, "Not Found")


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""


def run(server_class=ThreadedHTTPServer, handler_class=MyHandler):
    server_address = ("", 55443)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
