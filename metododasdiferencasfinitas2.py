import numpy as np
import matplotlib.pyplot as plt

# Específico para a matriz do exercício
def build_matrix(ny, nx):
    empty_matrix = np.zeros((ny, nx))
    for i in range (nx):
        for j in range (ny):
            if (i == (ny-1)):            # horizontal baixo
                empty_matrix[i][j] = 150
            elif(j == 0):                # vertical esquerda
                empty_matrix[i][j] = 23
            elif(i == 0):                # horizontal cima
                empty_matrix[i][j] = 23
            elif(j == (nx-1)):           # vertical direita
                empty_matrix[i][j] = 23
            else:
                empty_matrix[i][j]= -1
    return empty_matrix

def solve_matrix(act_matrix, nx, ny, alpha):
    nxt_matrix = build_matrix(ny, nx)
    for i in range (nx):
        for j in range (ny):
            if (nxt_matrix[i][j] == -1):
                nxt_matrix[i][j] = alpha * 0.01  * ((act_matrix[i+1][j]+act_matrix[i-1][j]-2*act_matrix[i][j])/0.01 + (act_matrix[i][j+1]+act_matrix[i][j-1]-2*act_matrix[i][j])/0.01) + act_matrix[i][j]
    return nxt_matrix



act_matrix = build_matrix(30, 30) # para 50 cm de 10 em 10 cm
for i in range (30):
    for j in range (30):
        if (act_matrix[i][j] == -1):
            act_matrix[i][j] = 0


for qq in range(1000):
    act_matrix = solve_matrix(act_matrix, 30, 30, 0.25)

#print(act_matrix)



plt.imshow(act_matrix)
plt.colorbar()
plt.show()
