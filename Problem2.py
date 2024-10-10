'''
Approach 1
1. If the character is a digit, then add to the previous value by moving one decimal place. 
2. If it is a operator or End of the expression then compute value till now using last operator. 
3. Update the tail value at every step to undo it in case of * and /. Return the calculated value after evaluating entire expression.
 
TC: O(n)
SC: O(1)

Approach 2
1. If the character is a digit, then add to the previous value by moving one decimal place.
2. If the prev op is a + or - then simply append the value to the stack (tail).
3. When we encounter * or / oe end of exp, pop the top value from the stack, mul to or div by the cur number and append it back to the stack.
4. Finally add all the elements in the stack to get the calc value.

TC: O(n)
SC: O(n)
'''
# Approach 1
class Solution:
    def calculate(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0

        tail = 0
        num = 0
        calc = 0
        op = '+'
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = num * 10 + int(c)
            if (not c.isdigit() and c != ' ') or (i == len(s) - 1):
                if op == '+':
                    calc = calc + num
                    tail = +num
                elif op == '-':
                    calc = calc - num
                    tail = -num
                elif op == '*':
                    calc = calc - tail + (tail * num)
                    tail = tail * num
                elif op == '/':
                    calc = calc - tail + int(tail / num)
                    tail = int(tail / num)
                op = c
                num = 0

        return calc
    
# Approach 2
class Solution:
    def calculate(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0

        stack = []
        num = 0
        op = '+'
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = num * 10 + int(c)
            if (not c.isdigit() and c != ' ') or (i == len(s) - 1):
                if op == '+':
                    stack.append(num)
                if op == '-':
                    stack.append(-num)
                if op == '*':
                    top = stack.pop()
                    stack.append(top * num)
                if op == '/':
                    top = stack.pop()
                    stack.append(int(top / num))
                op = c
                num = 0
        return sum(stack)