"""
1. Identifying the PLCs that are connected to the internet 
2. And then using port scanning techniques to find open ports on the PLCs. 
3. Once an open port is found 
4. Print the port numbers as a output
"""

import socket
import sys
import os
import time
import threading
import subprocess
import re

# Global variables
global_ip_list = []
global_port_list = []
global_port_list_lock = threading.Lock()
global_ip_list_lock = threading.Lock()

# Function to get the IP address of the system
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

# Function to get the subnet mask of the system
def get_subnet_mask():
    ip_address = get_ip_address()
    subnet_mask = subprocess.check_output(["ifconfig", "en0"])
    subnet_mask = subnet_mask.decode("utf-8")
    subnet_mask = re.findall(r'netmask (.*?) ', subnet_mask)
    subnet_mask = subnet_mask[0]
    return subnet_mask

# Function to get the network address of the system
def get_network_address():
    ip_address = get_ip_address()
    subnet_mask = get_subnet_mask()
    network_address = socket.inet_ntoa(
        socket.inet_aton(ip_address) & socket.inet_aton(subnet_mask))
    return network_address

# Function to get the broadcast address of the system
def get_broadcast_address():
    ip_address = get_ip_address()
    subnet_mask = get_subnet_mask()
    broadcast_address = socket.inet_ntoa(
        socket.inet_aton(ip_address) | ~socket.inet_aton(subnet_mask))
    return broadcast_address

# Function to get the IP address range of the system
def get_ip_address_range():
    network_address = get_network_address()
    broadcast_address = get_broadcast_address()
    ip_address_range = network_address + "-" + broadcast_address
    return ip_address_range

# Function to get the IP address list of the system
def get_ip_address_list():
    ip_address_range = get_ip_address_range()
    ip_address_list = ip_address_range.split("-")
    ip_address_list = ip_address_list[0].split(".")
    ip_address_list[3] = str(int(ip_address_list[3]) + 1)
    ip_address_list = ".".join(ip_address_list)
    ip_address_list = ip_address_list + "-" + ip_address_range.split("-")[1]
    return ip_address_list

# Function to get the IP address list of the system
def get_ip_address_list_from_range(ip_address_range):
    ip_address_list = ip_address_range.split("-")
    ip_address_list = ip_address_list[0].split(".")
    ip_address_list[3] = str(int(ip_address_list[3]) + 1)
    ip_address_list = ".".join(ip_address_list)
    ip_address_list = ip_address_list + "-" + ip_address_range.split("-")[1]
    return ip_address_list

# Function to get the IP address list of the system
def get_ip_address_list_from_file(file_name):
    ip_address_list = []
    with open(file_name, "r") as file:
        for line in file:
            ip_address_list.append(line.strip())
    return ip_address_list

# Function to get the IP address list of the system
def get_ip_address_list_from_ip_address(ip_address):
    ip_address_list = []
    ip_address_list.append(ip_address)
    return ip_address_list

# Function to get the IP address list of the system
def get_ip_address_list_from_ip_address_range(ip_address_range):
    ip_address_list = []
    ip_address_list.append(ip_address_range)
    return ip_address_list

# Function to get the IP address list of the system
def get_ip_address_list_from_ip_address_list(ip_address_list):
    return ip_address_list

# Function to get the IP address list of the system
def get_ip_address_list_from_ip_address_list_file(file_name):
    ip_address_list = []
    with open(file_name, "r") as file:
        for line in file:
            ip_address_list.append(line.strip())
    return ip_address_list

