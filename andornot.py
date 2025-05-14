driver_insurance = True
driver_license = True
working = False
if (driver_insurance or driver_license) and not working:
    print(" Driver is Not Eligible")
else:
    print(" Driver is Eligible")
