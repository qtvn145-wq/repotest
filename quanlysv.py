"""
Chương trình Quản lý Sinh viên
==============================

Module này cung cấp lớp QuanLySinhVien để quản lý danh sách sinh viên
với 3 chức năng chính: THÊM, XOÁ, TÌM KIẾM sinh viên.

Mỗi sinh viên được lưu dưới dạng dictionary gồm các trường:
    - mssv (str): Mã số sinh viên (khóa duy nhất)
    - ten (str): Họ và tên
    - tuoi (int): Tuổi
    - lop (str): Lớp học

Tác giả: Claude
"""


class QuanLySinhVien:
    """
    Lớp quản lý danh sách sinh viên.

    Thuộc tính:
        danh_sach (list[dict]): Danh sách các sinh viên, mỗi sinh viên
            là một dict có dạng {"mssv": ..., "ten": ..., "tuoi": ..., "lop": ...}
    """

    def __init__(self):
        """Khởi tạo danh sách sinh viên rỗng."""
        self.danh_sach = []

    def them_sinh_vien(self, mssv, ten, tuoi, lop):
        """
        Thêm một sinh viên mới vào danh sách.

        Args:
            mssv (str): Mã số sinh viên, phải là duy nhất.
            ten (str): Họ tên sinh viên.
            tuoi (int): Tuổi sinh viên.
            lop (str): Tên lớp học.

        Returns:
            bool: True nếu thêm thành công, False nếu mssv đã tồn tại.

        Ví dụ:
            >>> ql = QuanLySinhVien()
            >>> ql.them_sinh_vien("SV001", "Nguyen Van A", 20, "CNTT1")
            True
        """
        # Kiểm tra trùng mã số sinh viên trước khi thêm
        if self.tim_sinh_vien(mssv) is not None:
            print(f"[LỖI] Mã số sinh viên '{mssv}' đã tồn tại!")
            return False

        sinh_vien = {"mssv": mssv, "ten": ten, "tuoi": tuoi, "lop": lop}
        self.danh_sach.append(sinh_vien)
        print(f"[OK] Đã thêm sinh viên: {ten} ({mssv})")
        return True

    def xoa_sinh_vien(self, mssv):
        """
        Xoá một sinh viên khỏi danh sách dựa theo mã số sinh viên.

        Args:
            mssv (str): Mã số sinh viên cần xoá.

        Returns:
            bool: True nếu xoá thành công, False nếu không tìm thấy.

        Ví dụ:
            >>> ql = QuanLySinhVien()
            >>> ql.them_sinh_vien("SV001", "Nguyen Van A", 20, "CNTT1")
            True
            >>> ql.xoa_sinh_vien("SV001")
            True
        """
        sinh_vien = self.tim_sinh_vien(mssv)
        if sinh_vien is None:
            print(f"[LỖI] Không tìm thấy sinh viên có mã '{mssv}' để xoá!")
            return False

        self.danh_sach.remove(sinh_vien)
        print(f"[OK] Đã xoá sinh viên có mã: {mssv}")
        return True

    def tim_sinh_vien(self, mssv):
        """
        Tìm một sinh viên theo mã số sinh viên (tìm chính xác).

        Args:
            mssv (str): Mã số sinh viên cần tìm.

        Returns:
            dict | None: Thông tin sinh viên nếu tìm thấy, ngược lại None.
        """
        for sv in self.danh_sach:
            if sv["mssv"] == mssv:
                return sv
        return None

    def tim_theo_ten(self, tu_khoa):
        """
        Tìm kiếm sinh viên theo tên (tìm gần đúng, không phân biệt hoa/thường).

        Args:
            tu_khoa (str): Từ khoá xuất hiện trong tên sinh viên.

        Returns:
            list[dict]: Danh sách các sinh viên có tên chứa từ khoá.
        """
        tu_khoa = tu_khoa.lower()
        return [sv for sv in self.danh_sach if tu_khoa in sv["ten"].lower()]

    def hien_thi_tat_ca(self):
        """In toàn bộ danh sách sinh viên hiện có ra màn hình."""
        if not self.danh_sach:
            print("Danh sách sinh viên trống.")
            return
        for sv in self.danh_sach:
            print(f"  - {sv['mssv']} | {sv['ten']} | {sv['tuoi']} tuổi | Lớp {sv['lop']}")


