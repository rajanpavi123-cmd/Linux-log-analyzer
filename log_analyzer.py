import re

with open("sample.log", "r") as file:
    logs = file.readlines()

for line in logs:
    if re.search("error", line, re.IGNORECASE):
        print(line)
