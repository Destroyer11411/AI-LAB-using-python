# graph = {
#     1:[2,3,4],
#     2:[5,6],
#     3:[7],
#     4:[],
#     5:[],
#     6:[8],
#     7:[],
#     8:[9],
#     9:[10],
#     10:[]
# }


# ser = int(input("Enter the search element\n"))
# lim = int(input("Enter the search limit\n"))
# visited=[]

# def dls(src,ser,lim):
#     if src not in visited:
#         visited.append(src)

#     if ser==src:
#         return True

#     if lim<=0:
#         return False

#     for i in graph[src]:
#         if (dls(i,ser,lim-1)):
#             return True
#     return False


# if (dls(1,ser,lim)):
#     print("The element was found\n")
# else:
#     print("The element was not found\n")

# print("The search path was\n")

# for i in visited:
#     print(f"{i}-->",end=" ")


# graph = {
#     1:[2,3,4],
#     2:[5,6],
#     3:[7],
#     4:[8,9],
#     5:[10],
#     6:[],
#     7:[],
#     8:[],
#     9:[],
#     10:[]
# }


# ser = int(input("Enter the search element\n"))
# lim = int(input("Enter the search limit\n"))
# visited=[]

# def dls(src,ser,lim):
#     if src not in visited:
#         visited.append(src)

#     if ser==src:
#         return True

#     if lim<=0:
#         return False

#     for i in graph[src]:
#         if(dls(i,ser,lim-1)):
#             return True
#     return False


# if (dls(1,ser,lim)):
#     print("The element was found\n")

# else:
#     print("Element was not found\n")

# print("The search path is\n")
# for i in visited:
#     print(f"{i}-->",end=" ")


# graph = {
#     1:[2,3,4],
#     2:[5,6],
#     3:[7],
#     4:[8,9],
#     5:[10],
#     6:[],
#     7:[],
#     8:[],
#     9:[],
#     10:[]
# }

# ser = int(input("Enter the search element\n"))
# lim = int(input("Enter the saerch limit\n"))
# visited = []

# def dls(src,ser,lim):
#     if src not in visited:
#         visited.append(src)
#     if ser==src:
#         return True
#     if lim<=0:
#         return False
#     for i in graph[src]:
#         if (dls(i,ser,lim)):
#             return True
#     return False

# if (dls(1,ser,lim)):
#     print("The element was found\n")

# else:
#     print("The element was not found\n")

# print("The saerch path is\n")
# for i in visited:
#     print(f"{i}-->",end=" ")


# graph={
#     'arad':{'zerind':75,'sibiu':140,'timisoara':118},
#     'zerind':{'arad':75,'oradea':71},
#     'oradea':{'zerind':71,'sibiu':151},
#     'timisoara':{'arad':118,'lugoj':111},
#     'sibiu':{'arad':140,'oradea':151,'fagaras':99,'rimnicu vilcea':80},
#     'lugoj':{'timisoara':111,'mehadia':70},
#     'fagaras':{'sibiu':99,'bucharest':211},
#     'rimnicu vilcea':{'sibiu':80,'pitesti':97,'craiova':146},
#     'mehadia':{'lugoj':70,'dobreta':75},
#     'dobreta':{'mehadia':75,'craiova':120},
#     'bucharest':{'fagaras':211,'pitesti':101,'urziceni':85,'giurglu':90},
#     'giurglu':{'bucharest':90},
#     'pitesti':{'bucharest':101,'craiova':138,'rimnicu vilcea':97},
#     'craiova':{'dobreta':120,'rimnicu vilcea':146,'pitesti':138},
#     'urziceni':{'hirsova':98,'vaslui':142,'bucharest':85},
#     'hirsova':{'urziceni':98,'eforie':86},
#     'vaslui':{'urziceni':142,'lasi':92},
#     'lasi':{'vaslui':92,'neamt':87},
#     'eforie':{'hirsova':86},
#     'neamt':{'lasi':87}
# }

# frontier = []
# flag=0

