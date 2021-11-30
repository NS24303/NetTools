'''
- This script will be based on w3_ex5.py and will allow a user to ping a range of IPs based on a
given subnet and range
- At present script will assume a /24 range but this can be changed later
'''

import os

def capture_inputs():
    ip_range = input("Please enter the range (first 3 octets, i.e. 10.20.30.): ")
    start = input("What is the first IP in the range? ")
    end = input("What is the last IP in the range? ")
    return ip_range, start, end

def verify_range():
    verify = input("Is this correct? (y/n): ")
    verify = verify.lower()
    return verify

def main():
    base_cmd_linux = "ping -c 2"
    base_cmd_windows = "ping -n 2"
    WINDOWS = False
    base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux
    verify = 'n'
    while verify != 'y':
        ip_range, start, end = capture_inputs()
        print("\n\nIP Address range is", ip_range + start, "-", end)
        verify = verify_range()
        if verify == 'n':
            print("Verification failed. Restarting...")
        elif verify == 'y':
            range_start = int(start)
            range_end = int(end)
            for ip in range(range_start, range_end+1):
                ip = str(ip)
                address = ip_range + ip
                print("IP Address to Ping is: ", address)
                return_code = os.system("{} {}".format(base_cmd, address))
                print("-" * 40, "\n")

main()

# Future improvement to this script will be error checking on the IP address.
# This will ensure the first 3 octets are in the valid format:
# i.e. '10.20.30.' vs '10.20.30' or '356.20.30.'

