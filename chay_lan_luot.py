import os
import sys
import subprocess

# Thiet lap Windows Console Code Page sang UTF-8 bang Win32 API
if sys.platform == 'win32':
    try:
        import ctypes
        ctypes.windll.kernel32.SetConsoleOutputCP(65001)
        ctypes.windll.kernel32.SetConsoleCP(65001)
    except Exception:
        pass

try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stdin.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

tasks = [
    {
        "id": "HINH 1",
        "name": "lab-01/hello.py (Chuong trinh dau tien)",
        "file": "lab-01/hello.py",
        "inputs": None,
        "note": "In loi chao va thong tin sinh vien"
    },
    {
        "id": "HINH 2",
        "name": "lab-01/ex02/ex02_01.py (Nhap ho ten va tuoi)",
        "file": "lab-01/ex02/ex02_01.py",
        "inputs": "Phuoc Nguyen\n26\n",
        "note": "Nhap ten: Phuoc Nguyen | Tuoi: 26"
    },
    {
        "id": "HINH 3",
        "name": "lab-01/ex02/ex02_02.py (Tinh dien tich hinh tron)",
        "file": "lab-01/ex02/ex02_02.py",
        "inputs": "5.7\n",
        "note": "Nhap ban kinh: 5.7"
    },
    {
        "id": "HINH 4",
        "name": "lab-01/ex02/ex02_03.py (Kiem tra so chan le)",
        "file": "lab-01/ex02/ex02_03.py",
        "inputs": "10\n",
        "note": "Nhap so nguyen: 10 (chan)"
    },
    {
        "id": "HINH 5",
        "name": "lab-01/ex02/ex02_04.py (So chia het cho 7 khong chia het cho 5)",
        "file": "lab-01/ex02/ex02_04.py",
        "inputs": None,
        "note": "Tu dong duyet tu 2000 den 3200 va in ket qua"
    },
    {
        "id": "HINH 6",
        "name": "lab-01/ex02/ex02_05.py (Tinh luong nhan vien)",
        "file": "lab-01/ex02/ex02_05.py",
        "inputs": "76.5\n150000\n",
        "note": "Nhap gio lam: 76.5 | Thu lao: 150000"
    },
    {
        "id": "HINH 7",
        "name": "lab-01/ex02/ex02_06.py (Tao mang 2 chieu X x Y)",
        "file": "lab-01/ex02/ex02_06.py",
        "inputs": "3, 5\n",
        "note": "Nhap X, Y: 3, 5"
    },
    {
        "id": "HINH 8",
        "name": "lab-01/ex02/ex02_07.py (Chuyen chuoi thanh in hoa)",
        "file": "lab-01/ex02/ex02_07.py",
        "inputs": "hutech university\nthuc hanh an toan thong tin\nlap trinh bang ngon ngu python\ndone\n",
        "note": "Nhap cac chuoi va ket thuc bang 'done'"
    },
    {
        "id": "HINH 9",
        "name": "lab-01/ex02/ex02_08.py (So nhi phan chia het cho 5)",
        "file": "lab-01/ex02/ex02_08.py",
        "inputs": "0100, 0011, 1010, 1001\n",
        "note": "Nhap: 0100, 0011, 1010, 1001"
    },
    {
        "id": "HINH 10",
        "name": "lab-01/ex02/ex02_09.py (Kiem tra so nguyen to)",
        "file": "lab-01/ex02/ex02_09.py",
        "inputs": "7\n",
        "note": "Nhap so: 7 (nguyen to)"
    },
    {
        "id": "HINH 11",
        "name": "lab-01/ex02/ex02_10.py (Dao nguoc chuoi)",
        "file": "lab-01/ex02/ex02_10.py",
        "inputs": "hutech university\n",
        "note": "Nhap chuoi: hutech university"
    },
    {
        "id": "HINH 12",
        "name": "lab-01/ex03/ex03_01.py (Tong so chan trong List)",
        "file": "lab-01/ex03/ex03_01.py",
        "inputs": "1,-2,3,4,5,-6,7,8,-9\n",
        "note": "Nhap list: 1,-2,3,4,5,-6,7,8,-9"
    },
    {
        "id": "HINH 13",
        "name": "lab-01/ex03/ex03_02.py (Dao nguoc List)",
        "file": "lab-01/ex03/ex03_02.py",
        "inputs": "1,-2,3,4,5,-6,7,8,-9\n",
        "note": "Nhap list: 1,-2,3,4,5,-6,7,8,-9"
    },
    {
        "id": "HINH 14",
        "name": "lab-01/ex03/ex03_03.py (Tao Tuple tu List)",
        "file": "lab-01/ex03/ex03_03.py",
        "inputs": "1,-2,3,4,5,-6,7,8,-9\n",
        "note": "Nhap list: 1,-2,3,4,5,-6,7,8,-9"
    },
    {
        "id": "HINH 15",
        "name": "lab-01/ex03/ex03_04.py (Truy cap phan tu dau va cuoi Tuple)",
        "file": "lab-01/ex03/ex03_04.py",
        "inputs": "(1, -2, 3, 4, -5)\n",
        "note": "Nhap tuple: (1, -2, 3, 4, -5)"
    },
    {
        "id": "HINH 16",
        "name": "lab-01/ex03/ex03_05.py (Dem tan suat tu vao Dictionary)",
        "file": "lab-01/ex03/ex03_05.py",
        "inputs": "hutech khoa cong nghe thong tin bao mat thong tin\n",
        "note": "Nhap tu: hutech khoa cong nghe thong tin bao mat thong tin"
    },
    {
        "id": "HINH 17",
        "name": "lab-01/ex03/ex03_06.py (Xoa phan tu Dictionary theo key)",
        "file": "lab-01/ex03/ex03_06.py",
        "inputs": None,
        "note": "Xoa key 'b' khoi dictionary co san"
    },
    {
        "id": "HINH 18",
        "name": "lab-01/ex04/Main.py (Quan ly sinh vien OOP)",
        "file": "lab-01/ex04/Main.py",
        "inputs": "1\nPhuoc Nguyen\nNam\nCNTT\n8.5\n7\n0\n",
        "note": "Thao tac: Chon 1 them SV -> Chon 7 hien thi danh sach -> Chon 0 thoat"
    }
]

