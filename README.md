# ansible-docugen


Mannualy add the following tags in the ansible script. Typically, 
- One tag per line.
- `# @hosts` goes above hosts block
- `# @title`, `# @name`, `# @comment`, `# @code`, `# @input`, `# @output` should go above each task 

### Example
```yaml
# @title: Install build tools

# @hosts all
- hosts: all #specify the host(s)
  become: yes #elevate privileges

# @name: Install gcc tools
# @comment: Tools needed to compile code
# @code: yum install gcc gcc-g++ make -y
# @input: TODO
# @output: TODO
- name: Install gcc tools
  yum:
    name:
      - gcc
      - gcc-g++
      - make
    state: present

# @name: Install vim text editor 
# @comment: Tools needed to edit code
# @code: yum install vim -y
# @input: TODO
# @output: TODO
- name: Install vim
  yum:
    name:
      - vim
    state: present
```

or run 

`add-comments.py` to add them for you. 
this will also take the contents of name and copies it to the `# @name tag
generate-markdown.py


`# @hosts` converts to `#` in markdwon

`# @title` converts to `##` in markdown

`# @name` converts to `###` in markdown

`# @comment` converts to *italic* in markdown

`# @code` converts to `` in markdown

`# @input` converts to `TODO` in markdown

`# @output` converts to `TODO` in markdown
