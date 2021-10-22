'''
- This script will be based on w3_ex5.py and will allow a user to ping a range of IPs based on a
given subnet and range
- At present script will assume a /24 range but this can be changed later
- Another future addition -> error checking to confirm IP entered is valid
- User verification using an if statmment
'''

ip_range = input("Please enter the range (first 3 octets): ")
start = input("What is the first IP in the range? ")
end = input("What is the last IP in the range? ")

print("\n\nIP Address range is" ,ip_range + start,"-" ,end)

verify = input("Is this correct? (y/n)")

# if statement to verify if 'y' or 'n'
# if y continue, otherwise break

