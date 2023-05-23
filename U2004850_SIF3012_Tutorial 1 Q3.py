import numpy as np
import matplotlib.pyplot as plt

length=50
grid=np.zeros((length,length))
check_grid=np.zeros((length,length))
gridlen=np.shape(grid)[0]
counter=0

T_top=100
T_bot=50
T_left=75
T_right=100

grid[0]=T_top
grid[-1]=T_bot
grid[:,0]=T_left
grid[:,-1]=T_right

def gauss_seidel(grid,i,j,tol,check):
    if check[i][j]==0:
        gridnew=(grid[i+1][j]+grid[i-1][j]+grid[i][j+1]+grid[i][j-1])/4
        if grid[i][j]!=0:
            error=abs(gridnew-grid[i][j])/grid[i][j]
            if error<tol:
                grid[i][j]=gridnew
                check[i][j]=1
                print(str(round(np.count_nonzero(check)/((length-2)**2)*100,2))+'% done')
            else:
                grid[i][j]=gridnew
        else:
            grid[i][j]=gridnew
        return grid[i][j]
    else:
        pass
    return grid[i][j]

while np.all(check_grid[1:gridlen-1,1:gridlen-1])==False:
# while counter<2:
    for i in range(gridlen):
        for j in range(gridlen):
            if 0<i<(gridlen-1) and 0<j<(gridlen-1):
                gauss_seidel(grid,i,j,0.01,check_grid)
            else:
                pass
    counter=counter+1
    
x=np.arange(0,50,1)
y=np.arange(0,50,1)
X,Y=np.meshgrid(x,y)

Z=X*Y*0



for i in range(gridlen):
    for j in range(gridlen):
        Z[i,j]=grid[i,j]

print("No. of iterations = ",counter)
gridplot=np.flip(grid,0)
ax = plt.axes(projection = "3d")
ax.plot_surface(X,Y,Z, cmap='plasma', vmin = np.abs(grid).min(),vmax = np.abs(grid).max())

# ax.set_xlabel('Bottom')
# ax.set_ylabel('Left')
# ax.set_title('Heat Map')
# ticklist=np.arange(length)
# secax = ax.secondary_xaxis('top')

# secax.set_xlabel('Top')
# ax.set_yticks(ticklist)
# ax.set_yticklabels(np.flip(ticklist))
# yticks = ax.yaxis.get_major_ticks()
# for i in range(length):
#     if i%(length/10)!=0:
#         yticks[i-1].set_visible(False)

# fig.colorbar(im, orientation='vertical',label='Temp (°C)')

# plt.show()
