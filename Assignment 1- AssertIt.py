machineCapacity={'Large':10, 'XLarge':20, '2XLarge':40, '4XLarge':80, '8XLarge':160, '10XLarge':320}

NYcost={'Large':120, 'XLarge':230, '2XLarge':450, '4XLarge':774, '8XLarge':1400, '10XLarge':2820}
INcost={'Large':140, '2XLarge':413, '4XLarge':890, '8XLarge':1300, '10XLarge':2970}
CHcost={'Large':110, 'XLarge':200, '4XLarge':670, '8XLarge':1180}

NYcostRatio={}
INcostRatio={}
CHcostRatio={}

for i in NYcost:
    NYcostRatio[i]=NYcost[i]/machineCapacity[i]
for i in INcost:
    INcostRatio[i]=INcost[i]/machineCapacity[i]
for i in CHcost:
    CHcostRatio[i]=CHcost[i]/machineCapacity[i]
    
#sorting dictionaries
NYcostRatio= dict(sorted(NYcostRatio.items(),key = lambda kv: kv[1]))
INcostRatio= dict(sorted(INcostRatio.items(),key = lambda kv: kv[1]))
CHcostRatio= dict(sorted(CHcostRatio.items(),key = lambda kv: kv[1]))
    

print(NYcostRatio)
print(INcostRatio)
print(CHcostRatio)

capacity= 1100
hours= 12

def Identify_machine(total, machineCapacity, countyCostRatio):
    l=[]
    for i in countyCostRatio:
        c= total//machineCapacity[i]
        if c>=1:
            l.append((i, c))
            total= total-machineCapacity[i]*c
    return l

print(Identify_machine(capacity, machineCapacity, NYcostRatio))
print(Identify_machine(capacity, machineCapacity, INcostRatio))
print(Identify_machine(capacity, machineCapacity, CHcostRatio))
        

def CalculateCost(Identified_machines, CountyCost, hour):
    cost=0
    for i in Identified_machines:
        cost+= CountyCost[i[0]]*i[1]*hour
    return cost
print(CalculateCost(Identify_machine(capacity, machineCapacity, NYcostRatio), NYcost, hours))
print(CalculateCost(Identify_machine(capacity, machineCapacity, INcostRatio), INcost, hours))
print(CalculateCost(Identify_machine(capacity, machineCapacity, CHcostRatio), CHcost, hours))

output=[{
    'region':'New York',
    'total_cost':'$'+str(CalculateCost(Identify_machine(capacity, machineCapacity, NYcostRatio), NYcost, hours)),
    'machines':Identify_machine(capacity, machineCapacity, NYcostRatio)},
    {
    'region':'India',
    'total_cost':'$'+str(CalculateCost(Identify_machine(capacity, machineCapacity, INcostRatio), INcost, hours)),
    'machines':Identify_machine(capacity, machineCapacity, INcostRatio)},
    {
    'region':'China',
    'total_cost':'$'+str(CalculateCost(Identify_machine(capacity, machineCapacity, CHcostRatio), CHcost, hours)),
    'machines':Identify_machine(capacity, machineCapacity, CHcostRatio)}]

print(output)

