n=3
def ismagicSqare(mat):
    s=0
    for i in range(o,N):
        s=s+mat[i][i]
    s2=0
    for i in range(o,N):
        s2=s2+mat[i][n-i-1]
        if (s1=s2):
            return False
        for i in range(o,N):
            row sum=0
            for j in range(o,N):
                row sum+=mat[i][j]
                if(rowsum!=s):
                    return False
        for i in range(o,N):
            colsum=0
            for j in range(o,N):
                colsum+=mat[j][i]
            if (s!=colsum):
                return False
            return True 
mat=[[2,7,6],[9,5,1],[4,3,8]] 
if (is MagicSquare(mat)):
    print("magic square")  
else:
    print("not magic square")                                    


