#UCS

# from queue import PriorityQueue
 
# graph = {
#     "A":{"B":1,"C":3,"D":7},
#     "B":{"D":5},
#     "C":{"D":12},
# }
 
# def UCS(graph, start, end):
#     if start == end:
#         print("cost is 0")
#         return True
#     queue = PriorityQueue()
#     queue.put((0 , [start]))
#     while not queue.empty():
#         temp = queue.get()
#         if temp[1][-1] == end:
#             print("path found",temp[1], "with cost", temp[0])
#             return
#         child = graph[temp[1][-1]].keys()
#         b = []
#         for i in temp[1]:
#             b.append(i)
#         for i in child:
#             queue.put((graph[temp[1][-1]][i] + temp[0] , b + [i]))

# UCS(graph, "A", "D")





#MinMax

# import math
# def Minimax(tree,depth):
#     max_turn=bool(depth%2)
#     #print(max_turn)
#     for i in range (int(depth)):
#         zipped=zip(tree[::2],tree[1::2])
#         print(tree[::2],tree[1::2])
#         if max_turn:
#             tree=[max(a,b) for a,b in zipped]
#            # print(max_turn)
#         else:
#             tree=[min(a,b) for a,b in zipped]
#           #  print(max_turn)
#         max_turn=not max_turn
#     return tree[0]
# A=[3,5,2,9,12,5,23,23]
# depth=math.ceil(math.log(len(A),2))
# print(Minimax(A,depth))





#aStar

from queue import PriorityQueue
graph={
       "A":{"B":1,"C":3,"D":7},
       "B":{"D":5},
       "C":{"D":12},
}
h_value={
    "A":2,
    "B":2,
    "C":2,
    "D":2,
}
def  search(graph,start,end):
    queue=PriorityQueue()
    queue.put((0+h_value[start],[start]))
    while not queue.empty():
        node=queue.get()
        current=node[1][len(node[1])-1]
       
        if end in node[1]:
            print("path found:"+str(node[1])+",cost="+str(node[0]))
            break
        cost=node[0]-h_value[current]
        for neighbor in graph[current]:
            temp=node[1][:]
            temp.append(neighbor)
            queue.put((cost+graph[current][neighbor]+h_value[neighbor],temp)) 
search(graph,"A","D")