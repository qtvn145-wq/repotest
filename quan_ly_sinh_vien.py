"""
Module quan_ly_sinh_vien.py
============================
File này đóng vai trò là "tầng dữ liệu" (data layer) của chương trình quản lý sinh viên.

Chứa:
    - Class SinhVien: đại diện cho 1 sinh viên.
    - Class QuanLySinhVien: quản lý danh sách sinh viên, đọc/ghi dữ liệu ra file JSON,
      và cung cấp các chức năng nghiệp vụ: THÊM, XOÁ, TÌM KIẾM, LẤY TOÀN BỘ DANH SÁCH.

File dữ liệu mặc định: data_sinh_vien.json (tự động tạo nếu chưa tồn tại).
Hai file giao diện (giao_dien_quan_tri.py và giao_dien_tra_cuu.py) đều import
và sử dụng lại module này để đảm bảo logic xử lý dữ liệu chỉ có 1 nơi duy nhất.
"""

import json
import os


class SinhVien:
    """Đại diện cho một sinh viên với các thuộc tính cơ bản."""

    def __init__(self, ma_sv, ho_ten, lop, diem_tb=0.0):
        """
        Khởi tạo đối tượng SinhVien.

        Args:
            ma_sv (str): Mã sinh viên, duy nhất.
            ho_ten (str): Họ và tên sinh viên.
            lop (str): Lớp học.
            diem_tb (float): Điểm trung bình (mặc định 0.0).
        """
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten
        self.lop = lop
        self.diem_tb = diem_tb

    def to_dict(self):
        """Chuyển đối tượng SinhVien thành dict để lưu vào JSON."""
        return {
            "ma_sv": self.ma_sv,
            "ho_ten": self.ho_ten,
            "lop": self.lop,
            "diem_tb": self.diem_tb,
        }

    @staticmethod
    def from_dict(d):
        """Tạo đối tượng SinhVien từ dict (đọc từ JSON)."""
        return SinhVien(d["ma_sv"], d["ho_ten"], d["lop"], d.get("diem_tb", 0.0))

    def __str__(self):
        return f"{self.ma_sv:<10}{self.ho_ten:<25}{self.lop:<10}{self.diem_tb:<6}"


class QuanLySinhVien:
    """
    Class quản lý toàn bộ nghiệp vụ liên quan tới sinh viên:
    thêm, xoá, tìm kiếm, lấy danh sách và lưu/đọc file dữ liệu JSON.
    """

    def __init__(self, duong_dan_file="data_sinh_vien.json"):
        """
        Args:
            duong_dan_file (str): Đường dẫn tới file JSON lưu dữ liệu sinh viên.
        """
        self.duong_dan_file = duong_dan_file
        self.danh_sach = []
        self.doc_du_lieu()

    def doc_du_lieu(self):
        """Đọc dữ liệu sinh viên từ file JSON vào bộ nhớ (self.danh_sach)."""
        if os.path.exists(self.duong_dan_file):
            with open(self.duong_dan_file, "r", encoding="utf-8") as f:
                try:
                    du_lieu = json.load(f)
                except json.JSONDecodeError:
                    du_lieu = []
            self.danh_sach = [SinhVien.from_dict(d) for d in du_lieu]
        else:
            self.danh_sach = []

    def ghi_du_lieu(self):
        """Ghi dữ liệu sinh viên hiện tại trong bộ nhớ xuống file JSON."""
        with open(self.duong_dan_file, "w", encoding="utf-8") as f:
            json.dump([sv.to_dict() for sv in self.danh_sach], f, ensure_ascii=False, indent=2)

    def them_sinh_vien(self, ma_sv, ho_ten, lop, diem_tb=0.0):
        """
        Thêm 1 sinh viên mới vào danh sách.

        Args:
            ma_sv (str): Mã sinh viên (phải duy nhất).
            ho_ten (str): Họ tên.
            lop (str): Lớp.
            diem_tb (float): Điểm trung bình.

        Returns:
            bool: True nếu thêm thành công, False nếu mã sinh viên đã tồn tại.
        """
        if self.tim_theo_ma(ma_sv) is not None:
            return False
        sv = SinhVien(ma_sv, ho_ten, lop, diem_tb)
        self.danh_sach.append(sv)
        self.ghi_du_lieu()
        return True

    def xoa_sinh_vien(self, ma_sv):
        """
        Xoá sinh viên theo mã số.

        Args:
            ma_sv (str): Mã sinh viên cần xoá.

        Returns:
            bool: True nếu xoá thành công, False nếu không tìm thấy.
        """
        sv = self.tim_theo_ma(ma_sv)
        if sv is None:
            return False
        self.danh_sach.remove(sv)
        self.ghi_du_lieu()
        return True

    def tim_theo_ma(self, ma_sv):
        """Tìm 1 sinh viên chính xác theo mã số. Trả về đối tượng SinhVien hoặc None."""
        for sv in self.danh_sach:
            if sv.ma_sv == ma_sv:
                return sv
        return None

    def tim_kiem(self, tu_khoa):
        """
        Tìm kiếm sinh viên theo mã số HOẶC họ tên (không phân biệt hoa thường, tìm gần đúng).

        Args:
            tu_khoa (str): Từ khoá tìm kiếm.

        Returns:
            list[SinhVien]: Danh sách sinh viên khớp với từ khoá.
        """
        tu_khoa = tu_khoa.strip().lower()
        ket_qua = [
            sv for sv in self.danh_sach
            if tu_khoa in sv.ma_sv.lower() or tu_khoa in sv.ho_ten.lower()
        ]
        return ket_qua

    def lay_tat_ca(self):
        """Trả về toàn bộ danh sách sinh viên hiện có."""
        return self.danh_sach
