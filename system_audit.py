# system_audit.py

from datetime import datetime

print("=== System User Audit Tool ===")

username = input("Enter username: ").strip()
role = input("Enter role (IT / Dev / Student): ").strip()
years_raw = input("Years of experience: ").strip()

if not years_raw.isdigit():
    print("Error: Years must be a number.")
    raise SystemExit(1)

years = int(years_raw)

if years < 1:
    level = "Entry Level"
elif years <= 3:
    level = "Junior"
elif years <= 7:
    level = "Mid-Level"
else:
    level = "Senior"

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

report = (
    f"{timestamp} | "
    f"User: {username} | "
    f"Role: {role} | "
    f"Experience: {years} | "
    f"Level: {level}\n"
)

print("\n--- AUDIT REPORT ---")
print(report)

# Save to file
with open("audit_log.txt", "a") as file:
    file.write(report)

print("Audit saved to audit_log.txt")
