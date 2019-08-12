def Print_Array(A,x,y):
    i=j=0
    print()
    while j<y:
        while i<x:
            print("%3d"%A[j][i],end="  ")
            i+=1
        print()
        i=0
        j+=1
    print()

def Make_Array(A):
    x=int(input("행의 수를 입력해 주세요 : "))
    y=int(input("열의 수를 입력해 주세요 : "))
    i=j=1
    while j<=y:
        Z=[]
        while i<=x:
            print(j,"열",i,"행의 값을 입력해주세요 :", end=" ")
            while 1:
                z=input()
                if z>="0" and z<="9": break
                print("정수치를 입력해주세요 :",end=" ")
            Z.append(int(z))
            i+=1
        A.append(Z)
        j+=1
        i=1
    return int(x),int(y)

A=[]
B=[]
result=[]
x1,y1=Make_Array(A)
x2,y2=Make_Array(B)
Print_Array(A,x1,y1)
Print_Array(B,x2,y2)