import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from giaodien import Ui_Form  # Import giao diện từ file test.py
from database import Database  # Import lớp kết nối MySQL

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.uic = Ui_Form()
        self.uic.setupUi(self)

        # Khởi tạo Database
        self.db = Database()

        # Load dữ liệu vào TableWidget
        self.load_data()

        # Gán sự kiện cho các nút
        self.uic.btnThem.clicked.connect(self.add_customer)
        self.uic.btnSua.clicked.connect(self.update_customer)
        self.uic.btnXoa.clicked.connect(self.delete_customer)
        self.uic.tableWidget.itemSelectionChanged.connect(self.select_row)

        # Biến lưu MaKhachHang của hàng đang chọn
        self.selected_customer_id = None

    def load_data(self):
        """Load dữ liệu từ MySQL vào TableWidget."""
        rows = self.db.fetch_all_customers()
        self.uic.tableWidget.setRowCount(len(rows))
        self.uic.tableWidget.setColumnCount(3)
        self.uic.tableWidget.setHorizontalHeaderLabels(["Mã KH", "Tên KH", "Số ĐT"])

        for row_idx, row_data in enumerate(rows):
            for col_idx, col_data in enumerate(row_data):
                self.uic.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

    def select_row(self):
        """Lấy dữ liệu của hàng được chọn và hiển thị vào các ô nhập."""
        selected_row = self.uic.tableWidget.currentRow()
        if selected_row != -1:
            self.selected_customer_id = self.uic.tableWidget.item(selected_row, 0).text()
            self.uic.txtTenKhachHang.setText(self.uic.tableWidget.item(selected_row, 1).text())
            self.uic.txtSoDienThoai.setText(self.uic.tableWidget.item(selected_row, 2).text())

    def add_customer(self):
        """Thêm khách hàng mới vào MySQL."""
        ten_kh = self.uic.txtTenKhachHang.text()
        so_dt = self.uic.txtSoDienThoai.text()

        if ten_kh and so_dt:
            try:
                self.db.add_customer(ten_kh, so_dt)
                QMessageBox.information(self, "Thành công", "Thêm khách hàng thành công!")
                self.load_data()
            except Exception as e:
                QMessageBox.warning(self, "Lỗi", f"Lỗi khi thêm khách hàng: {e}")
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")

    def update_customer(self):
        """Cập nhật thông tin khách hàng."""
        if self.selected_customer_id:
            ten_kh = self.uic.txtTenKhachHang.text()
            so_dt = self.uic.txtSoDienThoai.text()

            if ten_kh and so_dt:
                try:
                    self.db.update_customer(self.selected_customer_id, ten_kh, so_dt)
                    QMessageBox.information(self, "Thành công", "Cập nhật khách hàng thành công!")
                    self.load_data()
                except Exception as e:
                    QMessageBox.warning(self, "Lỗi", f"Lỗi khi cập nhật khách hàng: {e}")
            else:
                QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin!")
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn khách hàng để cập nhật!")

    def delete_customer(self):
        """Xóa khách hàng."""
        if self.selected_customer_id:
            try:
                self.db.delete_customer(self.selected_customer_id)
                QMessageBox.information(self, "Thành công", "Xóa khách hàng thành công!")
                self.load_data()
                self.selected_customer_id = None
                self.uic.txtTenKhachHang.clear()
                self.uic.txtSoDienThoai.clear()
            except Exception as e:
                QMessageBox.warning(self, "Lỗi", f"Lỗi khi xóa khách hàng: {e}")
        else:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn khách hàng để xóa!")

    def closeEvent(self, event):
        """Đóng kết nối MySQL khi đóng ứng dụng."""
        self.db.close_connection()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = Main()
    main_win.show()
    sys.exit(app.exec())
