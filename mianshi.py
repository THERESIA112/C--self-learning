grid=[
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]
for n in range(len(grid)):
    for m in range(len(grid[0])):
        if(n==m==0):
            continue
        elif(n==0):
            grid[n][m]+=grid[n][m-1]
        elif(m==0):
            grid[n][m]+=grid[n-1][m]
        else:
            grid[n][m]+=min(grid[n][m-1],grid[n-1][m])
print(grid[-1][-1])
    

    



