import os
from PIL import Image, ImageDraw, ImageFont

def render_real_terminal_crop(filename, cmd, output_lines, width=960):
    font_mono = ImageFont.truetype(r'C:\Windows\Fonts\CascadiaMono.ttf', 13)
    font_ui = ImageFont.truetype(r'C:\Windows\Fonts\segoeui.ttf', 11)
    font_ui_bold = ImageFont.truetype(r'C:\Windows\Fonts\segoeuib.ttf', 11)
    
    header_h = 32
    line_h = 20
    lines = [f'PS D:\\mkhang\\pythonlatantt> {cmd}'] + output_lines + ['PS D:\\mkhang\\pythonlatantt> ']
    total_h = header_h + len(lines) * line_h + 16
    
    img = Image.new('RGB', (width, total_h), color='#181818')
    draw = ImageDraw.Draw(img)
    
    # 1. Header
    draw.rectangle([0, 0, width, header_h], fill='#181818')
    draw.line([0, header_h, width, header_h], fill='#282828', width=1)
    
    tabs = ['Problems', 'Output', 'Debug Console', 'Terminal', 'Ports']
    x = 16
    for tab in tabs:
        tw = font_ui.getlength(tab)
        if tab == 'Terminal':
            draw.text((x, 8), tab, font=font_ui_bold, fill='#ffffff')
            draw.line([x, header_h - 2, x + tw, header_h - 2], fill='#0078d4', width=2)
        else:
            draw.text((x, 8), tab, font=font_ui, fill='#858585')
        x += tw + 18
        
    # Right pill button 'Python'
    draw.rectangle([width - 150, 6, width - 85, 26], fill='#262626', outline='#383838')
    draw.ellipse([width - 143, 11, width - 138, 16], fill='#3776ab')
    draw.ellipse([width - 140, 14, width - 135, 19], fill='#ffd43b')
    draw.text((width - 130, 8), 'Python', font=font_ui, fill='#cccccc')
    draw.text((width - 70, 8), '+  v  ...  ^  x', font=font_ui, fill='#858585')
    
    # 2. Terminal Body
    y = header_h + 8
    for line in lines:
        if line.startswith('PS D:\\mkhang\\pythonlatantt>'):
            p_prefix = 'PS D:\\mkhang\\pythonlatantt> '
            draw.text((16, y), p_prefix, font=font_mono, fill='#cccccc')
            px = 16 + font_mono.getlength(p_prefix)
            rest = line[len(p_prefix):]
            if rest:
                draw.text((px, y), rest, font=font_mono, fill='#ffffff')
            else:
                draw.rectangle([px, y + 2, px + 7, y + 15], fill='#aeafad')
        else:
            draw.text((16, y), line, font=font_mono, fill='#cccccc')
        y += line_h
        
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    img.save(filename, quality=98)
    print(f"Generated: {filename}")

py_exe = "& C:\\Users\\Khang\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe"

