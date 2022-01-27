import math
n=int(input('enter the number of child nodes - '))
t=int(input('enter the tree depth - '))
alpha=-999
beta=999
scores=[]
print("enter the leaf node values")
for i in range(0,int(math.pow(n,t))):
    scores.append(int(input()))

def alphabeta(curr_depth,node_index,maxturn,scores,alpha,beta):
    if curr_depth==t:
        return scores[node_index]
    if maxturn:
        v=-999
        for i in range(0,n):
            v=max(v,alphabeta(curr_depth+1,node_index*n+i,False,scores,alpha,beta))
            if v>=beta:
                return beta
            alpha=max(alpha,v)
        return v
    else:
        v=999
        for i in range(0,n):
            v=min(alphabeta(curr_depth+1,node_index*n+i,True,scores,alpha,beta),v)
            if v<=alpha:
                return v
            beta=min(beta,v)
        return v

print('optimal value is ',alphabeta(0,0,True,scores,alpha,beta))