# PsonSetup
pson
Simple JSON utility library for Python.
Install
Windows:
Run install.bat
Linux / Mac:
Run:
chmod +x install.sh
./install.sh
Version
1.0.0
Usage
Import:
import pson
Create JSON:
pson.create("file.json", {
"name": "Adriel",
"age": 100
})
Read JSON:
pson.read("file.json")
Get value:
b = pson.value("file.json", "name")
print(b)
Output:
Adriel
Array access:
pson.create("data.json", {
"list": ["a", "b", "c"]
})
print(pson.value("data.json", "list", "1"))
Output:
b
CLI
pson -v
Errors
pson returns messages like:
[pson error] File not found
[pson error] Key not found
