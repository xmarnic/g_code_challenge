def ans(s):
    operands = []
    operators = []
    for c in s:
        if c in '*+':
            operators.insert(0, c)
        else:
            operands.append(c)

    return ''.join(operands + operators)

def answer(s):
    out = ''
    adds = ''
    muls = ''
    last = None
    for c in s:
        if c.isdigit():
            out += c
        else:
            if c == '+':
                adds += c
                if last == '*':
                    out += muls
                    muls = ''
                last = '+'
            else:
                muls += c
                last = '*'
    return (out + muls + adds)
