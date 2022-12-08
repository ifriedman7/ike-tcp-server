#!/usr/bin/python3

import nmap, socket

scanner = nmap.PortScanner()

print("Welcome. This is nmap automation tool.")

ip_addr = input("Enter IP address to scan (default localhost): ")
if ip_addr == '':
    ip_addr = socket.gethostname()
print("IP entered: ", ip_addr)
type(ip_addr)

resp = input(""" \nEnter scan type:
                1) SYN ACK scan
                2) UDP scan
                3) Comprehensive scan""")
print("Option selected: ", resp)

if resp == '1':
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-3000', '--privileged -v -sS')
    print(scanner.scaninfo())
    print("IP state: ", scanner[ip_addr].state)
    print(scanner[ip_addr].all_protocols())
    print("Open ports: ", scanner[ip_addr]['tcp'].keys())
