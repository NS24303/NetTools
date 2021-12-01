# Simple script to prompt user for an IP and mask and output network id, mask len, b/cast address
# modified from
# https://stackoverflow.com/questions/47316777/calculate-broadcast-by-ip-and-mask
# https://realpython.com/python-ipaddress-module/

import ipaddress

ip = input("Enter an IP Address: ")
mask = input("Enter the Subnet Mask: ")

host = ipaddress.IPv4Address(ip)
net = ipaddress.IPv4Network(ip + '/' + mask, False)
print('IP:', ip)
print('Mask:', mask, 'or /{}'.format(net.prefixlen))
print('Network ID:', ipaddress.IPv4Address(int(host) & int(net.netmask)))
print('Host Bits:', ipaddress.IPv4Address(int(host) & int(net.hostmask)))
print('Broadcast Address:', net.broadcast_address)