def sum_of_intervals(intervals):
    lst=[]
    for elem in intervals:
        for i in range(elem[0],elem[1]):
            if i not in lst:
                lst.append(i)
    return len(lst)
