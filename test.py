string="""KOREA CCC BBB AAA
KOREA CCC 1.0 0.0 0.0
AAA BBB 0.428 0.144 0.428
AAA KOREA 0.0 0.0 1.0
CCC BBB 0.0 0.0 1.0
KOREA BBB 1.0 0.0 0.0
CCC AAA 0.0 0.0 1.0"""
country=[0,0,0,0]
winning_rate=[0,0,0,0]
Nation = {"KOREA" : 0,"AAA" : 1,"BBB" : 2,"CCC" : 3}

def score(A,B,x,y,z,country):
    for i in [A,B]:
        k= 1 if i is A else 0
        country[Nation[i]]+=3*k*x+y+3*(1-k)*z
String=string.split("\n")
for i in range(1,7):
    line=String[i].split()
    score(line[0],line[1],float(line[2]),float(line[3]),float(line[4]),country)
count1=0
while country!=[0,0,0,0]:
    Max=max(country)
    count2=country.count(Max)
    count1+=count2
    for i in [0,1,2,3]:
        if country[i]==Max: 
            winning_rate[i]=1/count2
            country[i]=0
    if count1>=2: break
for i in [0,3,2,1]:
    print(winning_rate[i])