#!/usr/bin/python3

import sys
from os import path

print("UsernameGenerator.py - Simple username generator based on a list of names and surnames")

if len(sys.argv) < 3:
    print("Usage: python3 UsernameGenerator.py [user file] [output file] [optional: domain name]")
    exit()

# arguments
user_file = str(sys.argv[1])
output_file = str(sys.argv[2])
domain = str(sys.argv[3]) if len(sys.argv) == 4 else None

print("------------------------------------------------------")
print(f"Input file: {user_file}")
print(f"Output file: {output_file}")
if domain:
    print(f"Domain: {domain}")
print("------------------------------------------------------")

if path.exists(output_file):
    print(f"The file {output_file} exists!\nDelete this file before running this script!\n------------------------------------------------------")
    exit()

# file output
output = open(output_file, 'w')
nb_user = 0

def write_username(username):
    """Helper to write username, optionally appending domain."""
    if domain:
        output.write(f"{username}@{domain}\n")
    else:
        output.write(f"{username}\n")

with open(user_file) as fp:
    line = fp.readline().lower()
    while line:
        list_name = line.strip().split()
        if len(list_name) != 2:
            print(f"Warning: The line \"{line.rstrip()}\" inside {user_file} is not correct. Format must be: [first name] [surname]")
            line = fp.readline().lower()
            continue

        patterns = [
            list_name[1], list_name[0],
            f"{list_name[0]}.{list_name[1]}", f"{list_name[1]}.{list_name[0]}",
            f"{list_name[0]}-{list_name[1]}", f"{list_name[1]}-{list_name[0]}",
            f"{list_name[0]}{list_name[1]}", f"{list_name[1]}{list_name[0]}",
            f"{list_name[0]}_{list_name[1]}", f"{list_name[1]}_{list_name[0]}",
            f"{list_name[0][0]}.{list_name[1]}", f"{list_name[1][0]}.{list_name[0]}",
            f"{list_name[1]}.{list_name[0][0]}", f"{list_name[0]}.{list_name[1][0]}",
            f"{list_name[0][0]}-{list_name[1]}", f"{list_name[1][0]}-{list_name[0]}",
            f"{list_name[1]}-{list_name[0][0]}", f"{list_name[0]}-{list_name[1][0]}",
            f"{list_name[0][0]}{list_name[1]}", f"{list_name[1][0]}{list_name[0]}",
            f"{list_name[1]}{list_name[0][0]}", f"{list_name[0]}{list_name[1][0]}",
            f"{list_name[0][0]}_{list_name[1]}", f"{list_name[1][0]}_{list_name[0]}",
            f"{list_name[1]}_{list_name[0][0]}", f"{list_name[0]}_{list_name[1][0]}"
        ]

        # lowercase versions
        for p in patterns:
            write_username(p)

        # capitalize versions
        list_name = [n.capitalize() for n in list_name]
        patterns_caps = [p.capitalize() if not any(ch in p for ch in ['.', '-', '_']) else p for p in patterns]
        for p in patterns_caps:
            write_username(p)

        nb_user += len(patterns) * 2  # lowercase + capitalized
        line = fp.readline().lower()

print(f"Usernames written to output file {output_file}")
print(f"Number of users created: {nb_user}")
print("------------------------------------------------------")
