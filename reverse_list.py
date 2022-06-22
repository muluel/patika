q=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def reverse(x):
    if type(x) == (list):
        x = [reverse(subx) for subx in x]
        x = x[::-1]
    return x

reverse(q)