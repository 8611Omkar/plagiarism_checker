from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><body><h1>GET request received</h1></body></html>")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # Get the size of the POST data
        post_data = self.rfile.read(content_length)  # Read the POST data

        # Log or process the POST data
        print("Received POST data:", post_data.decode('utf-8'))

        # Respond to the client
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"status": "success", "message": "POST request received"}')

# Create an HTTPS server
httpd = HTTPServer(('localhost', 4443), MyHTTPRequestHandler)

# Configure SSL
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)

print("Serving on https://localhost:4443")
httpd.serve_forever()
