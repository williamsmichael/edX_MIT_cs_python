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


# 2 - paying debt off in a year - 15pts
# test case
balance = 594
annualInterestRate = 0.18

# -----------------submitted script below
month = 0
lowest = 0
minimum = 10
original = balance

def monthlyInterestRate(annualInterestRate):
    return annualInterestRate / 12.0
    
def monthlyUnpaidBalance(balance, minimum):
    return balance - minimum

def updatedBalanceEachMonth(unpaid, monthlyInterestRate):
    return unpaid + monthlyInterestRate * unpaid
    
monthlyInterestRate = monthlyInterestRate(annualInterestRate)

# run while loop for one year
while balance > 0:
    
    # reset if reach a year
    if month == 12:
        month = 0
        minimum += 10
        balance = original
        # print "---------------- $" + str(minimum)
        
    # call and bind the functions
    unpaid = monthlyUnpaidBalance(balance, minimum)
    print(str(month) + "|" + str(unpaid))
    balance = updatedBalanceEachMonth(unpaid, monthlyInterestRate)
    
    # increment month
    month += 1
    
lowest = minimum
print(lowest)
print "Lowest Payment:", int(lowest / 10) * 10