"""
1. write a function to Identify the PLCs that are connected to the internet
"""

def identify_plc_connected_to_internet(plc_list):
    """
    This function identifies the PLCs that are connected to the internet
    :param plc_list:
    :return:
    """
    plc_connected_to_internet = []
    for plc in plc_list:
        if plc.is_connected_to_internet:
            plc_connected_to_internet.append(plc)
    return plc_connected_to_internet

"""
2. write a function to Identify the PLCs that are not connected to the internet
"""

def identify_plc_not_connected_to_internet(plc_list):
    """
    This function identifies the PLCs that are not connected to the internet
    :param plc_list:
    :return:
    """
    plc_not_connected_to_internet = []
    for plc in plc_list:
        if not plc.is_connected_to_internet:
            plc_not_connected_to_internet.append(plc)
    return plc_not_connected_to_internet

"""
3. write a function to Identify the PLCs that are connected to the internet and are in the same subnet
"""

def identify_plc_connected_to_internet_in_same_subnet(plc_list):
    """
    This function identifies the PLCs that are connected to the internet and are in the same subnet
    :param plc_list:
    :return:
    """
    plc_connected_to_internet_in_same_subnet = []
    for plc in plc_list:
        if plc.is_connected_to_internet and plc.is_in_same_subnet:
            plc_connected_to_internet_in_same_subnet.append(plc)
    return plc_connected_to_internet_in_same_subnet

"""
4. write a function to Identify the PLCs that are connected to the internet and are not in the same subnet
"""

def identify_plc_connected_to_internet_not_in_same_subnet(plc_list):
    """
    This function identifies the PLCs that are connected to the internet and are not in the same subnet
    :param plc_list:
    :return:
    """
    plc_connected_to_internet_not_in_same_subnet = []
    for plc in plc_list:
        if plc.is_connected_to_internet and not plc.is_in_same_subnet:
            plc_connected_to_internet_not_in_same_subnet.append(plc)
    return plc_connected_to_internet_not_in_same_subnet

"""
5. write a function to Identify the PLCs that are not connected to the internet and are in the same subnet
"""

def identify_plc_not_connected_to_internet_in_same_subnet(plc_list):
    """
    This function identifies the PLCs that are not connected to the internet and are in the same subnet
    :param plc_list:
    :return:
    """
    plc_not_connected_to_internet_in_same_subnet = []
    for plc in plc_list:
        if not plc.is_connected_to_internet and plc.is_in_same_subnet:
            plc_not_connected_to_internet_in_same_subnet.append(plc)
    return plc_not_connected_to_internet_in_same_subnet

"""
6. write a function to Identify the PLCs that are not connected to the internet and are not in the same subnet
"""

def identify_plc_not_connected_to_internet_not_in_same_subnet(plc_list):
    """
    This function identifies the PLCs that are not connected to the internet and are not in the same subnet
    :param plc_list:
    :return:
    """
    plc_not_connected_to_internet_not_in_same_subnet = []
    for plc in plc_list:
        if not plc.is_connected_to_internet and not plc.is_in_same_subnet:
            plc_not_connected_to_internet_not_in_same_subnet.append(plc)
    return plc_not_connected_to_internet_not_in_same_subnet

"""
7. write a function to Identify the PLCs that are connected to the internet and are in the same subnet and are in the same rack
"""

def identify_plc_connected_to_internet_in_same_subnet_in_same_rack(plc_list):
    """
    This function identifies the PLCs that are connected to the internet and are in the same subnet and are in the same rack
    :param plc_list:
    :return:
    """
    plc_connected_to_internet_in_same_subnet_in_same_rack = []
    for plc in plc_list:
        if plc.is_connected_to_internet and plc.is_in_same_subnet and plc.is_in_same_rack:
            plc_connected_to_internet_in_same_subnet_in_same_rack.append(plc)
    return plc_connected_to_internet_in_same_subnet_in_same_rack

"""
8. write a function to Identify the PLCs that are connected to the internet and are in the same subnet and are not in the same rack
"""

def identify_plc_connected_to_internet_in_same_subnet_not_in_same_rack(plc_list):
    """
    This function identifies the PLCs that are connected to the internet and are in the same subnet and are not in the same rack
    :param plc_list:
    :return:
    """
    plc_connected_to_internet_in_same_subnet_not_in_same_rack = []
    for plc in plc_list:
        if plc.is_connected_to_internet and plc.is_in_same_subnet and not plc.is_in_same_rack:
            plc_connected_to_internet_in_same_subnet_not_in_same_rack.append(plc)
    return plc_connected_to_internet_in_same_subnet_not_in_same_rack

"""
9. write a function to Identify the PLCs that are connected to the internet and are not in the same subnet and are in the same rack
"""

def identify_plc_connected_to_internet_not_in_same_subnet_in_same_rack(plc_list):
    """
    This function identifies the PLCs that are connected to the internet and are not in the same subnet and are in the same rack
    :param plc_list:
    :return:
    """
    plc_connected_to_internet_not_in_same_subnet_in_same_rack = []
    for plc in plc_list:
        if plc.is_connected_to_internet and not plc.is_in_same_subnet and plc.is_in_same_rack:
            plc_connected_to_internet_not_in_same_subnet_in_same_rack.append(plc)
    return plc_connected_to_internet_not_in_same_subnet_in_same_rack