# def ucs(goal):
#     global frontier
#     global flag

#     if frontier:
#         node_p = sorted(frontier)[0]
#         frontier.remove(node_p)
#         node = node_p[1]
#         cost = node_p[0]

#         for a in graph[node]:
#             frontier.append((cost+graph[node][a],a))

#             if (a==goal):
#                 print("Found the city\n")
#                 print(f"cost {cost+graph[node][a]}")
#                 flag=1

#         if (flag!=1):
#             ucs(goal)

# ser = input("Enter the search element\n")
# src = input("Enter the starting element\n")

# frontier.append((0,src))

# ucs(ser)


# graph={
#     'arad':{'zerind':75,'sibiu':140,'timisoara':118},
#     'zerind':{'arad':75,'oradea':71},
#     'oradea':{'zerind':71,'sibiu':151},
#     'timisoara':{'arad':118,'lugoj':111},
#     'sibiu':{'arad':140,'oradea':151,'fagaras':99,'rimnicu vilcea':80},
#     'lugoj':{'timisoara':111,'mehadia':70},
#     'fagaras':{'sibiu':99,'bucharest':211},
#     'rimnicu vilcea':{'sibiu':80,'pitesti':97,'craiova':146},
#     'mehadia':{'lugoj':70,'dobreta':75},
#     'dobreta':{'mehadia':75,'craiova':120},
#     'bucharest':{'fagaras':211,'pitesti':101,'urziceni':85,'giurglu':90},
#     'giurglu':{'bucharest':90},
#     'pitesti':{'bucharest':101,'craiova':138,'rimnicu vilcea':97},
#     'craiova':{'dobreta':120,'rimnicu vilcea':146,'pitesti':138},
#     'urziceni':{'hirsova':98,'vaslui':142,'bucharest':85},
#     'hirsova':{'urziceni':98,'eforie':86},
#     'vaslui':{'urziceni':142,'lasi':92},
#     'lasi':{'vaslui':92,'neamt':87},
#     'eforie':{'hirsova':86},
#     'neamt':{'lasi':87}
# }


# frontier=[]
# flag=0

# def ucs(goal):
#     global frontier
#     global flag

#     if frontier:
#         node_p = sorted(frontier)[0]
#         frontier.remove(node_p)

#         node = node_p[1]
#         cost = node_p[0]

#         for a in graph[node]:
#             frontier.append((cost+graph[node][a],a))

#             if (a==goal):
#                 print("The element was found\n")
#                 print(f"The cost is {cost+graph[node][a]}")
#                 flag = 1
#         if (flag!=1):
#             ucs(goal)


# ser = input("Enter the search city\n")
# start = input("Enter the starting city\n")
# frontier.append((0,start))
# ucs(ser)


# graph={
#     'arad':{'zerind':75,'sibiu':140,'timisoara':118},
#     'zerind':{'arad':75,'oradea':71},
#     'oradea':{'zerind':71,'sibiu':151},
#     'timisoara':{'arad':118,'lugoj':111},
#     'sibiu':{'arad':140,'oradea':151,'fagaras':99,'rimnicu vilcea':80},
#     'lugoj':{'timisoara':111,'mehadia':70},
#     'fagaras':{'sibiu':99,'bucharest':211},
#     'rimnicu vilcea':{'sibiu':80,'pitesti':97,'craiova':146},
#     'mehadia':{'lugoj':70,'dobreta':75},
#     'dobreta':{'mehadia':75,'craiova':120},
#     'bucharest':{'fagaras':211,'pitesti':101,'urziceni':85,'giurglu':90},
#     'giurglu':{'bucharest':90},
#     'pitesti':{'bucharest':101,'craiova':138,'rimnicu vilcea':97},
#     'craiova':{'dobreta':120,'rimnicu vilcea':146,'pitesti':138},
#     'urziceni':{'hirsova':98,'vaslui':142,'bucharest':85},
#     'hirsova':{'urziceni':98,'eforie':86},
#     'vaslui':{'urziceni':142,'lasi':92},
#     'lasi':{'vaslui':92,'neamt':87},
#     'eforie':{'hirsova':86},
#     'neamt':{'lasi':87}
# }


