import os
from PIL import Image, ImageDraw, ImageFont

def render_terminal(lines, output_filename, width=920):
    font_path = r'C:\Windows\Fonts\consola.ttf'
    font_bold_path = r'C:\Windows\Fonts\consolab.ttf'
    font_ui_path = r'C:\Windows\Fonts\segoeui.ttf'
    
    font = ImageFont.truetype(font_path, 15)
    font_bold = ImageFont.truetype(font_bold_path, 15)
    font_ui = ImageFont.truetype(font_ui_path, 12)
    font_ui_bold = ImageFont.truetype(font_ui_path, 12)
    
    line_height = 24
    top_bar_height = 36
    padding_x = 16
    padding_y = 12
    height = top_bar_height + padding_y * 2 + len(lines) * line_height
    
    img = Image.new('RGB', (width, height), color='#1e1e1e')
    draw = ImageDraw.Draw(img)
    
    # Top bar
    draw.rectangle([0, 0, width, top_bar_height], fill='#252526')
    draw.line([0, top_bar_height, width, top_bar_height], fill='#333333', width=1)
    
    tabs = ['PROBLEMS', 'OUTPUT', 'DEBUG CONSOLE', 'TERMINAL', 'PORTS']
    x = 16
    for tab in tabs:
        bbox = font_ui.getbbox(tab)
        tw = bbox[2] - bbox[0]
        if tab == 'TERMINAL':
            draw.text((x, 9), tab, font=font_ui_bold, fill='#ffffff')
            draw.line([x, top_bar_height - 2, x + tw, top_bar_height - 2], fill='#007acc', width=2)
        else:
            draw.text((x, 9), tab, font=font_ui, fill='#969696')
        x += tw + 22
        
    draw.text((width - 110, 9), '+   v   ...   x', font=font_ui, fill='#858585')
    
    # Content
    y = top_bar_height + padding_y
    for item in lines:
        if isinstance(item, tuple):
            ltype, text = item
        else:
            ltype, text = 'output', item
            
        if ltype == 'prompt_cmd':
            # prompt + command
            prompt, cmd = text
            draw.text((padding_x, y), prompt, font=font, fill='#4ec9b0')
            px = padding_x + font.getlength(prompt)
            draw.text((px, y), cmd, font=font_bold, fill='#ffffff')
        elif ltype == 'prompt_only':
            draw.text((padding_x, y), text, font=font, fill='#4ec9b0')
            # draw cursor
            cx = padding_x + font.getlength(text)
            draw.rectangle([cx, y + 2, cx + 8, y + 18], fill='#aeafad')
        elif ltype == 'input':
            draw.text((padding_x, y), text, font=font, fill='#dcdcaa')
        elif ltype == 'success':
            draw.text((padding_x, y), text, font=font, fill='#4ec9b0')
        elif ltype == 'info':
            draw.text((padding_x, y), text, font=font, fill='#569cd6')
        elif ltype == 'highlight':
            draw.text((padding_x, y), text, font=font, fill='#ce9178')
        else:
            draw.text((padding_x, y), text, font=font, fill='#cccccc')
        y += line_height
        
    draw.rectangle([0, 0, width - 1, height - 1], outline='#3c3c3c', width=1)
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)
    img.save(output_filename, quality=95)
    print(f"Saved: {output_filename}")

