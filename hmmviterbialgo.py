states = []   
# 
nstates = int(input("no of states:")) 
nobs=int(input("no of observatoin:"))
  
for i in range(0, nstates): 
    ele=float(input()) 
  
    states.append(ele) # adding the element 
      
print(states) 
#following code for inputting states and then creating a matrix which inputs the possible probabilites of each observation in a particular state
print("matrices for states and observations probabilities:")
mat1 = [[float(input()) for x in range (nobs)] for y in range(nstates)] 

print("matrices for states probability in between:")
mat2 = [[float(input()) for x in range (nstates)] for y in range(nstates)] 

noofobs=int(input("no of observation:"))
obs=[]

for j in range (0,noofobs):  
    ele1=int(input())
    obs.append(ele1)
print("observation and their possibilities :")
print(obs)
 
 #the following matrix vi stores maximum probabilities of every trail
vi= []

 
for t in range (0,noofobs):
    v12=[]  
    v1=[]
    #initialisation
    if(t==0):
        for i1 in range (0,nstates):
            v11=states[i1]*mat1[i1][obs[0]-1]
            v1.append(v11)
        vi.append(v1)
    #its the alternate algo for recursion....this finds the maximum
    else :
        for j1 in range (0,nstates):
            max=0
            for j2 in range(0,nstates):
                v11=vi[t-1][j2]*mat2[j2][j1]*mat1[j1][obs[t]-1]
                if v11>max :
                    max=v11

            v12.append(max)
        vi.append(v12)
print(vi)
#for printing the sequence of our desired output of states
seq=[]
for x in range (0,noofobs):
    maax=0
    ind=0
    for y in range (0,nstates):
        if(vi[x][y]>maax):
            maax=vi[x][y]
            ind=y
    seq.append(ind)
print("Final sequence:")
print(seq)


#both inputs of observation and states are taken in form of indices... so inter the input starting from 1,2,3,,...