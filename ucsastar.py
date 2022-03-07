
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

graph={
    'a':{'b':3,'c':4},
    'b':{'d':3,'e':7},
    'c':{'f':1,'g':2},
    'd':{'h':6,'i':2},
    'e':{'j':3},
    'f':{'k':5},
    'g':{'l':4},
    'h':{},
    'i':{},
    'j':{},
    'k':{},
    'l':{}

}

sld = {
    'a':2,
    'b':2,
    'c':2,
    'd':2,
    'e':2,
    'f':2,
    'g':2,
    'h':2,
    'i':2,
    'j':2,
    'k':2,
    'l':2
}







frontier = []
flag = 0

def astar(goal):
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
                print("Found the city\n")
                print(f"The cost is {cost+graph[node][a]+sld[goal]} ")
                
                flag = 1
        if flag!=1:
            astar(goal)

search = input("Enter the city to be searched \n")
start = input("Enter the starting city\n")
frontier.append((0,start))

astar(search)









