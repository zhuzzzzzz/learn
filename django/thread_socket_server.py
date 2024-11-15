import errno
import socket
import threading
import time

from setuptools.config.setupcfg import Target

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
body = "Hello, world! <h1> from zzz </h1> -from {thread_name}"
response_params = [
    'HTTP/1.0 200 OK',
    'Date: THUR',
    'Content-Type: text',
    'Content-Length: {length}\r\n',
    body
]
response = '\r\n'.join(response_params)


def handle_connection(conn, addr):
    print(conn, addr)
    import time
    time.sleep(20)

    request = b""
    while EOL1 not in request and EOL2 not in request:
        request += conn.recv(1024)
    print(request)
    current_thread = threading.current_thread()
    current_length = len(body.format(thread_name=current_thread.name).encode())
    print(current_thread.name)

    conn.send(response.format(thread_name=current_thread.name, length=current_length).encode())
    conn.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', 8000))
    server_socket.listen(5)
    print('http://127.0.0.1:8000')
    server_socket.setblocking(0)

    try:
        i=0
        while True:
            try:
                conn, address = server_socket.accept()
            except socket.error as e:
                if e.args[0] != errno.EAGAIN:
                    raise
                continue
            i += 1
            print(i)
            t = threading.Thread(target=handle_connection, args=(conn, address), name='thread-%s' % i)
            t.start()
    finally:
        server_socket.close()


if __name__ == '__main__':
    main()