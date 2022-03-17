def scoreOfParentheses(s: str) -> int:
    stack=[0]
    for char in s:
        if char=='(':
            stack.append(0)
        else: # 把最後一個取出來乘以二再加回上一個 element
            prev=stack.pop()*2
            stack[-1]+=max(1, prev)
    return stack[0]

