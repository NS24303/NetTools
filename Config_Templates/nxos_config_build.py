import jinja2
import csv

csv_file = "nxos_variables.csv"

with open(csv_file) as f:
    read_csv = csv.DictReader(f)
    for nxos_vars in read_csv:
        ssh_acl = nxos_vars['ssh_acl']
        ssh_acl = ssh_acl.split()
        # convert csv string to a list
        nxos_vars['ssh_acl'] = ssh_acl

        template_file = 'nxos_template.j2'
        with open(template_file) as f:
            nxos_template = f.read()

        template = jinja2.Template(nxos_template)
        hostname = nxos_vars['device_id']
        print()
        print('-' * 65)
        print(template.render(nxos_vars))
        print('-' * 65)

        f = open(hostname + ".txt", mode="w")
        f.write(template.render(nxos_vars))
        f.flush()

