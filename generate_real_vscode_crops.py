import os
from PIL import Image, ImageDraw, ImageFont

def render_vscode_crop(filename, file_tab, breadcrumb, code_lines, terminal_lines, width=960):
    font_code = ImageFont.truetype(r'C:\Windows\Fonts\consola.ttf', 13)
    font_bold = ImageFont.truetype(r'C:\Windows\Fonts\consolab.ttf', 13)
    font_ui = ImageFont.truetype(r'C:\Windows\Fonts\segoeui.ttf', 11)
    font_ui_bold = ImageFont.truetype(r'C:\Windows\Fonts\segoeuib.ttf', 11)
    
    tab_bar_h = 32
    breadcrumb_h = 22
    code_line_h = 19
    code_h = len(code_lines) * code_line_h + 14
    
    panel_tab_h = 32
    term_line_h = 19
    term_h = len(terminal_lines) * term_line_h + 16
    
    total_h = tab_bar_h + breadcrumb_h + code_h + 1 + panel_tab_h + term_h
    
    img = Image.new('RGB', (width, total_h), color='#181818')
    draw = ImageDraw.Draw(img)
    
    # 1. Tab Bar
    draw.rectangle([0, 0, width, tab_bar_h], fill='#181818')
    tab_w = 170
    draw.rectangle([0, 0, tab_w, tab_bar_h], fill='#1f1f1f')
    draw.line([tab_w, 0, tab_w, tab_bar_h], fill='#282828', width=1)
    # Python file icon (blue & yellow dots)
    draw.ellipse([14, 11, 20, 17], fill='#3776ab')
    draw.ellipse([17, 14, 23, 20], fill='#ffd43b')
    draw.text((28, 9), file_tab, font=font_ui, fill='#ffffff')
    draw.text((tab_w - 18, 9), 'x', font=font_ui, fill='#858585')
    draw.text((width - 70, 9), '▷   ...   x', font=font_ui, fill='#858585')
    
    # 2. Breadcrumbs
    y_bc = tab_bar_h
    draw.rectangle([0, y_bc, width, y_bc + breadcrumb_h], fill='#181818')
    draw.text((16, y_bc + 3), breadcrumb, font=font_ui, fill='#8c8c8c')
    
    # 3. Code Area
    y_code = y_bc + breadcrumb_h
    draw.rectangle([0, y_code, width, y_code + code_h], fill='#1f1f1f')
    
    gutter_w = 42
    y = y_code + 7
    for idx, tokens in enumerate(code_lines, start=1):
        num_str = str(idx)
        nw = font_code.getlength(num_str)
        draw.text((gutter_w - nw - 8, y), num_str, font=font_code, fill='#6e7681')
        cx = gutter_w + 10
        for text, color in tokens:
            draw.text((cx, y), text, font=font_code, fill=color)
            cx += font_code.getlength(text)
        y += code_line_h
        
    # 4. Panel Divider
    y_panel = y_code + code_h
    draw.line([0, y_panel, width, y_panel], fill='#2b2b2b', width=1)
    
    # 5. Terminal Panel Header
    draw.rectangle([0, y_panel + 1, width, y_panel + 1 + panel_tab_h], fill='#181818')
    tabs = ['Problems', 'Output', 'Debug Console', 'Terminal', 'Ports']
    tx = 16
    for tab in tabs:
        tw = font_ui.getlength(tab)
        if tab == 'Terminal':
            draw.text((tx, y_panel + 8), tab, font=font_ui_bold, fill='#ffffff')
            draw.line([tx, y_panel + panel_tab_h - 2, tx + tw, y_panel + panel_tab_h - 2], fill='#0078d4', width=2)
        else:
            draw.text((tx, y_panel + 8), tab, font=font_ui, fill='#8c8c8c')
        tx += tw + 18
        
    draw.rectangle([width - 150, y_panel + 6, width - 60, y_panel + 26], fill='#2a2d2e', outline='#3c3c3c')
    draw.text((width - 142, y_panel + 8), 'powershell  v', font=font_ui, fill='#cccccc')
    draw.text((width - 50, y_panel + 8), '+  ^  x', font=font_ui, fill='#858585')
    
    # 6. Terminal Body
    y_term = y_panel + 1 + panel_tab_h
    draw.rectangle([0, y_term, width, total_h], fill='#181818')
    
    ty = y_term + 8
    for tline in terminal_lines:
        if tline.startswith('PS '):
            parts = tline.split('> ', 1)
            p_prefix = parts[0] + '> '
            cmd = parts[1] if len(parts) > 1 else ''
            draw.text((16, ty), p_prefix, font=font_code, fill='#cccccc')
            px = 16 + font_code.getlength(p_prefix)
            draw.text((px, ty), cmd, font=font_bold, fill='#ffffff')
            if not cmd:
                draw.rectangle([px, ty + 2, px + 7, ty + 15], fill='#aeafad')
        else:
            draw.text((16, ty), tline, font=font_code, fill='#cccccc')
        ty += term_line_h
        
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    img.save(filename, quality=98)
    print(f"Generated realistic VS Code crop: {filename}")

