import math
n=int(input('enter the number of child nodes - '))
t=int(input('enter the tree depth - '))
scores=[]
for i in range(0,int(math.pow(n,t))):
    scores.append(int(input()))

def minmax(curr_depth,node_index,scores,tree_depth,maxturn):
    if curr_depth==tree_depth:
        return scores[node_index]
    if maxturn:
        a=-999
        for i in range(0,n):
            a= max(minmax(curr_depth+1,node_index*n+i,scores,tree_depth,False),a)
        return a
    else:
        a=999
        for i in range(0,n):
            a=min(minmax(curr_depth+1,node_index*n+i,scores,tree_depth,True),a)
        return a

print('optimal value is ',minmax(0,0,scores,t,False))