import jinja2
import csv

csv_file = "asa_variables.csv"

with open(csv_file) as f:
    read_csv = csv.DictReader(f)
    for asa_vars in read_csv:
        #ssh_acl = asa_vars['ssh_acl']
        #ssh_acl = ssh_acl.split()
        #asa_vars['ssh_acl'] = ssh_acl

        template_file = 'asa_template.j2'
        with open(template_file) as f:
            asa_template = f.read()

        template = jinja2.Template(asa_template)
        hostname = asa_vars['device_id']
        print()
        print('-' * 65)
        print(template.render(asa_vars))
        print('-' * 65)

        f = open(hostname + ".txt", mode="w")
        f.write(template.render(asa_vars))
        f.flush()

