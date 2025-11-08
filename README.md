# 🧩 UsernameGenerator

A simple and flexible username generator for penetration testers, red teamers, and security researchers.  
It generates possible username formats from a list of first and last names — and now includes an optional domain appending feature (e.g., `@example.com`).

---

## 🚀 Features

- Generates a wide variety of common username patterns:
  - `firstname.lastname`, `lastname.firstname`
  - `f.lastname`, `firstname.l`
  - `firstname_lastname`, `lastname_firstname`
  - `firstname-lastname`, `lastname-firstname`, etc.
- Supports both lowercase and capitalized variations.
- Optionally append a domain name (e.g., `@example.com`) for email-style usernames.
- Simple CLI usage — **no dependencies required**.
- Great for OSINT, password spraying prep, or user enumeration simulations.

---

## 🛠️ Usage

```bash
python3 UsernameGenerator.py [user_file] [output_file] [optional: domain]
```

**Example 1 — Without domain**
```bash
python3 UsernameGenerator.py names.txt usernames.txt
```
**Output sample:**
```
john.doe
doe.john
j.doe
```

**Example 2 — With domain**
```bash
python3 UsernameGenerator.py names.txt usernames.txt example.com
```
**Output sample:**
```
john.doe@example.com
doe.john@example.com
j.doe@example.com
```

---

## 📂 Input Format

Your input file should contain one name per line in the following format:

```
firstname lastname
```

**Example:**
```
John Doe
Mary Smith
```

---

## ⚙️ Output

The script will generate multiple username combinations for each name and save them to the specified output file.  
If the output file already exists, the script will abort to prevent overwriting.

---

## 🧑‍💻 Example Use Case

Perfect for preparing a username list during:

- Internal Active Directory penetration tests
- Password spraying simulations
- OSINT investigations to identify corporate email formats
- Social engineering pretext planning

---
