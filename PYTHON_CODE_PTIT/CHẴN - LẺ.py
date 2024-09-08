# Cho số nguyên dương N. Hãy kiểm tra xem N có thỏa mãn đồng thời hai tính chất sau đây hay không?

# Tổng chữ số của N chia hết cho 10
# Các chữ số cạnh nhau đều khác nhau đúng 2 đơn vị
# Input

# Dòng đầu ghi số bộ test. Mỗi bộ test ghi trên một dòng số nguyên dương N. N có ít nhất 3 chữ số nhưng không quá 18 chữ số.

# Output

# Ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra

# Ví dụ

# Input

# Output

# 3

# 1353 NO

# 246864 YES

# 123435 NO



# # C1 - CONG NGHIEP 
from math import*
def tong(n):
    count = 0
    while n > 0:
        m = n%10
        count += m
        n//=10
    if count % 10 != 0:
        return False
    else:
        return True

def  check(n):
    m = n%10
    n//=10
    while n>0:
        x = n%10
        if abs(x-m) != 2:
            return False
    m = x
    n//=10


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        x = int(input())
        if tong(x) and check(x) :
            print('YES')
        else:
            print('NO')


# C2 - CHAT GPT

def check_conditions(n):
    total_sum = 0
    so_cuoi = n%10 # lay chu so cuoi
    n//=10 # loai bo chu so cuoi

    while n > 0:
        hien_tai = n%10
        total_sum += so_cuoi

        if abs(so_cuoi-hien_tai) !=2:
            return False
        
        so_cuoi = hien_tai
        n//=10
    

    total_sum += so_cuoi
    return total_sum % 10 == 0

if __name__ == '__main__':
    x = int(input())
    for _ in range(x):
        a = int(input())
        if check_conditions(a):
            print('YES')
        else:
            print('NO')


