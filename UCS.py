# graph = {
#     'arad': {'zerind':75,'sibiu':140,'timisoara':118},
#     'zerind': {'arad':75,'oradea':71}

# }



# visited =[]
# frontier =[]
# flag = 0

# def ucs(goal):
#     global flag
#     global frontier
#     global visited

#     if frontier:
#         node_p = sorted(frontier)[0]
#         frontier.remove(node_p)
#         node = node_p[1]
#         cost = node_p[0]
#         for a in graph[node]:
#             frontier.append((cost+graph[node][a],a))
#             if (a==goal):
#                 print(f"City found\n total cost {cost+graph[node][a]}")
#                 flag=1
#         if flag!=1:
#                 ucs(goal)


# ser = input("Enter the city to be searched\n")
# start = input("Enter the starting city\n")
# frontier.append((0,start))
# ucs(ser)










# graph = {
#     'arad': {'zerind':75,'sibiu':140,'timisoara':118},
#     'zerind': {'arad':75,'oradea':71}

# }



# frontier = []
# visited =[]
# flag = 0

# def ucs(goal):
#     global frontier
#     global visited
#     global flag

#     node_p = sorted(frontier)[0]
#     frontier.remove(node_p)
#     node = node_p[1]
#     cost = node_p[0]

#     for a in graph[node]:
#         frontier.append((cost+graph[node][a],a))
#         if (a==goal):
#             print("The city was found\n")
#             print(f"the cost was {cost+graph[node][a]}")
#             flag=1
#     if (flag!=1):
#         ucs(goal)


# search  = input("Enter the city to be found\n")
# start = input("Enter the starting city\n")

# frontier.append((0,start))

# ucs(search)







# graph = {
#     'arad': {'zerind':75,'sibiu':140,'timisoara':118},
#     'zerind': {'arad':75,'oradea':71}

# }

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

            if (a==goal):
                print("Found the city\n")
                print(f"cost is {cost+graph[node][a]}")
                flag=1
        if (flag!=1):
            ucs(goal)

search = input("Enter the element to be searched\n")
start = input("Enter the starting city\n")
frontier.append((0,start))
ucs(search)