# frontier=[]
# flag=0

# def ucs(goal):
#     global frontier
#     global flag

#     if frontier:
#         node_p = sorted(frontier)[0]
#         frontier.remove(node_p)
#         node = node_p[1]
#         cost = node_p[0]

#         for i in graph[node]:
#             frontier.append((cost+graph[node][i],i))

#             if (i==goal):
#                 print("Path found\n")
#                 print(f"cost {cost+graph[node][i]}")
#                 flag=1
#         if flag!=1:
#             ucs(goal)


# ser = input("Enter the city name to be searched\n")
# start  = input("Enter the starting city name\n")
# frontier.append((0,start))
# ucs(ser)


# graph = {
#     1:[2,3,4],
#     2:[5,6],
#     3:[7],
#     4:[8,9],
#     5:[10],
#     6:[],
#     7:[],
#     8:[],
#     9:[],
#     10:[]
# }
# visited = []

# def dls(src,ser,lim):
#     if src not in visited:
#         visited.append(src)

#     if src == ser:
#         return True

#     if lim<=0:
#         return False

#     for i in graph[src]:
#         if ( dls(i,ser,lim-1)):
#             return True
#     return False

# ser = int(input("Enter the element to be saerched\n"))
# lim = int(input("enter the saerch limit\n"))

# if(dls(1,ser,lim)):
#     print("The element was found\n")
# else:
#     print("The element was not found\n")

# print("search path\n")
# for i in visited:
#     print(f"{i}-->",end=" ")


# graph={
#     'arad':{'zerind':75,'sibiu':140,'timisoara':118},
#     'zerind':{'arad':75,'oradea':71},
#     'oradea':{'zerind':71,'sibiu':151},
#     'timisoara':{'arad':118,'lugoj':111},
#     'sibiu':{'arad':140,'oradea':151,'fagaras':99,'rimnicu vilcea':80},
#     'lugoj':{'timisoara':111,'mehadia':70},
#     'fagaras':{'sibiu':99,'bucharest':211},
#     'rimnicu vilcea':{'sibiu':80,'pitesti':97,'craiova':146},
#     'mehadia':{'lugoj':70,'dobreta':75},
#     'dobreta':{'mehadia':75,'craiova':120},
#     'bucharest':{'fagaras':211,'pitesti':101,'urziceni':85,'giurglu':90},
#     'giurglu':{'bucharest':90},
#     'pitesti':{'bucharest':101,'craiova':138,'rimnicu vilcea':97},
#     'craiova':{'dobreta':120,'rimnicu vilcea':146,'pitesti':138},
#     'urziceni':{'hirsova':98,'vaslui':142,'bucharest':85},
#     'hirsova':{'urziceni':98,'eforie':86},
#     'vaslui':{'urziceni':142,'lasi':92},
#     'lasi':{'vaslui':92,'neamt':87},
#     'eforie':{'hirsova':86},
#     'neamt':{'lasi':87}
# }


# frontier =[]
# flag =0

# def ucs(goal):
#     global frontier
#     global flag

#     if frontier:
#         node_p = sorted(frontier)[0]
#         frontier.remove(node_p)
#         node = node_p[1]
#         cost = node_p[0]

#         for i in graph[node]:
#             frontier.append((cost+graph[node][i],i))

#             if (i==goal):
#                 print("Element was found\n")
#                 print(f"cost: {cost+graph[node][i]}")
#                 flag = 1
#         if flag!=1:
#             ucs(goal)


# ser = input("Enter the city to be  saerched\n")
# src = input("Enter the starting city\n")

# frontier.append((0,src))

# ucs(ser)




