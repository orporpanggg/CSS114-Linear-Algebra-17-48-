def gauss_jordan_elimination():
    
    #รับข้อมูล
    n = int(input("Enter number of variables: "))
    
    # สร้าง Augmented Matrix
    matrix = []
    print("Enter Augmented Matrix (" + str(n) + "x" + str(n + 1) + "):")
    for i in range(n):
        # รับค่าทั้ง row (เช่น ถ้า n=3 ต้องกรอก 4 ตัวเลข)
        row = [float(x) for x in input().split()]
        matrix.append(row)

    #Gauss-Jordan
    for i in range(n):
        #หาค่าสัมบูรณ์มากที่สุดในคอลัมน์ เหมือนกับการทำ pivoting
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k
        
        # สลับแถวเพื่อให้ค่ามากที่สุดเป็น Pivot
        temp = matrix[i]           #เอาแถวปัจจุบันไปฝากไว้ใน temp
        matrix[i] = matrix[max_row] #เอาแถวที่ใหญ่กว่ามาทับแถวปัจจุบัน
        matrix[max_row] = temp     # 3เอาค่าใน temp กลับไปวางที่แถวที่เคยใหญ่ที่สุด
        
        # ตรวจสอบ Singular Matrix (ป้องกันการหารด้วยศูนย์)
        if abs(matrix[i][i]) < 1e-12:
            print("Matrix is singular.")
            return

        # ทำให้ Pivot เป็น 1
        # นำค่า Pivot มาหารทั้งแถวเพื่อให้ตำแหน่ง A[i][i] กลายเป็น 1
        pivot = matrix[i][i]
        for j in range(i, n + 1):
            matrix[i][j] /= pivot

        #ทำให้คอลัมน์นั้นเป็น 0 ทั้งด้านบนและด้านล่าง
        for k in range(n):
            if k != i:  # ทำทุกแถวที่ไม่ใช่แถว Pivot ปัจจุบัน
                factor = matrix[k][i]
                for j in range(i, n + 1):
                    # R_k = R_k - (factor * R_i)
                    matrix[k][j] -= factor * matrix[i][j]

    #สรุปคำตอบ โดยผลลัพธ์จะอยู่ในคอลัมน์สุดท้ายของ matrix
    result = [row[n] for row in matrix]
    return result

# ส่วนที่โปรแกรมทำงาน
result = gauss_jordan_elimination()
if result:
    for idx, val in enumerate(result):
        print(f"x{idx+1} = {round(val, 3)}")
