import socket

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
body = "Hello, world! <h1> from zzz </h1>"
response_params = [
    'HTTP/1.0 200 OK',
    'Date: THUR',
    'Content-Type: text',
    'Content-Length: {}\r\n'.format(len(body.encode())),
    body
]
response = '\r\n'.join(response_params)


def handle_connection(conn, addr):
    print(conn, addr)
    import time
    time.sleep(100)

    request = b""
    while EOL1 not in request and EOL2 not in request:
        request += conn.recv(1024)
    print(request)
    conn.send(response.encode())
    conn.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', 8000))
    server_socket.listen(5)
    print('http://127.0.0.1:8000')

    try:
        while True:
            conn, address = server_socket.accept()
            handle_connection(conn, address)
    finally:
        server_socket.close()


if __name__ == '__main__':
    main()