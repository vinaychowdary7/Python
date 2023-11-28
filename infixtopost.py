def notGreater(c,stack):
    precedence = {'+':1, '-':1, '*':2, '/':2, '%':2, '^':3}
    if stack[-1]=="(":
        return False
    a = precedence[c]
    b = precedence[stack[-1]] 
    if a  <= b:
        return True
    else:
        return False
def toPostfix(infix):
    stack = []
    postfix = ''

    for c in infix:
        if c.isalpha():
            postfix += c
        else:
            if c=="(":
                stack.append(c)
            elif c==")":
                operator = stack.pop()
                while operator!="(":
                    postfix += operator
                    operator = stack.pop()              
            else:
                while (len(stack)!=0) and notGreater(c,stack):
                    postfix += stack.pop()
                stack.append(c)

    while (len(stack)!=0):
        postfix += stack.pop()
    return postfix
i=input()
j=toPostfix(i)
print(j)