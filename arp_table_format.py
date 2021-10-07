mac1 = "Internet 10.220.88.29 94 5254.abbe.5b7b ARPA FastEthernet4"
mac2 = "Internet 10.220.88.30 3 5254.ab71.e119 ARPA FastEthernet4"
mac3 = "Internet 10.220.88.32 231 5254.abc7.26aa ARPA FastEthernet4"

print()
print("{:>20}{:>20}".format("IP Address" ,"MAC Address"))
print('-'*40)

new_mac1=mac1.split()
ip1=new_mac1[1]
mac_1=new_mac1[3]
new_mac2=mac2.split()
ip2=new_mac2[1]
mac_2=new_mac2[3]
new_mac3=mac3.split()
ip3=new_mac3[1]
mac_3=new_mac3[3]

print("{:>20}{:>20}".format(ip1, mac_1))
print("{:>20}{:>20}".format(ip2, mac_2))
print("{:>20}{:>20}".format(ip3, mac_3))