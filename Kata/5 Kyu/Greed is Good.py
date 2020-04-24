def score(dice):
    from collections import Counter
    x=Counter(dice)
    score=0
    for elem in x:
       
        if elem==1:
            score+=(x[elem]//3)*1000
            score+=(x[elem]%3)*100
        elif elem==5:
            score+=(x[elem]//3)*100*elem
            score+=(x[elem]%3)*50
        else: score+=(x[elem]//3)*100*elem   
    return score 
