candidate_vote={
    "m":5,
    "n":5,
    "m":5,
    "j":1
}

def add_vote(name:str):
    if candidate_vote.get(name):
        candidate_vote[name]+=1
        return True
    return "invalid ballot"

def print_winner():
    max_vote=max(list(candidate_vote.values()))
    for k,v in candidate_vote.items():
        if v==max_vote:
            print(k)
# print_winner()
# print(add_vote("m"))