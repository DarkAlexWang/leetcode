#
# Given an org-chart denoted as a string in the following format:
#
# "id:name:manager_id,id:name:manager_id"
#
# Ex.
# "1:Name1:4,2:Name2:0,3:Name3:2,4:Name4:2"
#
# Print out an orgchart in simple ascii
#
# For the example above print out the following:
#
# Name2
# - Name3
# - Name4
# -- Name1
#

class Employee(object):
    def __init__(self, id, name, m_id):
        self.id = id
        self.name = name
        self.m_id = m_id

def generate_org_chart(ip_str):
    emp_map = {}

    # Parse the string
    emp_arr = ip_str.split(",")
    emp = []
    for e in emp_arr:
        emp.append(e.split(":"))
        temp_emp = emp[len(emp) - 1]
        emp_map[temp_emp[0]] = Employee(temp_emp[0], temp_emp[1], temp_emp[2])

    chart = {}
    root = ""

    #Loop througth the map
    for key, value in emp_map.items():
        if value.name not in chart:
            chart[value.name] = []
        if value.m_id == "0":
            root = value.name
        for j_key, j_value in emp_map.items():
            if value.id == j_value.m_id and j_value.id != value.id:
                chart[value.name].append(j_value.name)
    display(chart, root, 0)


def display(chart, name, level):
    prefix = ""
    for i in range(level):
        prefix += "-"
    print(prefix + name)

    emps = chart[name]
    for e in emps:
        display(chart, e, level + 1)

generate_org_chart("1:Name1:4,2:Name2:0,3:Name3:2,4:Name4:2")
