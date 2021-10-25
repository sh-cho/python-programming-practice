import socket
import threading

BUF_SIZE = 64
PORT = 11111
SERVER_HOST = socket.gethostbyname("localhost")
ADDR = (SERVER_HOST, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"


def handle_client(conn: socket.socket, addr):
    print(f"[New Connection] {addr} connected.")

    connected = True
    while connected:
        tmp = conn.recv(BUF_SIZE).decode(FORMAT)
        if not tmp:
            continue

        msg_length = int(tmp)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            connected = False

        print(f"[{addr}] {msg}")

    conn.close()


def main():
    sock = socket.socket(
        family=socket.AF_INET,
        type=socket.SOCK_STREAM,
    )
    sock.bind(ADDR)
    sock.listen()
    print(f"Server is listening on {SERVER_HOST}:{PORT}")
    while True:
        conn, addr = sock.accept()
        t = threading.Thread(
            target=handle_client,
            args=(conn, addr),
        )
        t.start()

        print(f"[Active Connections] {threading.active_count() - 1}")


if __name__ == "__main__":
    main()
