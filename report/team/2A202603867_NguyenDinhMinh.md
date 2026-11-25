# Báo cáo cá nhân — Nguyễn Đình Minh — 2A202603867

## 1. Thông tin thành viên

- Họ tên: Nguyễn Đình Minh
- MSSV: 2A202603867
- Email: nguyenminh25112k4@gmail.com
- Nhóm / lớp: Hihihuhu / L3B
- GitHub / nhánh làm việc: `minhh25` / `minhnd`
- Vai trong nhóm: viết code A–B, kiểm số sau khi bàn giao code cho Hải, tích hợp và rà soát hồ sơ nộp.

## 2. Phần việc phụ trách

- Hoàn thiện A1–A4: xác suất và số lần chạy kỳ vọng, mô hình chi phí từ trace, phân tích theo loại yêu cầu, phân bổ chi phí cố định.
- Hoàn thiện B1–B4: độ nhạy, tác động đồng thời hai yếu tố, giới hạn chạy lại và kịch bản xem lại 100%.
- Bàn giao code cho Hải lập bảng chi phí, tiếp tục D1 và E1; đối chiếu số giữa code, bảng chi phí, kế hoạch pilot và hồ sơ launch.
- Tổng hợp báo cáo nhóm, cập nhật đóng góp trong `TEAM.md` và rà soát yêu cầu của `SUBMISSION.md`.

## 3. Đóng góp cụ thể

- A1 đạt ba phép thử **1,20 · 1,25 · 1,25**. Hàm `mo_hinh` cộng token và tool trên mọi lần chạy, kể cả lỗi; mẫu số chỉ đếm yêu cầu có `ket_qua = thanh_cong`.
- A2 tính được **978** việc thành công, CPS **4.471,97 đ** và chi phí cả hệ thống **5.864,65 đ/yêu cầu** sau khi cộng nhân viên làm thay (simulated, chưa gồm chi phí cố định).
- A3 lọc trace theo `request_id` của từng loại, tính thêm tỉ lệ `status = ok` theo lần thử. `quoc_te` có CPS **22.515 đ = 1,88×** mức 12.000 đ (simulated), hỗ trợ quyết định thu hẹp phạm vi pilot.
- A4 ngoại suy thành công trong phạm vi `noi_dia + hang_nang` trên toàn mẫu: **900/1.200**. Ở 45.000 yêu cầu/tháng, có **33.750** việc thành công; CPS cộng cố định **4.599,09 đ**, tăng lên **5.784,27 đ** khi khối lượng giảm một nửa (simulated).
- B1–B2 tính đủ **9** kịch bản và một cặp: làm lại, xem lại và lương nhân viên là ba yếu tố ảnh hưởng mạnh nhất trong các kịch bản tăng chi phí; cặp token + xem lại cho CPS **6.543,12 đ**, tăng **46,31%** (simulated).
- B3 xác định giới hạn **2 lần chạy** có tổng chi phí thấp nhất **6.901.220,23 đ**, còn **1 lần chạy** có CPS thấp nhất **4.110,99 đ** nhưng chuyển thêm **85** yêu cầu sang nhân viên (simulated cho các chi phí).
- B4 đếm mỗi yêu cầu có run `ok` một lần: **948** lượt xem lại, **48** ca làm lại, **900** việc thành công. CPS là **11.742,79 đ** với 9 phút làm lại/ca và **12.414,79 đ** với 15,3 phút/ca (simulated).
- Rà soát bản tích hợp A–E; hoàn thiện báo cáo và làm rõ kế hoạch pilot về cỡ mẫu hiệu dụng, thời gian theo dõi 7 ngày, luật dừng và trạng thái chưa duyệt chéo.
- Hoàn thiện CP4–CP5 theo slide bổ sung: chênh mở lại +2 điểm chỉ từ bước 10 người, xử lý hoàn trùng/báo hoàn sai ở mọi bước; ngưỡng 8.000 đ dùng CPS biến đổi. Bổ sung code tính số mẫu thô, ngày thu mẫu và chi phí cố định khi mở 4/10/20 người; đồng bộ 13 event, 4 rủi ro và hồ sơ launch. Phần hỏi–đáp và kết quả nhóm khác chấm Hihihuhu tiếp tục ghi chưa thực hiện; đánh giá hồ sơ A90 được ghi riêng trong phiếu chấm.

## 4. Bằng chứng

| Phần việc | Bằng chứng trong repo |
| --- | --- |
| Phân công nhóm | Commit `99971af`, [TEAM.md](../../TEAM.md) |
| Code A1–A4 | Commit `6d98671`, [src/lab13.py](../../src/lab13.py) |
| Code B1–B4 | Commit `43891a3`, các hàm `phan_tich_do_nhay`, `in_phan_b` |
| Kết quả và bàn giao | [bang_chi_phi.md](bang_chi_phi.md); Hải hoàn thiện bảng và code D1/E1 ở `9f0ccd3`, `a8bebf9` |
| Tích hợp hồ sơ | [group_report.md](group_report.md), [ho_so_launch_v0.md](ho_so_launch_v0.md), [pilot_plan.yaml](pilot_plan.yaml) và phần đóng góp thực tế trong `TEAM.md` |
| Hoàn thiện CP4–CP5 | Hàm `phan_tich_co_mau`, `kinh_te_rollout`; mục đo luật dừng và rủi ro tại [chi_so.md](chi_so.md); phiếu chấm phân biệt đánh giá hồ sơ A90 với phần hỏi–đáp chưa diễn ra |

## 5. Công cụ và cách kiểm tra

- Python trong `src/.venv`, pandas để đọc và tổng hợp CSV; Git/GitHub để commit, push và bàn giao từng phần qua PR.
- Chạy `.venv/bin/python lab13.py` trong `src/`: ba phép thử A1 đạt, chương trình in đầy đủ A–B–D–E và kết thúc thành công.
- Đối chiếu A2–A4 và B1–B4 với hướng dẫn, kiểm tra tổng chi phí theo loại bằng toàn mẫu và tác động kết hợp B2 bằng tổng tác động riêng.
- Kiểm tra bằng bộ dữ liệu nhỏ tính tay có lần lỗi, chạy lại và trace ngoài phạm vi; kiểm tra B4 không đếm trùng lượt xem lại và các hàm không sửa dữ liệu đầu vào.
- Đọc `pilot_plan.yaml` bằng `yaml.safe_load`, đối chiếu D1/E1 với code và kiểm tra danh sách file theo `SUBMISSION.md`.

## 6. Tự đánh giá

Hoàn thành phần code A–B và bàn giao số liệu để các thành viên tiếp tục C–E. Bài học chính là phải tính cả thời gian con người và phần việc chuyển nhân viên khi đánh giá hiệu quả kinh tế; việc giảm CPS riêng của agent chưa bảo đảm giảm chi phí công ty.

Đề xuất hiện tại là **Go có điều kiện** cho pilot nội địa và hàng nặng. Số phút vẫn là simulated; mức đồng thuận gắn nhãn ban đầu **60%** và power khoảng **0,64** nếu hiệu ứng thật chỉ +5 điểm là các hạn chế cần nêu rõ. Đã đọc hồ sơ, chạy kiểm tra code A90 tại commit **a7da2b4** và tổng hợp phiếu đề xuất **25/30**, **Go có điều kiện**; chưa nhận trả lời trực tiếp từ A90. Nhóm mình **chưa được nhóm khác chấm**, nên không ghi điểm nhận về hoặc kết quả bảo vệ chưa diễn ra.
