import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, hex_color):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=70, bottom=70, left=120, right=120):
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
    set_cell_background(cell, "F6F8FA")
    set_cell_margins(cell, top=100, bottom=100, left=160, right=160)
    
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>\n'
        f'  <w:left w:val="single" w:sz="18" w:space="0" w:color="0969DA"/>\n'
        f'  <w:bottom w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>\n'
        f'  <w:right w:val="single" w:sz="4" w:space="0" w:color="D0D7DE"/>\n'
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
    run.font.color.rgb = RGBColor(36, 41, 47)
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_after = Pt(2)

def add_heading_1(doc, text):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(14)
    h.paragraph_format.space_after = Pt(4)
    h.paragraph_format.keep_with_next = True
    run = h.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(13.5)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0, 51, 102)
    return h

def add_heading_2(doc, text):
    h = doc.add_paragraph()
    h.paragraph_format.space_before = Pt(8)
    h.paragraph_format.space_after = Pt(3)
    h.paragraph_format.keep_with_next = True
    run = h.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    run.font.bold = True
    run.font.color.rgb = RGBColor(20, 70, 130)
    return h

def add_image(doc, img_path):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(2)
        p_img.paragraph_format.space_after = Pt(8)
        p_img.add_run().add_picture(img_path, width=Inches(5.9))

doc = docx.Document()

# Page Margins
for s in doc.sections:
    s.top_margin = Inches(0.8)
    s.bottom_margin = Inches(0.8)
    s.left_margin = Inches(0.85)
    s.right_margin = Inches(0.85)

# Logo
if os.path.exists('report_assets/hutech_logo.jpeg'):
    p_logo = doc.add_paragraph()
    p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_logo.paragraph_format.space_after = Pt(2)
    p_logo.add_run().add_picture('report_assets/hutech_logo.jpeg', width=Inches(1.1))

# University Header
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
p_line.paragraph_format.space_after = Pt(8)
r_line = p_line.add_run("-----------------------------------------------------------------------------------------")
r_line.font.color.rgb = RGBColor(180, 180, 180)

# Student Info Box
tbl = doc.add_table(rows=2, cols=2)
tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
for r in tbl.rows:
    for c in r.cells:
        set_cell_background(c, "F5F8FA")
        set_cell_margins(c, 70, 70, 120, 120)

def add_box_field(cell, label, val):
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    r1 = p.add_run(label)
    r1.font.name = 'Times New Roman'
    r1.font.bold = True
    r2 = p.add_run(val)
    r2.font.name = 'Times New Roman'

add_box_field(tbl.cell(0, 0), "Họ và Tên: ", "Trần Minh Khang")
add_box_field(tbl.cell(0, 1), "MSSV: ", "2387700027")
add_box_field(tbl.cell(1, 0), "Lớp: ", "23DATA1 / ATTT")
add_box_field(tbl.cell(1, 1), "GitHub: ", "khang1233/TH_LTANTT_2387700027")

p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_title.paragraph_format.space_before = Pt(14)
p_title.paragraph_format.space_after = Pt(12)
run_t = p_title.add_run("BÁO CÁO THỰC HÀNH\nBÀI 1: LẬP TRÌNH CƠ BẢN VỚI NGÔN NGỮ PYTHON")
run_t.font.name = 'Times New Roman'
run_t.font.size = Pt(14)
run_t.font.bold = True
run_t.font.color.rgb = RGBColor(0, 51, 102)

# ================= 1.1 =================
add_heading_1(doc, "1.1 CÀI ĐẶT MÔI TRƯỜNG & CHƯƠNG TRÌNH ĐẦU TIÊN")
add_heading_2(doc, "Hình 1: Kết quả chạy chương trình hello.py")
add_code_box(doc, """print("Hello, World!")
print("My name is Tran Minh Khang")
print("HUTECH University")""")
add_image(doc, "report_assets/hinh1_hello.png")

# ================= 1.2 =================
add_heading_1(doc, "1.2 LẬP TRÌNH PYTHON CƠ BẢN (ex02)")

add_heading_2(doc, "Hình 2: ex02_01.py - Nhập họ tên, tuổi và in lời chào")
add_code_box(doc, """ten = input("Nhap ten cua ban: ")
tuoi = input("Nhap tuoi cua ban: ")
print("Chao mung,", ten, "! Ban", tuoi, "tuoi.")""")
add_image(doc, "report_assets/hinh2_ex02_01.png")

add_heading_2(doc, "Hình 3: ex02_02.py - Tính diện tích hình tròn (Pi = 3.14)")
add_code_box(doc, """ban_kinh = float(input("Nhap ban kinh cua hinh tron: "))
dien_tich = 3.14 * (ban_kinh ** 2)
print("Dien tich cua hinh tron la:", dien_tich)""")
add_image(doc, "report_assets/hinh3_ex02_02.png")

