def iterative_answer(s):
    precedence = {'+' : 0, '*': 1}
    output, operators = [], []
    for c in s:
        if c.isdigit():
            output.append(c)
        elif not operators:
            operators.insert(0, c)
            precedenceLevel = precedence[c]
        else:
            if precedence[c] < precedence[operators[0]]:
                while (operators
                        and precedence[operators[0]] == precedenceLevel):
                    output.append(operators.pop(0))
            operators.insert(0, c)
            precedenceLevel = precedence[c]
    return ''.join(output + operators)

def answer(s):
    def RPN(s, out, ops, precedence):
        if not s:
            return ''.join(out + ops)
        elif not s[0].isdigit():
            if ops and precedence[s[0]] < precedence[ops[0]]:
                while ops and precedence[ops[0]] == precedence['current']:
                    out.append(ops.pop(0))
            ops.insert(0, s[0])
            precedence['current'] = precedence[s[0]]
        else:
            out.append(s[0])
        return RPN(s[1:], out, ops, precedence)

    precedence = {'+' : 0, '*' : 1, 'current' : 0}
    return RPN(s, [], [], precedence)
