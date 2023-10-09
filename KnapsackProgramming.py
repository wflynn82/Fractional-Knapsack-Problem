from time import perf_counter
filein = input("Whats the input file? \n")

file = open(filein, 'r')

wholefile = file.readlines()


wholefile[0] = wholefile[0].strip()
#print(wholefile[0])
#print(int(wholefile[0][2:5]))

val = wholefile[1].strip()
values = val.split(" ")
for i in range(len(values)):
    values[i] = int(values[i])



wei = wholefile[2]

weights = wei.split(' ')
for i in range(len(weights)):
    weights[i] = int(weights[i])

if len(values) >15:
    wei = wholefile[3]
    weights = wei.split(' ')
    
#print(weights)

if len(values) >=15:
    for i in weights:
        values.append(i)

#print(values)    
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

start = perf_counter()
def fractionalSolution(w, arr):
 
    knapsackvalue = 0

    taken = []
    frac = []

    for i in arr:
 
        # add full item
        if i.weight <= w:
            w -= i.weight
            knapsackvalue += i.value
            #print("full",knapsackvalue)
            taken.append(i.value)
            
        # adds fractional parts
        else:
            knapsackvalue += i.value * w / i.weight
            #print("fraction",knapsackvalue)
            frac.append(knapsackvalue)
            break
    
    return knapsackvalue
    #return taken,frac
stop = perf_counter()

if __name__ == "__main__":
    
   
    w = int(wholefile[0][2:6])

    r = list(zip(values,weights))
    #print(r)
    
    Objects = [Item(*x) for x in r]        
    #arra = [Item(60, 10), Item(100, 20), Item(120, 30)]
 
    maxv = fractionalSolution(w, Objects)
    
    print("Total Time for greedy (fractional) solution:",stop-start,"\n")
    print("Total value taken:", maxv,"\n")
    print("Total weight taken:", w,"\n")
    print("Taken as:")
