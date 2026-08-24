"""
test_quan_ly_sinh_vien.py
===========================
File kiểm thử (unit test) cho 3 chức năng chính: THÊM, XOÁ, TÌM KIẾM.
Sử dụng module unittest có sẵn của Python (không cần cài thêm thư viện).

Chạy: python -m unittest test_quan_ly_sinh_vien.py -v
"""

import os
import unittest

from quan_ly_sinh_vien import QuanLySinhVien


class TestQuanLySinhVien(unittest.TestCase):
    """Bộ test cho class QuanLySinhVien."""

    def setUp(self):
        """Chạy trước mỗi test: tạo 1 file dữ liệu tạm riêng để không ảnh hưởng dữ liệu thật."""
        self.file_test = "test_data_sinh_vien.json"
        if os.path.exists(self.file_test):
            os.remove(self.file_test)
        self.qlsv = QuanLySinhVien(self.file_test)

    def tearDown(self):
        """Chạy sau mỗi test: xoá file dữ liệu tạm để dọn dẹp môi trường test."""
        if os.path.exists(self.file_test):
            os.remove(self.file_test)

    def test_them_sinh_vien(self):
        """Test case 1: Thêm sinh viên mới thành công; thêm trùng mã sẽ thất bại."""
        ket_qua = self.qlsv.them_sinh_vien("SV001", "Nguyen Van A", "10A1", 8.5)
        self.assertTrue(ket_qua)
        self.assertEqual(len(self.qlsv.lay_tat_ca()), 1)

        # Thêm trùng mã sinh viên -> phải thất bại
        ket_qua_trung = self.qlsv.them_sinh_vien("SV001", "Nguyen Van B", "10A2", 7.0)
        self.assertFalse(ket_qua_trung)
        self.assertEqual(len(self.qlsv.lay_tat_ca()), 1)

    def test_xoa_sinh_vien(self):
        """Test case 2: Xoá sinh viên tồn tại thành công; xoá sinh viên không tồn tại thất bại."""
        self.qlsv.them_sinh_vien("SV002", "Tran Thi B", "11A2", 9.0)
        ket_qua = self.qlsv.xoa_sinh_vien("SV002")
        self.assertTrue(ket_qua)
        self.assertEqual(len(self.qlsv.lay_tat_ca()), 0)

        # Xoá mã không tồn tại -> phải thất bại
        ket_qua_khong_ton_tai = self.qlsv.xoa_sinh_vien("SV999")
        self.assertFalse(ket_qua_khong_ton_tai)

    def test_tim_kiem(self):
        """Test case 3: Tìm kiếm theo mã và theo tên (gần đúng, không phân biệt hoa thường)."""
        self.qlsv.them_sinh_vien("SV003", "Le Van Cuong", "12A3", 6.5)
        self.qlsv.them_sinh_vien("SV004", "Pham Thi Cuc", "12A3", 7.5)

        # Tìm theo 1 phần mã
        ket_qua_ma = self.qlsv.tim_kiem("sv003")
        self.assertEqual(len(ket_qua_ma), 1)
        self.assertEqual(ket_qua_ma[0].ma_sv, "SV003")

        # Tìm theo 1 phần tên, không phân biệt hoa thường (khớp cả 2 SV vì đều chứa "cu")
        ket_qua_ten = self.qlsv.tim_kiem("cu")
        self.assertEqual(len(ket_qua_ten), 2)

        # Tìm từ khoá không khớp -> danh sách rỗng
        ket_qua_rong = self.qlsv.tim_kiem("khongtontai")
        self.assertEqual(len(ket_qua_rong), 0)


if __name__ == "__main__":
    unittest.main()