def main():
    print("=" * 70)
    print("     CHAY LAN LUOT TUNG BAI DE CHUP ANH BAO CAO (LAB 01)")
    print("=" * 70)
    print("Chon che do:")
    print("  [1] TU DONG nap san input mau (Nhanh nhat - chay xong dung cho chup)")
    print("  [2] TU NHAP bang tay tu ban phim")
    print("=" * 70)
    
    choice = input("Nhap lua chon (1 hoac 2, mac dinh la 1): ").strip()
    auto_mode = (choice != '2')
    
    total = len(tasks)
    for idx, t in enumerate(tasks, start=1):
        print("\n" + "=" * 75)
        print(f"  >>> [{t['id']}] ({idx}/{total}): {t['name']}")
        print(f"  >>> Goi y test: {t['note']}")
        print("=" * 75)

        env = os.environ.copy()
        env['PYTHONIOENCODING'] = 'utf-8'

        cmd_display = f"PS {os.getcwd()}> python {t['file']}"
        print(cmd_display)

        if auto_mode and t['inputs'] is not None:
            proc = subprocess.run(
                [sys.executable, t['file']],
                input=t['inputs'],
                text=True,
                capture_output=True,
                env=env
            )
            if proc.stdout:
                print(proc.stdout.strip())
            if proc.stderr:
                print(proc.stderr.strip())
        else:
            subprocess.run([sys.executable, t['file']], env=env)

        print("-" * 75)
        print(f">>> [CHUP ANH BAY GIO]: Nhan Win + Shift + S de chup vung Terminal tren")
        print(f">>> Tuong ung voi: {t['id']} trong file BaoCao_ThucHanh_Lab01.docx")
        print("-" * 75)
        
        if idx < total:
            cont = input(f"\nNhan [ENTER] de sang bai tiep theo ({idx+1}/{total}) hoac go 'q' de dung: ")
            if cont.strip().lower() == 'q':
                print("Da dung chuong trinh.")
                break
        else:
            print("\nDA HOAN THANH TAT CA CAC BAI THUC HANH!")

if __name__ == '__main__':
    main()
