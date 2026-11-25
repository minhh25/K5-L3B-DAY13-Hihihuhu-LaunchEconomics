# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: Hihihuhu
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Lab 13 yêu cầu dựng hồ sơ launch v0 cho trợ lý hoàn phí của LogiX-VN (dữ liệu giả lập: 1.200 yêu cầu, 1.624 lần chạy của agent) và bảo vệ trước hội đồng Gate 2a. Nhóm trả lời bốn câu: có đáng chạy không (chi phí mỗi việc thành công), nhân viên có dùng không (chỉ số sử dụng), khi hỏng thì sao (bảng lỗi), và pilot thiết kế thế nào để ra được quyết định (đối chứng, cỡ mẫu, luật dừng).

Cách làm: bốn người chia vai theo `TEAM.md` (viết code, kiểm số, hai người gắn nhãn). Mỗi người làm trên nhánh riêng (`minhnd`, `haindv`, `baodxd`, `hungvt`) và gộp vào `main` qua Pull Request (PR #1–#8). Tại một thời điểm chỉ một người sửa `src/lab13.py`: Minh viết A–B trước giải lao, Hải tiếp quản sau giải lao. Mọi con số trong hồ sơ lấy từ `src/lab13.py`; người nhận bàn giao chạy lại và đối chiếu trước khi dùng. Hai người gắn nhãn (Bảo, Hùng) làm độc lập trong CP3 rồi mới so.

## 3. Giải pháp

| Nhiệm vụ | Cách nhóm làm | File |
| --- | --- | --- |
| A · Chi phí mỗi việc thành công | Cộng token, tool, xem lại, làm lại của mọi lần chạy (kể cả lần lỗi), chia cho số yêu cầu thành công; tách theo 4 loại yêu cầu; cộng chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang` | `src/lab13.py`, `report/team/bang_chi_phi.md` |
| B · Bảng độ nhạy | 9 kịch bản đổi từng yếu tố, một cặp yếu tố, so giới hạn chạy lại 1/2/3 lần, kịch bản xem lại 100% | `report/team/bang_chi_phi.md` |
| C · Bảng lỗi và cách khắc phục | Hai người gắn nhãn độc lập 20 ca theo 5 loại Google PAIR; so nhãn, viết lại định nghĩa vì đồng thuận dưới 80%; chọn 5 ca, mỗi loại một ca, kèm cách phát hiện đo được và người phụ trách | `report/team/bang_loi.md`, `report/team/nhan_doc_lap_hung.md` |
| D · Kế hoạch pilot | Tính cỡ mẫu theo yêu cầu, theo nhân viên, theo depot; chọn chia theo nhân viên 20 + 20 với mức chênh +6 điểm; viết rollout, 3 luật dừng và rollback | `src/lab13.py`, `report/team/pilot_plan.yaml` |
| E · Chỉ số, rủi ro, hồ sơ launch | 3 chỉ số tính thử, 2 chỉ số đề xuất, 10 event có `trace_id`, 3 rủi ro kinh tế; tổng hợp hồ sơ một trang 7 mục | `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md` |

## 4. Kết quả

Số tính từ cột `_simulated` ghi nhãn *simulated*.

- Chi phí mỗi việc thành công: 4.472 đ [simulated], gấp 16,28 lần cách chỉ lấy hoá đơn token và tool chia số yêu cầu (274,65 đ). Làm lại chiếm 51,77% và xem lại 40,70% tổng chi phí.
- Ba yếu tố nhạy nhất: số ca làm lại +51,77%, tỉ lệ xem lại +40,70%, lương nhân viên +23,12% [simulated].
- So với nhân viên tự làm (12.000 đ): phạm vi `noi_dia` + `hang_nang` đã cộng chi phí cố định là 4.599 đ = 0,38× [simulated]; `quoc_te` 22.515 đ = 1,88× nên loại khỏi phạm vi. Xem lại 100% đẩy chi phí lên 12.415 đ = 1,03× [simulated].
- Chỉ số đợt chạy thử (không có nhóm đối chứng): chỉ số chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), lỗi lọt đến khách 4,25% (51/1.200).
- Đồng thuận gắn nhãn lỗi: 12/20 = 60%, dưới mục tiêu 80% nên nhóm viết lại định nghĩa 5 loại.
- Pilot: chia theo nhân viên 20 + 20, 859 yêu cầu/nhóm, DE 6,96, chỉ thấy được +6 điểm; nếu tác động thật là +5 điểm thì power còn 0,64.
- Đề xuất cuối của `ho_so_launch_v0.md`: **Go có điều kiện** cho pilot `noi_dia` + `hang_nang`, với 4 điều kiện (sửa khoá chống trùng và thông báo "đã hoàn", Giám đốc vận hành ký chấp nhận +6 điểm, đo phút thật sau tuần 1, giảm xem lại theo bậc).
- Kết quả duyệt chéo nhóm nhận được từ hội đồng: ... (điền sau buổi Gate 2a: điểm /30, quyết định, câu hỏi và nhận xét chính)

## 5. Khó khăn và cách xử lý

- Đồng thuận gắn nhãn chỉ đạt 60% ở lần đầu (8 ca lệch giữa hai người). Nhóm viết lại định nghĩa 5 loại theo nguyên nhân gốc, ghi một câu quy tắc cho từng ca lệch và giữ nguyên hai bộ nhãn độc lập ban đầu.
- Chia theo nhân viên không đạt cỡ mẫu cho mức chênh +5 điểm (cỡ mẫu hiệu dụng tối đa 1.000 < 1.251; theo m = 75 cần 84 nhân viên, nhiều hơn 40 hiện có). Nhóm chấp nhận đánh đổi: mức chênh +6 điểm với 859 yêu cầu/nhóm, mỗi nhân viên xử lý ít nhất 299 yêu cầu, và ghi rõ power 0,64 nếu tác động thật là +5 điểm.
- Phối hợp bốn người trên một repo: mỗi người một nhánh, một người sửa `src/lab13.py` tại một thời điểm, pull `main` trước khi push và người nhận chạy lại kiểm tra kết quả trước khi dùng số.
- Lỗi kỹ thuật (cài đặt, chạy code) và bằng chứng: ... (cả nhóm bổ sung nếu có; nếu không có thì ghi "không có")

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Chi phí xem lại và làm lại dùng phút giả lập (`_simulated`), chiếm 92,5% tổng chi phí; hai khoản này quyết định kết luận kinh tế. Cải thiện: đo phút xem lại và làm lại thật sau tuần 1 của pilot.
- Đợt chạy thử không có nhóm đối chứng nên chưa kết luận được trợ lý nâng chỉ số chính bao nhiêu; chỉ pilot có đối chứng mới trả lời được.
- Mô hình chi phí cộng tuyến tính và coi các lần chạy độc lập; dữ liệu cho thấy lỗi có thể lặp lại trên cùng yêu cầu, nên giới hạn chạy lại cần kiểm chứng trong pilot.
- Cỡ mẫu giả định ICC 0,02; nếu ICC thực tế cao hơn thì cần thêm nhân viên hoặc kéo dài pilot.
- Chỉ phạm vi `noi_dia` + `hang_nang`; `quoc_te` và `doi_tac` chưa được đánh giá cho pilot.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, https://arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", https://pair.withgoogle.com
- Tài liệu statsmodels, lớp `NormalIndPower` (mục `stats.power`)
