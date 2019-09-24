from python_stack import Stack

def is_valid_parenthesis(str):
    stack = Stack()
    is_valid = True

    for i in range(0,len(str)):
        if str[i] in "{[(" and is_valid:
            stack.push(str[i])
        else:
            if stack.is_Empty():
                is_valid = False
            else:
                top = stack.pop()
                if not matching(top,str[i]):
                    is_valid = False
    return stack,is_valid

def matching(top,paren):
    if top == "(" and paren == ")":
        return True
    if top == "[" and paren == "]":
        return True
    if top == "{" and paren == "}":
        return True
    return False

stack,is_valid = is_valid_parenthesis("))((")
print(stack.items)
print(is_valid)
if stack.is_Empty() and is_valid:
    print("Valid")
else:
    print("inValid")