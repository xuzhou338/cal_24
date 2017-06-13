def adjust(methods):
    """This function eliminates the methods with same operation combinations"""
    method_adj = []
    for method in methods:
        if method[1] not in method_adj:
            method_adj.append(method[0])
            method_adj.append(method[1])
    return method_adj

def translate(methods):
    """Translate from the method list into readable equations."""
    method_adj = adjust(methods)
    ans_eqs = []
    for x in range(int(len(method_adj)/2)):
        num = method_adj[x*2]
        op = method_adj[x*2+1]
        if len(op) == 3:
            ans_eq = ' '.join([str(num[0]), op[0], str(num[1]), op[1],
                               str(num[2]), op[2], str(num[3]), '= 24'])
        elif len(op) == 5:
            ans_eq = ' '.join([op[0], str(num[0]), op[1], str(num[1]), op[2],
                               str(num[2]), op[3], op[4], str(num[3]), '= 24'])
        elif len(op) == 7:
            ans_eq = ' '.join([op[0], str(num[0]), op[1], str(num[1]), op[2],
                               op[3], op[4], str(num[2]), op[5], str(num[3]),
                               op[6], '= 24'])
        ans_eqs.append(ans_eq)

    return ans_eqs