def scan_ports(ip, port_list):
    """
    scan a list of ports on a given ip address
    :param ip: ip address to scan
    :param port_list: list of ports to scan
    :return: list of open ports
    """
    open_ports = []
    for port in port_list:
        if port_scan(ip, port):
            open_ports.append(port)
    return open_ports


def port_scan(ip, port):
    """
    scan a single port on a given ip address
    :param ip: ip address to scan
    :param port: port to scan
    :return: True if port is open, False if port is closed
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((ip, port))
    if result == 0:
        return True
    else:
        return False