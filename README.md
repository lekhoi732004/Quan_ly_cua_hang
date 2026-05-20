## 🏬 Hệ Thống Quản Lý Cửa Hàng (Store Management System)

Dự án này là một ứng dụng Console biên dịch và chạy bằng ngôn ngữ **Python 3**, được thiết kế nhằm mục đích quản lý thông tin dữ liệu của các cửa hàng thương mại. Hệ thống cung cấp đầy đủ các tính năng cốt lõi của một ứng dụng quản lý dữ liệu (CRUD), tích hợp khả năng tính toán tài chính tự động (tính thuế, thực thu) và đồng bộ lưu trữ dữ liệu lâu dài dưới cấu trúc file **CSV**.



## 🚀 Tính Năng Chính

Chương trình hoạt động thông qua giao diện dòng lệnh (CLI - Command Line Interface) trực quan với menu tùy chọn từ 1 đến 8 để người dùng tương tác:

1. **Thêm cửa hàng mới (`1`):** - Cho phép nhập các thông tin: *Mã cửa hàng, Tên cửa hàng, Doanh thu, Vốn đầu tư*.
   - **Tự động áp thuế:** Hệ thống tự động tính toán mức thuế phải nộp dựa trên số vốn đầu tư:
     - Nếu vốn đầu tư $\le$ 50.000.000đ: Thuế suất là **5%**.
     - Nếu vốn đầu tư > 50.000.000đ: Thuế suất là **10%**.
   - **Tự động tính Thực thu:** `Tiền thực thu = Doanh thu - Thuế`.
2. **Xem danh sách cửa hàng (`2`):** Xuất toàn bộ danh sách cửa hàng hiện có trong bộ nhớ tạm ra màn hình dưới dạng bảng căn chỉnh ngay hàng thẳng lối.
3. **Tra cứu cửa hàng (`3`):** Tìm kiếm thông tin chi tiết một cửa hàng cụ thể theo *Mã cửa hàng*. Nếu không tìm thấy, hệ thống sẽ đưa ra thông báo phù hợp.
4. **Xóa cửa hàng (`4`):** Cho phép xóa một cửa hàng khỏi danh sách thông qua hệ thống định danh *Mã cửa hàng*. Quá trình xóa có bước xác nhận lại (`c/C` hoặc `k/K`) để tránh thao tác nhầm lẫn.
5. **Thống kê tài chính (`5`):** Tổng hợp và tính toán toàn bộ dữ liệu trong hệ thống bao gồm: *Tổng doanh thu của tất cả các cửa hàng, Tổng số thuế phải nộp,* và *Tổng số tiền thực thu còn lại*.
6. **Sắp xếp dữ liệu (`6`):** Sắp xếp lại danh sách các cửa hàng dựa trên tiêu chí **Doanh thu** theo thứ tự tăng dần/giảm dần để phục vụ việc tối ưu theo dõi hiệu quả kinh doanh.
7. **Lưu dữ liệu ra file CSV (`7`):** Đồng bộ dữ liệu hiện có từ danh sách tạm thời (List of Dictionaries) ghi đè hoặc tạo mới vào file cơ sở dữ liệu `ds_cua_hang.csv`.
8. **Đọc dữ liệu từ file CSV (`8`):** Khởi tạo dữ liệu ban đầu cho ứng dụng bằng cách đọc và nạp toàn bộ danh sách cửa hàng đã lưu từ file `ds_cua_hang.csv` vào bộ nhớ.

---

## 📁 Cấu Trúc Thư Mục

Để mã nguồn được sạch sẽ và dễ bảo trì, dự án được tổ chức theo cấu trúc mô-đun hóa:

Kết quả chạy mã
SUCCESS

```text
.
├── qlycuahang.py             # File thực thi chính (Main Entry Point), chứa vòng lặp menu điều khiển
├── xu_ly_cua_hang.py         # Thư viện/Mô-đun chứa toàn bộ các hàm xử lý logic và tính toán dữ liệu
└── files/
    └── ds_cua_hang.csv       # File văn bản phẳng (CSV) đóng vai trò làm cơ sở dữ
