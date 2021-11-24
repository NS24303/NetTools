import jinja2
import csv

csv_file = "arista_variables.csv"

with open(csv_file) as f:
    read_csv = csv.DictReader(f)
    for arista_vars in read_csv:
        ssh_acl = arista_vars['ssh_acl']
        ssh_acl = ssh_acl.split()
        arista_vars['ssh_acl'] = ssh_acl

        template_file = 'arista_template.j2'
        with open(template_file) as f:
            arista_template = f.read()

        template = jinja2.Template(arista_template)
        hostname = arista_vars['device_id']
        print()
        print('-' * 65)
        print(template.render(arista_vars))
        print('-' * 65)

        f = open(hostname + ".txt", mode="w")
        f.write(template.render(arista_vars))
        f.flush()

