#!/usr/bin/env python3
import csv
import re

input_file = "/var/www/html/credentials.txt"
output_file = "/var/www/html/dataset.csv"

pattern = re.compile(
    r"\[(?P<time>.*?)\] IP: (?P<ip>\S+) \| Username: (?P<user>.*?) \| Password: (?P<pw>.*?) \| User-Agent: (?P<ua>.*)"
)

with open(input_file, "r") as infile, open(output_file, "w", newline="") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["timestamp", "ip", "username", "password", "user_agent"])

    for line in infile:
        match = pattern.match(line.strip())
        if match:
            writer.writerow([
                match.group("time"),
                match.group("ip"),
                match.group("user"),
                match.group("pw"),
                match.group("ua"),
            ])