# =========================================================
# PHẦN TEST: 3 test case cho 3 chức năng (thêm, xoá, tìm)
# =========================================================

def test_them_sinh_vien():
    """Test case 1: Kiểm tra chức năng THÊM sinh viên."""
    print("\n=== TEST 1: THÊM SINH VIÊN ===")
    ql = QuanLySinhVien()

    # Thêm thành công
    ket_qua_1 = ql.them_sinh_vien("SV001", "Nguyen Van A", 20, "CNTT1")
    assert ket_qua_1 is True, "Thêm sinh viên mới phải trả về True"
    assert len(ql.danh_sach) == 1, "Danh sách phải có 1 sinh viên"

    # Thêm trùng mssv -> phải thất bại
    ket_qua_2 = ql.them_sinh_vien("SV001", "Tran Thi B", 19, "CNTT2")
    assert ket_qua_2 is False, "Thêm trùng mssv phải trả về False"
    assert len(ql.danh_sach) == 1, "Danh sách vẫn phải chỉ có 1 sinh viên"

    print("=> PASS: Chức năng thêm hoạt động đúng.")


def test_xoa_sinh_vien():
    """Test case 2: Kiểm tra chức năng XOÁ sinh viên."""
    print("\n=== TEST 2: XOÁ SINH VIÊN ===")
    ql = QuanLySinhVien()
    ql.them_sinh_vien("SV001", "Nguyen Van A", 20, "CNTT1")
    ql.them_sinh_vien("SV002", "Tran Thi B", 19, "CNTT2")

    # Xoá sinh viên tồn tại -> thành công
    ket_qua_1 = ql.xoa_sinh_vien("SV001")
    assert ket_qua_1 is True, "Xoá sinh viên tồn tại phải trả về True"
    assert len(ql.danh_sach) == 1, "Danh sách phải còn 1 sinh viên"

    # Xoá sinh viên không tồn tại -> thất bại
    ket_qua_2 = ql.xoa_sinh_vien("SV999")
    assert ket_qua_2 is False, "Xoá sinh viên không tồn tại phải trả về False"

    print("=> PASS: Chức năng xoá hoạt động đúng.")


def test_tim_sinh_vien():
    """Test case 3: Kiểm tra chức năng TÌM KIẾM sinh viên."""
    print("\n=== TEST 3: TÌM SINH VIÊN ===")
    ql = QuanLySinhVien()
    ql.them_sinh_vien("SV001", "Nguyen Van A", 20, "CNTT1")
    ql.them_sinh_vien("SV002", "Nguyen Thi Hoa", 19, "CNTT2")

    # Tìm theo mssv chính xác -> tìm thấy
    ket_qua_1 = ql.tim_sinh_vien("SV001")
    assert ket_qua_1 is not None, "Phải tìm thấy sinh viên SV001"
    assert ket_qua_1["ten"] == "Nguyen Van A"

    # Tìm theo mssv không tồn tại -> None
    ket_qua_2 = ql.tim_sinh_vien("SV999")
    assert ket_qua_2 is None, "Không được tìm thấy sinh viên không tồn tại"

    # Tìm theo tên gần đúng -> tìm ra 2 sinh viên có "Nguyen"
    ket_qua_3 = ql.tim_theo_ten("nguyen")
    assert len(ket_qua_3) == 2, "Phải tìm thấy 2 sinh viên có chứa 'Nguyen'"

    print("=> PASS: Chức năng tìm kiếm hoạt động đúng.")


if __name__ == "__main__":
    test_them_sinh_vien()
    test_xoa_sinh_vien()
    test_tim_sinh_vien()
    print("\n✅ TẤT CẢ TEST CASE ĐỀU PASS!")