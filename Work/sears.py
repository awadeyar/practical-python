# sears.py
bill_thickness = 0.11 * 0.001 # Meters (0.11mm)
sears_height = 442 #
num_bills = 1
day = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print("Number of Days", day)
print("Number of Bills", num_bills)
print("Final Height", num_bills * bill_thickness)
