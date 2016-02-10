# Your task is to change the definition of SimpleDivide so that the call does not raise an exception. When dividing by 0, FancyDivide should return a list with all 0 elements. Any other error cases should still raise exceptions. You should only handle the ZeroDivisionError.

def FancyDivide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [SimpleDivide(item, denom)
               for item in list_of_numbers]
               
def SimpleDivide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0
        
FancyDivide([0, 2, 4], 0) # return [0, 0, 0]
FancyDivide([0, 2, 4], 1) # return [0, 1, 2]