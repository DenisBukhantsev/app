def mnog(*args):

    uniqe = []
    for i in args:
        if i not in uniqe:
            uniqe.append(i)
    return uniqe
print(mnog(1,1,2,3,4,4,4,5,5,6))