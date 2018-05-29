# -*- coding: utf-8 -*-
# @Time    : 2018/5/29 21:33
# @Author  : play4fun
# @File    : echoserver.py
# @Software: PyCharm

"""
echoserver.py:
"""

# Echo server program
import socket, ssl

HOST = 'localhost'  # Symbolic name meaning all available interfaces
PORT = 9980  # Arbitrary non-privileged port

context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.load_cert_chain(certfile="mycertfile.pem", keyfile="mykeyfile.pem")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
try:
    while True:
        conn, addr = s.accept()
        print('Connected by', conn, addr)

        ssl_conn = context.wrap_socket(conn, server_side=True)
        try:
            while True:
                data = ssl_conn.recv(1024)
                print("recv data: ", repr(data))
                if not data: break
                ssl_conn.sendall(data)
        finally:
            ssl_conn.close()
finally:
    s.close()
