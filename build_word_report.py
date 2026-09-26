import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, hex_color):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def add_code_box(doc, code_text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, "F5F5F5")
    set_cell_margins(cell, top=120, bottom=120, left=200, right=200)
    
    # Border
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>\n'
        f'  <w:left w:val="single" w:sz="18" w:space="0" w:color="0078D4"/>\n'
        f'  <w:bottom w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>\n'
        f'  <w:right w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>\n'
        f'</w:tcBorders>'
    )
    tcPr.append(tcBorders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.05
    run = p.add_run(code_text.strip())
    run.font.name = 'Consolas'
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(30, 30, 30)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)

def add_heading_1(doc, text):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(14)
    h.paragraph_format.space_after = Pt(6)
    h.paragraph_format.keep_with_next = True
    run = h.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(14)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0, 51, 102)
    return h

def add_heading_2(doc, text):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(10)
    h.paragraph_format.space_after = Pt(4)
    h.paragraph_format.keep_with_next = True
    run = h.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12.5)
    run.font.bold = True
    run.font.color.rgb = RGBColor(20, 80, 140)
    return h

def add_p(doc, text, bold=False, italic=False, space_after=4):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = RGBColor(40, 40, 40)
    return p

def add_image_with_caption(doc, img_path, caption_text, width=Inches(5.8)):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(4)
        p_img.paragraph_format.space_after = Pt(2)
        run = p_img.add_run()
        run.add_picture(img_path, width=width)
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_after = Pt(10)
        run_cap = p_cap.add_run(caption_text)
        run_cap.font.name = 'Times New Roman'
        run_cap.font.size = Pt(10.5)
        run_cap.font.italic = True
        run_cap.font.bold = True
        run_cap.font.color.rgb = RGBColor(60, 60, 60)

doc = docx.Document()

# Margins
sections = doc.sections
for s in sections:
    s.top_margin = Inches(0.8)
    s.bottom_margin = Inches(0.8)
    s.left_margin = Inches(0.9)
    s.right_margin = Inches(0.9)

# Header with Logo
p_logo = doc.add_paragraph()
p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_logo.paragraph_format.space_after = Pt(4)
if os.path.exists('report_assets/hutech_logo.jpeg'):
    run_logo = p_logo.add_run()
    run_logo.add_picture('report_assets/hutech_logo.jpeg', width=Inches(1.1))

p_top = doc.add_paragraph()
p_top.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_top.paragraph_format.space_after = Pt(2)
run = p_top.add_run("TRƯỜNG ĐẠI HỌC CÔNG NGHỆ TP. HỒ CHÍ MINH (HUTECH)\nKHOA CÔNG NGHỆ THÔNG TIN\n")
run.font.name = 'Times New Roman'
run.font.size = Pt(12)
run.font.bold = True
run.font.color.rgb = RGBColor(0, 51, 102)

run_sub = p_top.add_run("Môn học: Thực hành Lập trình An toàn thông tin\n")
run_sub.font.name = 'Times New Roman'
run_sub.font.size = Pt(12)
run_sub.font.bold = True
run_sub.font.color.rgb = RGBColor(180, 50, 20)

p_line = doc.add_paragraph()
p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_line.paragraph_format.space_after = Pt(10)
run_l = p_line.add_run("-----------------------------------------------------------------------------------------")
run_l.font.color.rgb = RGBColor(160, 160, 160)

# Student Info Box
tbl_info = doc.add_table(rows=2, cols=2)
tbl_info.alignment = WD_TABLE_ALIGNMENT.CENTER
for r in tbl_info.rows:
    for c in r.cells:
        set_cell_background(c, "F9FBFD")
        set_cell_margins(c, 80, 80, 140, 140)

c00 = tbl_info.cell(0, 0).paragraphs[0]
r = c00.add_run("Họ và Tên: ")
r.font.bold = True
r.font.name = 'Times New Roman'
r = c00.add_run("Võ Duy Khang")
r.font.name = 'Times New Roman'

c01 = tbl_info.cell(0, 1).paragraphs[0]
r = c01.add_run("Mã số sinh viên (MSSV): ")
r.font.bold = True
r.font.name = 'Times New Roman'
r = c01.add_run("2387700027")
r.font.name = 'Times New Roman'

