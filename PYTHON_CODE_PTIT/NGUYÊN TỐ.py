# Trong toán học, một cặp số được gọi là nguyên tố cùng nhau nếu ước số chung lớn nhất của 2 số đó là 1. Cho số nguyên dương N,
# giả sử ta đếm được K số nguyên dương nhỏ hơn N có tính chất nguyên tố cùng nhau với N. Hãy kiểm tra xem K có phải là số nguyên tố hay không.

# Input

# Dòng đầu ghi số bộ test, không quá 10.

# Dòng thứ 2 ghi số N (1 < N < 10000)

# Output

# Với mỗi test ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

# Ví dụ

# Input

# Output

# 2

# 2  NO

# 3  YES

from math import*
def nt(n):
    if n<2:
        return False
    else:
        for i in range(2,isqrt(n)+1):
            if n%i==0:
                return False
    return True


def count_coprimes(N):
    count = 0
    for i in range(N):
        if gcd(i,N) == 1:
            count += 1
    return count


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N  = int(input())
        coprime_count = count_coprimes(N)  # Đếm số các số nguyên tố cùng nhau với N
        if nt(coprime_count):   # Kiểm tra xem số đếm có phải là số nguyên tố không
            print('YES')
        else:
            print('NO')