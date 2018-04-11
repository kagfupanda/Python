#Siddharth Srinivasan
#Lab section 061
import math

print("Welcome to the Student Loan Calculator")
principle = int(input("Enter the amount of the loan in dollars with (no commas):\n")) #user input for principle
years = int(input("Enter the number of years the loan will be for:\n")) #amount of years
print("--------------------------------------------")
def subsidized_federal_direct(principle, years): #function to calcluate subsidized federal loans
    ir = round(0.034,3)
    feerate = 0.01051
    t = 12
    monthly_payment = (principle * ir)/(t * (1 - (math.pow(1+ir/t, (-years * t)))))
    total_paid_on_loan = monthly_payment * t * years
    interest_paid = total_paid_on_loan - principle
    additional_fees = round(principle * feerate, 3)
    total_cost = round(additional_fees + interest_paid, 2)
    print("Subsidized Federal Direct Loan")
    print('Principal: ', principle)
    print("Interest Rate: ", round(ir * 100,2))
    print("Years: ", years)
    print("Monthly Payment: ", round(monthly_payment, 2))
    print("Total Paid On Loan: ", round(total_paid_on_loan,2))
    print("Total Interest Paid: ", round(interest_paid,2))
    print("Additional Fees Paid: ", round(additional_fees,2))
    print("Total Costs over Principal", round(total_cost,2))
    return
def unsubsidized_federal_direct(principle, years): #calculate unsubsidized federal direct loans
    ir = round(0.068, 3)
    new_principle = principle * (1 + ir * 4.25)
    feerate = 0.01051
    t = 12
    monthly_payment = (new_principle * ir) / (t * (1 - (math.pow(1 + ir / t, (-years * t)))))
    total_paid_on_loan = monthly_payment * t * years
    interest_paid = total_paid_on_loan - principle
    additional_fees = principle * feerate
    total_cost = additional_fees + interest_paid
    print("Unsubsidized Federal Direct Loan")
    print('Principal: ', principle)
    print("Interest Rate: ", round(ir * 100, 2))
    print("Years: ", years)
    print("Monthly Payment: ", round(monthly_payment, 2))
    print("Total Paid On Loan: ", round(total_paid_on_loan, 2))
    print("Total Interest Paid: ", round(interest_paid, 2))
    print("Additional Fees Paid: ", round(additional_fees, 2))
    print("Total Costs over Principal", round(total_cost, 2))
    return
def federal_plus_loan(principle, years): #function to calculate federal plus loan
    ir = round(0.079, 3)
    new_principle = principle * (1 + ir * 4.25)
    feerate = 0.04204
    t = 12
    monthly_payment = (new_principle * ir) / (t * (1 - (math.pow(1 + ir / t, (-years * t)))))
    total_paid_on_loan = monthly_payment * t * years
    interest_paid = total_paid_on_loan - principle
    additional_fees = principle * feerate
    total_cost = additional_fees + interest_paid
    print("Federal Plus Loan")
    print('Principal: ', principle)
    print("Interest Rate: ", round(ir * 100, 2))
    print("Years: ", years)
    print("Monthly Payment: ", round(monthly_payment, 2))
    print("Total Paid On Loan: ", round(total_paid_on_loan, 2))
    print("Total Interest Paid: ", round(interest_paid, 2))
    print("Additional Fees Paid: ", round(additional_fees, 2))
    print("Total Costs over Principal", round(total_cost, 2))
    return
subsidized_federal_direct(principle, years)
print("--------------------------------------------")
unsubsidized_federal_direct(principle, years)
print("--------------------------------------------")
federal_plus_loan(principle, years)