# graph = {
#     'arad': {'zerind': 75, 'sibiu': 140, 'timisoara': 118},
#     'zerind': {'arad': 75, 'oradea': 71},
#     'oradea': {'zerind': 71, 'sibiu': 151},
#     'timisoara': {'arad': 118, 'lugoj': 111},
#     'sibiu': {'arad': 140, 'oradea': 151, 'rimnicu vilcea': 80, 'fagaras': 99},
#     'lugoj': {'timisoara': 111, 'mehadia': 70},
#     'fagaras': {'sibiu': 99, 'bucharest': 211},
#     'rimnicu vilcea': {'sibiu': 80, 'pitesti': 97, 'craiova': 146},
#     'mehadia': {'lugoj': 70, 'dobreta': 75},
#     'dobreta': {'mehadia': 75, 'craiova': 120},
#     'bucharest': {'fagaras': 211, 'pitesti': 101, 'urziceni': 85, 'giurglu': 90},
#     'giurglu': {'bucharest': 90},
#     'pitesti': {'bucharest': 101, 'craiova': 138, 'rimnicu vilcea': 97},
#     'craiova': {'dobreta': 120, 'rimnicu vilcea': 146, 'pitesti': 138},
#     'urziceni': {'hirsova': 98, 'vaslui': 142, 'bucharest': 85},
#     'hirsova': {'urziceni': 98, 'eforie': 86},
#     'vaslui': {'urziceni': 142, 'lasi': 92},
#     'lasi': {'vaslui': 92, 'neamt': 87},
#     'eforie': {'hirsova': 86},
#     'neamt': {'lasi': 87}
# }
# sld = {
#     'arad': 366,
#     'zerind': 374,
#     'oradea': 380,
#     'timisoara': 329,
#     'sibiu': 253,
#     'lugoj': 244,
#     'fagaras': 176,
#     'rimnicu vilcea': 193,
#     'mehadia': 241,
#     'dobreta': 242,
#     'bucharest': 0,
#     'giurglu': 77,
#     'pitesti': 100,
#     'craiova': 160,
#     'urziceni': 80,
#     'hirsova': 151,
#     'vaslui': 199,
#     "lasi": 226,
#     'eforie': 161,
#     'neamt': 234
# }

# frontier=[]
# flag=0

# def astar(start,goal):
#     global frontier
#     global flag
#     global graph
#     frontier.append((0+sld[start],[start]))
#     while frontier:
#         node_p = sorted(frontier)[0]
#         node = node_p[1] [len(node_p[1])-1]
#         cost = node_p[0] - sld[node]
#         frontier.remove(node_p)

#         if goal in node_p[1]:
#             print("Path found\n")
#             print(f"cost {str(node_p[0])}")
#             break
#         for i in graph[node]:
#             temp = node_p[1][:]
#             temp.append(i)
#             frontier.append((cost+graph[node][i]+sld[i],temp))

# start = input("Enter the start city\n")
# goal = input("enter the city to be saerched\n")
# astar(start,goal)

# frontier = []
# flag = 0


# def astar(goal):
#     global frontier
#     global flag

#     if frontier:
#         node_p = sorted(frontier)[0]
#         frontier.remove(node_p)

#         node = node_p[1]
#         cost = node_p[0] 
        
#         for a in graph[node]:
#             frontier.append((cost+graph[node][a],a))
            
            

#             if a==goal:
#                 print("Found the city\n")
#                 print(f"cost is {cost+graph[node][a]+sld[goal]}")
#                 flag = 1
#         if flag!=1:
#             astar(goal)


# search = input("enter the search city\n")
# src = input("Enter the start city\n")
# frontier.append((0,src))

# astar(search)







