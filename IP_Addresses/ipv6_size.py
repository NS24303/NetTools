# Use of the ipaddress module to validate how many IPv6 addresses are in a range
# I am using locale and num2words to format the output in a nicer way.

import ipaddress
import locale
from num2words import num2words

locale.setlocale(locale.LC_ALL, 'en_GB')

user_ipv6 = input("Enter an IPv6 Subnet: ")

net6 = ipaddress.ip_network(user_ipv6)

print('-'*40)
large_number = net6.num_addresses
number_wang = net6.num_addresses
large_number = locale.format_string("%d", large_number, grouping=True)
print("The total number of addresses in the subnet is", large_number)
#example 2a03:6440::/32
print('-'*40)
print(num2words(number_wang))
print('-'*40)
