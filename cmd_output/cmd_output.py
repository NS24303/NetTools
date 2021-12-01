from netmiko import Netmiko
from netmiko import ConnectHandler
from getpass import getpass
import click

@click.command()
@click.option('-c', '--command', help='Command to run on devices', required=True)
@click.option('-u', '--username', help='Username', required=True)
def connection(command,username):
    password = getpass()
    device_list = 'device_list.txt'
    with open(device_list) as f:
        # remove \n whitespace from list.
        devices = f.read().splitlines()
    for ip in devices:
        firewall = {
            'host': ip,
            'username': username,
            'password': password,
            'secret': password,
            'device_type': 'cisco_asa'
        }
        print(firewall)

connection()

