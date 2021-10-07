'''
Some examples of working with Python2 vs Python3
'''
# if using Python2 would have to use raw_input whereas in python3 just need input.

#first try python2 method
#try:
#    ip_addr2 = raw_input("Enter another IP Address: ")
    # Then try Python3 method
#except NameError:
#    ip_addr2 = input("Enter Another IP Address:")

ip_a = '1.1.1.1'
ip_b = '8.8.8.8'
ip_c = '8.8.4.4'

ipvsix_a=str("1001:0000:3238:DFE1:0063:0000:0000:FEFB")
IPVSIX_B=str("2001:0000:3238:DFE1:0063:0000:0000:FEFB")
IPv6_C=str("3001:0000:3238:DFE1:0063:0000:0000:FEFB")

print(ipvsix_a)
print(IPVSIX_B)
print(IPv6_C)

print("Does IPv6_a and IPv6_b match?: " ,ipvsix_a == IPVSIX_B)
print("Does IPv6_a note match IPv6_b ?: " ,ipvsix_a != IPVSIX_B)

ip_addr = input("enter an IP address: ")

#print(ip_addr)
print(ip_addr)
# split the IP address by .
octets  = ip_addr.split(".")
print("-"*80)
print(octets)
print("-"*80)
#octets becomes a list
#print(type(octets))
print("-"*80)
# print ip address variables on one line with centre spacing and 15 wide
print("{:^15}{:^15}{:^15}".format(ip_a, ip_b, ip_c))
print("\n\nOctets of ip_addr are:\n\n {:5}{:5}{:5}{:5}".format(octets[0], octets[1], octets[2], octets[3]))
#another way to do the same thing as above
print("\n\ndiff: Octets of ip_addr are:\n\n {:5}{:5}{:5}{:5}".format(*octets))

print("-"*80)
print("-"*80)