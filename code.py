from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse

def add(a, b):
    print("Shresty")
    return a + b

class AdditionHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        query_params = urlparse.parse_qs(parsed_path.query)

        try:
            a = int(query_params.get('a', [None])[0])
            b = int(query_params.get('b', [None])[0])
            
            if a is None or b is None:
                raise ValueError("Parameters 'a' and 'b' must be provided")

            result = add(a, b)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(str(result).encode())
        except (ValueError, TypeError):
            self.send_response(400)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Parameters 'a' and 'b' must be integers")

def run(server_class=HTTPServer, handler_class=AdditionHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server listening on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()




