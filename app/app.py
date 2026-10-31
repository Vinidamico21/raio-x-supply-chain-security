from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        response = {
            "application": "Supply Chain Security Lab",
            "status": "running",
            "message": "Aplicacao de demonstracao"
        }

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

server = HTTPServer(("0.0.0.0", 8080), Handler)

print("Aplicacao iniciada na porta 8080")

server.serve_forever()