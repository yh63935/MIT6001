# -*- coding: utf-8 -*-
"""
Calculate the number of months needed to pay the down payment of a house based
on your annual salary, percent of salary saved, and cost of dream home
"""

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04
months = 0
monthly_salary = annual_salary/12
monthly_salary_saved = monthly_salary*portion_saved

while current_savings < portion_down_payment:
    monthly_roi = current_savings*r/12
    current_savings += monthly_salary_saved + monthly_roi
    months+=1

print("Number of months:", months);
