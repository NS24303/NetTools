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
verify = verify.lower()
print(verify)

# if verify is 'y' continue
if verify == 'y':
    pass
else:
    print("Verification failed. Exiting script")
    exit()

# do something else to verify if loop continues script vs stop if not
print ("script continues")

# rather then exit, could it restart the script?