c10 = tbl_info.cell(1, 0).paragraphs[0]
r = c10.add_run("Lớp: ")
r.font.bold = True
r.font.name = 'Times New Roman'
r = c10.add_run("23DATA1 / ATTT")
r.font.name = 'Times New Roman'

c11 = tbl_info.cell(1, 1).paragraphs[0]
r = c11.add_run("GitHub Repo: ")
r.font.bold = True
r.font.name = 'Times New Roman'
r = c11.add_run("khang1233/TH_LTANTT_2387700027")
r.font.name = 'Times New Roman'

p_sp = doc.add_paragraph()
p_sp.paragraph_format.space_before = Pt(10)
p_sp.paragraph_format.space_after = Pt(4)

# Report Title
p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_title.paragraph_format.space_after = Pt(2)
run_title = p_title.add_run("BÁO CÁO THỰC HÀNH\n")
run_title.font.name = 'Times New Roman'
run_title.font.size = Pt(18)
run_title.font.bold = True
run_title.font.color.rgb = RGBColor(180, 30, 30)

run_subt = p_title.add_run("BÀI 1: LẬP TRÌNH CƠ BẢN VỚI NGÔN NGỮ PYTHON")
run_subt.font.name = 'Times New Roman'
run_subt.font.size = Pt(14)
run_subt.font.bold = True
run_subt.font.color.rgb = RGBColor(0, 51, 102)

# SECTION I
add_heading_1(doc, "I. MỤC TIÊU VÀ MÔI TRƯỜNG THỰC HÀNH")
add_p(doc, "1. Mục tiêu bài thực hành:", bold=True)
add_p(doc, "- Nắm vững quy trình thiết lập môi trường lập trình Python chuẩn mực trên hệ điều hành Windows bao gồm Python Runtime, Visual Studio Code và các tiện ích mở rộng (Python, Pylance, Python Indent).")
add_p(doc, "- Sử dụng thành thạo hệ thống quản lý mã nguồn phân tán Git/GitHub để quản lý phiên bản, cam kết (commit) và đẩy mã nguồn (push) lên kho lưu trữ trực tuyến theo chuẩn đề tài môn học.")
add_p(doc, "- Làm quen và thành thạo các cú pháp nền tảng của Python: nhập/xuất dữ liệu, các phép toán số học, cấu trúc rẽ nhánh điều kiện (if-else), vòng lặp lặp lại (for, while), định nghĩa hàm tự định nghĩa.")
add_p(doc, "- Làm chủ các cấu trúc dữ liệu cốt lõi trong Python: List (danh sách), Tuple (bộ dữ liệu bất biến) và Dictionary (từ điển ánh xạ key-value).")
add_p(doc, "- Tiếp cận tư duy Lập trình hướng đối tượng (Object-Oriented Programming - OOP): xây dựng lớp (Class), phương thức khởi tạo (__init__), đóng gói thuộc tính và các phương thức nghiệp vụ quản lý sinh viên.")

add_p(doc, "2. Môi trường và công cụ sử dụng:", bold=True)
add_p(doc, "- Hệ điều hành: Microsoft Windows 11 x64 Pro.")
add_p(doc, "- Trình thông dịch: Python 3.12 / Python 3.14 (đã tích hợp vào biến môi trường PATH).")
add_p(doc, "- Công cụ phát triển (IDE): Visual Studio Code phiên bản mới nhất cùng các extension hỗ trợ lập trình.")
add_p(doc, "- Kho chứa mã nguồn: https://github.com/khang1233/TH_LTANTT_2387700027.git")

add_p(doc, "3. Khởi tạo dự án và chương trình đầu tiên (hello.py):", bold=True)
add_p(doc, "Tại thư mục gốc dự án, tạo thư mục lab-01 và tạo tệp tin hello.py thực thi in lời chào và thông tin sinh viên:")
add_code_box(doc, """print("Hello, World!")
print("My name is Khang")
print("HUTECH University")""")
add_image_with_caption(doc, 'report_assets/hinh1_hello.png', "Hình 1: Kết quả chạy chương trình hello.py trên Terminal của VS Code")
add_p(doc, "*(Ghi chú chụp màn hình thực tế: Chạy lệnh 'python lab-01/hello.py' tại terminal và dùng Win + Shift + S chụp lại)*", italic=True)

