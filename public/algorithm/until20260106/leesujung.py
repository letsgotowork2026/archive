n = int(input())

m_vote = []

for i in range(n):
    m_vote.append(int(input()))


def findBiggestIndex(vote_list:list): 
    max_idx = 0
    for i in range(n):
        if vote_list[max_idx] <= vote_list[i]:
            max_idx = i
    return max_idx

def calculate_vote(vote_list:list):
    ans = 0

    if findBiggestIndex(vote_list) == 0:
        ans = 0
        print(ans)
        return   
        
    if n == 1:
        print(ans)
        return
    else :
        count = 0
        copy_vote = m_vote[1:n+1]
        while True:
            count += 1
            copy_vote[copy_vote.index(max(copy_vote))] -= 1
            m_vote[0] += 1
            if m_vote[0] > max(copy_vote):
                print(count)
                break

calculate_vote(m_vote)
        