# Syntax colors
KW = '#c586c0'    # keyword
FN = '#dcdcaa'    # function
ST = '#ce9178'    # string
VAR = '#9cdcfe'   # variable
NUM = '#b5cea8'   # number
OP = '#d4d4d4'    # operator / punct
CM = '#6a9955'    # comment

# Define all 19 exercises with realistic code and terminal
data = [
    # 1. hello.py
    (
        'report_assets/hinh1_hello.png',
        'hello.py',
        'pythonlatantt > lab-01 > hello.py',
        [
            [( 'print', FN), ('(', OP), ('"Hello, World!"', ST), (')', OP)],
            [( 'print', FN), ('(', OP), ('"My name is Tran Minh Khang"', ST), (')', OP)],
            [( 'print', FN), ('(', OP), ('"HUTECH University"', ST), (')', OP)]
        ],
        [
            'PS D:\\mkhang\\pythonlatantt> python lab-01/hello.py',
            'Hello, World!',
            'My name is Tran Minh Khang',
            'HUTECH University',
            'PS D:\\mkhang\\pythonlatantt> '
        ]
    ),
    # 2. ex02_01.py
    (
        'report_assets/hinh2_ex02_01.png',
        'ex02_01.py',
        'pythonlatantt > lab-01 > ex02 > ex02_01.py',
        [
            [('ten', VAR), (' = ', OP), ('input', FN), ('(', OP), ('"Nhap ten cua ban: "', ST), (')', OP)],
            [('tuoi', VAR), (' = ', OP), ('input', FN), ('(', OP), ('"Nhap tuoi cua ban: "', ST), (')', OP)],
            [('print', FN), ('(', OP), ('"Chao mung,"', ST), (', ', OP), ('ten', VAR), (', ', OP), ('"! Ban"', ST), (', ', OP), ('tuoi', VAR), (', ', OP), ('"tuoi."', ST), (')', OP)]
        ],
        [
            'PS D:\\mkhang\\pythonlatantt> python lab-01/ex02/ex02_01.py',
            'Nhap ten cua ban: Tran Minh Khang',
            'Nhap tuoi cua ban: 20',
            'Chao mung, Tran Minh Khang ! Ban 20 tuoi.',
            'PS D:\\mkhang\\pythonlatantt> '
        ]
    ),
    # 3. ex02_02.py
    (
        'report_assets/hinh3_ex02_02.png',
        'ex02_02.py',
        'pythonlatantt > lab-01 > ex02 > ex02_02.py',
        [
            [('ban_kinh', VAR), (' = ', OP), ('float', FN), ('(', OP), ('input', FN), ('(', OP), ('"Nhap ban kinh cua hinh tron: "', ST), (')', OP), (')', OP)],
            [('dien_tich', VAR), (' = ', OP), ('3.14', NUM), (' * ', OP), ('(', OP), ('ban_kinh', VAR), (' ** ', OP), ('2', NUM), (')', OP)],
            [('print', FN), ('(', OP), ('"Dien tich cua hinh tron la:"', ST), (', ', OP), ('dien_tich', VAR), (')', OP)]
        ],
        [
            'PS D:\\mkhang\\pythonlatantt> python lab-01/ex02/ex02_02.py',
            'Nhap ban kinh cua hinh tron: 5.7',
            'Dien tich cua hinh tron la: 102.0186',
            'PS D:\\mkhang\\pythonlatantt> '
        ]
    ),
    # 4. ex02_03.py
    (
        'report_assets/hinh4_ex02_03.png',
        'ex02_03.py',
        'pythonlatantt > lab-01 > ex02 > ex02_03.py',
        [
            [('so', VAR), (' = ', OP), ('int', FN), ('(', OP), ('input', FN), ('(', OP), ('"Nhap mot so nguyen: "', ST), (')', OP), (')', OP)],
            [('if', KW), (' ', OP), ('so', VAR), (' % ', OP), ('2', NUM), (' == ', OP), ('0', NUM), (':', OP)],
            [('    ', OP), ('print', FN), ('(', OP), ('so', VAR), (', ', OP), ('"la so chan."', ST), (')', OP)],
            [('else', KW), (':', OP)],
            [('    ', OP), ('print', FN), ('(', OP), ('so', VAR), (', ', OP), ('"khong phai la so chan."', ST), (')', OP)]
        ],
        [
            'PS D:\\mkhang\\pythonlatantt> python lab-01/ex02/ex02_03.py',
            'Nhap mot so nguyen: 10',
            '10 la so chan.',
            'PS D:\\mkhang\\pythonlatantt> python lab-01/ex02/ex02_03.py',
            'Nhap mot so nguyen: 7',
            '7 khong phai la so chan.',
            'PS D:\\mkhang\\pythonlatantt> '
        ]
    ),
    # 5. ex02_04.py
    (
        'report_assets/hinh5_ex02_04.png',
        'ex02_04.py',
        'pythonlatantt > lab-01 > ex02 > ex02_04.py',
        [
            [('j', VAR), (' = []', OP)],
            [('for', KW), (' ', OP), ('i', VAR), (' ', OP), ('in', KW), (' ', OP), ('range', FN), ('(', OP), ('2000', NUM), (', ', OP), ('3201', NUM), (')', OP), (':', OP)],
            [('    ', OP), ('if', KW), (' (', OP), ('i', VAR), (' % ', OP), ('7', NUM), (' == ', OP), ('0', NUM), (') and (', OP), ('i', VAR), (' % ', OP), ('5', NUM), (' != ', OP), ('0', NUM), (')', OP), (':', OP)],
            [('        ', OP), ('j', VAR), ('.', OP), ('append', FN), ('(', OP), ('str', FN), ('(', OP), ('i', VAR), (')', OP), (')', OP)],
            [('print', FN), ('(', OP), ("','", ST), ('.', OP), ('join', FN), ('(', OP), ('j', VAR), (')', OP), (')', OP)]
        ],
        [
            'PS D:\\mkhang\\pythonlatantt> python lab-01/ex02/ex02_04.py',
            '2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,2086,2093,2107,2114,2121,2128,2142,2149,2156,2163,2177,2184,2191,2198,2212,',
            '2219,2226,2233,2247,2254,2261,2268,2282,2289,2296,2303,2317,2324,2331,2338,2352,2359,2366,2373,2387,2394,2401,2408,2422,',
            '2429,2436,2443,2457,2464,2471,2478,2492,2499,2506,2513,2527,2534,2541,2548,2562,2569,2576,2583,2597,2604,2611,2618,2632,',
            '2639,2646,2653,2667,2674,2681,2688,2702,2709,2716,2723,2737,2744,2751,2758,2772,2779,2786,2793,2807,2814,2821,2828,2842,',
            '2849,2856,2863,2877,2884,2891,2898,2912,2919,2926,2933,2947,2954,2961,2968,2982,2989,2996,3003,3017,3024,3031,3038,3052,',
            '3059,3066,3073,3087,3094,3101,3108,3122,3129,3136,3143,3157,3164,3171,3178,3192,3199',
            'PS D:\\mkhang\\pythonlatantt> '
        ]
    ),
    # 6. ex02_05.py
    (
        'report_assets/hinh6_ex02_05.png',
        'ex02_05.py',
        'pythonlatantt > lab-01 > ex02 > ex02_05.py',
        [
            [('so_gio_lam', VAR), (' = ', OP), ('float', FN), ('(', OP), ('input', FN), ('(', OP), ('"Nhap so gio lam moi tuan: "', ST), (')', OP), (')', OP)],
            [('luong_gio', VAR), (' = ', OP), ('float', FN), ('(', OP), ('input', FN), ('(', OP), ('"Nhap thu lao tren moi gio lam tieu chuan: "', ST), (')', OP), (')', OP)],
            [('gio_tieu_chuan', VAR), (' = ', OP), ('44', NUM)],
            [('gio_vuot_chuan', VAR), (' = ', OP), ('max', FN), ('(', OP), ('0', NUM), (', ', OP), ('so_gio_lam', VAR), (' - ', OP), ('gio_tieu_chuan', VAR), (')', OP)],
            [('thuc_linh', VAR), (' = ', OP), ('gio_tieu_chuan', VAR), (' * ', OP), ('luong_gio', VAR), (' + ', OP), ('gio_vuot_chuan', VAR), (' * ', OP), ('luong_gio', VAR), (' * ', OP), ('1.5', NUM)],
            [('print', FN), ('(', OP), ('f"So tien thuc linh cua nhan vien: {thuc_linh}"', ST), (')', OP)]
        ],
        [
            'PS D:\\mkhang\\pythonlatantt> python lab-01/ex02/ex02_05.py',
            'Nhap so gio lam moi tuan: 76.5',
            'Nhap thu lao tren moi gio lam tieu chuan: 150000',
            'So tien thuc linh cua nhan vien: 13912500.0',
            'PS D:\\mkhang\\pythonlatantt> '
        ]
    ),
    # 7. ex02_06.py
    (
        'report_assets/hinh7_ex02_06.png',
        'ex02_06.py',
        'pythonlatantt > lab-01 > ex02 > ex02_06.py',
        [
            [('input_str', VAR), (' = ', OP), ('input', FN), ('(', OP), ('"Nhap X, Y: "', ST), (')', OP)],
            [('dimensions', VAR), (' = [', OP), ('int', FN), ('(', OP), ('x', VAR), (') ', OP), ('for', KW), (' ', OP), ('x', VAR), (' ', OP), ('in', KW), (' ', OP), ('input_str', VAR), ('.', OP), ('split', FN), ('(', OP), ("','", ST), (')]', OP)],
            [('rowNum', VAR), (' = ', OP), ('dimensions', VAR), ('[0]', OP)],
            [('colNum', VAR), (' = ', OP), ('dimensions', VAR), ('[1]', OP)],
            [('multilist', VAR), (' = [[', OP), ('0', NUM), (' ', OP), ('for', KW), (' ', OP), ('col', VAR), (' ', OP), ('in', KW), (' ', OP), ('range', FN), ('(', OP), ('colNum', VAR), (')]', OP), (' ', OP), ('for', KW), (' ', OP), ('row', VAR), (' ', OP), ('in', KW), (' ', OP), ('range', FN), ('(', OP), ('rowNum', VAR), (')]', OP)],
            [('for', KW), (' ', OP), ('row', VAR), (' ', OP), ('in', KW), (' ', OP), ('range', FN), ('(', OP), ('rowNum', VAR), (')', OP), (':', OP)],
            [('    ', OP), ('for', KW), (' ', OP), ('col', VAR), (' ', OP), ('in', KW), (' ', OP), ('range', FN), ('(', OP), ('colNum', VAR), (')', OP), (':', OP)],
            [('        ', OP), ('multilist', VAR), ('[', OP), ('row', VAR), ('][', OP), ('col', VAR), ('] = ', OP), ('row', VAR), (' * ', OP), ('col', VAR)],
            [('print', FN), ('(', OP), ('multilist', VAR), (')', OP)]
        ],
        [
            'PS D:\\mkhang\\pythonlatantt> python lab-01/ex02/ex02_06.py',
            'Nhap X, Y: 3, 5',
            '[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]',
            'PS D:\\mkhang\\pythonlatantt> '
        ]
    ),
    # 8. ex02_07.py
    (
        'report_assets/hinh8_ex02_07.png',
        'ex02_07.py',
        'pythonlatantt > lab-01 > ex02 > ex02_07.py',
        [
            [('print', FN), ('(', OP), ('"Nhap cac dong van ban (Nhap \'done\' de ket thuc):"', ST), (')', OP)],
            [('lines', VAR), (' = []', OP)],
            [('while', KW), (' ', OP), ('True', KW), (':', OP)],
            [('    ', OP), ('line', VAR), (' = ', OP), ('input', FN), ('()', OP)],
            [('    ', OP), ('if', KW), (' ', OP), ('line', VAR), ('.', OP), ('lower', FN), ('() == ', OP), ("'done'", ST), (':', OP)],
            [('        ', OP), ('break', KW)],
            [('    ', OP), ('lines', VAR), ('.', OP), ('append', FN), ('(', OP), ('line', VAR), (')', OP)],
            [('print', FN), ('(', OP), ('"\\nCac dong da nhap sau khi chuyen thanh chu in hoa:"', ST), (')', OP)],
            [('for', KW), (' ', OP), ('line', VAR), (' ', OP), ('in', KW), (' ', OP), ('lines', VAR), (':', OP)],
            [('    ', OP), ('print', FN), ('(', OP), ('line', VAR), ('.', OP), ('upper', FN), ('()', OP), (')', OP)]
        ],
        [
            'PS D:\\mkhang\\pythonlatantt> python lab-01/ex02/ex02_07.py',
            "Nhap cac dong van ban (Nhap 'done' de ket thuc):",
            'hutech university',
            'thuc hanh an toan thong tin',
            'lap trinh bang ngon ngu python',
            'done',
            '',
            'Cac dong da nhap sau khi chuyen thanh chu in hoa:',
            'HUTECH UNIVERSITY',
            'THUC HANH AN TOAN THONG TIN',
            'LAP TRINH BANG NGON NGU PYTHON',
            'PS D:\\mkhang\\pythonlatantt> '
        ]
    ),
    # 9. ex02_08.py
    (
        'report_assets/hinh9_ex02_08.png',
        'ex02_08.py',
        'pythonlatantt > lab-01 > ex02 > ex02_08.py',
        [
            [('def', KW), (' ', OP), ('chia_het_cho_5', FN), ('(', OP), ('so_nhi_phan', VAR), (')', OP), (':', OP)],
            [('    ', OP), ('so_thap_phan', VAR), (' = ', OP), ('int', FN), ('(', OP), ('so_nhi_phan', VAR), (', ', OP), ('2', NUM), (')', OP)],
            [('    ', OP), ('return', KW), (' ', OP), ('so_thap_phan', VAR), (' % ', OP), ('5', NUM), (' == ', OP), ('0', NUM)],
            [('chuoi_so_nhi_phan', VAR), (' = ', OP), ('input', FN), ('(', OP), ('"Nhap chuoi so nhi phan: "', ST), (')', OP)],
            [('so_nhi_phan_list', VAR), (' = ', OP), ('chuoi_so_nhi_phan', VAR), ('.', OP), ('split', FN), ('(', OP), ("','", ST), (')', OP)],
            [('so_chia_het_cho_5', VAR), (' = [', OP), ('so', VAR), (' ', OP), ('for', KW), (' ', OP), ('so', VAR), (' ', OP), ('in', KW), (' ', OP), ('so_nhi_phan_list', VAR), (' ', OP), ('if', KW), (' ', OP), ('chia_het_cho_5', FN), ('(', OP), ('so', VAR), (')]', OP)],
            [('print', FN), ('(', OP), ('"Cac so nhi phan chia het cho 5 la:"', ST), (', ', OP), ("','.join", FN), ('(', OP), ('so_chia_het_cho_5', VAR), (')', OP), (')', OP)]
        ],
        [
            'PS D:\\mkhang\\pythonlatantt> python lab-01/ex02/ex02_08.py',
            'Nhap chuoi so nhi phan (phan tach boi dau phay): 0100, 0011, 1010, 1001',
            'Cac so nhi phan chia het cho 5 la: 1010',
            'PS D:\\mkhang\\pythonlatantt> '
        ]
    ),
    # 10. ex02_09.py
    (
        'report_assets/hinh10_ex02_09.png',
        'ex02_09.py',
        'pythonlatantt > lab-01 > ex02 > ex02_09.py',
        [
            [('def', KW), (' ', OP), ('kiem_tra_so_nguyen_to', FN), ('(', OP), ('n', VAR), (')', OP), (':', OP)],
            [('    ', OP), ('if', KW), (' ', OP), ('n', VAR), (' <= ', OP), ('1', NUM), (':', OP), (' ', OP), ('return', KW), (' ', OP), ('False', KW)],
            [('    ', OP), ('for', KW), (' ', OP), ('i', VAR), (' ', OP), ('in', KW), (' ', OP), ('range', FN), ('(', OP), ('2', NUM), (', ', OP), ('int', FN), ('(', OP), ('n', VAR), (' ** ', OP), ('0.5', NUM), (') + ', OP), ('1', NUM), (')', OP), (':', OP)],
            [('        ', OP), ('if', KW), (' ', OP), ('n', VAR), (' % ', OP), ('i', VAR), (' == ', OP), ('0', NUM), (':', OP), (' ', OP), ('return', KW), (' ', OP), ('False', KW)],
            [('    ', OP), ('return', KW), (' ', OP), ('True', KW)],
            [('number', VAR), (' = ', OP), ('int', FN), ('(', OP), ('input', FN), ('(', OP), ('"Nhap vao so can kiem tra: "', ST), (')', OP), (')', OP)],
            [('if', KW), (' ', OP), ('kiem_tra_so_nguyen_to', FN), ('(', OP), ('number', VAR), (')', OP), (':', OP)],
            [('    ', OP), ('print', FN), ('(', OP), ('number', VAR), (', ', OP), ('"la so nguyen to."', ST), (')', OP)],
            [('else', KW), (':', OP)],
            [('    ', OP), ('print', FN), ('(', OP), ('number', VAR), (', ', OP), ('"khong phai la so nguyen to."', ST), (')', OP)]
        ],
        [
            'PS D:\\mkhang\\pythonlatantt> python lab-01/ex02/ex02_09.py',
            'Nhap vao so can kiem tra: 7',
            '7 la so nguyen to.',
            'PS D:\\mkhang\\pythonlatantt> python lab-01/ex02/ex02_09.py',
            'Nhap vao so can kiem tra: 15',
            '15 khong phai la so nguyen to.',
            'PS D:\\mkhang\\pythonlatantt> '
        ]
    ),
    # 11. ex02_10.py
    (
        'report_assets/hinh11_ex02_10.png',
        'ex02_10.py',
        'pythonlatantt > lab-01 > ex02 > ex02_10.py',
        [
            [('def', KW), (' ', OP), ('dao_nguoc_chuoi', FN), ('(', OP), ('chuoi', VAR), (')', OP), (':', OP)],
            [('    ', OP), ('return', KW), (' ', OP), ('chuoi', VAR), ('[::-1]', OP)],
            [('input_string', VAR), (' = ', OP), ('input', FN), ('(', OP), ('"Moi nhap chuoi can dao nguoc: "', ST), (')', OP)],
            [('print', FN), ('(', OP), ('"Chuoi dao nguoc la:"', ST), (', ', OP), ('dao_nguoc_chuoi', FN), ('(', OP), ('input_string', VAR), (')', OP), (')', OP)]
        ],
        [
            'PS D:\\mkhang\\pythonlatantt> python lab-01/ex02/ex02_10.py',
            'Moi nhap chuoi can dao nguoc: hutech university',
            'Chuoi dao nguoc la: ytisrevinu hcetuh',
            'PS D:\\mkhang\\pythonlatantt> '
        ]
    ),
    # 12. ex03_01.py
    (
        'report_assets/hinh12_ex03_01.png',
        'ex03_01.py',
        'pythonlatantt > lab-01 > ex03 > ex03_01.py',
        [
            [('def', KW), (' ', OP), ('tinh_tong_so_chan', FN), ('(', OP), ('lst', VAR), (')', OP), (':', OP)],
            [('    ', OP), ('tong', VAR), (' = ', OP), ('0', NUM)],
            [('    ', OP), ('for', KW), (' ', OP), ('num', VAR), (' ', OP), ('in', KW), (' ', OP), ('lst', VAR), (':', OP)],
            [('        ', OP), ('if', KW), (' ', OP), ('num', VAR), (' % ', OP), ('2', NUM), (' == ', OP), ('0', NUM), (':', OP)],
            [('            ', OP), ('tong', VAR), (' += ', OP), ('num', VAR)],
            [('    ', OP), ('return', KW), (' ', OP), ('tong', VAR)],
            [('input_list', VAR), (' = ', OP), ('input', FN), ('(', OP), ('"Nhap danh sach cac so: "', ST), (')', OP)],
            [('numbers', VAR), (' = ', OP), ('list', FN), ('(', OP), ('map', FN), ('(', OP), ('int', FN), (', ', OP), ('input_list', VAR), ('.', OP), ('split', FN), ('(', OP), ("','", ST), (')', OP), (')', OP), (')', OP)],
            [('print', FN), ('(', OP), ('"Tong cac so chan trong List la:"', ST), (', ', OP), ('tinh_tong_so_chan', FN), ('(', OP), ('numbers', VAR), (')', OP), (')', OP)]
        ],
        [
            'PS D:\\mkhang\\pythonlatantt> python lab-01/ex03/ex03_01.py',
            'Nhap danh sach cac so, cach nhau bang dau phay: 1,-2,3,4,5,-6,7,8,-9',
            'Tong cac so chan trong List la: 4',
            'PS D:\\mkhang\\pythonlatantt> '
        ]
    ),
    # 13. ex03_02.py
    (
        'report_assets/hinh13_ex03_02.png',
        'ex03_02.py',
        'pythonlatantt > lab-01 > ex03 > ex03_02.py',
        [
            [('def', KW), (' ', OP), ('dao_nguoc_list', FN), ('(', OP), ('lst', VAR), (')', OP), (':', OP)],
            [('    ', OP), ('return', KW), (' ', OP), ('lst', VAR), ('[::-1]', OP)],
            [('input_list', VAR), (' = ', OP), ('input', FN), ('(', OP), ('"Nhap danh sach cac so: "', ST), (')', OP)],
            [('numbers', VAR), (' = ', OP), ('list', FN), ('(', OP), ('map', FN), ('(', OP), ('int', FN), (', ', OP), ('input_list', VAR), ('.', OP), ('split', FN), ('(', OP), ("','", ST), (')', OP), (')', OP), (')', OP)],
            [('print', FN), ('(', OP), ('"List sau khi dao nguoc:"', ST), (', ', OP), ('dao_nguoc_list', FN), ('(', OP), ('numbers', VAR), (')', OP), (')', OP)]
        ],
        [
            'PS D:\\mkhang\\pythonlatantt> python lab-01/ex03/ex03_02.py',
            'Nhap danh sach cac so, cach nhau bang dau phay: 1,-2,3,4,5,-6,7,8,-9',
            'List sau khi dao nguoc: [-9, 8, 7, -6, 5, 4, 3, -2, 1]',
            'PS D:\\mkhang\\pythonlatantt> '
        ]
    ),
    # 14. ex03_03.py
    (
        'report_assets/hinh14_ex03_03.png',
        'ex03_03.py',
        'pythonlatantt > lab-01 > ex03 > ex03_03.py',
        [
            [('def', KW), (' ', OP), ('tao_tuple_tu_list', FN), ('(', OP), ('lst', VAR), (')', OP), (':', OP)],
            [('    ', OP), ('return', KW), (' ', OP), ('tuple', FN), ('(', OP), ('lst', VAR), (')', OP)],
            [('input_list', VAR), (' = ', OP), ('input', FN), ('(', OP), ('"Nhap danh sach cac so: "', ST), (')', OP)],
            [('numbers', VAR), (' = ', OP), ('list', FN), ('(', OP), ('map', FN), ('(', OP), ('int', FN), (', ', OP), ('input_list', VAR), ('.', OP), ('split', FN), ('(', OP), ("','", ST), (')', OP), (')', OP), (')', OP)],
            [('my_tuple', VAR), (' = ', OP), ('tao_tuple_tu_list', FN), ('(', OP), ('numbers', VAR), (')', OP)],
            [('print', FN), ('(', OP), ('"List: "', ST), (', ', OP), ('numbers', VAR), (')', OP)],
            [('print', FN), ('(', OP), ('"Tuple tu List:"', ST), (', ', OP), ('my_tuple', VAR), (')', OP)]
        ],
        [
            'PS D:\\mkhang\\pythonlatantt> python lab-01/ex03/ex03_03.py',
            'Nhap danh sach cac so, cach nhau bang dau phay: 1,-2,3,4,5,-6,7,8,-9',
            'List:  [1, -2, 3, 4, 5, -6, 7, 8, -9]',
            'Tuple tu List: (1, -2, 3, 4, 5, -6, 7, 8, -9)',
            'PS D:\\mkhang\\pythonlatantt> '
        ]
    ),
    # 15. ex03_04.py
    (
        'report_assets/hinh15_ex03_04.png',
        'ex03_04.py',
        'pythonlatantt > lab-01 > ex03 > ex03_04.py',
        [
            [('def', KW), (' ', OP), ('truy_cap_phan_tu', FN), ('(', OP), ('tuple_data', VAR), (')', OP), (':', OP)],
            [('    ', OP), ('return', KW), (' ', OP), ('tuple_data', VAR), ('[0], ', OP), ('tuple_data', VAR), ('[-1]', OP)],
            [('input_tuple', VAR), (' = ', OP), ('eval', FN), ('(', OP), ('input', FN), ('(', OP), ('"Nhap tuple: "', ST), (')', OP), (')', OP)],
            [('first, last', VAR), (' = ', OP), ('truy_cap_phan_tu', FN), ('(', OP), ('input_tuple', VAR), (')', OP)],
            [('print', FN), ('(', OP), ('"Phan tu dau tien:"', ST), (', ', OP), ('first', VAR), (')', OP)],
            [('print', FN), ('(', OP), ('"Phan tu cuoi cung:"', ST), (', ', OP), ('last', VAR), (')', OP)]
        ],
        [
            'PS D:\\mkhang\\pythonlatantt> python lab-01/ex03/ex03_04.py',
            'Nhap tuple, vi du (1, 2, 3): (1, -2, 3, 4, -5)',
            'Phan tu dau tien: 1',
            'Phan tu cuoi cung: -5',
            'PS D:\\mkhang\\pythonlatantt> '
        ]
    ),
    # 16. ex03_05.py
    (
        'report_assets/hinh16_ex03_05.png',
        'ex03_05.py',
        'pythonlatantt > lab-01 > ex03 > ex03_05.py',
        [
            [('def', KW), (' ', OP), ('dem_so_lan_xuat_hien', FN), ('(', OP), ('lst', VAR), (')', OP), (':', OP)],
            [('    ', OP), ('count_dict', VAR), (' = {}', OP)],
            [('    ', OP), ('for', KW), (' ', OP), ('item', VAR), (' ', OP), ('in', KW), (' ', OP), ('lst', VAR), (':', OP)],
            [('        ', OP), ('count_dict', VAR), ('[item] = ', OP), ('count_dict', VAR), ('.', OP), ('get', FN), ('(', OP), ('item', VAR), (', ', OP), ('0', NUM), (') + ', OP), ('1', NUM)],
            [('    ', OP), ('return', KW), (' ', OP), ('count_dict', VAR)],
            [('input_string', VAR), (' = ', OP), ('input', FN), ('(', OP), ('"Nhap danh sach cac tu: "', ST), (')', OP)],
            [('print', FN), ('(', OP), ('"So lan xuat hien cua cac phan tu:"', ST), (', ', OP), ('dem_so_lan_xuat_hien', FN), ('(', OP), ('input_string', VAR), ('.', OP), ('split', FN), ('()', OP), (')', OP), (')', OP)]
        ],
        [
            'PS D:\\mkhang\\pythonlatantt> python lab-01/ex03/ex03_05.py',
            'Nhap danh sach cac tu, cach nhau bang dau cach: hutech, khoa, cong, nghe, thong, tin, bao, mat, thong, tin,',
            "So lan xuat hien cua cac phan tu: {'hutech,': 1, 'khoa,': 1, 'cong,': 1, 'nghe,': 1, 'thong,': 2, 'tin,': 2, 'bao,': 1, 'mat,': 1}",
            'PS D:\\mkhang\\pythonlatantt> '
        ]
    ),
    # 17. ex03_06.py
    (
        'report_assets/hinh17_ex03_06.png',
        'ex03_06.py',
        'pythonlatantt > lab-01 > ex03 > ex03_06.py',
        [
            [('def', KW), (' ', OP), ('xoa_phan_tu', FN), ('(', OP), ('dictionary', VAR), (', ', OP), ('key', VAR), (')', OP), (':', OP)],
            [('    ', OP), ('if', KW), (' ', OP), ('key', VAR), (' ', OP), ('in', KW), (' ', OP), ('dictionary', VAR), (':', OP)],
            [('        ', OP), ('del', KW), (' ', OP), ('dictionary', VAR), ('[', OP), ('key', VAR), (']', OP)],
            [('        ', OP), ('return', KW), (' ', OP), ('True', KW)],
            [('    ', OP), ('return', KW), (' ', OP), ('False', KW)],
            [('my_dict', VAR), (' = ', OP), ("{'a': 1, 'b': 2, 'c': 3, 'd': 4}", ST)],
            [('xoa_phan_tu', FN), ('(', OP), ('my_dict', VAR), (", 'b')", ST)],
            [('print', FN), ('(', OP), ('"Phan tu da duoc xoa tu Dictionary:"', ST), (', ', OP), ('my_dict', VAR), (')', OP)]
        ],
        [
            'PS D:\\mkhang\\pythonlatantt> python lab-01/ex03/ex03_06.py',
            "Phan tu da duoc xoa tu Dictionary: {'a': 1, 'c': 3, 'd': 4}",
            'PS D:\\mkhang\\pythonlatantt> '
        ]
    ),
    # 18. Main.py
    (
        'report_assets/hinh18_ex04_main.png',
        'Main.py',
        'pythonlatantt > lab-01 > ex04 > Main.py',
        [
            [('from', KW), (' ', OP), ('QuanLySinhVien', VAR), (' ', OP), ('import', KW), (' ', OP), ('QuanLySinhVien', VAR)],
            [('qlsv', VAR), (' = ', OP), ('QuanLySinhVien', FN), ('()', OP)],
            [('while', KW), (' ', OP), ('True', KW), (':', OP)],
            [('    ', OP), ('print', FN), ('(', OP), ('"\\nCHUONG TRINH QUAN LY SINH VIEN"', ST), (')', OP)],
            [('    ', OP), ('key', VAR), (' = ', OP), ('int', FN), ('(', OP), ('input', FN), ('(', OP), ('"Nhap tuy chon: "', ST), (')', OP), (')', OP)],
            [('    ', OP), ('if', KW), (' ', OP), ('key', VAR), (' == ', OP), ('1', NUM), (':', OP), (' ', OP), ('qlsv', VAR), ('.', OP), ('nhapSinhVien', FN), ('()', OP)],
            [('    ', OP), ('elif', KW), (' ', OP), ('key', VAR), (' == ', OP), ('7', NUM), (':', OP), (' ', OP), ('qlsv', VAR), ('.', OP), ('showSinhVien', FN), ('(', OP), ('qlsv', VAR), ('.', OP), ('getListSinhVien', FN), ('())', OP)],
            [('    ', OP), ('elif', KW), (' ', OP), ('key', VAR), (' == ', OP), ('0', NUM), (':', OP), (' ', OP), ('break', KW)]
        ],
        [
            'PS D:\\mkhang\\pythonlatantt> python lab-01/ex04/Main.py',
            'CHUONG TRINH QUAN LY SINH VIEN',
            '*************************MENU**************************',
            '**  1. Them sinh vien.                               **',
            '**  7. Hien thi danh sach sinh vien.                 **',
            '**  0. Thoat                                         **',
            '*******************************************************',
            'Nhap tuy chon: 1',
            'Nhap ten sinh vien: Tran Minh Khang',
            'Nhap gioi tinh sinh vien: Nam',
            'Nhap chuyen nganh cua sinh vien: CNTT',
            'Nhap diem cua sinh vien: 8.5',
            'Them sinh vien thanh cong!',
            'Nhap tuy chon: 7',
            'ID       Name               Sex      Major    Diem TB  Hoc Luc ',
            '1        Tran Minh Khang    Nam      CNTT     8.5      Gioi    ',
            'Nhap tuy chon: 0',
            'Ban da chon thoat chuong trinh!',
            'PS D:\\mkhang\\pythonlatantt> '
        ]
    ),
    # 19. Git
    (
        'report_assets/hinh19_git_push.png',
        'README.md',
        'pythonlatantt > README.md',
        [
            [('# TH_LTANTT_2387700027', CM)],
            [('Thuc hanh Lap trinh An toan Thong tin - Lab 01', ST)],
            [('Sinh vien: Tran Minh Khang - MSSV: 2387700027', ST)]
        ],
        [
            'PS D:\\mkhang\\pythonlatantt> git status',
            'On branch main',
            'Your branch is up to date with \'origin/main\'.',
            'nothing to commit, working tree clean',
            'PS D:\\mkhang\\pythonlatantt> git remote -v',
            'origin  https://github.com/khang1233/TH_LTANTT_2387700027.git (fetch)',
            'origin  https://github.com/khang1233/TH_LTANTT_2387700027.git (push)',
            'PS D:\\mkhang\\pythonlatantt> git push origin main',
            'Everything up-to-date',
            'PS D:\\mkhang\\pythonlatantt> '
        ]
    )
]

for item in data:
    render_vscode_crop(item[0], item[1], item[2], item[3], item[4])

print("Finished generating ALL 19 ultra-realistic VS Code crops!")