# SECTION II
add_heading_1(doc, "II. CÁC BÀI THỰC HÀNH LẬP TRÌNH PYTHON CƠ BẢN (ex02)")
add_p(doc, "Các bài tập lập trình cơ bản được tổ chức gọn gàng trong thư mục 'lab-01/ex02'. Dưới đây là chi tiết mã nguồn và kết quả thực thi từng câu:")

# Câu 1
add_heading_2(doc, "Câu 1: Nhập họ tên, tuổi và in thông điệp chào mừng (ex02_01.py)")
add_p(doc, "- Yêu cầu: Yêu cầu người dùng nhập họ tên và tuổi, sau đó in ra thông điệp chào mừng kèm thông tin vừa nhập.")
add_code_box(doc, """ten = input("Nhập tên của bạn: ")
tuoi = input("Nhập tuổi của bạn: ")
print("Chào mừng,", ten, "! Bạn", tuoi, "tuổi.")""")
add_image_with_caption(doc, 'report_assets/hinh2_ex02_01.png', "Hình 2: Kết quả thực thi ex02_01.py")
add_p(doc, "*(Vị trí chụp: Terminal tại thư mục lab-01/ex02, chạy 'python ex02_01.py', nhập họ tên và tuổi)*", italic=True)

# Câu 2
add_heading_2(doc, "Câu 2: Tính diện tích hình tròn (ex02_02.py)")
add_p(doc, "- Yêu cầu: Nhập bán kính r từ người dùng, tính diện tích hình tròn với Pi = 3.14 theo công thức: S = Pi * r^2.")
add_code_box(doc, """ban_kinh = float(input("Nhập bán kính của hình tròn: "))
dien_tich = 3.14 * (ban_kinh ** 2)
print("Diện tích của hình tròn là:", dien_tich)""")
add_image_with_caption(doc, 'report_assets/hinh3_ex02_02.png', "Hình 3: Kết quả thực thi ex02_02.py với bán kính r = 5.7")
add_p(doc, "*(Vị trí chụp: Chạy 'python ex02_02.py', nhập bán kính 5.7)*", italic=True)

# Câu 3
add_heading_2(doc, "Câu 3: Kiểm tra số chẵn / số lẻ (ex02_03.py)")
add_p(doc, "- Yêu cầu: Nhập vào một số nguyên và kiểm tra số đó là số chẵn hay số lẻ thông qua toán tử chia lấy dư (%).")
add_code_box(doc, """so = int(input("Nhập một số nguyên: "))
if so % 2 == 0:
    print(so, "là số chẵn.")
else:
    print(so, "không phải là số chẵn.")""")
add_image_with_caption(doc, 'report_assets/hinh4_ex02_03.png', "Hình 4: Kết quả thực thi ex02_03.py kiểm tra số 10 (chẵn) và số 7 (lẻ)")
add_p(doc, "*(Vị trí chụp: Chạy 'python ex02_03.py' lần lượt với 10 và 7)*", italic=True)

# Câu 4
add_heading_2(doc, "Câu 4: Tìm số chia hết cho 7 nhưng không phải bội số của 5 (ex02_04.py)")
add_p(doc, "- Yêu cầu: Tìm tất cả các số trong đoạn [2000, 3200] thỏa mãn: chia hết cho 7 và không chia hết cho 5. In kết quả trên 1 dòng cách nhau bởi dấu phẩy.")
add_code_box(doc, """j = []
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
print(','.join(j))""")
add_image_with_caption(doc, 'report_assets/hinh5_ex02_04.png', "Hình 5: Kết quả thực thi ex02_04.py in danh sách các số thỏa mãn")
add_p(doc, "*(Vị trí chụp: Chạy 'python ex02_04.py')*", italic=True)

