import json
import datetime
import os

# Allowed countries for data transfer
allowed_countries = [
    "Kenya",
    "Germany",
    "France",
    "Netherlands",
    "Canada"
]

def log_transfer(data, risk_score, issues):

    log_file = "C:\\Users\\machm\\CyberLab\\logs\\system.log"

    status = "COMPLIANT"

    if risk_score > 0:
        status = "NON-COMPLIANT"

    log_entry = f"""
Time: {data['timestamp']}
Source: {data['source_country']}
Destination: {data['destination_country']}
Risk Score: {risk_score}
Status: {status}
Issues: {issues}
------------------------
"""

    with open(log_file, "a") as file:
        file.write(log_entry)

def evaluate_transfer(data):

    risk_score = 0
    issues = []

    # Check encryption
    if data["encrypted"] == False:
        risk_score += 40
        issues.append("Data not encrypted")

    # Check consent
    if data["patient_consent"] == False:
        risk_score += 30
        issues.append("No patient consent")

    # Check destination country
    if data["destination_country"] not in allowed_countries:
        risk_score += 30
        issues.append("Country not approved")

    return risk_score, issues


# Test example transfer

sample_transfer = {

    "source_country": "Kenya",
    "destination_country": "Germany",
    "encrypted": True,
    "patient_consent": True,
    "timestamp": str(datetime.datetime.now())

}

risk, issues = evaluate_transfer(sample_transfer)

print("Risk Score:", risk)
print("Issues:", issues)

log_transfer(sample_transfer, risk, issues)