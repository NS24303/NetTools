# Simple script to prompt user for an IP and mask and output network id, mask len, b/cast address
# modified from
# https://stackoverflow.com/questions/47316777/calculate-broadcast-by-ip-and-mask
# https://realpython.com/python-ipaddress-module/

import ipaddress

ip = input("Enter an IP Address: (i.e. 10.2.1.32) ")
mask = input("Enter the Subnet Mask: (i.e. 255.255.255.224) ")

host = ipaddress.IPv4Address(ip)
net = ipaddress.IPv4Network(ip + '/' + mask, False)
qty = net.num_addresses
# print(net)
print('IP:', ip)
print('Mask:', mask, 'or /{}'.format(net.prefixlen))
print('Host Bits:', ipaddress.IPv4Address(int(host) & int(net.hostmask)))
print('Network ID:', ipaddress.IPv4Address(int(host) & int(net.netmask)))
print('Broadcast Address:', net.broadcast_address)
print('Total Addresses in subnet:', qty)
print('Total Usable Addresses:', qty -2 )

