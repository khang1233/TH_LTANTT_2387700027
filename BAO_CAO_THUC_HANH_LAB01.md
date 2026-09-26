# TRƯỜNG ĐẠI HỌC CÔNG NGHỆ TP. HỒ CHÍ MINH (HUTECH)
### KHOA CÔNG NGHỆ THÔNG TIN
**Môn học:** Thực hành Lập trình An toàn thông tin  
**Họ và Tên:** Trần Minh Khang - **MSSV:** 2387700027 - **Lớp:** 23DATA1 / ATTT  
**GitHub:** [khang1233/TH_LTANTT_2387700027](https://github.com/khang1233/TH_LTANTT_2387700027.git)  

---

# BÁO CÁO THỰC HÀNH - BÀI 1: LẬP TRÌNH CƠ BẢN VỚI NGÔN NGỮ PYTHON

---

## 1.1 CÀI ĐẶT MÔI TRƯỜNG & CHƯƠNG TRÌNH ĐẦU TIÊN

### Hình 1: Kết quả chạy chương trình hello.py
```python
print("Hello, World!")
print("My name is Tran Minh Khang")
print("HUTECH University")
```
![Hình 1](report_assets/hinh1_hello.png)

---

## 1.2 LẬP TRÌNH PYTHON CƠ BẢN (ex02)

### Hình 2: ex02_01.py - Nhập họ tên, tuổi và in lời chào
```python
ten = input("Nhap ten cua ban: ")
tuoi = input("Nhap tuoi cua ban: ")
print("Chao mung,", ten, "! Ban", tuoi, "tuoi.")
```
![Hình 2](report_assets/hinh2_ex02_01.png)

### Hình 3: ex02_02.py - Tính diện tích hình tròn
```python
ban_kinh = float(input("Nhap ban kinh cua hinh tron: "))
dien_tich = 3.14 * (ban_kinh ** 2)
print("Dien tich cua hinh tron la:", dien_tich)
```
![Hình 3](report_assets/hinh3_ex02_02.png)

### Hình 4: ex02_03.py - Kiểm tra số chẵn / số lẻ
```python
so = int(input("Nhap mot so nguyen: "))
if so % 2 == 0:
    print(so, "la so chan.")
else:
    print(so, "khong phai la so chan.")
```
![Hình 4](report_assets/hinh4_ex02_03.png)

### Hình 5: ex02_04.py - Tìm số chia hết cho 7 không chia hết cho 5 trong đoạn [2000, 3200]
```python
j = []
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
print(','.join(j))
```
![Hình 5](report_assets/hinh5_ex02_04.png)

### Hình 6: ex02_05.py - Tính tiền lương thực nhận của nhân viên
```python
so_gio_lam = float(input("Nhap so gio lam moi tuan: "))
luong_gio = float(input("Nhap thu lao tren moi gio lam tieu chuan: "))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
thuc_linh = gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5
print(f"So tien thuc linh cua nhan vien: {thuc_linh}")
```
![Hình 6](report_assets/hinh6_ex02_05.png)

### Hình 7: ex02_06.py - Tạo mảng 2 chiều X x Y với giá trị phần tử i * j
```python
input_str = input("Nhap X, Y: ")
dimensions = [int(x) for x in input_str.split(',')]
rowNum = dimensions[0]
colNum = dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row * col
print(multilist)
```
![Hình 7](report_assets/hinh7_ex02_06.png)

### Hình 8: ex02_07.py - Chuyển đổi các dòng văn bản thành chữ in hoa
```python
print("Nhap cac dong van ban (Nhap 'done' de ket thuc):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)

print("\nCac dong da nhap sau khi chuyen thanh chu in hoa:")
for line in lines:
    print(line.upper())
```
![Hình 8](report_assets/hinh8_ex02_07.png)

### Hình 9: ex02_08.py - Lọc các số nhị phân 4 chữ số chia hết cho 5
```python
def chia_het_cho_5(so_nhi_phan):
    so_thap_phan = int(so_nhi_phan, 2)
    return so_thap_phan % 5 == 0

chuoi_so_nhi_phan = input("Nhap chuoi so nhi phan (phan tach boi dau phay): ")
so_nhi_phan_list = chuoi_so_nhi_phan.split(',')
so_chia_het_cho_5 = [so for so in so_nhi_phan_list if chia_het_cho_5(so)]

if len(so_chia_het_cho_5) > 0:
    ket_qua = ','.join(so_chia_het_cho_5)
    print("Cac so nhi phan chia het cho 5 la:", ket_qua)
else:
    print("Khong co so nhi phan nao chia het cho 5 trong chuoi da nhap.")
```
![Hình 9](report_assets/hinh9_ex02_08.png)

### Hình 10: ex02_09.py - Hàm kiểm tra số nguyên tố
```python
def kiem_tra_so_nguyen_to(n):
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
    print(number, "khong phai la so nguyen to.")
```
![Hình 10](report_assets/hinh10_ex02_09.png)

### Hình 11: ex02_10.py - Hàm đảo ngược chuỗi ký tự
```python
def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]

input_string = input("Moi nhap chuoi can dao nguoc: ")
print("Chuoi dao nguoc la:", dao_nguoc_chuoi(input_string))
```
![Hình 11](report_assets/hinh11_ex02_10.png)

---

## 1.3 CẤU TRÚC DỮ LIỆU LIST, TUPLE, DICTIONARY (ex03)

### Hình 12: ex03_01.py - Tính tổng các số chẵn trong List
```python
def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

input_list = input("Nhap danh sach cac so, cach nhau bang dau phay: ")
numbers = list(map(int, input_list.split(',')))
tong_chan = tinh_tong_so_chan(numbers)
print("Tong cac so chan trong List la:", tong_chan)
```
![Hình 12](report_assets/hinh12_ex03_01.png)

### Hình 13: ex03_02.py - Đảo ngược vị trí các phần tử trong List
```python
def dao_nguoc_list(lst):
    return lst[::-1]

input_list = input("Nhap danh sach cac so, cach nhau bang dau phay: ")
numbers = list(map(int, input_list.split(',')))
list_dao_nguoc = dao_nguoc_list(numbers)
print("List sau khi dao nguoc:", list_dao_nguoc)
```
![Hình 13](report_assets/hinh13_ex03_02.png)

### Hình 14: ex03_03.py - Tạo một Tuple từ một List nhập vào
```python
def tao_tuple_tu_list(lst):
    return tuple(lst)

input_list = input("Nhap danh sach cac so, cach nhau bang dau phay: ")
numbers = list(map(int, input_list.split(',')))
my_tuple = tao_tuple_tu_list(numbers)
print("List: ", numbers)
print("Tuple tu List:", my_tuple)
```
![Hình 14](report_assets/hinh14_ex03_03.png)

### Hình 15: ex03_04.py - Truy cập phần tử đầu tiên và cuối cùng trong Tuple
```python
def truy_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element

input_tuple = eval(input("Nhap tuple, vi du (1, 2, 3): "))
first, last = truy_cap_phan_tu(input_tuple)
print("Phan tu dau tien:", first)
print("Phan tu cuoi cung:", last)
```
![Hình 15](report_assets/hinh15_ex03_04.png)

### Hình 16: ex03_05.py - Đếm số lần xuất hiện của từ vào Dictionary
```python
def dem_so_lan_xuat_hien(lst):
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
print("So lan xuat hien cua cac phan tu:", so_lan_xuat_hien)
```
![Hình 16](report_assets/hinh16_ex03_05.png)

### Hình 17: ex03_06.py - Xóa phần tử khỏi Dictionary theo khóa
```python
def xoa_phan_tu(dictionary, key):
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
    print("Khong tim thay phan tu can xoa trong Dictionary.")
```
![Hình 17](report_assets/hinh17_ex03_06.png)

---

## 1.4 LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON (OOP - ex04)

### Bảng tiêu chuẩn phân loại học lực:
| Phân loại học lực | Thang điểm Trung bình (hệ 10) | Quy tắc logic |
| :--- | :--- | :--- |
| **Loại Giỏi** | Từ 8.0 trở lên | `diemTB >= 8.0` |
| **Loại Khá** | Từ 6.5 đến dưới 8.0 | `6.5 <= diemTB < 8.0` |
| **Loại Trung bình** | Từ 5.0 đến dưới 6.5 | `5.0 <= diemTB < 6.5` |
| **Loại Yếu** | Dưới 5.0 | `diemTB < 5.0` |

### Mã nguồn SinhVien.py:
```python
class SinhVien:
    def __init__(self, id, name, sex, major, diemTB):
        self._id = id
        self._name = name
        self._sex = sex
        self._major = major
        self._diemTB = diemTB
        self._hocLuc = ""
```

### Mã nguồn QuanLySinhVien.py:
```python
from SinhVien import SinhVien

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
        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien
```

### Mã nguồn Main.py:
```python
from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while True:
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
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
    # ... xu ly cac chuc nang ...
```

### Hình 18: Kết quả thực thi Main.py (Thêm sinh viên Trần Minh Khang và hiển thị bảng)
![Hình 18](report_assets/hinh18_ex04_main.png)

---

## 1.5 ĐỒNG BỘ MÃ NGUỒN LÊN GITHUB REPOSITORY

### Hình 19: Trạng thái Git Status và Push lên GitHub
```bash
git init
git branch -M main
git remote add origin https://github.com/khang1233/TH_LTANTT_2387700027.git
git add .
git commit -m "Hoan thanh toan bo Lab 01"
git push -u origin main
```
![Hình 19](report_assets/hinh19_git_push.png)
