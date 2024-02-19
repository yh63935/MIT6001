# -*- coding: utf-8 -*-
"""
Find the savings rate to achieve the down payment in 36 months
"""
annual_salary = float(input("Enter your annual salary: "))
total_cost = 1000000
semi_annual_raise = 0.07

epsilon = 100
low = 0
high = 10000
guess = (low + high) / 2
portion_down_payment = 0.25 * total_cost
print("down payment: ", portion_down_payment)
r = 0.04
steps = 0
current_savings = 0
while abs(current_savings - portion_down_payment) >= epsilon:
    months = 0
    current_savings = 0
    while months <= 36:
        monthly_salary = annual_salary / 12
        print("guess for rate", guess / 10000)
        monthly_salary_saved = monthly_salary * guess / 10000
        monthly_roi = current_savings * r / 12
        current_savings += monthly_salary_saved + monthly_roi
        print("current savings at month: ", current_savings, months)
        print("is current savings greater than down payment: ", current_savings < portion_down_payment)
        months += 1

        """If months are divisible evenly by 6, increase the annual salary"""
        if months % 6 == 0:
            annual_salary *= (1 + semi_annual_raise)

    if current_savings < portion_down_payment:
        low = guess
    else:
        high = guess
    guess = (low + high) / 2
    steps += 1

print("Best savings rate: ", guess / 10000)
print("Steps in bisection search", steps)