# graph = {
#     'arad': {'zerind': 75, 'sibiu': 140, 'timisoara': 118},
#     'zerind': {'arad': 75, 'oradea': 71},
#     'oradea': {'zerind': 71, 'sibiu': 151},
#     'timisoara': {'arad': 118, 'lugoj': 111},
#     'sibiu': {'arad': 140, 'oradea': 151, 'rimnicu vilcea': 80, 'fagaras': 99},
#     'lugoj': {'timisoara': 111, 'mehadia': 70},
#     'fagaras': {'sibiu': 99, 'bucharest': 211},
#     'rimnicu vilcea': {'sibiu': 80, 'pitesti': 97, 'craiova': 146},
#     'mehadia': {'lugoj': 70, 'dobreta': 75},
#     'dobreta': {'mehadia': 75, 'craiova': 120},
#     'bucharest': {'fagaras': 211, 'pitesti': 101, 'urziceni': 85, 'giurglu': 90},
#     'giurglu': {'bucharest': 90},
#     'pitesti': {'bucharest': 101, 'craiova': 138, 'rimnicu vilcea': 97},
#     'craiova': {'dobreta': 120, 'rimnicu vilcea': 146, 'pitesti': 138},
#     'urziceni': {'hirsova': 98, 'vaslui': 142, 'bucharest': 85},
#     'hirsova': {'urziceni': 98, 'eforie': 86},
#     'vaslui': {'urziceni': 142, 'lasi': 92},
#     'lasi': {'vaslui': 92, 'neamt': 87},
#     'eforie': {'hirsova': 86},
#     'neamt': {'lasi': 87}
# }
# sld = {
#     'arad': 366,
#     'zerind': 374,
#     'oradea': 380,
#     'timisoara': 329,
#     'sibiu': 253,
#     'lugoj': 244,
#     'fagaras': 176,
#     'rimnicu vilcea': 193,
#     'mehadia': 241,
#     'dobreta': 242,
#     'bucharest': 0,
#     'giurglu': 77,
#     'pitesti': 100,
#     'craiova': 160,
#     'urziceni': 80,
#     'hirsova': 151,
#     'vaslui': 199,
#     "lasi": 226,
#     'eforie': 161,
#     'neamt': 234
# }



# frontier=[]
# flag=0

# def astar(goal):
#     global frontier
#     global flag

#     if frontier:
#         node_p = sorted(frontier)[0]
#         frontier.remove(node_p)

#         node = node_p[1]
#         cost = node_p[0]

#         for a in graph[node]:
#             frontier.append((cost+graph[node][a],a))

#             if a==goal:
#                 print("Found the city\n")
#                 print(f"cost is {cost+graph[node][a]+sld[goal]}")
#                 flag = 1
#         if flag!=1:
#             astar(goal)
        





          

    


# ser = input("Enter the saerch element\n")
# src = input("Enter the starting element\n")
# frontier.append((0,src))

# astar(ser)


# import math

# n=int(input("Enter the number of child nodes\n"))
# t = int(input("Enter the tree depth\n"))

# scores=[]
# print("Enter the values of the leaf node\n")


# for i in range(0,int(math.pow(n,t))):
#     scores.append(int(input()))


# def minmax(c_d,n_i,scores,t_d,maxturn):
#     if c_d == t_d:
#         return scores[n_i]

#     if maxturn:
#         a=-999

#         for i in range(0,n):
#             a=max(minmax(c_d+1,n_i*n+1,scores,t_d,False),a)
#         return a
    
#     else:
#         a=999

#         for i in range(0,n):
#             a=min(minmax(c_d+1,n_i*n+1,scores,t_d,True),a)
#         return a




# print(f"the optimal value is {minmax(0,0,scores,t,False)}")



# import math
# n=int(input("Enter the number of leaf nodes\n"))
# t=int(input("Enter the tree depth\n"))
# alpha=-999
# beta=999
# scores=[]

# print("Enter the values of the leaf nodes\n")
# for i in range(0,int(math.pow(n,t))):
#     scores.append(int(input()))


# def alphabeta(c_d,n_i,maxturn,scores,alpha,beta):
#     if c_d == t:
#         return scores[n_i]

#     if maxturn:
#         a=-999

#         for i in range(0,n):
#             a=max(alphabeta(c_d+1,n_i*n+i,False,scores,alpha,beta),a)

#             if a>=beta:
#                 return beta
#             alpha = max(alpha,a)
#         return a

#     else:
#         a=999

