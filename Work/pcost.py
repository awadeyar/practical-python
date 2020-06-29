# pcost.py
#
# Exercise 1.27

with open('Data/portfolio.csv') as f:
    headers = next(f)
    totalAmount = 0.0
    for line in f:
        data = line.split(",")
        totalAmount = totalAmount + int(data[1]) * float(data[2])

    print(f'Total cost {totalAmount:0.2f}')


