salary_1 = int(input("enter your first month's salary"))
salary_2 = int(input("enter the salary for the second month"))
salary_3 = int(input("enter the salary for the third month"))

single_tax = (salary_1 + salary_2 + salary_3) * (1/20)

ssc = 4422

total = single_tax + ssc
print(total)
