#!/usr/bin/python3

# Import tools to list dirs
import os

# Directory containing Ansible scripts
#ansibleDir = "/home/admin/develop/ansible-docugen/example/scripts"
ansibleDir = "/home/jluna/develop/ansible/playbooks/"
ansibleRolesDir = "/home/jluna/develop/ansible/playbooks/roles"
docsDir = "/home/jluna/develop/ansible/docs/plays/"
mdFile = ""
markdownLine = []
currentLineNumber=0


# List of styles - h1, h2, h3, h4, comment, code
def writeMdLine(mdFile, tag):

    if tag["style"] == "hosts":
        markdownLine.append("## hosts\n")
        markdownLine.append("- " + tag["content"] + "\n\n")
        markdownLine.append("----\n\n")
    if tag["style"] == "title":
        markdownLine.append("# " + tag["content"] + "\n\n")
    if tag["style"] == "name":
        markdownLine.append("&nbsp;\n\n")
        markdownLine.append("&nbsp;\n\n")
        markdownLine.append("## " + tag["content"] + "\n\n")
    if tag["style"] == "para":
        markdownLine.append(tag["content"] + "\n")
    if tag["style"] == "comment":
        markdownLine.append("*" + tag["content"] + "*" + "\n\n")
    if tag["style"] == "code":
        markdownLine.append("```bash\n")
        markdownLine.append(tag["content"])
        markdownLine.append("\n```\n\n")
    if tag["style"] == "output":
        markdownLine.append("### output\n")
        markdownLine.append("```\n")
        markdownLine.append(tag["content"])
        markdownLine.append("\n```\n\n")

    # Write to file
    with open(mdFile, "w") as file:
        file.writelines(markdownLine)

    # Rename from yml to md
    base = os.path.splitext(mdFile)[0]
    os.rename(mdFile, base + ".md")


# Tag may start be - # @name,  # @comment,  # @code,  # @input,  # @output,
def generateDocs(ansibleScriptPath, markdownPath):
    global currentLineNumber
    with open(ansibleScriptPath, "r") as file:
        lines = file.readlines()

    for line in lines:
        currentLineNumber+=1
        print("Current Line Number: " + str(currentLineNumber), end='\r')
        content=""
        tagline=""
        if line.strip().startswith("# @hosts"):
            content=line.strip()[9:].strip()
            tagline={"style": "hosts", "content" : content }
            writeMdLine(markdownPath, tagline)
        if line.strip().startswith("# @title"):
            content=line.strip()[9:].strip()
            tagline={"style": "title", "content" : content }
            writeMdLine(markdownPath, tagline)
        if line.strip().startswith("# @name"):
            content=line.strip()[9:].strip()
            tagline={"style": "name", "content" : content }
            writeMdLine(markdownPath, tagline)
        if line.strip().startswith("# @comment"):
            content=line.strip()[11:].strip()
            tagline={"style": "comment", "content" : content }
            writeMdLine(markdownPath, tagline)
        if line.strip().startswith("# @code"):
            content=line.strip()[8:].strip()
            tagline={"style": "code", "content" : content }
            writeMdLine(markdownPath, tagline)
        if line.strip().startswith("# @para"):
            content=line.strip()[8:].strip()
            tagline={"style": "para", "content" : content }
            writeMdLine(markdownPath, tagline)
        if line.strip().startswith("# @output"):
            content=line.strip()[10:].strip()
            tagline={"style": "output", "content" : content }
            writeMdLine(markdownPath, tagline)

# Generate Documentation for Playbooks
for filename in os.listdir(ansibleDir):
    # Check for ansible scripts. Assume they end with yml or yaml
    if filename.endswith(".yml") or filename.endswith(".yaml"):

        # Generate full path to new markdown file
        mdFilePath = os.path.join(docsDir, filename)
        ansibleFilePath = os.path.join(ansibleDir, filename)
        markdownLine = []

        generateDocs(ansibleFilePath, mdFilePath)

# Loop through ~/ansible/playbooks/ - store playbooks as filename

## Generate Documentation for Roles
for filename in os.listdir(ansibleRolesDir):
    # strip and store the name of the role from role.yml to just role
    docsRolesDir  = os.path.join(docsDir, "roles", filename)
    rolesTasksDir = os.path.join(ansibleRolesDir, filename, "tasks")
    if not os.path.exists(docsRolesDir):
        os.mkdir(docsRolesDir)
    if os.path.exists(rolesTasksDir):
        for task in os.listdir(rolesTasksDir):
            if task.endswith(".yml") or task.endswith(".yaml"):
                mdFilePath = os.path.join(docsRolesDir, task)
                tasks = os.path.join(rolesTasksDir, task)
                markdownLine = [] # Reset array
                print ("FROM: " + tasks)
                print("TO   : " + mdFilePath)
                generateDocs(tasks, mdFilePath)



print ("\nDone.")
