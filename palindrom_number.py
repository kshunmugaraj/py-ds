"""
Input: N = 12321
Output: Yes
Explanation: 12321 is a Palindrome number because after reversing its digits, the number becomes 12321 which is same as the original number.

Input: N = 1234
Output: No
Explanation: 1234 is not a Palindrome number because after reversing its digits, the number becomes 4321 which is different from the original number.
"""
def check_palindrome(number:int)->bool:
    reverse=0
    temp = number    
    while temp !=0:
        reverse = reverse*10 + temp%10
        temp = temp//10        
    return reverse == number

number = 12321

if check_palindrome(number):
    print("Yes")
else:
    print("No")