# Câu 5
add_heading_2(doc, "Câu 5: Tính tiền lương thực nhận của nhân viên (ex02_05.py)")
add_p(doc, "- Yêu cầu: Nhập số giờ làm việc trong tuần và thù lao giờ tiêu chuẩn. Giờ tiêu chuẩn là 44h/tuần; giờ làm thêm hưởng 150% mức lương tiêu chuẩn.")
add_code_box(doc, """so_gio_lam = float(input("Nhập số giờ làm mỗi tuần: "))
luong_gio = float(input("Nhập thù lao trên mỗi giờ làm tiêu chuẩn: "))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
thuc_linh = gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5
print(f"Số tiền thực lĩnh của nhân viên: {thuc_linh}")""")
add_image_with_caption(doc, 'report_assets/hinh6_ex02_05.png', "Hình 6: Kết quả thực thi ex02_05.py với 76.5 giờ làm và thù lao 150.000 VNĐ/giờ")
add_p(doc, "*(Vị trí chụp: Chạy 'python ex02_05.py', nhập 76.5 và 150000)*", italic=True)

# Câu 6
add_heading_2(doc, "Câu 6: Tạo mảng 2 chiều theo chỉ số hàng và cột (ex02_06.py)")
add_p(doc, "- Yêu cầu: Nhập 2 số nguyên X và Y, khởi tạo ma trận 2 chiều kích thước X x Y trong đó giá trị tại hàng i cột j là i * j.")
add_code_box(doc, """input_str = input("Nhập X, Y: ")
dimensions = [int(x) for x in input_str.split(',')]
rowNum = dimensions[0]
colNum = dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row * col
print(multilist)""")
add_image_with_caption(doc, 'report_assets/hinh7_ex02_06.png', "Hình 7: Kết quả thực thi ex02_06.py với ma trận 3 x 5")
add_p(doc, "*(Vị trí chụp: Chạy 'python ex02_06.py', nhập '3, 5')*", italic=True)

# Câu 7
add_heading_2(doc, "Câu 7: Chuyển đổi các dòng văn bản thành chữ in hoa (ex02_07.py)")
add_p(doc, "- Yêu cầu: Nhập liên tiếp nhiều dòng chuỗi văn bản cho đến khi người dùng nhập 'done' thì dừng và in ra toàn bộ nội dung dưới dạng chữ IN HOA.")
add_code_box(doc, """print("Nhập các dòng văn bản (Nhập 'done' để kết thúc):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)

print("\\nCác dòng đã nhập sau khi chuyển thành chữ in hoa:")
for line in lines:
    print(line.upper())""")
add_image_with_caption(doc, 'report_assets/hinh8_ex02_07.png', "Hình 8: Kết quả thực thi ex02_07.py chuyển đổi hoa các chuỗi văn bản")
add_p(doc, "*(Vị trí chụp: Chạy 'python ex02_07.py', nhập các dòng chuỗi và gõ 'done')*", italic=True)

# Câu 8
add_heading_2(doc, "Câu 8: Lọc các số nhị phân 4 chữ số chia hết cho 5 (ex02_08.py)")
add_p(doc, "- Yêu cầu: Nhập chuỗi các số nhị phân phân tách bởi dấu phẩy, chuyển đổi sang hệ thập phân kiểm tra xem có chia hết cho 5 hay không và in các số thỏa mãn.")
add_code_box(doc, """def chia_het_cho_5(so_nhi_phan):
    so_thap_phan = int(so_nhi_phan, 2)
    return so_thap_phan % 5 == 0

chuoi_so_nhi_phan = input("Nhập chuỗi số nhị phân (phân tách bởi dấu phẩy): ")
so_nhi_phan_list = chuoi_so_nhi_phan.split(',')
so_chia_het_cho_5 = [so for so in so_nhi_phan_list if chia_het_cho_5(so)]

if len(so_chia_het_cho_5) > 0:
    ket_qua = ','.join(so_chia_het_cho_5)
    print("Các số nhị phân chia hết cho 5 là:", ket_qua)
else:
    print("Không có số nhị phân nào chia hết cho 5 trong chuỗi đã nhập.")""")
add_image_with_caption(doc, 'report_assets/hinh9_ex02_08.png', "Hình 9: Kết quả thực thi ex02_08.py lọc số nhị phân chia hết cho 5")
add_p(doc, "*(Vị trí chụp: Chạy 'python ex02_08.py', nhập '0100, 0011, 1010, 1001')*", italic=True)

