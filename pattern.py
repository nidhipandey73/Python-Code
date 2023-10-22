''' #hollow rectangle
for i in range (1,6) :
    for j in range(1,5) :
        if 1<i<5 and 1<j<4 :
            print(" ",end = "")
        else :
            print("*", end ="")
    print("\n") 
#inverted half pyramid
for i in range (6,1,-1) :
    for j in range (1,i): 
        print("*",end="")
    print("\n") 
#half pyramid after 180 rotation
for i in range (1,6) :
    for j in range(5,i,-1) :
        print(" ",end="")
    for k in range(1,i+1) :
        print("*",end="")
    print("\n")
#half pyramid using numbers
for i in range(1,6) :
    for j in range(1,i+1) :
        print(j,end = "")
    print("\n") 
#inverted half pyramid using numbers
for i in range(6,1,-1) :
    for j in range (1,i) :
        print(j,end = "")
    print("\n") 
#inverted half pyramid using numbers - 2
for i in range(1,6) :
    for j in range(6,i,-1) :
        print(i, end = "")
    print("\n")
#floyd's triangle
k=1
for i in range(2,7) : 
    for j in range(1,i) :
        print(k, end = " ")
        k=k+1
    print("\n") 
#0-1 pattern
for i in range(2,7) :
    for j in range(1,i) :
        if (i+j)%2==0 :
            print("0", end = " ")
        else :
            print("1", end = " ") 
    print("\n") 
#palindromic pattern
for i in range(1,6) :
    for j in range(5,i,-1) :
        print(" ",end = " ")
    for k in range(i,0,-1) :
        print(k, end = " ") 
    for l in range(1,i) :
        print(l+1, end = " ")
    print("\n") 
#diamond pattern
for i in range(1,6) :
    for j in range(5,i,-1) :
        print(" ", end= " ")
    for k in range(1,i+1) :
        print("*",end = " ")
    for l in range(1,i) :
        print("*",end =" ")
    print("\n")
for i in range(1,5) :
    for k in range(1,i+1) :
        print(" ", end= " ")
    for j in range(5,i,-1) :
        print("*", end = " ")
    for l in range(4,i,-1) :
        print("*", end = " ")
    print("\n")  
#hollow diamond
for i in range(1,6) :
    for j in range(5,i,-1) :
        print(" " , end = " ")
    for k in range(1,i+1) :
        if k>1 :
            print(" ", end = " ")
        else : 
            print("*", end = " ")
    for l in range(1,i) : 
        if l<i-1 :
            print(" " , end = " ")
        else : 
            print("*", end = " ") 
    print("\n") 
for i in range(1,5) :
    for j in range(1,i+1) :
        print(" ", end = " ")
    for k in range(5,i,-1) :
        if k<5 :
            print(" " , end = " ")
        else :
            print("*", end = " ") 
    for l in range(4,i,-1) :
        if l > i+1 :
            print(" " , end = " ")
        else :
            print("*", end = " ") 
    print("\n")   
#hollow diamond inscribed in a rectangle
for i in range(1,6) :
    for j in range(6,i,-1) :
        print("*", end = " ")
    for k in range(1,i) :
        print(" ", end = " ")
    for m in range(1,i) :
        print(" ", end = " ") 
    for l in range(6,i,-1) :
        print("*", end = " ")
    print("\n")  
for i in range(1,5) :
    for j in range(1,i+2) :
        print("*", end =" ")
    for k in range(4,i,-1) :
        print(" ", end = " ")
    for m in range(4,i,-1) :
        print(" ", end = " ")
    for l in range(1,i+2) :
        print("*", end = " ") 
    print("\n")  
#solid rhombus
for i in range(1,6) :
    for j in range (5,i,-1) :
        print(" ", end = " ") 
    for k in range(1,6) :
        print("*", end = " ") 
    print("\n") 
#hollow rhombus
for i in range(1,6) :
    for j in range(5,i,-1) :
        print(" ", end = " " )
    for k in range(1,6) : 
        if 1<i<5 and 1<k<5 :
            print(" ", end=" ")
        else:
            print("*", end = " ") 
    print("\n") 
#pyramid pattern for number - 1 
for i in range(1,6) :
    for j in range(5,i,-1) :
        print(" ", end = " ")
    for k in range(1,i+1) :
        print(i, end ="   ") 
    print("\n") 
#pyramid pattern for number - 2
for i in range(1,6) :
    for j in range(5,i,-1) :
        print(" ", end = " ")
    for k in range(1,i+1) :
        print(k, end ="   ") 
    print("\n") ''' 
    







