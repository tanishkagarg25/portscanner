#!/usr/bin/python3
import nmap
scanner=nmap.PortScanner()
print("welcome, this is a simple nmap automation tool")
print("<------------------------------------->")
ip_addr=input("please enter the IP address you want to scan:")
print("the IP you entered is:",ip_addr)
type(ip_addr)



resp = input("""\nPlease enter the type of scan you want to run
                1)SYN ACK Scan
                2)UDP scan
                3)comprehensive scan\n""")
print("you have selected option:",resp)


if resp == '1':
    
    for i in range(45,55):
	    res= scanner.scan(ip_addr,str(i))
	    res= res['scan'][ip_addr]['tcp'][i]['state']
	    print(f'port {i} is {res}.')
    for i in range(440,450):
	    res= scanner.scan(ip_addr,str(i))
	    res= res['scan'][ip_addr]['tcp'][i]['state']
	    print(f'port {i} is {res}.')
    




elif resp== '2':

    # print("Nmap version: ",scanner.nmap_version())
    # scanner.scan(ip_addr,'20-30','-v -sU')#range of ports we want to scan
    # print(scanner.scaninfo())
    # print("IP status: ",scanner[ip_addr].state())
    # print(scanner[ip_addr].all_protocols())
    # print("open ports",scanner[ip_addr]['udp'].keys())#keys will display all the open ports
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    # state() tells if target is up or down
    print("Ip Status: ", scanner[ip_addr].state())
    # all_protocols() tells which protocols are enabled like TCP UDP etc
    print("protocols:",scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())


elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    # sS for SYN scan, sv probe open ports to determine what service and version they are running on
    # O determine OS type, A tells Nmap to make an effort in identifying the target OS
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
    
# initialize the port scanner




    
# elif resp >='4':
#     print("please enter the valid option")