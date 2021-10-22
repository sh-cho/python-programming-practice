import socket

BUF_SIZE = 64
PORT = 11111
SERVER_HOST = socket.gethostbyname("localhost")
ADDR = (SERVER_HOST, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"


def send(msg: str, sock: socket.socket):
    message = msg.encode(FORMAT)
    message_sz = len(message)
    padded = str(message_sz).ljust(BUF_SIZE, " ").encode(FORMAT)

    sock.send(padded)
    sock.send(message)


if __name__ == "__main__":
    sock = socket.socket(
        family=socket.AF_INET,
        type=socket.SOCK_STREAM,
    )
    sock.connect(ADDR)
    send("hello world!", sock)
