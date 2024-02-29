annual_salary = float(input("Enter your annual salary: "))
total_cost = 1000000
semi_annual_raise = 0.07
original_salary = annual_salary

epsilon = 100
low = 0
high = 10000
guess = (low + high) / 2
portion_down_payment = 0.25 * total_cost
print("down payment: ", portion_down_payment)
r = 0.04
steps = 0
current_savings = 0

while abs(current_savings - portion_down_payment) > epsilon:
    steps += 1
    print('steps',steps)
    months = 0
    current_savings = 0
    annual_salary = original_salary
    monthly_salary = annual_salary / 12
    monthly_salary_saved = monthly_salary * guess / 10000
    while months < 36:
        monthly_roi = (current_savings) * r / 12
        current_savings += monthly_salary_saved + monthly_roi
        months += 1

        """If months are divisible evenly by 6, increase the annual salary"""
        if months % 6 == 0:
            annual_salary *= (1 + semi_annual_raise)
            monthly_salary = annual_salary / 12
            monthly_salary_saved = monthly_salary * guess / 10000
    if current_savings < portion_down_payment:
        low = guess
    else:
        high = guess
    guess = int(round((low + high) / 2))
    # if low is greater or equal to high, there is no more search area to be halved
    if low>=high:
        break;
if abs(current_savings - portion_down_payment) < epsilon:
    print("Best savings rate: ", guess/10000)
    print("Steps in bisection search", steps);
else: 
    print("It is not possible to pay the down payment in three years.")

