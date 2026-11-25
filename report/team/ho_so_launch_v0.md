# Hồ sơ launch v0 — LogiX-VN — Gate 2a

**Hihihuhu · L3B** · Dữ liệu giả lập, 1.200 yêu cầu / 1.624 lần chạy. Đây là đề xuất pilot; **chưa duyệt chéo**. Các số có nhãn simulated sử dụng phút lao động giả lập.

| Mục | Con số chính và bằng chứng | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 978 việc; CPS 4.472 đ, gấp 16,28 lần hoá đơn 274,65 đ/yêu cầu; chưa gồm cố định (simulated). [A2](bang_chi_phi.md) | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Làm lại +51,77%; xem lại +40,70%; lương +23,12% trong các kịch bản tăng chi phí (simulated). [B1–B2](bang_chi_phi.md) | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Phạm vi nội địa + hàng nặng: CPS cộng cố định 4.599 đ ở 45.000 yêu cầu/tháng; nửa khối lượng: 5.784 đ. Toàn mẫu: cả hệ thống 5.865 đ/yêu cầu, gồm nhân viên làm thay, chưa gồm cố định; mức tự làm 12.000 đ (simulated). [A3–A4](bang_chi_phi.md) | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số và event | Chạy thử: chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), mở lại 4,25% (51/1.200); 2 chỉ số đề xuất, 13 event có trace_id, đủ đo các luật dừng. Chưa có đối chứng để suy ra tác động. [Chỉ số](chi_so.md) | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 5 · Lỗi và khắc phục | Đồng thuận ban đầu 12/20 = 60%, dưới mục tiêu 80%; đã viết lại định nghĩa, xử lý 8 ca lệch, đủ 5 cách khắc phục. Giữ hai bộ nhãn gốc; ca 7 và 20 phải sửa trước pilot. [Bảng lỗi](bang_loi.md) | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot | 20 + 20 nhân viên; MDE +6 điểm cần 859 hiệu dụng/nhóm, 299 yêu cầu/người. Rollout 4 → 10 → 20; 5 luật dừng, chênh mở lại +2 điểm chỉ từ 10 người; CPS dừng 8.000 đ chưa gồm cố định; rollback 30 phút. Quyết định dự kiến 20/01/2027 sau đủ mẫu và theo dõi 7 ngày. [Pilot](pilot_plan.yaml) | Giả lập | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Xem lại 100%: CPS 11.743–12.415 đ; 2 lần chạy rẻ nhất cho hệ thống: 6.901.220 đ. Nếu 4 người gánh 40 triệu/tháng, CPS cộng cố định 15.266 đ dù biến đổi chỉ 3.414 đ (simulated); theo dõi ngân sách riêng. [B3–B4](bang_chi_phi.md), [rủi ro](chi_so.md) | Giả lập | PM trợ lý hoàn phí |

**Điều kiện trước và trong pilot** — ngày dưới đây là lịch đề xuất:

- **14/12/2026 — Kỹ sư trưởng agent:** kiểm thử chống hoàn trùng, chỉ báo đã hoàn khi sổ cái trả ok, bật đủ event và kiểm tra lại định nghĩa lỗi.
- **14/12/2026 — Giám đốc vận hành:** ký chấp nhận MDE +6 điểm; nếu hiệu ứng thật +5 điểm, power chỉ khoảng 0,64.
- **22/12/2026 — PM trợ lý hoàn phí:** thay phút simulated bằng phút đo thật sau tuần 1; Trưởng nhóm CSKH kiểm tra kế hoạch giảm xem lại an toàn.
- **20/01/2027 — Giám đốc vận hành:** quyết định sau khi đủ 20 cụm/nhóm, ít nhất 5.980 yêu cầu thô/nhóm với tối thiểu 299/người và đủ theo dõi 7 ngày; thiếu mẫu thì lùi ngày, không kết luận sớm.

**Đề xuất: Go có điều kiện** — chỉ pilot noi_dia + hang_nang theo các điều kiện trên; loại quoc_te và doi_tac.