# Câu 9
add_heading_2(doc, "Câu 9: Hàm kiểm tra số nguyên tố (ex02_09.py)")
add_p(doc, "- Yêu cầu: Xây dựng hàm kiem_tra_so_nguyen_to(n) trả về True nếu n là số nguyên tố, ngược lại trả về False. Tối ưu vòng lặp kiểm tra đến căn bậc hai của n.")
add_code_box(doc, """def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("Nhập vào số cần kiểm tra: "))
if kiem_tra_so_nguyen_to(number):
    print(number, "là số nguyên tố.")
else:
    print(number, "không phải là số nguyên tố.")""")
add_image_with_caption(doc, 'report_assets/hinh10_ex02_09.png', "Hình 10: Kết quả thực thi ex02_09.py kiểm tra số 7 và 15")
add_p(doc, "*(Vị trí chụp: Chạy 'python ex02_09.py' kiểm tra số 7 và số 15)*", italic=True)

# Câu 10
add_heading_2(doc, "Câu 10: Hàm đảo ngược chuỗi ký tự (ex02_10.py)")
add_p(doc, "- Yêu cầu: Xây dựng hàm nhận vào một chuỗi ký tự bất kỳ và trả về chuỗi đảo ngược sử dụng kỹ thuật slicing [::-1].")
add_code_box(doc, """def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]

input_string = input("Mời nhập chuỗi cần đảo ngược: ")
print("Chuỗi đảo ngược là:", dao_nguoc_chuoi(input_string))""")
add_image_with_caption(doc, 'report_assets/hinh11_ex02_10.png', "Hình 11: Kết quả thực thi ex02_10.py đảo ngược chuỗi")
add_p(doc, "*(Vị trí chụp: Chạy 'python ex02_10.py', nhập 'hutech university')*", italic=True)

# SECTION III
add_heading_1(doc, "III. DANH SÁCH, BỘ VÀ TỪ ĐIỂN (LIST, TUPLE, DICTIONARY - ex03)")
add_p(doc, "Các bài tập cấu trúc dữ liệu được lưu trong thư mục 'lab-01/ex03':")

# ex03_01
add_heading_2(doc, "Câu 1: Tính tổng các số chẵn trong List (ex03_01.py)")
add_p(doc, "- Yêu cầu: Nhập danh sách các số nguyên cách nhau bởi dấu phẩy, tính và in tổng của tất cả các phần tử là số chẵn.")
add_code_box(doc, """def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
tong_chan = tinh_tong_so_chan(numbers)
print("Tổng các số chẵn trong List là:", tong_chan)""")
add_image_with_caption(doc, 'report_assets/hinh12_ex03_01.png', "Hình 12: Kết quả thực thi ex03_01.py tính tổng số chẵn")
add_p(doc, "*(Vị trí chụp: Chạy 'python ex03_01.py', nhập '1,-2,3,4,5,-6,7,8,-9')*", italic=True)

# ex03_02
add_heading_2(doc, "Câu 2: Đảo ngược các phần tử trong List (ex03_02.py)")
add_p(doc, "- Yêu cầu: Nhập danh sách các phần tử số nguyên và đảo ngược vị trí các phần tử trong danh sách.")
add_code_box(doc, """def dao_nguoc_list(lst):
    return lst[::-1]

input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
list_dao_nguoc = dao_nguoc_list(numbers)
print("List sau khi đảo ngược:", list_dao_nguoc)""")
add_image_with_caption(doc, 'report_assets/hinh13_ex03_02.png', "Hình 13: Kết quả thực thi ex03_02.py đảo ngược danh sách")
add_p(doc, "*(Vị trí chụp: Chạy 'python ex03_02.py', nhập chuỗi số)*", italic=True)

# ex03_03
add_heading_2(doc, "Câu 3: Tạo Tuple từ List (ex03_03.py)")
add_p(doc, "- Yêu cầu: Chuyển đổi danh sách (List) các số nhập vào từ bàn phím thành bộ dữ liệu bất biến (Tuple).")
add_code_box(doc, """def tao_tuple_tu_list(lst):
    return tuple(lst)

input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
my_tuple = tao_tuple_tu_list(numbers)
print("List: ", numbers)
print("Tuple từ List:", my_tuple)""")
add_image_with_caption(doc, 'report_assets/hinh14_ex03_03.png', "Hình 14: Kết quả thực thi ex03_03.py tạo Tuple từ List")
add_p(doc, "*(Vị trí chụp: Chạy 'python ex03_03.py', nhập chuỗi số)*", italic=True)

