#!/usr/bin/python3

import socket

def banner(ip_addr, port):
    s= socket.socket()



    s.connect((ip_addr, int(port)))

    print(s.recv(1024))

def main():
    ip_addr = input("Enter IP address to grab (default localhost): ")
    if ip_addr == '':
        hostname = socket.gethostname()
        ip_addr = socket.gethostbyname(hostname)
    port = input("Enter port to grab (default ??): ")

    print("IP entered: ", ip_addr)

    banner(ip_addr, port)

main()



