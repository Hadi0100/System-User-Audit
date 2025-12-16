# system_audit.py

print("=== System User Audit Tool ===")

username = input("Enter username: ").strip()
role = input("Enter role (IT / Dev / Student): ").strip()
years_raw = input("Years of experience: ").strip()

# Basic input validation (so it doesn't crash if user types something weird)
if not years_raw.isdigit():
    print("Error: Years of experience must be a whole number (e.g., 0, 1, 5).")
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

print("\n--- AUDIT REPORT ---")
print(f"User: {username}")
print(f"Role: {role}")
print(f"Experience: {years} years")
print(f"Level: {level}")
print("--------------------")
