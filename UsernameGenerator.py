#!/usr/bin/python3

import sys
from os import path

print("UsernameGenerator.py - Simple username generator based on a list of names and surnames (with optional domain and deduplication)")

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

# track seen usernames (case-insensitive) to deduplicate
seen = set()
nb_generated = 0
nb_written = 0

def write_username(username):
    """Write username to file if not already seen (case-insensitive)."""
    global nb_written
    key = username.lower()
    if key not in seen:
        seen.add(key)
        if domain:
            output.write(f"{username}@{domain}\n")
        else:
            output.write(f"{username}\n")
        nb_written += 1

with open(user_file) as fp:
    line = fp.readline()
    while line:
        line_clean = line.strip()
        if not line_clean:
            line = fp.readline()
            continue

        parts = line_clean.split()
        if len(parts) != 2:
            print(f"Warning: The line \"{line_clean}\" inside {user_file} is not correct. Format must be: [first name] [surname]")
            line = fp.readline()
            continue

        # normalize to lowercase for base patterns (we will also add capitalized variants)
        fname = parts[0].lower()
        lname = parts[1].lower()

        patterns = [
            lname, fname,
            f"{fname}.{lname}", f"{lname}.{fname}",
            f"{fname}-{lname}", f"{lname}-{fname}",
            f"{fname}{lname}", f"{lname}{fname}",
            f"{fname}_{lname}", f"{lname}_{fname}",
            f"{fname[0]}.{lname}", f"{lname[0]}.{fname}",
            f"{lname}.{fname[0]}", f"{fname}.{lname[0]}",
            f"{fname[0]}-{lname}", f"{lname[0]}-{fname}",
            f"{lname}-{fname[0]}", f"{fname}-{lname[0]}",
            f"{fname[0]}{lname}", f"{lname[0]}{fname}",
            f"{lname}{fname[0]}", f"{fname}{lname[0]}",
            f"{fname[0]}_{lname}", f"{lname[0]}_{fname}",
            f"{lname}_{fname[0]}", f"{fname}_{lname[0]}"
        ]

        # write lowercase patterns (deduplicated)
        for p in patterns:
            write_username(p)
        nb_generated += len(patterns)

        # capitalized versions (Firstname Surname style)
        fname_cap = fname.capitalize()
        lname_cap = lname.capitalize()

        patterns_caps = [
            lname_cap, fname_cap,
            f"{fname_cap}.{lname_cap}", f"{lname_cap}.{fname_cap}",
            f"{fname_cap}-{lname_cap}", f"{lname_cap}-{fname_cap}",
            f"{fname_cap}{lname_cap}", f"{lname_cap}{fname_cap}",
            f"{fname_cap}_{lname_cap}", f"{lname_cap}_{fname_cap}",
            f"{fname_cap[0]}.{lname_cap}", f"{lname_cap[0]}.{fname_cap}",
            f"{lname_cap}.{fname_cap[0]}", f"{fname_cap}.{lname_cap[0]}",
            f"{fname_cap[0]}-{lname_cap}", f"{lname_cap[0]}-{fname_cap}",
            f"{lname_cap}-{fname_cap[0]}", f"{fname_cap}-{lname_cap[0]}",
            f"{fname_cap[0]}{lname_cap}", f"{lname_cap[0]}{fname_cap}",
            f"{lname_cap}{fname_cap[0]}", f"{fname_cap}{lname_cap[0]}",
            f"{fname_cap[0]}_{lname_cap}", f"{lname_cap[0]}_{fname_cap}",
            f"{lname_cap}_{fname_cap[0]}", f"{fname_cap}_{lname_cap[0]}"
        ]

        for p in patterns_caps:
            write_username(p)
        nb_generated += len(patterns_caps)

        line = fp.readline()

output.close()

print(f"Usernames generated (attempted patterns): {nb_generated}")
print(f"Unique usernames written to output file {output_file}: {nb_written}")
print("------------------------------------------------------")
