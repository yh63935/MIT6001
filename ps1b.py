# -*- coding: utf-8 -*-
"""
Calculate the number of months for your house down payment, but factoring in a raise every 6 months
"""

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))

portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04
months = 0

while current_savings < portion_down_payment:
    monthly_salary = annual_salary/12
    monthly_salary_saved = monthly_salary*portion_saved
    monthly_roi = current_savings*r/12
    current_savings += monthly_salary_saved + monthly_roi
    months+=1
    
    """If months are divisible evenly by 6, increase the annual salary"""
    if months%6==0:
        annual_salary*=(1+semi_annual_raise)

print("Number of months:", months);