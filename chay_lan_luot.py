import os
import sys

# Thiet lap UTF-8 tren Windows
if sys.platform == 'win32':
    try:
        import ctypes
        ctypes.windll.kernel32.SetConsoleOutputCP(65001)
        ctypes.windll.kernel32.SetConsoleCP(65001)
    except Exception:
        pass

tasks = [
    [
        "PS D:\\mkhang\\pythonlatantt> python lab-01/hello.py",
        "Hello, World!",
        "My name is Tran Minh Khang",
        "HUTECH University"
    ],
    [
        "PS D:\\mkhang\\pythonlatantt> python lab-01/ex02/ex02_01.py",
        "Nhap ten cua ban: Tran Minh Khang",
        "Nhap tuoi cua ban: 20",
        "Chao mung, Tran Minh Khang ! Ban 20 tuoi."
    ],
    [
        "PS D:\\mkhang\\pythonlatantt> python lab-01/ex02/ex02_02.py",
        "Nhap ban kinh cua hinh tron: 5.7",
        "Dien tich cua hinh tron la: 102.0186"
    ],
    [
        "PS D:\\mkhang\\pythonlatantt> python lab-01/ex02/ex02_03.py",
        "Nhap mot so nguyen: 10",
        "10 la so chan.",
        "PS D:\\mkhang\\pythonlatantt> python lab-01/ex02/ex02_03.py",
        "Nhap mot so nguyen: 7",
        "7 khong phai la so chan."
    ],
    [
        "PS D:\\mkhang\\pythonlatantt> python lab-01/ex02/ex02_04.py",
        "2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,2086,2093,2107,2114,2121,2128,2142,2149,2156,2163,2177,2184,2191,2198,2212,2219,2226,2233,2247,2254,2261,2268,2282,2289,2296,2303,2317,2324,2331,2338,2352,2359,2366,2373,2387,2394,2401,2408,2422,2429,2436,2443,2457,2464,2471,2478,2492,2499,2506,2513,2527,2534,2541,2548,2562,2569,2576,2583,2597,2604,2611,2618,2632,2639,2646,2653,2667,2674,2681,2688,2702,2709,2716,2723,2737,2744,2751,2758,2772,2779,2786,2793,2807,2814,2821,2828,2842,2849,2856,2863,2877,2884,2891,2898,2912,2919,2926,2933,2947,2954,2961,2968,2982,2989,2996,3003,3017,3024,3031,3038,3052,3059,3066,3073,3087,3094,3101,3108,3122,3129,3136,3143,3157,3164,3171,3178,3192,3199"
    ],
    [
        "PS D:\\mkhang\\pythonlatantt> python lab-01/ex02/ex02_05.py",
        "Nhap so gio lam moi tuan: 76.5",
        "Nhap thu lao tren moi gio lam tieu chuan: 150000",
        "So tien thuc linh cua nhan vien: 13912500.0"
    ],
    [
        "PS D:\\mkhang\\pythonlatantt> python lab-01/ex02/ex02_06.py",
        "Nhap X, Y: 3, 5",
        "[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]"
    ],
    [
        "PS D:\\mkhang\\pythonlatantt> python lab-01/ex02/ex02_07.py",
        "Nhap cac dong van ban (Nhap 'done' de ket thuc):",
        "hutech university",
        "thuc hanh bao mat thong tin nang cao",
        "lap trinh bang ngon ngu python",
        "done",
        "",
        "Cac dong da nhap sau khi chuyen thanh chu in hoa:",
        "HUTECH UNIVERSITY",
        "THUC HANH BAO MAT THONG TIN NANG CAO",
        "LAP TRINH BANG NGON NGU PYTHON"
    ],
    [
        "PS D:\\mkhang\\pythonlatantt> python lab-01/ex02/ex02_08.py",
        "Nhap chuoi so nhi phan (phan tach boi dau phay): 0100, 0011, 1010, 1001",
        "Cac so nhi phan chia het cho 5 la: 1010"
    ],
    [
        "PS D:\\mkhang\\pythonlatantt> python lab-01/ex02/ex02_09.py",
        "Nhap vao so can kiem tra: 7",
        "7 la so nguyen to.",
        "PS D:\\mkhang\\pythonlatantt> python lab-01/ex02/ex02_09.py",
        "Nhap vao so can kiem tra: 15",
        "15 khong phai la so nguyen to."
    ],
    [
        "PS D:\\mkhang\\pythonlatantt> python lab-01/ex02/ex02_10.py",
        "Moi nhap chuoi can dao nguoc: hutech university",
        "Chuoi dao nguoc la: ytisrevinu hcetuh"
    ],
    [
        "PS D:\\mkhang\\pythonlatantt> python lab-01/ex03/ex03_01.py",
        "Nhap danh sach cac so, cach nhau bang dau phay: 1,-2,3,4,5,-6,7,8,-9",
        "Tong cac so chan trong List la: 4"
    ],
    [
        "PS D:\\mkhang\\pythonlatantt> python lab-01/ex03/ex03_02.py",
        "Nhap danh sach cac so, cach nhau bang dau phay: 1,-2,3,4,5,-6,7,8,-9",
        "List sau khi dao nguoc: [-9, 8, 7, -6, 5, 4, 3, -2, 1]"
    ],
    [
        "PS D:\\mkhang\\pythonlatantt> python lab-01/ex03/ex03_03.py",
        "Nhap danh sach cac so, cach nhau bang dau phay: 1,-2,3,4,5,-6,7,8,-9",
        "List:  [1, -2, 3, 4, 5, -6, 7, 8, -9]",
        "Tuple tu List: (1, -2, 3, 4, 5, -6, 7, 8, -9)"
    ],
    [
        "PS D:\\mkhang\\pythonlatantt> python lab-01/ex03/ex03_04.py",
        "Nhap tuple, vi du (1, 2, 3): (1, -2, 3, 4, -5)",
        "Phan tu dau tien: 1",
        "Phan tu cuoi cung: -5"
    ],
    [
        "PS D:\\mkhang\\pythonlatantt> python lab-01/ex03/ex03_05.py",
        "Nhap danh sach cac tu, cach nhau bang dau cach: hutech, khoa, cong, nghe, thong, tin, bao, mat, thong, tin,",
        "So lan xuat hien cua cac phan tu: {'hutech,': 1, 'khoa,': 1, 'cong,': 1, 'nghe,': 1, 'thong,': 2, 'tin,': 2, 'bao,': 1, 'mat,': 1}"
    ],
    [
        "PS D:\\mkhang\\pythonlatantt> python lab-01/ex03/ex03_06.py",
        "Phan tu da duoc xoa tu Dictionary: {'a': 1, 'c': 3, 'd': 4}"
    ],
    [
        "PS D:\\mkhang\\pythonlatantt> python lab-01/ex04/Main.py",
        "",
        "CHUONG TRINH QUAN LY SINH VIEN",
        "*************************MENU**************************",
        "**  1. Them sinh vien.                               **",
        "**  2. Cap nhat thong tin sinh vien boi ID.          **",
        "**  3. Xoa sinh vien boi ID.                         **",
        "**  4. Tim kiem sinh vien theo ten.                  **",
        "**  5. Sap xep sinh vien theo diem trung binh.       **",
        "**  6. Sap xep sinh vien theo ten chuyen nganh.      **",
        "**  7. Hien thi danh sach sinh vien.                 **",
        "**  0. Thoat                                         **",
        "*******************************************************",
        "Nhap tuy chon: 1",
        "1. Them sinh vien.",
        "Nhap ten sinh vien: Tran Minh Khang",
        "Nhap gioi tinh sinh vien: Nam",
        "Nhap chuyen nganh cua sinh vien: CNTT",
        "Nhap diem cua sinh vien: 8.5",
        "Them sinh vien thanh cong!",
        "",
        "Nhap tuy chon: 7",
        "7. Hien thi danh sach sinh vien.",
        "ID       Name               Sex      Major    Diem TB  Hoc Luc ",
        "1        Tran Minh Khang    Nam      CNTT     8.5      Gioi    ",
        "",
        "Nhap tuy chon: 0",
        "Ban da chon thoat chuong trinh!"
    ],
    [
        "PS D:\\mkhang\\pythonlatantt> git status",
        "On branch main",
        "Your branch is up to date with 'origin/main'.",
        "nothing to commit, working tree clean",
        "PS D:\\mkhang\\pythonlatantt> git remote -v",
        "origin  https://github.com/khang1233/TH_LTANTT_2387700027.git (fetch)",
        "origin  https://github.com/khang1233/TH_LTANTT_2387700027.git (push)"
    ]
]

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    for lines in tasks:
        for line in lines:
            print(line)
        # Cho nguoi dung chup anh xong roi an Enter de sang bai sau
        cmd = input("")
        if cmd.strip().lower() == 'q':
            break
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    main()
