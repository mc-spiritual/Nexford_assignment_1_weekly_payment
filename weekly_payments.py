import csv
import random

# ========================
# Highridge Construction Co. Payroll Processor
# Developed to automate weekly payment records
# ========================

# STEP 1: Create a dynamic list of worker records
TOTAL_WORKERS = 400
worker_records = []

for worker_id in range(1, TOTAL_WORKERS + 1):
    profile = {
        "id": worker_id,
        "full_name": f"Employee_{worker_id}",
        "sex": random.choice(["Male", "Female"]),
        "weekly_salary": random.randint(5000, 35000)
    }
    worker_records.append(profile)

# STEP 2: Generate payment slips and assign employee levels based on conditions
payment_records = []

for profile in worker_records:
    try:
        level = "B2"  # Default level assigned to all unless conditions apply

        # STEP 4: Apply level rules based on salary and gender
        if 10000 < profile["weekly_salary"] < 20000:
            level = "A1"
        elif 7500 < profile["weekly_salary"] < 30000 and profile["sex"] == "Female":
            level = "A5-F"

        # Compose the finalized slip
        payment_slip = {
            "Worker ID": profile["id"],
            "Name": profile["full_name"],
            "Gender": profile["sex"],
            "Salary ($)": profile["weekly_salary"],
            "Level": level
        }
        payment_records.append(payment_slip)

    except Exception as error:
        # STEP 5: Handle any unexpected issues with data processing
        print(f"Issue with worker ID {profile['id']}: {error}")

# STEP 6: Export the compiled payment slips to a CSV file
output_filename = "highridge_payment_slips.csv"

with open(output_filename, "w", newline="") as f:
    headers = ["Worker ID", "Name", "Gender", "Salary ($)", "Level"]
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(payment_records)

# STEP 7: Indicate completion of the process
print(f"Payroll slips successfully saved to '{output_filename}'!")
