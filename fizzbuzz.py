# Write a program that outputs the string representation of numbers from 1 to n.
# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
# For numbers which are multiples of both three and five output “FizzBuzz”

num = input("Enter n: ")

if int(num) == 0:
    print("please enter other number")
arr = []
for i in range(1, int(num)+1):
    if i%15 == 0:
        arr.append("FizzBuzz")
    elif i%5 == 0:
        arr.append("Buzz")
    elif i%3 == 0:
        arr.append("Fizz")
    else:
        arr.append(str(i))
for element in arr:
    print(element)