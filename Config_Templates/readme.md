# Config_Templates

Scripts using Jinja2 to create configuration templates for various network platforms including
- ASA
- NX-OS
- Arista

All of the templates are based on a CSV file with the variables and the Jinja2 template file

The output of the script is a configuration file based on the device_id within the CSV. 

The CSV and templates are currently only a bare bones configuration. More could be added as the script evolves 