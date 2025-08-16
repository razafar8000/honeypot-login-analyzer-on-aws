#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset with custom column names
df = pd.read_csv(
    "/var/www/html/dataset.csv",
    names=["Time", "IP", "Username", "Password", "UserAgent"]
)


# --- 1. Count login attempts by IP ---
ip_counts = df["IP"].value_counts()

plt.figure(figsize=(8,5))
ip_counts.plot(kind="bar", color="skyblue")
plt.title("Login Attempts by IP")
plt.xlabel("IP Address")
plt.ylabel("Number of Attempts")
plt.tight_layout()
plt.savefig("/var/www/html/ip_attempts.png")
plt.close()

# --- 2. Count login attempts by Username ---
user_counts = df["Username"].value_counts()

plt.figure(figsize=(8,5))
user_counts.plot(kind="bar", color="salmon")
plt.title("Login Attempts by Username")
plt.xlabel("Username")
plt.ylabel("Number of Attempts")
plt.tight_layout()
plt.savefig("/var/www/html/user_attempts.png")
plt.close()

print("✅ Charts generated: ip_attempts.png, user_attempts.png")
