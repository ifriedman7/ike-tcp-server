#!/usr/bin/python3

import nmap, socket

scanner = nmap.PortScanner()

print("Welcome. This is nmap automation tool.")

ip_addr = input("Enter IP address to scan (default localhost): ")
if ip_addr == '':
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)

print("IP entered: ", ip_addr)
type(ip_addr)

resp = input(""" \nEnter scan type:
                1) SYN ACK scan
                2) UDP scan
                3) Comprehensive scan\n""")
print("Option selected: ", resp)

if resp == '1':
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-3000', '--privileged -v -sS')
    print("scaninfo: \n", scanner.scaninfo())
    print("IP state: ", scanner[ip_addr].state)
    print("All protocols: ", scanner[ip_addr].all_protocols())
    print("Open ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':    
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-3000', '--privileged -v -sU')
    print("scaninfo: \n", scanner.scaninfo())
    print("IP state: ", scanner[ip_addr].state)
    print("All protocols: ", scanner[ip_addr].all_protocols())
    print("Open ports: ", scanner[ip_addr]['udp'].keys()) 
elif resp == '3':    
    print("Nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-3000', '--privileged -v -sS -sV -sC -A -O')
    print("scaninfo: \n", scanner.scaninfo())
    print("IP state: ", scanner[ip_addr].state)
    print("All protocols: ", scanner[ip_addr].all_protocols())
    print("Open ports: ", scanner[ip_addr]['udp'].keys()) 