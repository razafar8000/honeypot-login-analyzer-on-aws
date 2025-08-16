Honeypot Login Analyzer on AWS

Project Overview:
Credential brute-force attacks are one of the most common threats against login systems.
This project sets up a honeypot login page on an AWS EC2 instance to capture unauthorized login attempts, store them in logs, and analyze attacker behavior.
The project includes:
A fake login page (index.html) served via Apache.
A backend script (login.py) that logs all login attempts (username, password, IP address, timestamp).
A log parser (parse_logs.py) that structures raw logs into CSV format.
A visualization script (visualize.py) that generates charts of attacker behavior.
This demonstrates end-to-end threat monitoring, log analysis, and data visualization — critical skills for security engineering.

Tech Stack:
AWS EC2 (Ubuntu) – Cloud hosting environment
Apache Web Server (CGI) – Serving the honeypot login page
Python – Data parsing (pandas) and visualization (matplotlib)
Linux & Bash – System setup, permissions, and secure transfers (scp)
Git & GitHub – Version control and project publishing

Sample Outputs:
When attackers interact with the honeypot:
ip_attempts.png → Shows number of login attempts grouped by IP address
user_attempts.png → Shows number of login attempts grouped by username
Example: An IP making 500 failed login attempts or a username like “admin” being targeted repeatedly.

How It Works:
Deployment: Honeypot hosted on AWS EC2 with Apache.
Data Capture: login.py records login attempts into a log file.
Parsing: parse_logs.py converts logs into a structured CSV (dataset.csv).
Visualization: visualize.py generates attacker behavior charts.
Analysis: Patterns of brute-force activity can be studied and used for security insights.

Future Improvements:
Add real-time alerting when brute-force attempts cross a threshold.
Store logs in a database (PostgreSQL / MongoDB) for advanced querying.
Deploy inside a Docker container for easier setup and reproducibility.
Integrate with a SIEM system (Splunk, ELK) for enterprise-grade monitoring.

What I Learned:
Deploying and managing a web service on AWS EC2
Handling log parsing and data transformation with Python & pandas
Creating security-focused visualizations to detect attacker patterns
Using GitHub for project sharing and version control
This project reflects my ability to combine cloud, Python, and cybersecurity skills to create practical defensive tools.
