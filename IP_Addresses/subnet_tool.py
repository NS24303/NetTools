# Generates Subnets from a user inputted supernet and new prefix length
# Some assistance from
# https://ttl255.com/working-with-ip-addresses-in-python-ipaddress-library-part-1/

import ipaddress
# from pprint import pprint

super = input("Enter the supernet: (i.e. 10.0.0.0/8) ")
length = input("What size subnets do you require (i.e. 24): ")
length = int(length)

parent = ipaddress.ip_network(super)
#pprint(list(netparent.subnets(new_prefix=length)))

for sub in parent.subnets(new_prefix=length):
    print(sub)
