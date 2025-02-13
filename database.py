import pymysql

class Database:
    def __init__(self):
        """Kết nối đến MySQL"""
        self.conn = pymysql.connect(
            host="localhost",
            port=3307,
            user="developer",
            password="",
            database="crud_mysql"
        )
        self.cursor = self.conn.cursor()

    def fetch_all_customers(self):
        """Lấy tất cả khách hàng"""
        self.cursor.execute("SELECT * FROM khachhang")
        return self.cursor.fetchall()

    def add_customer(self, ten_kh, so_dt):
        """Thêm khách hàng mới"""
        self.cursor.execute("INSERT INTO khachhang (TenKhachHang, SoDienThoai) VALUES (%s, %s)", (ten_kh, so_dt))
        self.conn.commit()

    def update_customer(self, ma_kh, ten_kh, so_dt):
        """Cập nhật khách hàng"""
        self.cursor.execute("UPDATE khachhang SET TenKhachHang=%s, SoDienThoai=%s WHERE MaKhachHang=%s",
                            (ten_kh, so_dt, ma_kh))
        self.conn.commit()

    def delete_customer(self, ma_kh):
        """Xóa khách hàng"""
        self.cursor.execute("DELETE FROM khachhang WHERE MaKhachHang=%s", (ma_kh,))
        self.conn.commit()

    def close_connection(self):
        """Đóng kết nối MySQL"""
        self.cursor.close()
        self.conn.close()