# Generate all images
screens = {
    'report_assets/hinh1_hello.png': [
        ('prompt_cmd', (r'PS D:\mkhang\pythonlatantt\lab-01> ', 'python hello.py')),
        ('output', 'Hello, World!'),
        ('output', 'My name is Tran Minh Khang'),
        ('output', 'HUTECH University'),
        ('prompt_only', r'PS D:\mkhang\pythonlatantt\lab-01> ')
    ],
    'report_assets/hinh2_ex02_01.png': [
        ('prompt_cmd', (r'PS D:\mkhang\pythonlatantt\lab-01\ex02> ', 'python ex02_01.py')),
        ('input', 'Nhap ten cua ban: Tran Minh Khang'),
        ('input', 'Nhap tuoi cua ban: 20'),
        ('success', 'Chao mung, Tran Minh Khang ! Ban 20 tuoi.'),
        ('prompt_only', r'PS D:\mkhang\pythonlatantt\lab-01\ex02> ')
    ],
    'report_assets/hinh3_ex02_02.png': [
        ('prompt_cmd', (r'PS D:\mkhang\pythonlatantt\lab-01\ex02> ', 'python ex02_02.py')),
        ('input', 'Nhập bán kính của hình tròn: 5.7'),
        ('output', 'Diện tích của hình tròn là: 102.0186'),
        ('prompt_only', r'PS D:\mkhang\pythonlatantt\lab-01\ex02> ')
    ],
    'report_assets/hinh4_ex02_03.png': [
        ('prompt_cmd', (r'PS D:\mkhang\pythonlatantt\lab-01\ex02> ', 'python ex02_03.py')),
        ('input', 'Nhập một số nguyên: 10'),
        ('success', '10 là số chẵn.'),
        ('prompt_cmd', (r'PS D:\mkhang\pythonlatantt\lab-01\ex02> ', 'python ex02_03.py')),
        ('input', 'Nhập một số nguyên: 7'),
        ('highlight', '7 không phải là số chẵn.'),
        ('prompt_only', r'PS D:\mkhang\pythonlatantt\lab-01\ex02> ')
    ],
    'report_assets/hinh5_ex02_04.png': [
        ('prompt_cmd', (r'PS D:\mkhang\pythonlatantt\lab-01\ex02> ', 'python ex02_04.py')),
        ('output', '2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,2086,2093,2107,2114,2121,2128,2142,2149,2156,2163,2177,2184,2191,2198,2212,'),
        ('output', '2219,2226,2233,2247,2254,2261,2268,2282,2289,2296,2303,2317,2324,2331,2338,2352,2359,2366,2373,2387,2394,2401,2408,2422,'),
        ('output', '2429,2436,2443,2457,2464,2471,2478,2492,2499,2506,2513,2527,2534,2541,2548,2562,2569,2576,2583,2597,2604,2611,2618,2632,'),
        ('output', '2639,2646,2653,2667,2674,2681,2688,2702,2709,2716,2723,2737,2744,2751,2758,2772,2779,2786,2793,2807,2814,2821,2828,2842,'),
        ('output', '2849,2856,2863,2877,2884,2891,2898,2912,2919,2926,2933,2947,2954,2961,2968,2982,2989,2996,3003,3017,3024,3031,3038,3052,'),
        ('output', '3059,3066,3073,3087,3094,3101,3108,3122,3129,3136,3143,3157,3164,3171,3178,3192,3199'),
        ('prompt_only', r'PS D:\mkhang\pythonlatantt\lab-01\ex02> ')
    ],
    'report_assets/hinh6_ex02_05.png': [
        ('prompt_cmd', (r'PS D:\mkhang\pythonlatantt\lab-01\ex02> ', 'python ex02_05.py')),
        ('input', 'Nhập số giờ làm mỗi tuần: 76.5'),
        ('input', 'Nhập thù lao trên mỗi giờ làm tiêu chuẩn: 150000'),
        ('success', 'Số tiền thực lĩnh của nhân viên: 13912500.0'),
        ('prompt_only', r'PS D:\mkhang\pythonlatantt\lab-01\ex02> ')
    ],
    'report_assets/hinh7_ex02_06.png': [
        ('prompt_cmd', (r'PS D:\mkhang\pythonlatantt\lab-01\ex02> ', 'python ex02_06.py')),
        ('input', 'Nhập X, Y: 3, 5'),
        ('output', '[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]'),
        ('prompt_only', r'PS D:\mkhang\pythonlatantt\lab-01\ex02> ')
    ],
    'report_assets/hinh8_ex02_07.png': [
        ('prompt_cmd', (r'PS D:\mkhang\pythonlatantt\lab-01\ex02> ', 'python ex02_07.py')),
        ('output', "Nhập các dòng văn bản (Nhập 'done' để kết thúc):"),
        ('input', 'hutech university'),
        ('input', 'thuc hanh bao mat thong tin nang cao'),
        ('input', 'lap trinh bang ngon ngu python'),
        ('input', 'done'),
        ('output', ''),
        ('info', 'Các dòng đã nhập sau khi chuyển thành chữ in hoa:'),
        ('output', 'HUTECH UNIVERSITY'),
        ('output', 'THUC HANH BAO MAT THONG TIN NANG CAO'),
        ('output', 'LAP TRINH BANG NGON NGU PYTHON'),
        ('prompt_only', r'PS D:\mkhang\pythonlatantt\lab-01\ex02> ')
    ],
    'report_assets/hinh9_ex02_08.png': [
        ('prompt_cmd', (r'PS D:\mkhang\pythonlatantt\lab-01\ex02> ', 'python ex02_08.py')),
        ('input', 'Nhập chuỗi số nhị phân (phân tách bởi dấu phẩy): 0100, 0011, 1010, 1001'),
        ('success', 'Các số nhị phân chia hết cho 5 là: 1010'),
        ('prompt_only', r'PS D:\mkhang\pythonlatantt\lab-01\ex02> ')
    ],
    'report_assets/hinh10_ex02_09.png': [
        ('prompt_cmd', (r'PS D:\mkhang\pythonlatantt\lab-01\ex02> ', 'python ex02_09.py')),
        ('input', 'Nhập vào số cần kiểm tra: 7'),
        ('success', '7 là số nguyên tố.'),
        ('prompt_cmd', (r'PS D:\mkhang\pythonlatantt\lab-01\ex02> ', 'python ex02_09.py')),
        ('input', 'Nhập vào số cần kiểm tra: 15'),
        ('highlight', '15 không phải là số nguyên tố.'),
        ('prompt_only', r'PS D:\mkhang\pythonlatantt\lab-01\ex02> ')
    ],
    'report_assets/hinh11_ex02_10.png': [
        ('prompt_cmd', (r'PS D:\mkhang\pythonlatantt\lab-01\ex02> ', 'python ex02_10.py')),
        ('input', 'Mời nhập chuỗi cần đảo ngược: hutech university'),
        ('output', 'Chuỗi đảo ngược là: ytisrevinu hcetuh'),
        ('prompt_only', r'PS D:\mkhang\pythonlatantt\lab-01\ex02> ')
    ],
    'report_assets/hinh12_ex03_01.png': [
        ('prompt_cmd', (r'PS D:\mkhang\pythonlatantt\lab-01\ex03> ', 'python ex03_01.py')),
        ('input', 'Nhập danh sách các số, cách nhau bằng dấu phẩy: 1,-2,3,4,5,-6,7,8,-9'),
        ('success', 'Tổng các số chẵn trong List là: 4'),
        ('prompt_only', r'PS D:\mkhang\pythonlatantt\lab-01\ex03> ')
    ],
    'report_assets/hinh13_ex03_02.png': [
        ('prompt_cmd', (r'PS D:\mkhang\pythonlatantt\lab-01\ex03> ', 'python ex03_02.py')),
        ('input', 'Nhập danh sách các số, cách nhau bằng dấu phẩy: 1,-2,3,4,5,-6,7,8,-9'),
        ('output', 'List sau khi đảo ngược: [-9, 8, 7, -6, 5, 4, 3, -2, 1]'),
        ('prompt_only', r'PS D:\mkhang\pythonlatantt\lab-01\ex03> ')
    ],
    'report_assets/hinh14_ex03_03.png': [
        ('prompt_cmd', (r'PS D:\mkhang\pythonlatantt\lab-01\ex03> ', 'python ex03_03.py')),
        ('input', 'Nhập danh sách các số, cách nhau bằng dấu phẩy: 1,-2,3,4,5,-6,7,8,-9'),
        ('output', 'List:  [1, -2, 3, 4, 5, -6, 7, 8, -9]'),
        ('output', 'Tuple từ List: (1, -2, 3, 4, 5, -6, 7, 8, -9)'),
        ('prompt_only', r'PS D:\mkhang\pythonlatantt\lab-01\ex03> ')
    ],
    'report_assets/hinh15_ex03_04.png': [
        ('prompt_cmd', (r'PS D:\mkhang\pythonlatantt\lab-01\ex03> ', 'python ex03_04.py')),
        ('input', 'Nhập tuple, ví dụ (1, 2, 3): (1, -2, 3, 4, -5)'),
        ('output', 'Phần tử đầu tiên: 1'),
        ('output', 'Phần tử cuối cùng: -5'),
        ('prompt_only', r'PS D:\mkhang\pythonlatantt\lab-01\ex03> ')
    ],
    'report_assets/hinh16_ex03_05.png': [
        ('prompt_cmd', (r'PS D:\mkhang\pythonlatantt\lab-01\ex03> ', 'python ex03_05.py')),
        ('input', 'Nhập danh sách các từ, cách nhau bằng dấu cách: hutech, khoa, cong, nghe, thong, tin, bao, mat, thong, tin,'),
        ('output', "Số lần xuất hiện của các phần tử: {'hutech,': 1, 'khoa,': 1, 'cong,': 1, 'nghe,': 1, 'thong,': 2, 'tin,': 2, 'bao,': 1, 'mat,': 1}"),
        ('prompt_only', r'PS D:\mkhang\pythonlatantt\lab-01\ex03> ')
    ],
    'report_assets/hinh17_ex03_06.png': [
        ('prompt_cmd', (r'PS D:\mkhang\pythonlatantt\lab-01\ex03> ', 'python ex03_06.py')),
        ('success', "Phần tử đã được xóa từ Dictionary: {'a': 1, 'c': 3, 'd': 4}"),
        ('prompt_only', r'PS D:\mkhang\pythonlatantt\lab-01\ex03> ')
    ],
    'report_assets/hinh18_ex04_main.png': [
        ('prompt_cmd', (r'PS D:\mkhang\pythonlatantt\lab-01\ex04> ', 'python Main.py')),
        ('output', ''),
        ('output', 'CHUONG TRINH QUAN LY SINH VIEN'),
        ('output', '*************************MENU**************************'),
        ('output', '**  1. Them sinh vien.                               **'),
        ('output', '**  2. Cap nhat thong tin sinh vien boi ID.          **'),
        ('output', '**  3. Xoa sinh vien boi ID.                         **'),
        ('output', '**  4. Tim kiem sinh vien theo ten.                  **'),
        ('output', '**  5. Sap xep sinh vien theo diem trung binh.       **'),
        ('output', '**  6. Sap xep sinh vien theo ten chuyen nganh.      **'),
        ('output', '**  7. Hien thi danh sach sinh vien.                 **'),
        ('output', '**  0. Thoat                                         **'),
        ('output', '*******************************************************'),
        ('input', 'Nhap tuy chon: 1'),
        ('output', '1. Them sinh vien.'),
        ('input', 'Nhap ten sinh vien: Tran Minh Khang'),
        ('input', 'Nhap gioi tinh sinh vien: Nam'),
        ('input', 'Nhap chuyen nganh cua sinh vien: CNTT'),
        ('input', 'Nhap diem cua sinh vien: 8.5'),
        ('success', 'Them sinh vien thanh cong!'),
        ('output', ''),
        ('input', 'Nhap tuy chon: 7'),
        ('info', '7. Hien thi danh sach sinh vien.'),
        ('output', 'ID       Name               Sex      Major    Diem TB  Hoc Luc '),
        ('output', '1        Tran Minh Khang    Nam      CNTT     8.5      Gioi    '),
        ('output', ''),
        ('input', 'Nhap tuy chon: 0'),
        ('highlight', 'Ban da chon thoat chuong trinh!'),
        ('prompt_only', r'PS D:\mkhang\pythonlatantt\lab-01\ex04> ')
    ],
    'report_assets/hinh19_git_push.png': [
        ('prompt_cmd', (r'PS D:\mkhang\pythonlatantt> ', 'git status')),
        ('output', 'On branch main'),
        ('output', 'Your branch is up to date with \'origin/main\'.'),
        ('output', 'nothing to commit, working tree clean'),
        ('prompt_cmd', (r'PS D:\mkhang\pythonlatantt> ', 'git remote -v')),
        ('output', 'origin  https://github.com/khang1233/TH_LTANTT_2387700027.git (fetch)'),
        ('output', 'origin  https://github.com/khang1233/TH_LTANTT_2387700027.git (push)'),
        ('prompt_cmd', (r'PS D:\mkhang\pythonlatantt> ', 'git push origin main')),
        ('output', 'Everything up-to-date'),
        ('prompt_only', r'PS D:\mkhang\pythonlatantt> ')
    ]
}

for path, data in screens.items():
    render_terminal(data, path)
print("Finished rendering all screenshots successfully!")