#         for i in range(0,n):
#             a=min(alphabeta(c_d+1,n_i*n+i,True,scores,alpha,beta),a)

#             if a<=alpha:
#                 return a
#             beta = min(beta,a)
#         return a





# print(f"The optimal value of  the graph is {alphabeta(0,0,True,scores,alpha,beta)}")





# import math

# n=int(input("Enter the child nodes\n"))
# t=int(input("Enter the tree depth\n"))

# alpha =-999
# beta=999

# scores=[]

# print("Enter the values of the leaf nodes\n")
# for i in range(0,int(math.pow(n,t))):
#     scores.append(int(input()))



# def alphabeta(c_d,n_i,scores,maxturn,alpha,beta):
#     if  c_d==t:
#         return scores[n_i]

#     if maxturn:
#         a=-999

#         for i in range(0,n):
#             a=max(alphabeta(c_d+1,n_i*n+i,scores,False,alpha,beta),a)

#             if a>=beta:
#                 return beta
#             alpha = max(alpha,a)
#         return a

#     else:
#         a=999

#         for i in range(0,n):
#             a=min(alphabeta(c_d+1,n_i*n+i,scores,True,alpha,beta),a)

#             if a<=alpha:
#                 return a
#             beta = min(a,beta)
#         return a




# print(f"the optimal value : {alphabeta(0,0,scores,True,alpha,beta)}")







# board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

# def drawboard():
#     print(f"{board[1]} | {board[2]} | {board[3]}")
#     print(f"{board[4]} | {board[5]} | {board[6]}")
#     print(f"{board[7]} | {board[8]} | {board[9]}")


# def checkposition(i):
#     if(board[i]==' '):
#         return True
#     else:
#         return False

# def checkwin(marker):
#     if (board[1] == board[2] == board[3] == marker):
#         return True
#     elif(board[4] == board[5] == board[6] == marker):
#         return True
#     elif(board[7] == board[8] == board[9] == marker):
#         return True
#     elif (board[1] == board[4] == board[7] == marker):
#         return True
#     elif (board[2] == board[5] == board[8] == marker):
#         return True
#     elif (board[3] == board[6] == board[9] == marker):
#         return True
#     elif (board[1] == board[5] == board[9] == marker):
#         return True
#     elif (board[3] == board[5] == board[7] == marker):
#         return True
#     else:
#         return False

# turn  =9
# chance=  0
# player = 1
# mark = 'X'

# print("Welcome to the TIC TAC TOE game\n")
# print("Player 1 has the first chance with the marker X\n")
# print("Player 2 has the marker O\n")

# while (chance<turn):
#     drawboard()

#     if (player%2!=0):
#         print("PLayer 1's turn \n")
#         mark = 'X'

#     else:
#         print("Player 2's turn\n")
#         mark = 'O'

#     choice = int(input("enter the position where you want to place the marker\n"))
#     if (checkposition(choice)):
#         board[choice]=mark
#         turn-=1
#         player+=1

#     if checkwin('X'):
#         print("Player 1 wins the game\n")
#         drawboard()
#         break
#     elif checkwin('O'):
#         print("Player 2 wins the game\n")
#         drawboard
#         break
#     elif turn==0:
#         print("You ran out of chances\n")
#         break







# from matplotlib.pyplot import draw


# board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

# def drawboard():
#     print(f"{board[1]} | {board[2]} | {board[3]}")
#     print(f"{board[4]} | {board[5]} | {board[6]}")
#     print(f"{board[7]} | {board[8]} | {board[9]}")

# def checkwin(marker):
#     if (board[1] == board[2] == board[3] == marker):
#         return True
#     elif(board[4] == board[5] == board[6] == marker):
#         return True
#     elif(board[7] == board[8] == board[9] == marker):
#         return True
#     elif (board[1] == board[4] == board[7] == marker):
#         return True
#     elif (board[2] == board[5] == board[8] == marker):
#         return True
#     elif (board[3] == board[6] == board[9] == marker):
#         return True
#     elif (board[1] == board[5] == board[9] == marker):
#         return True
#     elif (board[3] == board[5] == board[7] == marker):
#         return True
#     else:
#         return False



