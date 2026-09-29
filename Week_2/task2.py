# Task 2: sum and average of the digits in a string

if __name__=="__main__": 
   def digit_sum_and_average(s1):
     digits = [int(ch) for ch in s1 if ch.isdigit()]

     if len(digits) == 0:
        return 0, 0

     total = sum(digits)
     average = total / len(digits)

     return total, average


s1 = input("Enter the string value: ")
total, average = digit_sum_and_average(s1)

print("Sum:", total)
print("Average:", average)

