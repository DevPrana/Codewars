def solution(string,markers):
    string= string.split("\n")
    lst=[]
    lst1=[]
    for elems in string:
        word=[]
        for e in elems:
            if e not in markers:
                word.append(e)
            else: break
        lst.append(word)
    for elems in lst:
        lst1.append(''.join(elems).rstrip())
    return "\n".join(lst1)
