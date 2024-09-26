# Monthly Salary Input
print("You are now applying for a loan")
MonthlySalary = int(input("What is your monthly salary? "))

# Loan Elegibility
if MonthlySalary >= 30000.00:
    LoanAmount = int(input("How much will you loan? "))
else:
    print("You are not eligible for a loan.")

if LoanAmount <= MonthlySalary * 10:
    print("You are eligible for a loan.")
else:
    print("Loan request too high/low.")

# Interest
Months = int(input("How many months to pay? "))
Interest = LoanAmount * 0.10
NewLoanAmount = LoanAmount + Interest 
Payable = NewLoanAmount / Months
print("Interest =", Interest)
print("New Loan Amount =", NewLoanAmount)
print("Payable =", Payable)