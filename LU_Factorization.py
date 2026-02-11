def get_determinant(matrix): #หาค่า Determinant เพื่อตรวจสอบ Singular Matrix

    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for j in range(n):
        #สร้าง Minor matrix โดยการตัดแถวที่ 0 และหลักที่ j
        minor = [row[:j] + row[j+1:] for row in matrix[1:]]
        det += ((-1) ** j) * matrix[0][j] * get_determinant(minor)
    return det

def LU(A, b):
    n = len(A)
    
    #ตรวจสอบค่า Determinant
    det = get_determinant(A)
    if det == 0:
        return "Matrix is Singular (det = 0). No unique solution exists."

    #สร้างเมทริกซ์ L และ U (ค่าเริ่มต้นเป็น 0)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    #แยกตัวประกอบ LU 
    for i in range(n):
        L[i][i] = 1.0  #กำหนดให้ค่าแนวทแยงของ L เป็น 1

        # คำนวณเมทริกซ์ U
        for j in range(i, n):
            sum_val = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = A[i][j] - sum_val

        # ตรวจสอบการหารด้วยศูนย์ในเมทริกซ์ U (Pivot check)
        if U[i][i] == 0:
            return "Matrix might be singular or requires pivoting."

        # คำนวณเมทริกซ์ L
        for j in range(i + 1, n):
            sum_val = sum(L[j][k] * U[k][i] for k in range(i))
            L[j][i] = (A[j][i] - sum_val) / U[i][i]

    #Forward Substitution
    #แก้สมการ Ly = b เพื่อหา y
    y = [0.0] * n
    for i in range(n):
        sum_val = sum(L[i][j] * y[j] for j in range(i))
        y[i] = b[i] - sum_val

    #Back Substitution
    #แก้สมการ Ux = y เพื่อหา x
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        sum_val = sum(U[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - sum_val) / U[i][i]

    return x

def run_LUprogram():

    n = int(input("Enter number of variables: ")) #รับ input
    
    print("Enter Augmented Matrix (" + str(n) + "x" + str(n + 1) + "):")
    A = []
    b = []
    for i in range(n):
        row_data = [float(val) for val in input(f"Row {i+1}: ").split()]
        if len(row_data) != n + 1:
            print(f"Invalid input! Need {n+1} numbers.")
            return
        A.append(row_data[:n])  #ส่วนสัมประสิทธิ์
        b.append(row_data[n])   #เมทริกซ์คำตอบ/Column Vector B

    result = LU(A, b)


    if isinstance(result, str):
        print(result)
    else:
        for i, val in enumerate(result):
            print(f"x{i+1} = {round(val, 3)}")

#ส่วนที่โปรแกรมทำงาน
run_LUprogram()
