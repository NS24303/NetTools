from netmiko import Netmiko
import click

@click.command()
@click.option('-c', '--command', help='Command to run on devices', required=True)
@click.option('-u', '--username', help='Username to login to device', required=True)
@click.option('--password', prompt=True, hide_input=True)
def the_devices(command,username,password):
    device_list = 'device_list.txt'
    with open(device_list) as f:
        # remove \n whitespace from list.
        devices = f.read().splitlines()
    for ip in devices:
        net_device = {
            'host': ip,
            'username': username,
            'password': password,
            'secret': password,
            'device_type': 'cisco_asa'
        }
        # print(netdevice)
        return net_device

def connection():
        net_device = the_devices()
        net_conn = Netmiko(**net_device)
        output = net_conn.send_command(command)
        print('\n\n --- Logging into IP -', ip, "\n")
        print(net_conn.find_prompt())
        save_output()
        return output

def save_output():
    print(output)
    # write contents to file
    f = open("cmd_output.txt", mode="w")
    f.write(output)
    f.flush()

connection()

## above currently not working, no errors on run, just no output. Further troubleshooting tomorrow.