def lpu():
    {
        print("block number          block name\n01                    A-->design\n03,04--attached       B-->hospital+pharmacy\n06                    C-->architecture\n09-10-11-12           D-->girls hostel 1,2,3,4\n13                    E-->student welfare\n14                    F-->business block\n15                    G-->unimall+hotel management\n16                    H-->unipolis\n22-23                 I-->girls hostel 5,6\n29-30-31-32           J-->admission block\n33-34                 K-->computer science engineering\n35                    L-->shanti devi mittal auditorium\n36                    M-->electronics and electrical engineering\n37                    N-->central library\n40                    O-->bh8\n41-42-43-44           P-->apartments\n45                    Q-->bh1\n48-49-50-51-52-53-54  R-->bh2,3,4,5,6\n55,56,57              S-->mechanical and civil engineering+polytechnic\n25-26                 T-->agriculture")  }
def initial_graph() :
    
    return {
            
        'A': {'B':50},
        'B': {'A':50, 'C':50, 'D':80},
        'C': {'A':50, 'D':30, 'E':80, 'G':90},
        'D': {'B':80, 'C':30,'E':110,'G':120,'I':100},
        'E': {'C':80, 'D':110,'F':20,'G':10,'H':20},
        'F': {'E':20, 'G':30, 'H':20,'J':80,'T':100},
        'G': {'C':90, 'D':120,'E':10,'F':30,'H':10,'I':120},
        'H': {'E':20,'F':20,'G':10,'J':70,'T':90},
        'I':{'D':100,'G':120,'T':50},
        'J':{'F':80,'H':70,'T':50,'L':10,'K':20},
        'K':{'J':20,'L':10,'M':10},
        'L':{'J':10,'K':10,'M':10,'T':20,'N':10},
        'M':{'N':5,'L':10,'K':5},
        'N':{'L':10,'M':5,'O':60,'P':50,'T':20},
        'O':{'N':60,'P':10,'Q':70,'R':50,'T':40},
        'P':{'N':50,'O':10,'Q':60,'R':50,'T':10},
        'Q':{'O':70,'P':60,'R':30},
        'R':{'O':50,'P':50,'Q':60,'S':20},
        'S':{'R':20},
        'T':{'F':100,'H':90,'I':50,'J':50,'L':20,'N':20,'O':40,'P':10}
            
            
            
            }
lpu()

initial = eval(input("enter initial point :"))
path = {} 
adj_node = {} 
queue = [] 
graph = initial_graph()

for node in graph:
    path[node] = float("inf")
    adj_node[node] = None
    queue.append(node)
    
path[initial] = 0

while queue:
    key_min = queue[0]
    min_val = path[key_min]
    for n in range(1, len(queue)):
        if path[queue[n]] < min_val:
            key_min = queue[n]  
            min_val = path[key_min]
    cur = key_min
    queue.remove(cur)
    
    
    for i in graph[cur]:
        alternate = graph[cur][i] + path[cur]
        if path[i] > alternate:
            path[i] = alternate
            adj_node[i] = cur

x =eval(input("enter end point :"))
print('The path between ')
print(x, end = '<-')
while True:
    x = adj_node[x]
    if x is None:
        print("")
        break
    print(x, end='<-')
 