# ex03_04
add_heading_2(doc, "Câu 4: Truy cập phần tử đầu tiên và cuối cùng trong Tuple (ex03_04.py)")
add_p(doc, "- Yêu cầu: Nhập một Tuple và truy cập lấy ra phần tử đầu tiên (index 0) và phần tử cuối cùng (index -1).")
add_code_box(doc, """def truy_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element

input_tuple = eval(input("Nhập tuple, ví dụ (1, 2, 3): "))
first, last = truy_cap_phan_tu(input_tuple)
print("Phần tử đầu tiên:", first)
print("Phần tử cuối cùng:", last)""")
add_image_with_caption(doc, 'report_assets/hinh15_ex03_04.png', "Hình 15: Kết quả thực thi ex03_04.py truy cập phần tử Tuple")
add_p(doc, "*(Vị trí chụp: Chạy 'python ex03_04.py', nhập tuple '(1, -2, 3, 4, -5)')*", italic=True)

# ex03_05
add_heading_2(doc, "Câu 5: Đếm số lần xuất hiện của các từ vào Dictionary (ex03_05.py)")
add_p(doc, "- Yêu cầu: Nhập danh sách các từ cách nhau bởi khoảng trắng, đếm tần suất xuất hiện của từng từ và lưu vào Dictionary.")
add_code_box(doc, """def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

input_string = input("Nhập danh sách các từ, cách nhau bằng dấu cách: ")
word_list = input_string.split()
so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("Số lần xuất hiện của các phần tử:", so_lan_xuat_hien)""")
add_image_with_caption(doc, 'report_assets/hinh16_ex03_05.png', "Hình 16: Kết quả thực thi ex03_05.py đếm tần suất từ")
add_p(doc, "*(Vị trí chụp: Chạy 'python ex03_05.py', nhập danh sách các từ)*", italic=True)

# ex03_06
add_heading_2(doc, "Câu 6: Xóa phần tử khỏi Dictionary theo khóa (ex03_06.py)")
add_p(doc, "- Yêu cầu: Xây dựng hàm xóa một phần tử khỏi từ điển (Dictionary) dựa trên khóa (key) chỉ định và in kết quả từ điển sau khi xóa.")
add_code_box(doc, """def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key_to_delete = 'b'
result = xoa_phan_tu(my_dict, key_to_delete)
if result:
    print("Phần tử đã được xóa từ Dictionary:", my_dict)
else:
    print("Không tìm thấy phần tử cần xóa trong Dictionary.")""")
add_image_with_caption(doc, 'report_assets/hinh17_ex03_06.png', "Hình 17: Kết quả thực thi ex03_06.py xóa phần tử theo key")
add_p(doc, "*(Vị trí chụp: Chạy 'python ex03_06.py')*", italic=True)

# SECTION IV
add_heading_1(doc, "IV. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON (OOP - ex04)")
add_p(doc, "Hệ thống Quản lý Sinh viên được xây dựng theo chuẩn hướng đối tượng (OOP) phân tách thành 3 tệp tin chuyên biệt đặt tại thư mục 'lab-01/ex04':")

# Table of Grading
tbl_grade = doc.add_table(rows=5, cols=3)
tbl_grade.alignment = WD_TABLE_ALIGNMENT.CENTER
headers = ["Phân loại Học lực", "Thang điểm Trung bình (hệ 10)", "Quy tắc xếp loại"]
for idx, h_text in enumerate(headers):
    c = tbl_grade.cell(0, idx)
    set_cell_background(c, "005B96")
    set_cell_margins(c, 80, 80, 100, 100)
    p = c.paragraphs[0]
    r = p.add_run(h_text)
    r.font.bold = True
    r.font.name = 'Times New Roman'
    r.font.color.rgb = RGBColor(255, 255, 255)