# def checkpos(i):
#     if board[i]==' ':
#         return True
#     else:
#         return False


# print("Welcome to TIC TAC TOE game\n")
# print("Player 1 has first turn with marker X\n")
# print("Player 2 has the later turn with the marker O\n")


# player = 1
# turn = 9
# chance = 0
# mark = 'X'

# while chance<turn:
#     drawboard()

#     if (player%2!=0):
#         print("Player 1's turn \n")
#         mark = 'X'

#     else:
#         print("Player 2's turn \n")
#         mark = 'O'

#     choice = int(input("Enter the position where you want to place the marker\n"))

#     if (checkpos(choice)):
#         board[choice] = mark
#         turn-=1
#         player+=1
    
#     if(checkwin('X')):
#         print("Player 1 has won the game\n")
#         print("winning condition\n")
#         drawboard()
#         break
#     elif(checkwin('O')):
#         print("Player 2 has won the game\n")
#         print("Winning condition\n")
#         drawboard()
#         break

#     if turn==0:
#         print("You ran out of chances\n")
#         break









# graph = {
#     1:[2,3,4],
#     2:[5,6],
#     3:[7],
#     4:[],
#     5:[],
#     6:[],
#     7:[],
#     8:[],
#     9:[10],
#     10:[]

# }

# ser = int(input("Enter the node to be saerched\n"))
# lim = int(input("Enter the search limit\n"))
# visited=[]

# def dls(src,ser,lim):
#     if src not in visited:
#         visited.append(src)
    
#     if src==ser:
#         return True

#     if lim<=0:
#         return False

    
#     for i in graph[src]:
#         if (dls(i,ser,lim-1)):
#             return True
    
#     return False


# if(dls(1,ser,lim)):
#     print("Found theelement\n")

# else:
#     print("element was not found\n")

# for i in visited:
#     print(f"{i}-->",end=" ")









graph={
    'arad':{'zerind':75,'sibiu':140,'timisoara':118},
    'zerind':{'arad':75,'oradea':71},
    'oradea':{'zerind':71,'sibiu':151},
    'timisoara':{'arad':118,'lugoj':111},
    'sibiu':{'arad':140,'oradea':151,'fagaras':99,'rimnicu vilcea':80},
    'lugoj':{'timisoara':111,'mehadia':70},
    'fagaras':{'sibiu':99,'bucharest':211},
    'rimnicu vilcea':{'sibiu':80,'pitesti':97,'craiova':146},
    'mehadia':{'lugoj':70,'dobreta':75},
    'dobreta':{'mehadia':75,'craiova':120},
    'bucharest':{'fagaras':211,'pitesti':101,'urziceni':85,'giurglu':90},
    'giurglu':{'bucharest':90},
    'pitesti':{'bucharest':101,'craiova':138,'rimnicu vilcea':97},
    'craiova':{'dobreta':120,'rimnicu vilcea':146,'pitesti':138},
    'urziceni':{'hirsova':98,'vaslui':142,'bucharest':85},
    'hirsova':{'urziceni':98,'eforie':86},
    'vaslui':{'urziceni':142,'lasi':92},
    'lasi':{'vaslui':92,'neamt':87},
    'eforie':{'hirsova':86},
    'neamt':{'lasi':87}
}

frontier = []
flag = 0

def ucs(goal):
    global frontier
    global flag

    if frontier:
        node_p = sorted(frontier)[0]
        frontier.remove(node_p)

        node = node_p[1]
        cost = node_p[0]

        for a in graph[node]:
            frontier.append((cost+graph[node][a],a))

            if a==goal:
                print("found the element\n")
                print(f"cost: {cost+graph[node][a]}")
                flag = 1

        if (flag!=1):
            ucs(goal)



ser = input("enter the city to be searched\n")
src = input("enter the starting city\n")

frontier.append((0,src))

ucs(ser)








