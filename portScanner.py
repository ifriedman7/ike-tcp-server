#!/usr/bin/python3

#Can use hackthissite.org for testing

import socket

def main():
    
    hostname = input("Enter host name to scan (default localhost): ")
    if hostname == '':
        hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    port = input("Enter port to scan (default 443): ")
    if port == '':
        port = 443
    print("IP entered: ", ip_addr)

    portScan(ip_addr, int(port))

def portScan(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    if s.connect_ex((host,port)):
        print("The port ", str(port), "is closed.")
    else:
        print("The port ", str(port), "is open.")

main()