add_heading_2(doc, "Hình 4: ex02_03.py - Kiểm tra số chẵn / số lẻ")
add_code_box(doc, """so = int(input("Nhap mot so nguyen: "))
if so % 2 == 0:
    print(so, "la so chan.")
else:
    print(so, "khong phai la so chan.")""")
add_image(doc, "report_assets/hinh4_ex02_03.png")

add_heading_2(doc, "Hình 5: ex02_04.py - Tìm số chia hết cho 7 không chia hết cho 5 trong đoạn [2000, 3200]")
add_code_box(doc, """j = []
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
print(','.join(j))""")
add_image(doc, "report_assets/hinh5_ex02_04.png")

add_heading_2(doc, "Hình 6: ex02_05.py - Tính tiền lương thực nhận của nhân viên")
add_code_box(doc, """so_gio_lam = float(input("Nhap so gio lam moi tuan: "))
luong_gio = float(input("Nhap thu lao tren moi gio lam tieu chuan: "))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
thuc_linh = gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5
print(f"So tien thuc linh cua nhan vien: {thuc_linh}")""")
add_image(doc, "report_assets/hinh6_ex02_05.png")

add_heading_2(doc, "Hình 7: ex02_06.py - Tạo mảng 2 chiều X x Y với giá trị phần tử i * j")
add_code_box(doc, """input_str = input("Nhap X, Y: ")
dimensions = [int(x) for x in input_str.split(',')]
rowNum = dimensions[0]
colNum = dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row * col
print(multilist)""")
add_image(doc, "report_assets/hinh7_ex02_06.png")

add_heading_2(doc, "Hình 8: ex02_07.py - Chuyển đổi các dòng văn bản thành chữ in hoa")
add_code_box(doc, """print("Nhap cac dong van ban (Nhap 'done' de ket thuc):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)

print("\\nCac dong da nhap sau khi chuyen thanh chu in hoa:")
for line in lines:
    print(line.upper())""")
add_image(doc, "report_assets/hinh8_ex02_07.png")

add_heading_2(doc, "Hình 9: ex02_08.py - Lọc các số nhị phân 4 chữ số chia hết cho 5")
add_code_box(doc, """def chia_het_cho_5(so_nhi_phan):
    so_thap_phan = int(so_nhi_phan, 2)
    return so_thap_phan % 5 == 0

chuoi_so_nhi_phan = input("Nhap chuoi so nhi phan (phan tach boi dau phay): ")
so_nhi_phan_list = chuoi_so_nhi_phan.split(',')
so_chia_het_cho_5 = [so for so in so_nhi_phan_list if chia_het_cho_5(so)]

if len(so_chia_het_cho_5) > 0:
    ket_qua = ','.join(so_chia_het_cho_5)
    print("Cac so nhi phan chia het cho 5 la:", ket_qua)
else:
    print("Khong co so nhi phan nao chia het cho 5 trong chuoi da nhap.")""")
add_image(doc, "report_assets/hinh9_ex02_08.png")

add_heading_2(doc, "Hình 10: ex02_09.py - Hàm kiểm tra số nguyên tố")
add_code_box(doc, """def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("Nhap vao so can kiem tra: "))
if kiem_tra_so_nguyen_to(number):
    print(number, "la so nguyen to.")
else:
    print(number, "khong phai la so nguyen to.")""")
add_image(doc, "report_assets/hinh10_ex02_09.png")

add_heading_2(doc, "Hình 11: ex02_10.py - Hàm đảo ngược chuỗi ký tự")
add_code_box(doc, """def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]

input_string = input("Moi nhap chuoi can dao nguoc: ")
print("Chuoi dao nguoc la:", dao_nguoc_chuoi(input_string))""")
add_image(doc, "report_assets/hinh11_ex02_10.png")

# ================= 1.3 =================
add_heading_1(doc, "1.3 CẤU TRÚC DỮ LIỆU LIST, TUPLE, DICTIONARY (ex03)")

add_heading_2(doc, "Hình 12: ex03_01.py - Tính tổng các số chẵn trong List")
add_code_box(doc, """def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

input_list = input("Nhap danh sach cac so, cach nhau bang dau phay: ")
numbers = list(map(int, input_list.split(',')))
tong_chan = tinh_tong_so_chan(numbers)
print("Tong cac so chan trong List la:", tong_chan)""")
add_image(doc, "report_assets/hinh12_ex03_01.png")

