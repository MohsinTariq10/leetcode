def parens(n):
    if n == 0: return [""]
    if n == 1: return ["()"]
    l_paren = parens(n-1)
    res = set({})
    for l in l_paren:
        res.add("(" + l + ")")
        res.add("()" + l)
        res.add(l + "()")
    return res

print(parens(4))
