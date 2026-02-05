import numpy as np

def lu_method(A, b):
    A = A.astype(float)
    n = len(b)

    L = np.zeros((n,n))
    U = np.zeros((n,n))

    # สร้าง L และ U
    for i in range(n):
        L[i][i] = 1

        for j in range(i, n):
            sum_u = 0
            for k in range(i):
                sum_u += L[i][k] * U[k][j]
            U[i][j] = A[i][j] - sum_u

        for j in range(i+1, n):
            sum_l = 0
            for k in range(i):
                sum_l += L[j][k] * U[k][i]
            L[j][i] = (A[j][i] - sum_l) / U[i][i]

    # forward substitution (Ly = b)
    y = np.zeros(n)
    for i in range(n):
        sum_ly = 0
        for j in range(i):
            sum_ly += L[i][j] * y[j]
        y[i] = b[i] - sum_ly

    # back substitution (Ux = y)
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        sum_ux = 0
        for j in range(i+1, n):
            sum_ux += U[i][j] * x[j]
        x[i] = (y[i] - sum_ux) / U[i][i]

    return x

def get_input():
    n = int(input("Enter number of variables: "))
    
    print("Enter Matrix A (" + str(n) + "x" + str(n) + "):")
    matrix_a = []
    for i in range(n):
        row = list(map(float, input().split()))
        matrix_a.append(row)
    
    print("Enter Vector b ("+ str(n) + " values):")
    vector_b = list(map(float, input().split()))
    
    return np.array(matrix_a), np.array(vector_b)

#รับค่ามาเก็บไว้ในตัวแปร
A, b = get_input()

#ส่งค่าไปคำนวณในฟังก์ชัน
result = lu_method(A, b)

#แสดงผลลัพธ์โดยใช้
for i in range(len(result)):
    print("x_", i+1, "=", result[i])