def gauss_elimination_withpivoting(): #ฟังก์ชันในการแก้ปัญหาระบบสมการเชิงเส้นด้วยวิธี Gauss Elimination with pivoting
    # ส่วนที่รับสมการเข้ามาและแปลงรูปเป็น Matrix 
    n = int(input("Enter number of variables: ")) #ให้กรอกจำนวนเลขที่จะใส่ในแต่ละ rows เช่น ถ้ามี x_1, x_2, x_3 ให้พิมพ์ 3
    A = [] #สร้าง List ว่างเพื่อรอรับข้อมูล rows ของเมทริกซ์ A โดยจะเก็บเมทริกซ์ในรูปแบบ Nested List ก็คือ List ที่ซ้อนอยู่ข้างใน List
    
    #เริ่มสร้างเมทริกซ์
    print("Enter Matrix A (" + str(n) + "x" + str(n) + "):")
    for i in range(n): #วนลูปตามจำนวนแถวที่ระบุไว้ใน n
        A.append([float(x) for x in input().split()]) #ใช้ list comprehension สำหรับการรับค่าตัวเลขหลายๆ ตัวในบรรทัดเดียว
        
    print("Enter Vector b ("+ str(n) + " values):") #รับค่า matrix B
    B = [float(x) for x in input().split()] #ใช้ list comprehension

    #ทำให้เป็น Upper Triangular Matrix ด้วยวิธี Forward Elimination
    for i in range(n):
        
        #หาค่าที่มากที่สุดใน Column เพื่อเลือก Pivot
        
        #สมมติให้แถวปัจจุบัน (i) มีค่า Pivot มากที่สุดไว้ก่อน
        max_row = i
        #ลูป k จะเริ่มหาตั้งแต่แถวที่อยู่ใต้ Pivot ปัจจุบันลงไป (i + 1 ถึง n)
        for k in range(i + 1, n):
            #เปรียบเทียบค่าสัมบูรณ์ในคอลัมน์ i (คอลัมน์ปัจจุบันที่เรากำลังกำจัดเลข 0)
            #ถ้าแถวที่ k มีค่าใหญ่กว่าแถวที่เราจำไว้ (max_row)
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k #อัปเดตตำแหน่งแถวที่มีค่ามากที่สุดใหม่
        
        #สลับแถว
        # - สลับแถวใน Matrix A
        temp_A = A[i]          # 1. เอาแถวปัจจุบันไปฝากไว้ในที่ temp
        A[i] = A[max_row]      # 2. เอาแถวที่ใหญ่กว่ามาทับที่แถวปัจจุบัน
        A[max_row] = temp_A    # 3. เอาแถวใน temp กลับไปวางที่แถวที่ว่างอยู่
        # -สลับแถวใน Matrix B
        temp_B = B[i]          # 1. ฝากค่า b แถวปัจจุบันไว้ที่ temp
        B[i] = B[max_row]      # 2. เอาค่า b แถวที่ใหญ่กว่ามาทับ
        B[max_row] = temp_B    # 3. เอาค่าใน temp_B กลับไปวาง

        # ตรวจสอบ Singular matrix เพื่อป้องกันการหารด้วยศูนย์
        if abs(A[i][i]) < 1e-12: #เช็คว่ามันเล็กมากจนเข้าใกล้ 0 หรือไม่
            print("Matrix is singular") #คำตอบของ Singular matrix คือ No solution / Infinite Solutions
            return
            # ถ้า A[i][i] เป็น 0 คอมพิวเตอร์จะเกิด Division by Zero Error และโปรแกรมจะค้างหรือหยุดทำงานทันที

        # เริ่มต้นกำจัดตัวเลขใต้ Pivot
        for k in range(i + 1, n):
            factor = A[k][i] / A[i][i] # คือการคำนวณตัวคูณ โดยนำ "ตัวเลขที่ต้องการกำจัด" (A[k][i]) หารด้วย "ตัวเลขที่เป็น Pivot" (A[i][i]) เพื่อให้รู้ว่าต้องขยายแถว Pivot ไปกี่เท่าถึงจะนำไปลบแถวข้างล่างได้หมดพอดี
            for j in range(i, n): #ลูปนี้จะไล่คำนวณไปทีละคอลัมน์ในแถวนั้น ๆ ตั้งแต่ตำแหน่ง Pivot ไปจนจบแถว
                # ปรับปรุงค่าในเมทริกซ์ A: R_k = R_k - (factor * R_i)
                A[k][j] -= factor * A[i][j]
            # ปรับปรุงค่าในเวกเตอร์ b
            B[k] -= factor * B[i]

    # Backward Substitution
    x = [0] * n #สร้างลิสต์สำหรับเก็บคำตอบ x โดยเริ่มจากค่า 0 จำนวน n ตัว (เช่น [0, 0, 0])
    for i in range(n - 1, -1, -1): #คือการวนลูปถอยหลัง (Backward) จากแถวสุดท้ายขึ้นไปแถวแรก (เช่น จากดัชนี 2 -> 1 -> 0)
        # x_i = (b_i - sum(a_ij * x_j)) / a_ii
        ## ผลรวมของตัวแปรที่รู้ค่าแล้ว (ทางขวาของ Pivot)
        sum_ax = sum(A[i][j] * x[j] for j in range(i + 1, n)) #สูตร
        # คำนวณหาค่า x แถวปัจจุบัน
        x[i] = (B[i] - sum_ax) / A[i][i]
        
    return x

# ส่วนที่โปรแกรมทำงาน
result = gauss_elimination_withpivoting() #เรียกใช้ฟังก์ชัน gauss_elimination_withpivoting
if result: #ถ้ามีคำตอบให้ทำตามเงื่อนไขด้านล่าง
    print("x:", [round(val, 3) for val in result])
