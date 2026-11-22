# Mini Project: JSON-Based Log File Analyzer

import json
from collections import Counter

log_file = "Unit_4/sample.log"
json_file = "Unit_4/log_summary.json"

# Sample log messages
sample_lines = [
    "INFO: Application started",
    "WARNING: Low memory",
    "ERROR: File missing",
    "INFO: User logged in",
    "ERROR: Connection failed",
    "WARNING: Slow response"
]

# Create sample log file if it doesn't exist
try:
    with open(log_file, "r") as file:
        lines = file.readlines()

except FileNotFoundError:
    with open(log_file, "w") as file:
        file.writelines(line + "\n" for line in sample_lines)

    lines = sample_lines

# Count log levels
counts = Counter()

for line in lines:
    for level in ("INFO", "WARNING", "ERROR"):
        if level in line:
            counts[level] += 1

# Create summary
summary = {
    "total_lines": len(lines),
    "level_counts": dict(counts),
    "messages": [line.strip() for line in lines]
}

# Save summary in JSON file
with open(json_file, "w") as file:
    json.dump(summary, file, indent=4)

# Display result
print("Log summary:")
print(json.dumps(summary, indent=4))

print(f"\nSummary saved to {json_file}")