def oneaway(s1, s2):
    m, n = len(s1), len(s2)
    # replace
    if m == n :
        return one_replace(s1, s2)
    elif m+1 ==n:
        return one_add_remove(s1, s2)
    elif n+1 ==m:
        return one_add_remove(s2, s1)

def one_replace(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
            if count > 1:
                return False
    return True

def one_add_remove(s1, s2):
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if i != j:
                return False
            j += 1
        else:
            i += 1
            j += 1
    return True