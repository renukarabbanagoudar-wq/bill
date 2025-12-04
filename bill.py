import sys
if (sys.argv) ==2:
    unit=sys.argv[1]
    bill=sys.argv[2]
    total=unit * bill
else:
    print("Enter a electricity")
    print("Unit:",unit)
    print("Bill:",bill)
