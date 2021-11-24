# Config_Templates

Scripts using Jinja2 to create configuration templates for various network platforms including

Device Family | Script | CSV file | Jinja2 Template
--- | --- | --- | ---
Cisco ASA | asa_config_build.py | asa_variables.csv | asa_template.j2
Cisco NXOS | nxos_config_build.py | nxos_variables.csv | nxos_template.j2
Arista | arista_config_build.py |  arista_template.csv| arista_template.j2


All of the templates are based on a CSV file with the variables and the Jinja2 template file as detailed in the above table. 

The output of the script is a configuration file based on the device_id within the CSV. 

The CSV and templates are currently only a bare bones configuration. More could be added as the script evolves 