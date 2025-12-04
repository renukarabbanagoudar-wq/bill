
import sys

RATE = 5

if len(sys.argv) == 2:
    print("User provided input values:")
    script_name = sys.argv[0]
    units = int(sys.argv[1])
else:
    print("No input given - using default values:")
    script_name = sys.argv[0]
    units = 100

bill_amount = units * RATE

print("Script Name:", script_name)
print("Units Consumed:", units)
print("Rate per Unit:", RATE)
print("Total Electricity Bill:", bill_amount)
