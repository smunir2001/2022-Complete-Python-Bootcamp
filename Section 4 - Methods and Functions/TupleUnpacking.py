stockPrices = [('APPL', 200), ('GOOG', 400), ('MSFT', 100)]
for item in stockPrices:
    print(item)
print()
for ticker, price in stockPrices:
    print(ticker)
print()
for ticker, price in stockPrices:
    print(price + (0.1 * price))
print()

workHours = [('Abby', 100), ('Billy', 400), ('Cassie', 800)]
def employeeCheck(workHours):
    currentMax = 0
    employeeOfMonth = ''
    for employee, hours in workHours:
        if hours > currentMax:
            currentMax = hours
            employeeOfMonth = employee
        else:
            pass
    return (employeeOfMonth, currentMax)
print('Employee with the most hours worked:', employeeCheck(workHours))
name, hours = employeeCheck(workHours)
print(f'name: {name}')
print(f'hours: {hours}')