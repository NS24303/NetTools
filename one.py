'''
Some examples of working with Python2 vs Python3
'''
# if using Python2 would have to use raw_input whereas in python3 just need input.
ip_addr = input("enter an IP address: ")

#altnertive way is:

#first try python2 method
#try:
#    ip_addr2 = raw_input("Enter another IP Address: ")
    # Then try Python3 method
#except NameError:
#    ip_addr2 = input("Enter Another IP Address:")

#print(ip_addr)
print(ip_addr)
# split the IP address by .
octets  = ip_addr.split(".")
print(octets)
#octets becomes a list
#print(type(octets))