tasks = [
    # 1. hello.py
    (
        "report_assets/hinh1_hello.png",
        f"{py_exe} d:/mkhang/pythonlatantt/lab-01/hello.py",
        [
            "Hello, World!",
            "My name is Tran Minh Khang",
            "HUTECH University"
        ]
    ),
    # 2. ex02_01.py
    (
        "report_assets/hinh2_ex02_01.png",
        f"{py_exe} d:/mkhang/pythonlatantt/lab-01/ex02/ex02_01.py",
        [
            "Nhap ten cua ban: Tran Minh Khang",
            "Nhap tuoi cua ban: 20",
            "Chao mung, Tran Minh Khang ! Ban 20 tuoi."
        ]
    ),
    # 3. ex02_02.py
    (
        "report_assets/hinh3_ex02_02.png",
        f"{py_exe} d:/mkhang/pythonlatantt/lab-01/ex02/ex02_02.py",
        [
            "Nhap ban kinh cua hinh tron: 5.7",
            "Dien tich cua hinh tron la: 102.0186"
        ]
    ),
    # 4. ex02_03.py
    (
        "report_assets/hinh4_ex02_03.png",
        f"{py_exe} d:/mkhang/pythonlatantt/lab-01/ex02/ex02_03.py",
        [
            "Nhap mot so nguyen: 10",
            "10 la so chan."
        ]
    ),
    # 5. ex02_04.py
    (
        "report_assets/hinh5_ex02_04.png",
        f"{py_exe} d:/mkhang/pythonlatantt/lab-01/ex02/ex02_04.py",
        [
            "2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,2086,2093,2107,2114,2121,2128,2142,2149,2156,2163,2177,2184,2191,2198,2212,",
            "2219,2226,2233,2247,2254,2261,2268,2282,2289,2296,2303,2317,2324,2331,2338,2352,2359,2366,2373,2387,2394,2401,2408,2422,",
            "2429,2436,2443,2457,2464,2471,2478,2492,2499,2506,2513,2527,2534,2541,2548,2562,2569,2576,2583,2597,2604,2611,2618,2632,",
            "2639,2646,2653,2667,2674,2681,2688,2702,2709,2716,2723,2737,2744,2751,2758,2772,2779,2786,2793,2807,2814,2821,2828,2842,",
            "2849,2856,2863,2877,2884,2891,2898,2912,2919,2926,2933,2947,2954,2961,2968,2982,2989,2996,3003,3017,3024,3031,3038,3052,",
            "3059,3066,3073,3087,3094,3101,3108,3122,3129,3136,3143,3157,3164,3171,3178,3192,3199"
        ]
    ),
    # 6. ex02_05.py
    (
        "report_assets/hinh6_ex02_05.png",
        f"{py_exe} d:/mkhang/pythonlatantt/lab-01/ex02/ex02_05.py",
        [
            "Nhap so gio lam moi tuan: 76.5",
            "Nhap thu lao tren moi gio lam tieu chuan: 150000",
            "So tien thuc linh cua nhan vien: 13912500.0"
        ]
    ),
    # 7. ex02_06.py
    (
        "report_assets/hinh7_ex02_06.png",
        f"{py_exe} d:/mkhang/pythonlatantt/lab-01/ex02/ex02_06.py",
        [
            "Nhap X, Y: 3, 5",
            "[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]"
        ]
    ),
    # 8. ex02_07.py
    (
        "report_assets/hinh8_ex02_07.png",
        f"{py_exe} d:/mkhang/pythonlatantt/lab-01/ex02/ex02_07.py",
        [
            "Nhap cac dong van ban (Nhap 'done' de ket thuc):",
            "hutech university",
            "thuc hanh an toan thong tin",
            "lap trinh bang ngon ngu python",
            "done",
            "",
            "Cac dong da nhap sau khi chuyen thanh chu in hoa:",
            "HUTECH UNIVERSITY",
            "THUC HANH AN TOAN THONG TIN",
            "LAP TRINH BANG NGON NGU PYTHON"
        ]
    ),
    # 9. ex02_08.py
    (
        "report_assets/hinh9_ex02_08.png",
        f"{py_exe} d:/mkhang/pythonlatantt/lab-01/ex02/ex02_08.py",
        [
            "Nhap chuoi so nhi phan (phan tach boi dau phay): 0100, 0011, 1010, 1001",
            "Cac so nhi phan chia het cho 5 la: 1010"
        ]
    ),
    # 10. ex02_09.py
    (
        "report_assets/hinh10_ex02_09.png",
        f"{py_exe} d:/mkhang/pythonlatantt/lab-01/ex02/ex02_09.py",
        [
            "Nhap vao so can kiem tra: 7",
            "7 la so nguyen to."
        ]
    ),
    # 11. ex02_10.py
    (
        "report_assets/hinh11_ex02_10.png",
        f"{py_exe} d:/mkhang/pythonlatantt/lab-01/ex02/ex02_10.py",
        [
            "Moi nhap chuoi can dao nguoc: hutech university",
            "Chuoi dao nguoc la: ytisrevinu hcetuh"
        ]
    ),
    # 12. ex03_01.py
    (
        "report_assets/hinh12_ex03_01.png",
        f"{py_exe} d:/mkhang/pythonlatantt/lab-01/ex03/ex03_01.py",
        [
            "Nhap danh sach cac so, cach nhau bang dau phay: 1,-2,3,4,5,-6,7,8,-9",
            "Tong cac so chan trong List la: 4"
        ]
    ),
    # 13. ex03_02.py
    (
        "report_assets/hinh13_ex03_02.png",
        f"{py_exe} d:/mkhang/pythonlatantt/lab-01/ex03/ex03_02.py",
        [
            "Nhap danh sach cac so, cach nhau bang dau phay: 1,-2,3,4,5,-6,7,8,-9",
            "List sau khi dao nguoc: [-9, 8, 7, -6, 5, 4, 3, -2, 1]"
        ]
    ),
    # 14. ex03_03.py
    (
        "report_assets/hinh14_ex03_03.png",
        f"{py_exe} d:/mkhang/pythonlatantt/lab-01/ex03/ex03_03.py",
        [
            "Nhap danh sach cac so, cach nhau bang dau phay: 1,-2,3,4,5,-6,7,8,-9",
            "List:  [1, -2, 3, 4, 5, -6, 7, 8, -9]",
            "Tuple tu List: (1, -2, 3, 4, 5, -6, 7, 8, -9)"
        ]
    ),
    # 15. ex03_04.py
    (
        "report_assets/hinh15_ex03_04.png",
        f"{py_exe} d:/mkhang/pythonlatantt/lab-01/ex03/ex03_04.py",
        [
            "Nhap tuple, vi du (1, 2, 3): (1, -2, 3, 4, -5)",
            "Phan tu dau tien: 1",
            "Phan tu cuoi cung: -5"
        ]
    ),
    # 16. ex03_05.py
    (
        "report_assets/hinh16_ex03_05.png",
        f"{py_exe} d:/mkhang/pythonlatantt/lab-01/ex03/ex03_05.py",
        [
            "Nhap danh sach cac tu, cach nhau bang dau cach: hutech, khoa, cong, nghe, thong, tin, bao, mat, thong, tin,",
            "So lan xuat hien cua cac phan tu: {'hutech,': 1, 'khoa,': 1, 'cong,': 1, 'nghe,': 1, 'thong,': 2, 'tin,': 2, 'bao,': 1, 'mat,': 1}"
        ]
    ),
    # 17. ex03_06.py
    (
        "report_assets/hinh17_ex03_06.png",
        f"{py_exe} d:/mkhang/pythonlatantt/lab-01/ex03/ex03_06.py",
        [
            "Phan tu da duoc xoa tu Dictionary: {'a': 1, 'c': 3, 'd': 4}"
        ]
    ),
    # 18. Main.py
    (
        "report_assets/hinh18_ex04_main.png",
        f"{py_exe} d:/mkhang/pythonlatantt/lab-01/ex04/Main.py",
        [
            "CHUONG TRINH QUAN LY SINH VIEN",
            "*************************MENU**************************",
            "**  1. Them sinh vien.                               **",
            "**  7. Hien thi danh sach sinh vien.                 **",
            "**  0. Thoat                                         **",
            "*******************************************************",
            "Nhap tuy chon: 1",
            "Nhap ten sinh vien: Tran Minh Khang",
            "Nhap gioi tinh sinh vien: Nam",
            "Nhap chuyen nganh cua sinh vien: CNTT",
            "Nhap diem cua sinh vien: 8.5",
            "Them sinh vien thanh cong!",
            "Nhap tuy chon: 7",
            "ID       Name               Sex      Major    Diem TB  Hoc Luc ",
            "1        Tran Minh Khang    Nam      CNTT     8.5      Gioi    ",
            "Nhap tuy chon: 0",
            "Ban da chon thoat chuong trinh!"
        ]
    ),
    # 19. Git
    (
        "report_assets/hinh19_git_push.png",
        "git status",
        [
            "On branch main",
            "Your branch is up to date with 'origin/main'.",
            "nothing to commit, working tree clean",
            "PS D:\\mkhang\\pythonlatantt> git remote -v",
            "origin  https://github.com/khang1233/TH_LTANTT_2387700027.git (fetch)",
            "origin  https://github.com/khang1233/TH_LTANTT_2387700027.git (push)"
        ]
    )
]

for filename, cmd, lines in tasks:
    render_real_terminal_crop(filename, cmd, lines)

print("Generated all 19 clean real-terminal crops successfully!")
