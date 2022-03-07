def checkEnemy(table, e):
    for i in e:
        if i in table:
            return False
    return True


def csp(n, tables, enemy):
    visited = [False for i in range(n)]
    for i in range(n):
        for j in seating:
            if checkEnemy(j, enemy[i]) == True:
                j.append(i)
                visited[i] = True
                break
        if visited[i] == False:
            print("not possible")
            return False
    print(seating)
    return True


n = int(input("enter number of people : "))
tables = int(input("enter number of tables : "))
enemy = {}
for i in range(n):
    enemy[i] = set()
print("Enter elements of list of people who should not sit together")
line = input()
while(line):
    a, b = [int(i) for i in line.split()]
    enemy[a].add(b)
    enemy[b].add(a)
    line = input()

seating = [[] for i in range(tables)]
csp(n, tables, enemy)
