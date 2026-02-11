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

def solve_inverse():
    
    n = int(input("Enter size of matrix (n x n): ")) #รับข้อมูลจากผู้ใช้

    matrix = []
    print("Enter the matrix elements " + str(n) + " numbers:")
    
    i = 0
    while i < n:
        row = [float(x) for x in input("Row " + str(i+1) + ": ").split()]
        if len(row) != n:
            print("Error: You must enter " + str(n) + " numbers. Please try again.") # ให้กรอกแถวเดิมใหม่ถ้าจำนวนเลขไม่ครบ
            continue
        matrix.append(row)
        i += 1

    #ตรวจสอบค่า Determinant
    det = get_determinant(matrix)
    
    if det == 0:
        print("This is a Singular Matrix. Inverse does not exist (det = 0).")
        return

    #Gauss-Jordan
    # 1. สร้าง Augmented Matrix [A | I]
    aug = []
    for i in range(n):
        identity_row = [1.0 if i == j else 0.0 for j in range(n)]
        aug.append(matrix[i] + identity_row)

    # 2. เริ่มคำนวณกำจัดตัวเลข
    for i in range(n):
        # สลับแถว (Pivoting) กรณีเจอเลข 0 ในแนวทแยง
        if aug[i][i] == 0:
            for k in range(i + 1, n):
                if aug[k][i] != 0:
                    aug[i], aug[k] = aug[k], aug[i]
                    break
        
        # ปรับค่า Pivot (สมาชิกแนวทแยง) ให้เป็น 1
        pivot = aug[i][i]
        for j in range(2 * n):
            aug[i][j] /= pivot

        # ทำให้สมาชิกในหลักเดียวกันที่เหลือเป็น 0
        for k in range(n):
            if k != i:
                factor = aug[k][i]
                for j in range(2 * n):
                    aug[k][j] -= factor * aug[i][j]

    print("\n--- The Inverse Matrix is: ---")
    for row in aug:
        # ดึงเฉพาะส่วนขวาของ Augmented Matrix ออกมาแสดง
        inv_part = row[n:]
        formatted_row = [round(x, 3) for x in inv_part]
        print(formatted_row)

# ส่วนที่โปรแกรมทำงาน
solve_inverse()
