#!/usr/bin/local/python3
import sys

if len(sys.argv) > 1:
    read_name = sys.argv[1]
    write_name = sys.argv[2]

with open(read_name, 'r') as read_file:
    data = read_file.read()

data = '"' + data
data = data.replace('\n', '"\n"')
data = data + '"'

with open(write_name, 'w') as write_file:
    write_file.write(data)
