def backtrack(x, enemies, domain, assigned):
    if -1 not in assigned: # checking for unassigned people
        return x
    v = 999
 
    for i in range(len(domain)):               
        if v > len(domain[i]) and assigned[i] != 1:# finding unassigned people
            v = i
    order = []
    
    for i in domain[v]:                     
        min = 1000
        for j in enemies[v]:  
            temp = len(domain[j])
            if i in domain[j]:
                temp -= 1
            if temp < min:
                min = temp
        order.append((i, min))
        
    order = sorted(order, key=lambda x:x[1], reverse=True)
    ordered = [i[0] for i in order]
 
    for i in ordered:
        new_d = [[j for j in i] for i in domain]
        for j in enemies[v]:
            if i == x[j]:
                continue
        x[v] = i
        assigned[v] = 1
        new_d[v] = [z for z in new_d[v] if z==i]         
        temp = []
        for j in range(len(new_d)):
            if j!=v and j in enemies[v]:
                new_d[j] = [z for z in new_d[j] if z!=i]
        res = backtrack(x, enemies, new_d, assigned)
        if res!=0:
            return res
    x[v] = ""
    assigned[v] = -1
    return 0
 
if __name__ == "__main__":
    people = int(input("Number of people = "))
    tables = int(input("Number of tables = "))
    edges = []
    rows = input("People who should not sit together = ").split()
    while(rows):
        edges.append((int(rows[0]),int(rows[1])))
        rows = input().split()
 
    x = ["" for i in range(people)] 
    # filling out the enemies matrix
    enemies = [[] for i in range(people)]   
    for i in edges:                           
        enemies[i[0]].append(i[1])         
        enemies[i[1]].append(i[0])
 
    for i in range(people):
        j = list(set(enemies[i])) # deduplicating the each row       
        enemies[i] = j
    assigned = [-1 for i in range(people)]    
    domain = [[x for x in range(tables)] for i in range(people)]  
 
    res = backtrack(x, enemies, domain, assigned)  
 
    if res == 0:
        print("Tables could not be assigned")
    else:
        for i in range(len(res)):
            print(f"{i} : {res[i]}")