grade_data = [
    ("Loại Giỏi", "Từ 8.0 trở lên", "diemTB >= 8.0"),
    ("Loại Khá", "Từ 6.5 đến dưới 8.0", "6.5 <= diemTB < 8.0"),
    ("Loại Trung bình", "Từ 5.0 đến dưới 6.5", "5.0 <= diemTB < 6.5"),
    ("Loại Yếu", "Dưới 5.0", "diemTB < 5.0")
]
for row_idx, data in enumerate(grade_data, start=1):
    for col_idx, val in enumerate(data):
        c = tbl_grade.cell(row_idx, col_idx)
        set_cell_background(c, "F2F7FA" if row_idx % 2 == 1 else "FFFFFF")
        set_cell_margins(c, 60, 60, 100, 100)
        p = c.paragraphs[0]
        r = p.add_run(val)
        r.font.name = 'Times New Roman'

doc.add_paragraph().paragraph_format.space_after = Pt(4)

add_heading_2(doc, "1. Lớp đối tượng SinhVien (SinhVien.py)")
add_p(doc, "Đóng gói các thuộc tính cơ bản của một sinh viên bao gồm: id (mã sinh viên tự tăng), name (họ tên), sex (giới tính), major (chuyên ngành), diemTB (điểm trung bình hệ 10), và hocLuc (kết quả xếp loại học lực):")
add_code_box(doc, """class SinhVien:
    def __init__(self, id, name, sex, major, diemTB):
        self._id = id
        self._name = name
        self._sex = sex
        self._major = major
        self._diemTB = diemTB
        self._hocLuc = "" """)

add_heading_2(doc, "2. Lớp nghiệp vụ Quản lý sinh viên (QuanLySinhVien.py)")
add_p(doc, "Chứa các phương thức quản lý tập hợp sinh viên: tự động cấp phát ID không trùng lặp (generateID), thêm mới, cập nhật thông tin theo ID, xóa theo ID, tìm kiếm theo tên gần đúng, sắp xếp theo điểm TB hoặc chuyên ngành, và hiển thị danh sách dạng bảng:")
add_code_box(doc, """from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []

    def __init__(self):
        self.listSinhVien = []

    def generateID(self):
        maxId = 1
        if len(self.listSinhVien) > 0:
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if maxId < sv._id:
                    maxId = sv._id
            maxId = maxId + 1
        return maxId

    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh cua sinh vien: ")
        diemTB = float(input("Nhap diem cua sinh vien: "))
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv = self.findById(ID)
        if sv is not None:
            sv._name = input("Nhap ten sinh vien: ")
            sv._sex = input("Nhap gioi tinh sinh vien: ")
            sv._major = input("Nhap chuyen nganh cua sinh vien: ")
            sv._diemTB = float(input("Nhap diem cua sinh vien: "))
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh vien co ID = {} khong ton tai.".format(ID))

    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB)

    def sortByChuyenNganh(self):
        self.listSinhVien.sort(key=lambda x: x._major)

    def findById(self, ID):
        for sv in self.listSinhVien:
            if sv._id == ID:
                return sv
        return None

    def findByID(self, ID):
        return self.findById(ID)

    def findByName(self, keyword):
        return [sv for sv in self.listSinhVien if keyword.upper() in sv._name.upper()]

    def deleteById(self, ID):
        sv = self.findById(ID)
        if sv is not None:
            self.listSinhVien.remove(sv)
            return True
        return False

    def xepLoaiHocLuc(self, sv: SinhVien):
        if sv._diemTB >= 8:
            sv._hocLuc = "Gioi"
        elif sv._diemTB >= 6.5:
            sv._hocLuc = "Kha"
        elif sv._diemTB >= 5:
            sv._hocLuc = "Trung binh"
        else:
            sv._hocLuc = "Yeu"

    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format("ID", "Name", "Sex", "Major", "Diem TB", "Hoc Luc"))
        if listSV is not None and len(listSV) > 0:
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format(
                    sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
        print("\\n")

    def getListSinhVien(self):
        return self.listSinhVien""")

