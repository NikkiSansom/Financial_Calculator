##### This is a program for a financial calculator for calculating either: ####
# 1. The amount of interest earned from an investment, or
# 2. The amount to be repaid on a home loan

import math

#### Financial Calculator Instructions for the user ####
print()
print("Financial Calculator")
print("*****")
print("There are two uses for this calculator:\n")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan\n")

# User selects either 'investment' or 'bond' (any capitalisation will work)
while True:
   calculator_use = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
   calculator_use = calculator_use.lower()

#### Investment Calculations ####
   if calculator_use == "investment":
      money_deposited = float(input("How much money are you depositing (£)?: "))
      interest_rate = float(input("What is the interest rate (%)? :"))
      num_years = int(input("How many years are you investing for?: "))

      while True:
         interest = input("Simple or Compound Interest?: ")
         interest = interest.lower()
         # Simple Interest Calculation
         if interest == "simple":
            investment_returns = money_deposited*(1 + ((interest_rate/100)*num_years))   # A = P * (1 + r*t)
            print("Investment Returns: " + "£" + str(round(investment_returns, 2)))
            print()
            break
                  # Compound Interest Calculation
         elif interest == "compound":
            investment_returns = money_deposited * math.pow((1+(interest_rate/100)), num_years)  # A = P * math.pow((1+r),t)
            print("Investment Returns: " + "£" + str(round(investment_returns, 2)))
            print()
            break
         # If anything but simple or compound are entered by the user:
         else:
            print("There was an error with your input, please try again.")
            continue
      break

#### Bond Calculations ####
   elif calculator_use == "bond":
      house_value = float(input("What is the present value of the house (£)?: "))
      interest_rate = float(input("What is the annual interest rate (%)? :"))
      repay_months = int(input("What is the number of months you plan to take to repay the bond?: "))
      monthly_interest = (interest_rate/100)/12
      repayment = (monthly_interest*house_value)/(1-((1 + monthly_interest)**(-1 * repay_months)))    # repayment = (i*P)/(1-((1+i)**(-n)))
      print("Monthly Repayments: " + "£" + str(round(repayment, 2)))
      print()
      break

   else:
      print("There was an error with your input, please try again.")
      continue