# # 1 - paying the minimum - 10pts
# # test case
# balance = 4213
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04

# # -----------------submitted script below
# month = 1
# paid = 0

# def monthlyInterestRate(annualInterestRate):
#     return annualInterestRate / 12.0
    
# def minimumMonthlyPayment(monthlyPaymentRate, balance):
#     return monthlyPaymentRate * balance
    
# def monthlyUnpaidBalance(balance, minimum):
#     return balance - minimum

# def updatedBalanceEachMonth(unpaid, monthlyInterestRate):
#     return unpaid + monthlyInterestRate * unpaid

# monthlyInterestRate = monthlyInterestRate(annualInterestRate)
    
# # run while loop for one year
# while month <= 12:
    
#     # call and bind the functions
#     minimum = minimumMonthlyPayment(monthlyPaymentRate, balance)
#     unpaid = monthlyUnpaidBalance(balance, minimum)
#     balance = updatedBalanceEachMonth(unpaid, monthlyInterestRate)
    
#     # increment paid total
#     paid += minimum
    
#     print "Month:", str(month) + \
#     "\nMinimum monthly payment:", str(format(minimum, '.2f')) + \
#     "\nRemaining Balance:", str(format(balance, '.2f')) 
    
#     # increment month
#     month += 1
    
# print "Total paid:", str(format(paid, '.2f')) + \
# "\nRemaining balance:", str(format(balance, '.2f'))


# # 2 - paying debt off in a year - 15pts
# # test case
# balance = 799
# annualInterestRate = 0.2

# # -----------------submitted script below
# month = 0
# lowest = 0
# minimum = 10
# original = balance

# def monthlyInterestRate(annualInterestRate):
#     return annualInterestRate / 12.0
    
# def monthlyUnpaidBalance(balance, minimum):
#     return balance - minimum

# def updatedBalanceEachMonth(unpaid, monthlyInterestRate):
#     return unpaid + monthlyInterestRate * unpaid
    
# monthlyInterestRate = monthlyInterestRate(annualInterestRate)

# # run while loop for one year
# while balance > 0:
    
#     # reset if reaches 12-month span
#     if month == 12:
#         month = 0
#         minimum += 10
#         balance = original
#         # print "---------------- $" + str(minimum)
        
#     # call and bind the functions
#     unpaid = monthlyUnpaidBalance(balance, minimum)
#     print(str(month) + "|" + str(unpaid))
#     balance = updatedBalanceEachMonth(unpaid, monthlyInterestRate)
    
#     # increment month
#     month += 1
    
# lowest = minimum
# print "Lowest Payment:", lowest


# 3 - Using bisection search to make the program faster - 25pts
# test case
balance = 999999
annualInterestRate = 0.18

# -----------------submitted script below
def monthlyInterestRate(annualInterestRate):
    return annualInterestRate / 12.0
    
def monthlyPaymentLowerBound(balance):
    return balance / 12
    
def monthlyPaymentUpperBound(balance, monthlyInterestRate):
    return (balance * (1 + monthlyInterestRate) ** 12) / 12.0
    
def monthlyUnpaidBalance(balance, minimum):
    return balance - minimum

def updatedBalanceEachMonth(unpaid, monthlyInterestRate):
    return unpaid + monthlyInterestRate * unpaid
    
month = 0
unpaid = balance
original = balance
epsilon = 0.01
monthlyInterestRate = monthlyInterestRate(annualInterestRate)
lower = monthlyPaymentLowerBound(balance)
upper = monthlyPaymentUpperBound(balance, monthlyInterestRate)
minimum = (lower + upper) / 2.0

# run while loop for one year
while abs(unpaid) >= epsilon:
    
    # reset if reaches 12-month span
    if month == 12:
        print "-----------------------------" + str(lower) + " | " + str(upper) + " = " + str(minimum)
        if unpaid > 0:
            lower = minimum
        else:
            upper = minimum
        minimum = (lower + upper) / 2
        month = 0
        balance = original
        # print "---------------- $" + str(minimum)
        
    # call and bind the functions
    unpaid = monthlyUnpaidBalance(balance, minimum)
    print(str(month) + "|" + str(unpaid))
    balance = updatedBalanceEachMonth(unpaid, monthlyInterestRate)
    
    # increment month
    month += 1
    
lowest = minimum
print "Lowest Payment: " + str(format(lowest, '.2f'))