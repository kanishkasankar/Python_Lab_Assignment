# Lab Exercise 3: CSV-Based Payroll Management
import csv

filename = "payroll.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Employee ID", "Name", "Basic Salary", "Allowance", "Total"])
    count = int(input("How many employees? "))
    for _ in range(count):
        emp_id = input("Employee ID: ")
        name = input("Name: ")
        basic = float(input("Basic salary: "))
        allowance = float(input("Allowance: "))
        total = basic + allowance
        writer.writerow([emp_id, name, basic, allowance, total])

print("\\nPayroll records:")
with open(filename, "r") as file:
    for row in csv.reader(file):
        print(" | ".join(row))
