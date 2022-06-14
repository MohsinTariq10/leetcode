'''
    This is signature of helper function 'knows'.
    You should not implement it, or speculate about its implementation.

    def knows(int A, int B); 
    Function 'knows(A, B)' will returns "true" if the person having
    id 'A' knows the person having id 'B' in the party, "false" otherwise.
'''

def findCelebrity(n, knows):

    # Write your code here.
    celeb = [x for x in range(n)]
    
    while (len(celeb) >1):
        a = celeb[0]
        b = celeb[1]
        if knows(a,b):
            celeb.pop(0)
        else:
            celeb.pop(1)
    
    
    if len(celeb) == 1:
        for i in range(n):
            if (i != celeb[0]):
                if (not knows(i, celeb[0]) or knows(celeb[0], i)):
                    return -1
        return celeb[0]
    else:
        return -1