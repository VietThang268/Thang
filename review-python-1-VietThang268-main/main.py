import math

def solve_quadratic(a, b, c):
    """
    Giải phương trình bậc 2: ax^2 + bx + c = 0
    Trả về:
        - (x1, x2): nếu có 2 nghiệm phân biệt
        - (x1, None): nếu có nghiệm kép
        - None: nếu vô nghiệm
    """
    # Viết mã của bạn tại đây
    a = float(input("Nhap a:"))
    b = float(input("Nhap b:"))
    c = float(input("Nhap c:"))
    delta = b**2 - 4*a*c

    if delta < 0:
        print("None")
    elif delta == 0:
        print("Phuong Trinh Co Nghiem Kep x1=x2=", round(-b/(2*a)),1)
    else:
        print("Phuong Trinh Co 2 Nghiem Phan Biet:")
        print("x1=", round(-b - math.sqrt(delta) / 2*a),1)
        print("x2=", round(-b + math.sqrt(delta) / 2*a,1))

    pass
