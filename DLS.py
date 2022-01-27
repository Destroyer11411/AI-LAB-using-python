

# graph = {
#     '1':['2','3','4'],
#     '2':['5','6'],
#     '3':['7'],
#     '4':[],
#     '5':[],
#     '6':[],
#     '7':[],
#     '8':[],
#     '9':['10'],
#     '10':[]
# }

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




# ser = int(input("Enter the element to be serched\n"))
# lim =int(input("Enter the depth limt\n"))

# visited=[]

# def dls(src,ser,lim):
#     if src not in visited:
#         visited.append(src)
#     if src==ser:
#         return True
#     if lim<=0:
#         return False
    
#     for i in graph[src]:
#         if(dls(i,ser,lim-1)):
#             return True
#     return False



# if (dls(1,ser,lim)):
#     print("Search was succesfull\n")
# else:
#     print("Path was not found\n")







graph = {
    1:[2,3,4],
    2:[5,6],
    3:[7],
    4:[],
    5:[],
    6:[],
    7:[],
    8:[],
    9:[10],
    10:[]

}




ser = int(input("Enter the search element\n"))
lim = int(input("Enter the limit for the search\n"))

visited=[]


def dls(src,ser,lim):
    if src not in visited:
        visited.append(src)
    if src==ser:
        return True
    if lim<=0:
        return False
     
    for i in graph[src]:
        if(dls(i,ser,lim-1)):
            return True
    return False


if(dls(1,ser,lim)):
    print("The element was found\n")
    
else:
    print("The element was not found\n")

print("The path was\n")

for i in visited:
    print(f"{i}-->",end="")