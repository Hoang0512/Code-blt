import json
import os

ten_file = ""

def ghi_file():
    try:
        with open(ten_file, 'w', encoding='utf-8') as f:
            json.dump([
                {
                    "ten": cv["ten"],
                    "gio": int(cv["gio"]) if cv["gio"].is_integer() else cv["gio"],
                    "luong": int(cv["luong"]) if cv["luong"].is_integer() else cv["luong"]
                } for cv in danh_sach_cong_viec
            ], f, ensure_ascii=False, indent=4)
    except Exception as e:
        print("Lỗi khi ghi file:", e)

def them_cong_viec():
    ten = input("Nhập tên công việc: ")
    gio = int(input("Nhập số giờ làm: "))
    luong = int(input("Nhập lương mỗi giờ: "))
    cong_viec = {"ten": ten, "gio": gio, "luong": luong}
    danh_sach_cong_viec.append(cong_viec)
    ghi_file()
    print("Đã thêm công việc.")

def hien_thi_danh_sach():
    if not danh_sach_cong_viec:
        print("Danh sách trống.")
        return
    for i, cv in enumerate(danh_sach_cong_viec, 1):
        print(f"{i}. {cv['ten']} - {cv['gio']} giờ - {cv['luong']} đ/giờ")

def cap_nhat_tt_cong_viec():
    ten = input("Nhập tên công việc cần sửa: ")
    for cv in danh_sach_cong_viec:
        if cv['ten'].lower() == ten.lower():
            cv['ten'] = input("Tên mới: ")
            cv['gio'] = int(input("Giờ mới: "))
            cv['luong'] = int(input("Lương mới: "))
            ghi_file()
            print("Đã cập nhật công việc.")
            return
    print("Không tìm thấy công việc.")

def xoa_cong_viec():
    ten = input("Nhập tên công việc cần xóa: ")
    for cv in danh_sach_cong_viec:
        if cv['ten'].lower() == ten.lower():
            danh_sach_cong_viec.remove(cv)
            ghi_file()
            print("Đã xóa công việc.")
            return
    print("Không tìm thấy công việc.")

def tim_cong_viec():
    ten = input("Nhập tên công việc cần tìm: ")
    for cv in danh_sach_cong_viec:
        if cv['ten'].lower() == ten.lower():
            print(f"Tìm thấy: {cv['ten']} - {cv['gio']} giờ - {cv['luong']} đ/giờ")
            return  
    print("Không tìm thấy công việc.")

def tong_gio_lam():
    tong = sum(cv['gio'] for cv in danh_sach_cong_viec)
    print(f"Tổng số giờ làm: {tong} giờ")

def tong_thu_nhap():
    tong = sum(cv['gio'] * cv['luong'] for cv in danh_sach_cong_viec)
    print(f"Tổng thu nhập: {tong} đồng")

def cong_viec_thu_nhap_cao_nhat():
    if not danh_sach_cong_viec:
        print("Danh sách rỗng.")
        return
    max_cv = max(danh_sach_cong_viec, key=lambda x: x['gio'] * x['luong'])
    thu_nhap = max_cv['gio'] * max_cv['luong']
    print(f"Công việc thu nhập cao nhất: {max_cv['ten']} ({thu_nhap} đ)")

def gio_lam_nhieu_nhat():
    if not danh_sach_cong_viec:
        print("Danh sách công việc trống.")
        return
    max_cv = max(danh_sach_cong_viec, key=lambda x: x['gio'])
    print(f"Công việc làm nhiều giờ nhất: {max_cv['ten']} - {max_cv['gio']} giờ")


def luu_file_json():
    global ten_file
    ten_file = input("Nhập tên file để lưu (.json): ")
    try:
        with open(ten_file, 'w', encoding='utf-8') as f:
            json.dump(danh_sach_cong_viec, f, ensure_ascii=False, indent=4)
        print("Đã lưu dữ liệu vào file JSON.")
    except Exception as e:
        print("Lỗi khi lưu file:", e)

def doc_file_json():
    global ten_file
    ten_file = input("Nhập tên file JSON để đọc: ")
    try:
        with open(ten_file, 'r', encoding='utf-8') as f:
            global danh_sach_cong_viec
            danh_sach_cong_viec = json.load(f)
        print("Đã đọc dữ liệu từ file JSON.")
    except FileNotFoundError:
        print("File không tồn tại.")
    except Exception as e:
        print("Lỗi khi đọc file:", e)

if __name__ == "__main__":
    danh_sach_cong_viec = []
    while True:
        print("\n===== QUẢN LÝ CÔNG VIỆC LÀM THÊM =====")
        print("1. Thêm công việc")
        print("2. Xem danh sách công việc")
        print("3. Cập nhật thông tin công việc")
        print("4. Xóa công việc")
        print("5. Tìm công việc")
        print("6. Tính tổng số giờ làm")
        print("7. Tính tổng thu nhập")
        print("8. Công việc thu nhập cao nhất")
        print("9. Công việc nhiều giờ nhất")
        print("10. Xuất dữ liệu ra file")
        print("11. Đọc dữ liệu từ file")
        print("12. Thoát")

        chon = input("Chọn chức năng (1-12): ")

        if chon == "1":
            them_cong_viec()
        elif chon == "2":
            hien_thi_danh_sach()
        elif chon == "3":
            cap_nhat_tt_cong_viec()
        elif chon == "4":
            xoa_cong_viec()
        elif chon == "5":
            tim_cong_viec()
        elif chon == "6":
            tong_gio_lam()
        elif chon == "7":
            tong_thu_nhap()
        elif chon == "8":
            cong_viec_thu_nhap_cao_nhat()
        elif chon == "9":
            gio_lam_nhieu_nhat()
        elif chon == "10":
            luu_file_json()
        elif chon == "11":
            doc_file_json()
        elif chon == "12":
            print("kết thúc chương trình!")
            break
        else:
            print("Vui lòng chọn từ 1 đến 11.")
