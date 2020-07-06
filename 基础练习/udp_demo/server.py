import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(("127.0.0.1", 9001))

# msg = sk.recv(1024)
msg, addr = sk.recvfrom(1024)
print(msg)
# sk.sendto(b"aaa",addr)
sk.sendto("哈哈".encode("utf-8"), addr)
