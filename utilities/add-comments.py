#! /usr/bin/python3

import os

ansibleDir = "/home/jluna/develop/ansible/playbooks/"
rolesDir = "/home/jluna/develop/ansible/playbooks/roles/"

def insert_comment(file_path):
    with open(file_path, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if "- name" in line:
                name = line.split("- name", 1)[1]
                file.write("# @name: " + name)
                file.write("# @para: this is some text that describe the purpose of the plabook\n")
                file.write("# @comment: This is a comment\n")
                file.write("# @code: #! /usr/bin/bash \\n\\n echo \"this is a test\" \n")
                #file.write("# @output: \n")
            if "- hosts" in line:
                hosts = line.split("- hosts:", 1)[1]
                file.write("# @hosts: " + hosts)
            file.write(line)
        file.truncate()

# Example usage
#insert_comment('/home/jluna/develop/ansible/roles/tasks/')

for filename in os.listdir(rolesDir):
    tasks = os.path.join(rolesDir, filename + "/tasks/")
    if os.path.exists(tasks):
        for task in os.listdir(tasks):
            if task.endswith(".yml") or task.endswith(".yaml"):
                rolesFilePath = os.path.join(tasks, task)
                print (rolesFilePath)
                insert_comment(rolesFilePath)


for filename in os.listdir(ansibleDir):
    if filename.endswith(".yml") or filename.endswith(".yaml"):
        ansibleFilePath = os.path.join(ansibleDir, filename)
        print (ansibleFilePath)
        insert_comment(ansibleFilePath)
