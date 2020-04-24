from collections import Counter
def runoff(voters):
    while voters and len(voters[0]) > 1:
        tally = Counter([b[0] for b in voters])
        kick = min(tally[v] for v in voters[0])
        for b in voters: b[:] = [v for v in b if tally[v] > kick]
    return voters[0][0] if voters[0] else None
