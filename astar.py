graph={
    'arad':{'zerind':75,'sibiu':140,'timisoara':118},
    'zerind':{'arad':75,'oradea':71},
    'oradea':{'zerind':71,'sibiu':151},
    'timisoara':{'arad':118,'lugoj':111},
    'sibiu':{'arad':140,'oradea':151,'rimnicu vilcea':80,'fagaras':99},
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
sld={
    'arad':366,
    'zerind':374,
    'oradea':380,
    'timisoara':329,
    'sibiu':253,
    'lugoj':244,
    'fagaras':176,
    'rimnicu vilcea':193,
    'mehadia':241,
    'dobreta':242,
    'bucharest':0,
    'giurglu':77,
    'pitesti':100,
    'craiova':160,
    'urziceni':80,
    'hirsova':151,
    'vaslui':199,
    'lasi':226,
    'eforie':161,
    'neamt':234
}
frontier=[]
flag=0
def ucs(start,goal):
    global frontier
    global flag
    global graph
    frontier.append((0+sld[start],[start]))
    while frontier:
        node_popped=sorted(frontier)[0]
        curr_node=node_popped[1][len(node_popped[1])-1]
        cost=node_popped[0]-sld[curr_node]
        frontier.remove(node_popped)
        if goal in node_popped[1]:
            print('path found : ',str(node_popped[1]),"\nCost : ",str(node_popped[0]))
            break        
        for neighbour in graph[curr_node]:
            temp=node_popped[1][:]
            temp.append(neighbour)
            frontier.append((cost+graph[curr_node][neighbour]+sld[neighbour],temp))
            
start=input("enter the start city - ")
goal=input("enter the city to be searched - ")
ucs(start,goal)