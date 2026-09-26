# BÁO CÁO THỰC HÀNH: BÀI 1 - LẬP TRÌNH CƠ BẢN VỚI NGÔN NGỮ PYTHON

**TRƯỜNG ĐẠI HỌC CÔNG NGHỆ TP. HỒ CHÍ MINH (HUTECH)**  
**KHOA CÔNG NGHỆ THÔNG TIN**  
**Môn học:** Thực hành Lập trình An toàn thông tin  
**Học kỳ:** 1 - Năm học 2026-2027  

---

### THÔNG TIN SINH VIÊN
- **Họ và tên:** Võ Duy Khang  
- **MSSV:** 2387700027  
- **Lớp:** 23DATA1 / ATTT  
- **Kho lưu trữ GitHub:** [khang1233/TH_LTANTT_2387700027](https://github.com/khang1233/TH_LTANTT_2387700027.git)  

---

## I. MỤC TIÊU VÀ MÔI TRƯỜNG THỰC HÀNH

### 1. Mục tiêu bài thực hành
- Thiết lập và kiểm tra môi trường lập trình Python, trình soạn thảo Visual Studio Code cùng các tiện ích mở rộng phục vụ môn học.
- Nắm vững quy trình làm việc với hệ thống quản lý phiên bản Git và kho lưu trữ trực tuyến GitHub.
- Làm chủ cú pháp căn bản của ngôn ngữ Python: biến, kiểu dữ liệu, các phép toán số học, cấu trúc rẽ nhánh `if-else`, vòng lặp `for` / `while` và hàm tự định nghĩa.
- Sử dụng hiệu quả các cấu trúc dữ liệu nền tảng: `List`, `Tuple`, `Dictionary`.
- Vận dụng tư duy Lập trình hướng đối tượng (OOP) để xây dựng ứng dụng Quản lý Sinh viên với đầy đủ các thao tác CRUD và sắp xếp dữ liệu.

### 2. Môi trường thực hiện
- **Hệ điều hành:** Microsoft Windows 11 Pro 64-bit
- **Python version:** 3.12 / 3.14 (Add to PATH)
- **Công cụ:** Visual Studio Code (Extensions: Python, Pylance, Python Indent, Python Snippets)
- **Git version:** 2.x x64

### 3. Chương trình đầu tiên (`lab-01/hello.py`)
Mã nguồn:
```python
print("Hello, World!")
print("My name is Khang")
print("HUTECH University")
```

**Kết quả thực thi:**
![Hình 1: Kết quả chạy hello.py](report_assets/hinh1_hello.png)  
*Hình 1: Kết quả chạy chương trình hello.py trên Terminal VS Code*  
> 📷 **Vị trí chụp ảnh thực tế:** Mở Terminal trong VS Code, gõ `cd lab-01` và `python hello.py`, sau đó dùng tổ hợp phím `Win + Shift + S` chụp vùng cửa sổ terminal.

---

## II. LẬP TRÌNH PYTHON CƠ BẢN (THƯ MỤC `lab-01/ex02`)

### Câu 1: Nhập họ tên, tuổi và in lời chào (`ex02_01.py`)
- **Yêu cầu:** Nhập họ tên và tuổi người dùng, hiển thị thông điệp chào mừng kèm thông tin vừa nhập.
- **Mã nguồn:**
```python
ten = input("Nhập tên của bạn: ")
tuoi = input("Nhập tuổi của bạn: ")
print("Chào mừng,", ten, "! Bạn", tuoi, "tuổi.")
```
**Kết quả thực thi:**  
![Hình 2: Kết quả thực thi ex02_01.py](report_assets/hinh2_ex02_01.png)  
*Hình 2: Kết quả thực thi ex02_01.py*  
> 📷 **Vị trí chụp ảnh:** Chạy `python lab-01/ex02/ex02_01.py`, nhập tên và tuổi.

---

### Câu 2: Tính diện tích hình tròn (`ex02_02.py`)
- **Yêu cầu:** Nhập bán kính $r$, tính diện tích theo công thức $S = \pi \times r^2$ với $\pi = 3.14$.
- **Mã nguồn:**
```python
ban_kinh = float(input("Nhập bán kính của hình tròn: "))
dien_tich = 3.14 * (ban_kinh ** 2)
print("Diện tích của hình tròn là:", dien_tich)
```
**Kết quả thực thi:**  
![Hình 3: Kết quả thực thi ex02_02.py](report_assets/hinh3_ex02_02.png)  
*Hình 3: Kết quả thực thi ex02_02.py với r = 5.7*  
> 📷 **Vị trí chụp ảnh:** Chạy `python lab-01/ex02/ex02_02.py`, nhập giá trị bán kính `5.7`.

---

### Câu 3: Kiểm tra số chẵn / số lẻ (`ex02_03.py`)
- **Yêu cầu:** Nhập một số nguyên và kiểm tra số đó là số chẵn hay số lẻ qua toán tử `% 2`.
- **Mã nguồn:**
```python
so = int(input("Nhập một số nguyên: "))
if so % 2 == 0:
    print(so, "là số chẵn.")
else:
    print(so, "không phải là số chẵn.")
```
**Kết quả thực thi:**  
![Hình 4: Kết quả thực thi ex02_03.py](report_assets/hinh4_ex02_03.png)  
*Hình 4: Kết quả thực thi ex02_03.py với số 10 và 7*  
> 📷 **Vị trí chụp ảnh:** Chạy `python lab-01/ex02/ex02_03.py` hai lần (với 10 và 7).

---

### Câu 4: Tìm số chia hết cho 7 và không chia hết cho 5 (`ex02_04.py`)
- **Yêu cầu:** Tìm tất cả số trong đoạn $[2000, 3200]$ chia hết cho 7 nhưng không phải bội số của 5, in trên 1 dòng phân cách bằng dấu phẩy.
- **Mã nguồn:**
```python
j = []
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
print(','.join(j))
```
**Kết quả thực thi:**  
![Hình 5: Kết quả thực thi ex02_04.py](report_assets/hinh5_ex02_04.png)  
*Hình 5: Danh sách các số thỏa mãn yêu cầu trong đoạn 2000-3200*  
> 📷 **Vị trí chụp ảnh:** Chạy `python lab-01/ex02/ex02_04.py`.

---

### Câu 5: Tính tiền lương thực nhận của nhân viên (`ex02_05.py`)
- **Yêu cầu:** Giờ chuẩn là 44 giờ/tuần. Giờ làm thêm hưởng 150% mức lương giờ tiêu chuẩn.
- **Mã nguồn:**
```python
so_gio_lam = float(input("Nhập số giờ làm mỗi tuần: "))
luong_gio = float(input("Nhập thù lao trên mỗi giờ làm tiêu chuẩn: "))
gio_tieu_chuan = 44
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)
thuc_linh = gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5
print(f"Số tiền thực lĩnh của nhân viên: {thuc_linh}")
```
**Kết quả thực thi:**  
![Hình 6: Kết quả thực thi ex02_05.py](report_assets/hinh6_ex02_05.png)  
*Hình 6: Tính tiền lương thực nhận với 76.5 giờ làm và thù lao 150.000 VNĐ/giờ*  
> 📷 **Vị trí chụp ảnh:** Chạy `python lab-01/ex02/ex02_05.py`, nhập `76.5` và `150000`.

---

### Câu 6: Tạo mảng 2 chiều theo chỉ số hàng và cột (`ex02_06.py`)
- **Yêu cầu:** Nhập $X, Y$, khởi tạo mảng 2 chiều kích thước $X \times Y$ với phần tử tại hàng $i$, cột $j$ có giá trị $i \times j$.
- **Mã nguồn:**
```python
input_str = input("Nhập X, Y: ")
dimensions = [int(x) for x in input_str.split(',')]
rowNum = dimensions[0]
colNum = dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row * col
print(multilist)
```
**Kết quả thực thi:**  
![Hình 7: Kết quả thực thi ex02_06.py](report_assets/hinh7_ex02_06.png)  
*Hình 7: Mảng 2 chiều tạo từ X = 3, Y = 5*  
> 📷 **Vị trí chụp ảnh:** Chạy `python lab-01/ex02/ex02_06.py`, nhập `3, 5`.

---

### Câu 7: Chuyển đổi các dòng văn bản thành chữ in hoa (`ex02_07.py`)
- **Yêu cầu:** Nhập liên tục các dòng chuỗi cho đến khi nhập 'done' thì dừng và in ra dạng in hoa.
- **Mã nguồn:**
```python
print("Nhập các dòng văn bản (Nhập 'done' để kết thúc):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)

print("\nCác dòng đã nhập sau khi chuyển thành chữ in hoa:")
for line in lines:
    print(line.upper())
```
**Kết quả thực thi:**  
![Hình 8: Kết quả thực thi ex02_07.py](report_assets/hinh8_ex02_07.png)  
*Hình 8: Chuyển đổi các dòng văn bản thành chữ in hoa*  
> 📷 **Vị trí chụp ảnh:** Chạy `python lab-01/ex02/ex02_07.py`, nhập các chuỗi và gõ `done`.

---

### Câu 8: Lọc số nhị phân chia hết cho 5 (`ex02_08.py`)
- **Yêu cầu:** Nhập chuỗi các số nhị phân 4 chữ số cách nhau bởi dấu phẩy, lọc các số chia hết cho 5.
- **Mã nguồn:**
```python
def chia_het_cho_5(so_nhi_phan):
    so_thap_phan = int(so_nhi_phan, 2)
    return so_thap_phan % 5 == 0

chuoi_so_nhi_phan = input("Nhập chuỗi số nhị phân (phân tách bởi dấu phẩy): ")
so_nhi_phan_list = chuoi_so_nhi_phan.split(',')
so_chia_het_cho_5 = [so for so in so_nhi_phan_list if chia_het_cho_5(so)]

if len(so_chia_het_cho_5) > 0:
    ket_qua = ','.join(so_chia_het_cho_5)
    print("Các số nhị phân chia hết cho 5 là:", ket_qua)
else:
    print("Không có số nhị phân nào chia hết cho 5 trong chuỗi đã nhập.")
```
**Kết quả thực thi:**  
![Hình 9: Kết quả thực thi ex02_08.py](report_assets/hinh9_ex02_08.png)  
*Hình 9: Kết quả lọc số nhị phân chia hết cho 5*  
> 📷 **Vị trí chụp ảnh:** Chạy `python lab-01/ex02/ex02_08.py`, nhập chuỗi `0100, 0011, 1010, 1001`.

---

### Câu 9: Hàm kiểm tra số nguyên tố (`ex02_09.py`)
- **Yêu cầu:** Viết hàm `kiem_tra_so_nguyen_to(n)` kiểm tra số nguyên tố tối ưu lặp đến $\sqrt{n}$.
- **Mã nguồn:**
```python
def kiem_tra_so_nguyen_to(n):
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
    print(number, "không phải là số nguyên tố.")
```
**Kết quả thực thi:**  
![Hình 10: Kết quả thực thi ex02_09.py](report_assets/hinh10_ex02_09.png)  
*Hình 10: Kiểm tra số nguyên tố đối với 7 và 15*  
> 📷 **Vị trí chụp ảnh:** Chạy `python lab-01/ex02/ex02_09.py` với số 7 và 15.

---

### Câu 10: Hàm đảo ngược chuỗi (`ex02_10.py`)
- **Yêu cầu:** Viết hàm nhận vào chuỗi và trả về chuỗi đảo ngược sử dụng cú pháp slicing `[::-1]`.
- **Mã nguồn:**
```python
def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]

input_string = input("Mời nhập chuỗi cần đảo ngược: ")
print("Chuỗi đảo ngược là:", dao_nguoc_chuoi(input_string))
```
**Kết quả thực thi:**  
![Hình 11: Kết quả thực thi ex02_10.py](report_assets/hinh11_ex02_10.png)  
*Hình 11: Đảo ngược chuỗi ký tự*  
> 📷 **Vị trí chụp ảnh:** Chạy `python lab-01/ex02/ex02_10.py`, nhập chuỗi `hutech university`.

---

## III. CẤU TRÚC DỮ LIỆU LIST, TUPLE, DICTIONARY (THƯ MỤC `lab-01/ex03`)

### Câu 1: Tính tổng các số chẵn trong List (`ex03_01.py`)
- **Mã nguồn:**
```python
def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
tong_chan = tinh_tong_so_chan(numbers)
print("Tổng các số chẵn trong List là:", tong_chan)
```
**Kết quả thực thi:**  
![Hình 12: Kết quả thực thi ex03_01.py](report_assets/hinh12_ex03_01.png)  
*Hình 12: Tính tổng các số chẵn trong danh sách*  
> 📷 **Vị trí chụp:** Chạy `python lab-01/ex03/ex03_01.py`, nhập `1,-2,3,4,5,-6,7,8,-9`.

---

### Câu 2: Đảo ngược vị trí các phần tử trong List (`ex03_02.py`)
- **Mã nguồn:**
```python
def dao_nguoc_list(lst):
    return lst[::-1]

input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
list_dao_nguoc = dao_nguoc_list(numbers)
print("List sau khi đảo ngược:", list_dao_nguoc)
```
**Kết quả thực thi:**  
![Hình 13: Kết quả thực thi ex03_02.py](report_assets/hinh13_ex03_02.png)  
*Hình 13: Đảo ngược các phần tử của List*  
> 📷 **Vị trí chụp:** Chạy `python lab-01/ex03/ex03_02.py`, nhập `1,-2,3,4,5,-6,7,8,-9`.

---

### Câu 3: Tạo một Tuple từ List (`ex03_03.py`)
- **Mã nguồn:**
```python
def tao_tuple_tu_list(lst):
    return tuple(lst)

input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))
my_tuple = tao_tuple_tu_list(numbers)
print("List: ", numbers)
print("Tuple từ List:", my_tuple)
```
**Kết quả thực thi:**  
![Hình 14: Kết quả thực thi ex03_03.py](report_assets/hinh14_ex03_03.png)  
*Hình 14: Tạo Tuple từ List các phần tử đã nhập*  
> 📷 **Vị trí chụp:** Chạy `python lab-01/ex03/ex03_03.py`, nhập `1,-2,3,4,5,-6,7,8,-9`.

---

### Câu 4: Truy cập phần tử đầu tiên và cuối cùng trong Tuple (`ex03_04.py`)
- **Mã nguồn:**
```python
def truy_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element

input_tuple = eval(input("Nhập tuple, ví dụ (1, 2, 3): "))
first, last = truy_cap_phan_tu(input_tuple)
print("Phần tử đầu tiên:", first)
print("Phần tử cuối cùng:", last)
```
**Kết quả thực thi:**  
![Hình 15: Kết quả thực thi ex03_04.py](report_assets/hinh15_ex03_04.png)  
*Hình 15: Lấy phần tử đầu tiên và cuối cùng của Tuple*  
> 📷 **Vị trí chụp:** Chạy `python lab-01/ex03/ex03_04.py`, nhập `(1, -2, 3, 4, -5)`.

---

### Câu 5: Đếm tần suất xuất hiện của từ vào Dictionary (`ex03_05.py`)
- **Mã nguồn:**
```python
def dem_so_lan_xuat_hien(lst):
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
print("Số lần xuất hiện của các phần tử:", so_lan_xuat_hien)
```
**Kết quả thực thi:**  
![Hình 16: Kết quả thực thi ex03_05.py](report_assets/hinh16_ex03_05.png)  
*Hình 16: Thống kê số lần xuất hiện của từ trong Dictionary*  
> 📷 **Vị trí chụp:** Chạy `python lab-01/ex03/ex03_05.py`, nhập các từ cách nhau khoảng trắng.

---

### Câu 6: Xóa phần tử khỏi Dictionary theo khóa (`ex03_06.py`)
- **Mã nguồn:**
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
    print("Phần tử đã được xóa từ Dictionary:", my_dict)
else:
    print("Không tìm thấy phần tử cần xóa trong Dictionary.")
```
**Kết quả thực thi:**  
![Hình 17: Kết quả thực thi ex03_06.py](report_assets/hinh17_ex03_06.png)  
*Hình 17: Xóa phần tử theo key 'b' khỏi Dictionary*  
> 📷 **Vị trí chụp:** Chạy `python lab-01/ex03/ex03_06.py`.

---

## IV. LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG TRONG PYTHON (OOP - THƯ MỤC `lab-01/ex04`)

### 1. Bảng quy tắc phân loại học lực
| Phân loại học lực | Thang điểm trung bình (hệ 10) | Điều kiện kiểm tra logic |
| :--- | :--- | :--- |
| **Loại Giỏi** | Từ 8.0 trở lên | `diemTB >= 8.0` |
| **Loại Khá** | Từ 6.5 đến dưới 8.0 | `6.5 <= diemTB < 8.0` |
| **Loại Trung bình** | Từ 5.0 đến dưới 6.5 | `5.0 <= diemTB < 6.5` |
| **Loại Yếu** | Dưới 5.0 | `diemTB < 5.0` |

### 2. Thiết kế các lớp đối tượng
- **Lớp `SinhVien` (`SinhVien.py`):** Đại diện cho một đối tượng sinh viên với các trường dữ liệu `_id`, `_name`, `_sex`, `_major`, `_diemTB`, `_hocLuc`.
- **Lớp `QuanLySinhVien` (`QuanLySinhVien.py`):** Quản lý tập hợp danh sách đối tượng sinh viên, thực hiện các nghiệp vụ:
  + Tự động tạo mã sinh viên duy nhất `generateID()`.
  + Thêm, sửa thông tin, xóa sinh viên theo ID.
  + Tìm kiếm sinh viên theo từ khóa tên không phân biệt hoa thường.
  + Sắp xếp danh sách theo điểm trung bình hoặc theo chuyên ngành.
  + Hiển thị danh sách sinh viên dưới dạng bảng định dạng căn lề chuẩn.
- **Chương trình điều khiển (`Main.py`):** Vòng lặp giao diện dòng lệnh hiển thị bảng chọn 8 chức năng.

**Kết quả thực thi:**  
![Hình 18: Kết quả chạy Main.py](report_assets/hinh18_ex04_main.png)  
*Hình 18: Giao diện Menu quản lý sinh viên và kết quả hiển thị danh sách dạng bảng*  
> 📷 **Vị trí chụp:** Chạy `python lab-01/ex04/Main.py`, chọn chức năng 1 để thêm sinh viên, sau đó chọn chức năng 7 hiển thị danh sách.

---

## V. ĐƯA DỰ ÁN LÊN GITHUB REPOSITORY

Toàn bộ mã nguồn bài thực hành đã được đóng gói và cam kết lên kho lưu trữ GitHub chính thức:
- **URL Remote:** `https://github.com/khang1233/TH_LTANTT_2387700027.git`
- **Nhánh:** `main`

Các lệnh Git đã thực hiện:
```bash
git init
git branch -M main
git remote add origin https://github.com/khang1233/TH_LTANTT_2387700027.git
git add .
git commit -m "Hoan thanh Lab 01"
git push -u origin main
```

**Kết quả kiểm tra Git:**  
![Hình 19: Trạng thái Git Push](report_assets/hinh19_git_push.png)  
*Hình 19: Trạng thái nhánh Git sạch và hoàn tất đồng bộ lên GitHub*  
> 📷 **Vị trí chụp:** Mở terminal tại thư mục gốc, gõ `git status` và `git remote -v`.

---

## VI. KẾT LUẬN VÀ ĐÁNH GIÁ

1. **Về kết quả:**
   - Hoàn thành đầy đủ 100% các yêu cầu từ bài thực hành số 1 bao gồm phần khởi tạo, các bài tập cơ bản (`ex02`), cấu trúc dữ liệu nâng cao (`ex03`) và ứng dụng hướng đối tượng (`ex04`).
   - Mã nguồn được chuẩn hóa, không lỗi runtime, có sẵn tệp Word `.docx` và Markdown `.md` hoàn chỉnh phục vụ báo cáo.

2. **Kiến thức tiếp thu được:**
   - Nắm vững tư duy phân rã bài toán và cách tổ chức thư mục dự án chuyên nghiệp trong môi trường phát triển phần mềm an toàn thông tin.
   - Hiểu sâu về tính linh hoạt của cấu trúc dữ liệu `List`, `Tuple`, `Dictionary` và sức mạnh của lập trình hướng đối tượng OOP trong việc xây dựng hệ thống quản lý có tính module hóa cao.
