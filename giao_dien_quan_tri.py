"""
giao_dien_quan_tri.py
======================
Giao diện dòng lệnh (CLI) DÀNH CHO QUẢN TRỊ VIÊN.
Cung cấp đầy đủ chức năng: THÊM, XOÁ, TÌM KIẾM, XEM DANH SÁCH sinh viên.

Chạy: python giao_dien_quan_tri.py
"""

from quan_ly_sinh_vien import QuanLySinhVien


def in_danh_sach(danh_sach):
    """In danh sách sinh viên ra màn hình dạng bảng."""
    if not danh_sach:
        print(">> Không có sinh viên nào.")
        return
    print(f"{'Mã SV':<10}{'Họ tên':<25}{'Lớp':<10}{'Điểm TB':<6}")
    print("-" * 55)
    for sv in danh_sach:
        print(sv)


def menu():
    """Hiển thị menu chính và xử lý lựa chọn của người dùng."""
    qlsv = QuanLySinhVien()

    while True:
        print("\n===== QUẢN LÝ SINH VIÊN (ADMIN) =====")
        print("1. Thêm sinh viên")
        print("2. Xoá sinh viên")
        print("3. Tìm kiếm sinh viên")
        print("4. Xem toàn bộ danh sách")
        print("0. Thoát")
        lua_chon = input("Chọn chức năng: ").strip()

        if lua_chon == "1":
            ma_sv = input("Mã SV: ").strip()
            ho_ten = input("Họ tên: ").strip()
            lop = input("Lớp: ").strip()
            try:
                diem_tb = float(input("Điểm TB: ").strip() or 0)
            except ValueError:
                diem_tb = 0.0
            if qlsv.them_sinh_vien(ma_sv, ho_ten, lop, diem_tb):
                print(">> Thêm thành công!")
            else:
                print(">> Mã SV đã tồn tại, thêm thất bại.")

        elif lua_chon == "2":
            ma_sv = input("Nhập mã SV cần xoá: ").strip()
            if qlsv.xoa_sinh_vien(ma_sv):
                print(">> Xoá thành công!")
            else:
                print(">> Không tìm thấy sinh viên.")

        elif lua_chon == "3":
            tu_khoa = input("Nhập mã SV hoặc tên cần tìm: ").strip()
            in_danh_sach(qlsv.tim_kiem(tu_khoa))

        elif lua_chon == "4":
            in_danh_sach(qlsv.lay_tat_ca())

        elif lua_chon == "0":
            print("Tạm biệt!")
            break
        else:
            print(">> Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    menu()