add_heading_2(doc, "Hình 13: ex03_02.py - Đảo ngược vị trí các phần tử trong List")
add_code_box(doc, """def dao_nguoc_list(lst):
    return lst[::-1]

input_list = input("Nhap danh sach cac so, cach nhau bang dau phay: ")
numbers = list(map(int, input_list.split(',')))
list_dao_nguoc = dao_nguoc_list(numbers)
print("List sau khi dao nguoc:", list_dao_nguoc)""")
add_image(doc, "report_assets/hinh13_ex03_02.png")

add_heading_2(doc, "Hình 14: ex03_03.py - Tạo một Tuple từ một List nhập vào")
add_code_box(doc, """def tao_tuple_tu_list(lst):
    return tuple(lst)

input_list = input("Nhap danh sach cac so, cach nhau bang dau phay: ")
numbers = list(map(int, input_list.split(',')))
my_tuple = tao_tuple_tu_list(numbers)
print("List: ", numbers)
print("Tuple tu List:", my_tuple)""")
add_image(doc, "report_assets/hinh14_ex03_03.png")

add_heading_2(doc, "Hình 15: ex03_04.py - Truy cập phần tử đầu tiên và cuối cùng trong Tuple")
add_code_box(doc, """def truy_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element

input_tuple = eval(input("Nhap tuple, vi du (1, 2, 3): "))
first, last = truy_cap_phan_tu(input_tuple)
print("Phan tu dau tien:", first)
print("Phan tu cuoi cung:", last)""")
add_image(doc, "report_assets/hinh15_ex03_04.png")

add_heading_2(doc, "Hình 16: ex03_05.py - Đếm số lần xuất hiện của từ vào Dictionary")
add_code_box(doc, """def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

input_string = input("Nhap danh sach cac tu, cach nhau bang dau cach: ")
word_list = input_string.split()
so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("So lan xuat hien cua cac phan tu:", so_lan_xuat_hien)""")
add_image(doc, "report_assets/hinh16_ex03_05.png")

add_heading_2(doc, "Hình 17: ex03_06.py - Xóa phần tử khỏi Dictionary theo khóa")
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
    print("Phan tu da duoc xoa tu Dictionary:", my_dict)
else:
    print("Khong tim thay phan tu can xoa trong Dictionary.")""")
add_image(doc, "report_assets/hinh17_ex03_06.png")

# ================= 1.4 =================
add_heading_1(doc, "1.4 LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON (OOP - ex04)")

# Table of Grading
tbl_grade = doc.add_table(rows=5, cols=3)
tbl_grade.alignment = WD_TABLE_ALIGNMENT.CENTER
headers = ["Phân loại Học lực", "Thang điểm Trung bình (hệ 10)", "Quy tắc logic"]
for idx, h_text in enumerate(headers):
    c = tbl_grade.cell(0, idx)
    set_cell_background(c, "005B96")
    set_cell_margins(c, 70, 70, 100, 100)
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
        set_cell_background(c, "F5F8FA" if row_idx % 2 == 1 else "FFFFFF")
        set_cell_margins(c, 60, 60, 100, 100)
        p = c.paragraphs[0]
        r = p.add_run(val)
        r.font.name = 'Times New Roman'

p_sp = doc.add_paragraph()
p_sp.paragraph_format.space_after = Pt(4)

add_heading_2(doc, "Mã nguồn SinhVien.py:")
add_code_box(doc, """class SinhVien:
    def __init__(self, id, name, sex, major, diemTB):
        self._id = id
        self._name = name
        self._sex = sex
        self._major = major
        self._diemTB = diemTB
        self._hocLuc = "" """)

add_heading_2(doc, "Mã nguồn QuanLySinhVien.py:")
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

add_heading_2(doc, "Mã nguồn Main.py (Menu điều khiển):")
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
    # ... xu ly cac chuc nang 1-7 va 0 thoat ...""")

add_heading_2(doc, "Hình 18: Kết quả thực thi Main.py (Thêm sinh viên và hiển thị bảng)")
add_image(doc, "report_assets/hinh18_ex04_main.png")

# ================= Git =================
add_heading_1(doc, "1.5 ĐỒNG BỘ MÃ NGUỒN LÊN GITHUB REPOSITORY")
add_heading_2(doc, "Hình 19: Trạng thái Git Status và Push lên GitHub")
add_code_box(doc, """git init
git branch -M main
git remote add origin https://github.com/khang1233/TH_LTANTT_2387700027.git
git add .
git commit -m "Hoan thanh toan bo Lab 01"
git push -u origin main""")
add_image(doc, "report_assets/hinh19_git_push.png")

# Save files
for target in ["BaoCao_Lab01_HoanChinh.docx", "BaoCao_Lab01.docx"]:
    try:
        doc.save(target)
        print(f"Saved: {target}")
    except Exception as e:
        print(f"Could not save {target}: {e}")
