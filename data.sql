CREATE DATABASE crud_mysql;
USE crud_mysql;

CREATE TABLE khachhang (
    MaKhachHang INT AUTO_INCREMENT PRIMARY KEY,
    TenKhachHang VARCHAR(100),
    SoDienThoai VARCHAR(20)
);

INSERT INTO khachhang (TenKhachHang, SoDienThoai) VALUES 
('Nguyễn Văn A', '0987654321'),
('Trần Thị B', '0912345678'),
('Lê Văn C', '0901122334'),
('Phạm Thị D', '0977554433'),
('Hoàng Văn E', '0933221100');
