# Báo cáo nhóm — Lab 13

## 1. Thông tin nhóm

- Nhóm: **Hihihuhu** · Lớp: **L3B**.
- Thành viên: Nguyễn Đình Minh, Nguyễn Đình Vũ Hải, Đoàn Xuân Duy Bảo, Vũ Tiến Hùng; MSSV và đóng góp tại [TEAM.md](../../TEAM.md).
- Repo: [K5-L3B-DAY13-Hihihuhu-LaunchEconomics](https://github.com/minhh25/K5-L3B-DAY13-Hihihuhu-LaunchEconomics).

## 2. Mục tiêu và cách tiếp cận

Đánh giá trợ lý hoàn phí LogiX-VN từ mẫu giả lập **1.200 yêu cầu / 1.624 lần chạy** và lập hồ sơ xin duyệt pilot Gate 2a. Minh viết code A–B; Hải kiểm số, lập bảng rồi tiếp quản code D1/E1; Bảo và Hùng gắn nhãn lỗi độc lập; Bảo hoàn thiện pilot, chỉ số và event; Hùng hoàn thiện hồ sơ launch. Nhóm bàn giao qua commit/PR, mỗi thời điểm một người giữ code chính.

## 3. Giải pháp

| Nhiệm vụ | Cách làm và bằng chứng |
| --- | --- |
| A · Chi phí | Cộng token, tool của mọi lần chạy và giờ xem lại/làm lại; chia số việc thành công; tách theo loại, cộng cố định — [code](../../src/lab13.py), [bảng A](bang_chi_phi.md). |
| B · Độ nhạy | 9 kịch bản, một cặp yếu tố, giới hạn 1–3 lần chạy, xem lại 100%; tính phần nhân viên làm thay — [bảng B](bang_chi_phi.md). |
| C · Lỗi | Giữ hai bộ nhãn gốc, tính đồng thuận; viết lại định nghĩa và quy tắc cho 8 ca lệch; 5 cách khắc phục — [bảng lỗi](bang_loi.md). |
| D · Pilot | Tính đủ 5 câu D1 và trả lời 5 câu D2; chọn 20 + 20 nhân viên, MDE +6 điểm; 5 luật dừng theo bước rollout và rollback — [pilot](pilot_plan.yaml). |
| E · Hồ sơ | 3 chỉ số tính thử, 2 chỉ số đề xuất, 13 event nối qua trace_id, 4 rủi ro kinh tế; hồ sơ 7 mục — [chỉ số](chi_so.md), [launch v0](ho_so_launch_v0.md). |

## 4. Kết quả

- CPS toàn mẫu **4.472 đ**; cả hệ thống **5.865 đ/yêu cầu**, gồm nhân viên làm thay và chưa gồm cố định (simulated). Phạm vi nội địa + hàng nặng có CPS cộng cố định **4.599 đ** ở quy mô 45.000 yêu cầu/tháng (simulated).
- Ba yếu tố tăng chi phí mạnh nhất: làm lại **+51,77%**, xem lại **+40,70%**, lương **+23,12%** (simulated). Giới hạn **2 lần chạy** cho tổng hệ thống thấp nhất **6.901.220 đ** (simulated).
- Chỉ số chạy thử: chính **82,83% (994/1.200)**, bỏ qua gợi ý **27,12% (48/177)**, mở lại **4,25% (51/1.200)**. Chưa có đối chứng để kết luận tác động.
- Đề xuất: **Go có điều kiện** cho nội địa + hàng nặng; phải sửa lỗi hoàn trùng/sổ cái, bật event, đo phút thực tế và chấp nhận đánh đổi cỡ mẫu trước khi chạy.
- Đã kiểm tra hồ sơ/code **A90** tại **a7da2b4** và nhận phản hồi bằng văn bản. Câu trả lời giải quyết mốc theo dõi, năng lực tải và nguồn luật dừng; đang chờ commit đồng bộ từ A90 sau khi kiểm tra lại nhánh main. [Phiếu chấm](phieu_cham.md) tạm giữ **25/30**, **Go có điều kiện**; xem xét nâng lên 30/30 sau khi xác minh bản sửa.
- **Chưa có phiếu nhóm khác chấm Hihihuhu**; không dùng 25/30 chấm A90 làm điểm nhóm mình nhận được. Đề xuất launch của Hihihuhu chưa phải phê duyệt của hội đồng.

## 5. Khó khăn và cách xử lý

- Đồng thuận ban đầu **12/20 = 60%**, dưới mục tiêu 80%: giữ nguyên hai bộ nhãn, viết lại định nghĩa và quy tắc phân biệt; không thay kết quả ban đầu bằng nhãn thống nhất.
- Với 20 nhân viên/nhóm, cỡ mẫu hiệu dụng dưới **1.000**, không đủ phát hiện +5 điểm cần **1.251**. Chọn +6 điểm cần **859** hiệu dụng, tương ứng tối thiểu **299 yêu cầu/người**; power còn **0,64** nếu hiệu ứng thật chỉ +5 điểm.
- Xem lại 100% cho CPS **11.743–12.415 đ** (simulated): bổ sung độ nhạy theo phút làm lại và kế hoạch giảm xem lại có kiểm soát. Lịch pilot dành đủ cửa sổ theo dõi mở lại 7 ngày.
- Theo slide bổ sung D1/D3, chênh mở lại **+2 điểm** chỉ dùng từ bước **10 người**; hoàn trùng/báo hoàn sai và trần **6%** áp dụng mọi bước khi đủ dữ liệu. Ngưỡng **8.000 đ** chỉ tính CPS biến đổi; 4 người gánh toàn bộ cố định cho CPS cộng cố định **15.266 đ** (simulated) được xem xét riêng về ngân sách.

## 6. Tổng hợp đóng góp

Minh: code A–B, kiểm tra tích hợp, tổng hợp báo cáo. Hải: bảng A–B, code D1/E1. Bảo: bảng lỗi, pilot và chỉ số/event. Hùng: nhãn độc lập, hồ sơ launch và khung báo cáo/phiếu chấm. Bằng chứng commit và báo cáo của 4 thành viên nằm trong [TEAM.md](../../TEAM.md).

## 7. Hạn chế và hướng cải thiện

Dữ liệu và phút lao động là giả lập; cần đo thật trước khi chốt hiệu quả kinh tế. Pilot phải đủ mẫu ở 20 cụm mỗi nhánh và đủ thời gian theo dõi. Hải đã xác nhận chạy bản main `359e5c6` trên máy thứ hai, đủ bảng A–B–D1–E1–E2 và YAML hợp lệ, trong báo cáo cá nhân cập nhật ở commit `d4ec91e`. Mỗi thành viên tự nộp link repo trên LMS trước **23h59 GMT+7 ngày lab**; nhóm chưa có bằng chứng hoàn tất bước này.

## 8. Tài liệu tham khảo

- [Dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md), [hướng dẫn A–E](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md), [rubric](../../RUBRIC.md), [yêu cầu nộp](../../SUBMISSION.md).
- Đề gốc docs/Ngay13_Lab13_De_bai_hoc_vien.docx: 20 ca lỗi và khung pilot; slide Ngày 13: Cost-of-Pass, Google PAIR và thiết kế thử nghiệm.
- Slide bổ sung `slide-d1-ba-cach-chia.html`: ba cách phân nhóm, thời gian thu mẫu, luật dừng theo bước và phân biệt CPS biến đổi với cố định.
