# simple script using the ipaddress module to print the useable IP addresses in an ipv4 subnet

import ipaddress

user_subnet = input("Enter a subnet: ")
net4 = ipaddress.ip_network(user_subnet)

for x in net4.hosts():
    print(x)

print('-'*40)
print("The total number of addresses in the subnet is", net4.num_addresses)
print('-'*40)
