"""
giao_dien_tra_cuu.py
======================
Giao diện dòng lệnh (CLI) DÀNH CHO NGƯỜI DÙNG THƯỜNG.
Chỉ có 2 chức năng: TÌM KIẾM và XEM DANH SÁCH sinh viên
(không có quyền THÊM hay XOÁ, để tách biệt quyền hạn với quản trị viên).

Chạy: python giao_dien_tra_cuu.py
"""

from quan_ly_sinh_vien import QuanLySinhVien


def in_danh_sach(danh_sach):
    """In danh sách sinh viên ra màn hình dạng bảng."""
    if not danh_sach:
        print(">> Không tìm thấy sinh viên nào.")
        return
    print(f"{'Mã SV':<10}{'Họ tên':<25}{'Lớp':<10}{'Điểm TB':<6}")
    print("-" * 55)
    for sv in danh_sach:
        print(sv)


def menu():
    """Hiển thị menu tra cứu và xử lý lựa chọn của người dùng."""
    qlsv = QuanLySinhVien()

    while True:
        print("\n===== TRA CỨU SINH VIÊN =====")
        print("1. Tìm kiếm sinh viên")
        print("2. Xem toàn bộ danh sách")
        print("0. Thoát")
        lua_chon = input("Chọn chức năng: ").strip()

        if lua_chon == "1":
            tu_khoa = input("Nhập mã SV hoặc tên cần tìm: ").strip()
            in_danh_sach(qlsv.tim_kiem(tu_khoa))
        elif lua_chon == "2":
            in_danh_sach(qlsv.lay_tat_ca())
        elif lua_chon == "0":
            print("Tạm biệt!")
            break
        else:
            print(">> Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    menu()
