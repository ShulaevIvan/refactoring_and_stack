
class Stack:
    def __init__(self, inner_str='()'):
        self.validate = True 
        self.stack = list()
        self.inner_str = inner_str
    
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    
    def push(self, value):
        self.value = value
        self.stack.append(value)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def size(self):
        self.length = len(self.stack)
        return self.length
    
 
stack = Stack()
var_string = Stack('[([])((([[[]]])))]{()}').inner_str

for i in var_string:
    if i in '([{':
        stack.push(i)
    elif i in ')]}':
        if stack.size() == 0:
            validate = False
            break
        j = stack.pop()
        if j == '(' and i == ')':
           continue
        elif j == '[' and i == ']':
            continue
        elif j == '{' and i == '}':
            continue
    
        validate = False
        break

if stack.validate and stack.size() == 0:
    
    print("Сбалансированно")
else:
    print("Несбалансированно")

        