add_heading_2(doc, "3. Chương trình điều khiển Menu (Main.py)")
add_p(doc, "Giao diện Console tương tác với vòng lặp vô hạn cung cấp 8 tùy chọn (1-Thêm, 2-Cập nhật, 3-Xóa, 4-Tìm kiếm, 5-Sắp xếp điểm, 6-Sắp xếp ngành/tên, 7-Hiển thị, 0-Thoát):")
add_code_box(doc, """from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while True:
    print("\\nCHUONG TRINH QUAN LY SINH VIEN")
    print("*************************MENU**************************")
    print("**  1. Them sinh vien.                               **")
    print("**  2. Cap nhat thong tin sinh vien boi ID.          **")
    print("**  3. Xoa sinh vien boi ID.                         **")
    print("**  4. Tim kiem sinh vien theo ten.                  **")
    print("**  5. Sap xep sinh vien theo diem trung binh.       **")
    print("**  6. Sap xep sinh vien theo ten chuyen nganh.      **")
    print("**  7. Hien thi danh sach sinh vien.                 **")
    print("**  0. Thoat                                         **")
    print("*******************************************************")
    key = int(input("Nhap tuy chon: "))
    # ... xu ly tung chuc nang va goi qlsv ...""")

add_image_with_caption(doc, 'report_assets/hinh18_ex04_main.png', "Hình 18: Kết quả thực thi chương trình quản lý sinh viên Main.py (Thêm SV và hiển thị bảng)")
add_p(doc, "*(Vị trí chụp: Terminal tại lab-01/ex04, chạy 'python Main.py', chọn chức năng 1 thêm sinh viên và chức năng 7 hiển thị danh sách)*", italic=True)

# SECTION V
add_heading_1(doc, "V. QUẢN LÝ MÃ NGUỒN VÀ ĐẨY LÊN GITHUB REPOSITORY")
add_p(doc, "Dự án được khởi tạo và đẩy lên kho lưu trữ GitHub chính thức:")
add_p(doc, "- Đường dẫn Remote Repository: https://github.com/khang1233/TH_LTANTT_2387700027.git")
add_p(doc, "- Nhánh mặc định (Default branch): main")
add_p(doc, "- Các bước dòng lệnh đã thực hiện:")
add_code_box(doc, """git init
git branch -M main
git remote add origin https://github.com/khang1233/TH_LTANTT_2387700027.git
git add .
git commit -m "Hoan thanh Lab 01"
git push -u origin main""")
add_image_with_caption(doc, 'report_assets/hinh19_git_push.png', "Hình 19: Trạng thái Git Status và kết quả Push toàn bộ mã nguồn lên GitHub nhánh main")
add_p(doc, "*(Vị trí chụp: Terminal tại thư mục gốc dự án, chạy 'git status', 'git remote -v' và 'git push origin main')*", italic=True)

# SECTION VI
add_heading_1(doc, "VI. KẾT LUẬN VÀ BÀI HỌC KINH NGHIỆM")
add_p(doc, "1. Kết quả đạt được:", bold=True)
add_p(doc, "- Hoàn thành 100% các yêu cầu bài thực hành số 1 bao gồm toàn bộ các bài tập cơ bản ex02, các bài tập cấu trúc dữ liệu ex03 và ứng dụng OOP Quản lý sinh viên ex04.")
add_p(doc, "- Toàn bộ mã nguồn chạy ổn định, không phát sinh lỗi cú pháp hay ngoại lệ thời gian chạy, tuân thủ chặt chẽ cấu trúc thư mục quy định.")
add_p(doc, "- Mã nguồn đã được đồng bộ an toàn và lưu trữ trên GitHub cá nhân phục vụ việc đánh giá, chấm điểm trực tiếp.")

add_p(doc, "2. Bài học kinh nghiệm:", bold=True)
add_p(doc, "- Nắm bắt được ưu điểm cú pháp ngắn gọn, linh hoạt của Python so với các ngôn ngữ biên dịch truyền thống như C/C++ hay Java trong việc xử lý chuỗi và cấu trúc dữ liệu.")
add_p(doc, "- Hiểu sâu cơ chế làm việc của Dictionary và List slicing - hai công cụ cực kỳ mạnh mẽ trong phân tích dữ liệu và an toàn thông tin.")
add_p(doc, "- Nắm vững kiến trúc lập trình hướng đối tượng trong Python, biết cách phân tách module và đóng gói dữ liệu giúp chương trình dễ bảo trì, mở rộng cho các bài lab nâng cao tiếp theo.")

output_docx = "BaoCao_ThucHanh_Lab01.docx"
doc.save(output_docx)
print(f"Report saved successfully as {output_docx} (Size: {os.path.getsize(output_docx)} bytes)")
