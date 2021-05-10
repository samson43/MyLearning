# Calculate HRA, DA and PF to get Net Salary

basic_salary = int(input("Enter the Basic Salary:"))

hra_amount   = basic_salary * 0.43
pf_amount    = basic_salary * 0.12

net_salary   = basic_salary+hra_amount - pf_amount

print(f"HRA Amount : {hra_amount:5.0f}")
print(f"PF Amount  : {pf_amount:5.0f}")
print(f"           : -----")
print(f"Net Salary : {net_salary:5.0f}")


