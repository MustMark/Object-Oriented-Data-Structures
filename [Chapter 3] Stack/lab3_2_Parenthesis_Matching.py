check = input("Enter expresion : ")
stack = []
error = ""
open = 0
close = 0

for i in check:
    if i in "([{":
        stack.append(i)
        open += 1
    elif i in ")]}":
        if not stack:
            error = "close paren excess"
            break
        elif i == ")" and stack[-1] == "(":
            stack.pop()
        elif i == "]" and stack[-1] == "[":
            stack.pop()
        elif i == "}" and stack[-1] == "{":
            stack.pop()
        else:
            error = "Unmatch open-close"
            break
        close += 1

if error == "" and not stack:
    print(f"{check} MATCH")
elif error == "" and stack:
    error_stack = "".join(stack)
    print(f"{check} open paren excess   {len(stack)} : {error_stack}")
else:
    print(f"{check} {error}")