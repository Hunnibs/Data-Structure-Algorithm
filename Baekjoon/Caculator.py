'''
get_token_list(expr): expr은 문자열로 수식을 나타내므로 연산자와 피연산자로 나누어 리스트에 담아 리턴
infix_to_postfix(token_list): token_list를 postfix 수식으로 변환하고 그 결과를 리스트에 담아 리턴한다.
compute_postfix(token_list): postfix 형식의 token_list에 대한 계산 값을 리턴한다.
'''

class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)
  
    def isEmpty(self):
        return self.__len__() == 0
	
def get_token_list(expr):
    token_list = []
    tmp = ''
	
    for token in expr:
        if token == ' ':
            continue
	
        if token in '+-/*^()':  # 연산자 토큰
            if tmp != '':
                token_list.append(tmp)
                tmp = ''
            token_list.append(token)	
        else:  # 피연산자 토큰
            tmp += token
	
    if tmp != '':
        token_list.append(tmp)
	
    return token_list
	
def infix_to_postfix(token_list):
    opstack = Stack()
    outstack = []
		# 연산자의 우선순위 설정
    prec = {}
    prec['('] = 0
    prec['+'] = 1
    prec['-'] = 1
    prec['*'] = 2
    prec['/'] = 2
    prec['^'] = 3

    for token in token_list:
        if token == '(':
            opstack.push(token)
        elif token == ')':
            while opstack.top() != '(':
                outstack.append(opstack.pop())
            opstack.pop()
        elif token in '+-/*^':
            while not opstack.isEmpty():
                if prec[opstack.top()] >= prec[token]:
                    outstack.append(opstack.pop())
                else:
                    break
            opstack.push(token)
        else: # operand일 때
            outstack.append(token)

    # opstack 에 남은 모든 연산자를 pop 후 outstack에 append
    for i in range(0, opstack.__len__()):
      outstack.append(opstack.pop())

    return outstack
	
def compute_postfix(token_list):
    opstack = Stack()
	
    for token in token_list:
      if token in '+-/*^':
        a = float(opstack.pop())
        b = float(opstack.pop())
        if token == '+':
          tmp = a + b
        elif token == '-':
          tmp = b - a
        elif token == '/':
          tmp = b / a
        elif token == '*':
          tmp = b * a
        else:
          tmp = b ** a
	
        opstack.push(tmp)
      else:
        opstack.push(token)
	
    return opstack.pop()
	
# 아래 세 줄은 수정하지 말 것!
expr = input()
value = compute_postfix(infix_to_postfix(get_token_list(expr)))
print(value)