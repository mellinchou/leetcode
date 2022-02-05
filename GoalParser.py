def interpret(command: str) -> str:
    final=""
    curr=command[0]
    for i in range (0, len(command)-1):
        next=command[i+1]
        if (curr=='G'): final=final+"G"
        elif (curr=='('):
            if (next==')'): final=final+"o"
            elif (next=='a'): final=final+"al"
        curr=next
    if (curr=='G'): final=final+"G"
    print(final)

interpret("G()(al)")
interpret("G()()()()(al)")
interpret("(al)G(al)()()G")