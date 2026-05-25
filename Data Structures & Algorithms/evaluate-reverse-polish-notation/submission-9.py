class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i.lstrip('-').isdigit():
                stack.append(int(i))
            else:
                num1=stack.pop()

                num2=stack.pop()
                if i=="+":
                  stack.append(num1+num2)
                if i=="-":
                  stack.append(num2-num1)
                if i=="*":
                  stack.append(num1*num2)
                if i=="/":
                  stack.append(int(num2/num1))
             
             
        return stack[0]
