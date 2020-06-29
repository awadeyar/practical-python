# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.1
total_paid = 0.0
months = 1

while principal > 0:
    if months < 13:
        payment = payment + 1000

    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
    months = months + 1

print(f'${total_paid:0.2f}, {months}')