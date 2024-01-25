def createboard():
    a=[]
    for i in range (9):
        col=[]
        col=list(map(int,input().split()))
        a.append(col)
    return a        
def showboard(a):
    for i in range(9):
        for j in range (9):
            print(a[i][j],end=" ")
        print()    
def isvalid(a,row,col,num):
    x=(row//3)*3
    y=(col//3)*3
    for i in range (x,x+3):
        for j in range (y,y+3):
            if (a[i][j] == num):
                return 0
            
    for i in range (9):
        if a[row][i]==num:
            return 0
        if a[i][col]==num:
            return 0
    return 1    
def solve(a,row,col):
    # print("solving at{}{}".format(row,col))
    # showboard(a)
    if row==9 and col==0:
        # print("Breaking at{}{}".format(row,col))
        showboard(a)
        exit()
    if(col==8):
        nrow=row+1
        ncol=0
    else:
        nrow=row
        ncol=col+1
    if(a[row][col]!=0):
            solve(a,nrow,ncol)
    else:                    
        for i in range (1,10):
            if(isvalid(a,row,col,i)):
                a[row][col]=i
                solve(a,nrow,ncol)
                a[row][col]=0
    return 0                   
x=createboard()
solve(x,0,0)
