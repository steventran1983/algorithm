

def fibonachi(n):
    if n ==0:
        return("please enter other number")
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n>2:
        return fibonachi(n -1) + fibonachi(n-2)

for n in range(1,100):
    print(fibonachi(n))