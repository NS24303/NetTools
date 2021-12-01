# Testing of the ipaddress module to confirm if an address is valid with a graceful
# error message rather than traceback
# https://docs.python.org/3/howto/ipaddress.html

import ipaddress

def valid_ip():
    user_ip = input("Please enter an IP address: ")
    try:
        output = ipaddress.ip_address(user_ip)
        print("IP Address is Valid")
    except ValueError as e:
        #print(e.__class__)
        print(str(e))
        print("\n-- IP Address is NOT Valid --")
        print("-- SCRIPT STOPPED -- \n")

valid_ip()