"""
10. write a function to Identify the PLCs that are connected to the internet and are not in the same subnet and are not in the same rack
"""

def identify_plc_connected_to_internet_not_in_same_subnet_not_in_same_rack(plc_list):
    """
    This function identifies the PLCs that are connected to the internet and are not in the same subnet and are not in the same rack
    :param plc_list:
    :return:
    """
    plc_connected_to_internet_not_in_same_subnet_not_in_same_rack = []
    for plc in plc_list:
        if plc.is_connected_to_internet and not plc.is_in_same_subnet and not plc.is_in_same_rack:
            plc_connected_to_internet_not_in_same_subnet_not_in_same_rack.append(plc)
    return plc_connected_to_internet_not_in_same_subnet_not_in_same_rack

"""
11. write a function to Identify the PLCs that are not connected to the internet and are in the same subnet and are in the same rack
"""

def identify_plc_not_connected_to_internet_in_same_subnet_in_same_rack(plc_list):
    """
    This function identifies the PLCs that are not connected to the internet and are in the same subnet and are in the same rack
    :param plc_list:
    :return:
    """
    plc_not_connected_to_internet_in_same_subnet_in_same_rack = []
    for plc in plc_list:
        if not plc.is_connected_to_internet and plc.is_in_same_subnet and plc.is_in_same_rack:
            plc_not_connected_to_internet_in_same_subnet_in_same_rack.append(plc)
    return plc_not_connected_to_internet_in_same_subnet_in_same_rack

"""
12. write a function to Identify the PLCs that are not connected to the internet and are in the same subnet and are not in the same rack
"""

def identify_plc_not_connected_to_internet_in_same_subnet_not_in_same_rack(plc_list):
    """
    This function identifies the PLCs that are not connected to the internet and are in the same subnet and are not in the same rack
    :param plc_list:
    :return:
    """
    plc_not_connected_to_internet_in_same_subnet_not_in_same_rack = []
    for plc in plc_list:
        if not plc.is_connected_to_internet and plc.is_in_same_subnet and not plc.is_in_same_rack:
            plc_not_connected_to_internet_in_same_subnet_not_in_same_rack.append(plc)
    return plc_not_connected_to_internet_in_same_subnet_not_in_same_rack

"""
13. write a function to Identify the PLCs that are not connected to the internet and are not in the same subnet and are in the same rack
"""

def identify_plc_not_connected_to_internet_not_in_same_subnet_in_same_rack(plc_list):
    """
    This function identifies the PLCs that are not connected to the internet and are not in the same subnet and are in the same rack
    :param plc_list:
    :return:
    """
    plc_not_connected_to_internet_not_in_same_subnet_in_same_rack = []
    for plc in plc_list:
        if not plc.is_connected_to_internet and not plc.is_in_same_subnet and plc.is_in_same_rack:
            plc_not_connected_to_internet_not_in_same_subnet_in_same_rack.append(plc)
    return plc_not_connected_to_internet_not_in_same_subnet_in_same_rack

"""
14. write a function to Identify the PLCs that are not connected to the internet and are not in the same subnet and are not in the same rack
"""

def identify_plc_not_connected_to_internet_not_in_same_subnet_not_in_same_rack(plc_list):
    """
    This function identifies the PLCs that are not connected to the internet and are not in the same subnet and are not in the same rack
    :param plc_list:
    :return:
    """
    plc_not_connected_to_internet_not_in_same_subnet_not_in_same_rack = []
    for plc in plc_list:
        if not plc.is_connected_to_internet and not plc.is_in_same_subnet and not plc.is_in_same_rack:
            plc_not_connected_to_internet_not_in_same_subnet_not_in_same_rack.append(plc)
    return plc_not_connected_to_internet_not_in_same_subnet_not_in_same_rack

"""
15. write a function to Identify the PLCs that are connected to the internet and are in the same subnet and are in the same rack and are in the same switch
"""

def identify_plc_connected_to_internet_in_same_subnet_in_same_rack_in_same_switch(plc_list):
    """
    This function identifies the PLCs that are connected to the internet and are in the same subnet and are in the same rack and are in the same switch
    :param plc_list:
    :return:
    """
    plc_connected_to_internet_in_same_subnet_in_same_rack_in_same_switch = []
    for plc in plc_list:
        if plc.is_connected_to_internet and plc.is_in_same_subnet and plc.is_in_same_rack and plc.is_in_same_switch:
            plc_connected_to_internet_in_same_subnet_in_same_rack_in_same_switch.append(plc)
    return plc_connected_to_internet_in_same_subnet_in_same_rack_in_same_switch

"""
16. write a function to Identify the PLCs that are connected to the internet and are in the same subnet and are in the same rack and are not in the same switch
"""

def identify_plc_connected_to_internet_in_same_subnet_in_same_rack_not_in_same_switch(plc_list):
    """
    This function identifies the PLCs that are connected to the internet and are in the same subnet and are in the same rack and are not in the same switch
    :param plc_list:
    :return:
    """
    plc_connected_to_internet_in_same_subnet_in_same_rack_not_in_same_switch = []
    for plc in plc_list:
        if plc.is_connected_to_internet and plc.is_in_same_subnet and plc.is_in_same_rack and not plc.is_in_same_switch:
            plc_connected_to_internet_in_same_subnet_in_same_rack_not_in_same_switch.append(plc)
    return plc_connected_to_internet_in_same_subnet_in_same_rack_not_in_same_switch
