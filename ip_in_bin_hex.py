ip_address = input ("Please enter an IP address: ")

octets  = ip_address.split(".")
print("-"*80)
print("{:^15}{:^15}{:^15}{:^15}".format("octet1", "octet2", "octet3", "octet4"))
print("-"*80)
print("Dec{:^15}{:^15}{:^15}{:^15}".format(octets[0], octets[1], octets[2], octets[3]))
print("Bin{:^15}{:^15}{:^15}{:^15}".format(bin(int(octets[0])), bin(int(octets[1])), bin(int(octets[2])), bin(int(octets[3]))))
print("hex{:^15}{:^15}{:^15}{:^15}".format(hex(int(octets[0])), hex(int(octets[1])), hex(int(octets[2])), hex(int(octets[3]))))