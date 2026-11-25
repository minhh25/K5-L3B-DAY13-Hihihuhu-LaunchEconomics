# Báo cáo cá nhân — DoanXuanDuyBao-2A202603858

## 1. Thông tin thành viên

- Họ tên: Đoàn Xuân Duy Bảo
- MSSV: 2A202603858
- Email: doanxuanduybao96@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 1 (phụ trách bảng lỗi, kế hoạch pilot, đặc tả chỉ số/event và tổng hợp rủi ro kinh tế)

## 2. Phần việc phụ trách

- **Nhiệm vụ C (`report/team/bang_loi.md`):** Gắn nhãn độc lập 20 ca lỗi; phối hợp Hùng so nhãn, tính đồng thuận và viết quy tắc phân biệt; hoàn thiện bảng khắc phục 5 ca (đủ 5 loại Google PAIR).
- **Nhiệm vụ D (`report/team/pilot_plan.yaml`):** Chủ trì D2 (5 câu tách được tác động), hoàn thiện kế hoạch pilot, rollout, luật dừng và rollback từ số liệu D1 của Hải.
- **Nhiệm vụ E (`report/team/chi_so.md`):** Đặc tả chỉ số (kết hợp số liệu Hải bàn giao), danh sách event có `trace_id`, kiểm tra chéo event–chỉ số và tổng hợp rủi ro kinh tế từ bảng độ nhạy.
- **Gate 2a & hoàn tất:** Trả lời phản biện về lỗi, pilot, luật dừng; cùng nhóm chấm chéo; soát checklist nộp bài và hoàn thiện báo cáo cá nhân.

## 3. Đóng góp cụ thể

- **Đã triển khai (đến hiện tại):**
  - Hoàn thành **Nhiệm vụ C (`report/team/bang_loi.md`)**: giữ nguyên 2 bộ nhãn độc lập (Bảo vs Hùng từ `hungvt`), tính đồng thuận **12/20 = 60%**, viết lại định nghĩa 5 loại (vì < 80%), viết 8 câu quy tắc phân biệt cho các ca không trùng và chốt bảng khắc phục 5 ca (khớp phạm vi loại `quoc_te` từ A3).
  - Hoàn thành **Nhiệm vụ D (`report/team/pilot_plan.yaml`)**: sau khi pull và chạy `src/lab13.py` của Hải, đã điền đủ D1 (`1.251`, `3.103 / 42 người`, `1.000`, `300`, `m >= 299 / DE = 6,96`, power `0,64` ở mức 5 điểm), D2, `scope`, `rollout`, 3 `stop_rules` đủ 4 vế (dựa trên `mo_lai_trong_7_ngay` 4,25% toàn mẫu / 3,97% phạm vi pilot), `rollback`, `decision_date` và `simulated_inputs`.
  - Hoàn thành **Nhiệm vụ E1–E2 (`report/team/chi_so.md`)**: điền đủ 3 chỉ số tính thử từ `src/lab13.py` (`82,83%`, `27,12%`, `4,25%`), 2 chỉ số tự đề xuất, 10 event có `trace_id`, kiểm tra chéo event–chỉ số và bảng **E2 · Rủi ro kinh tế** (3 dòng từ `bang_chi_phi.md`).
- **Bước tiếp theo:**
  - Tham gia bảo vệ & chấm chéo **Gate 2a** cùng nhóm và cập nhật bằng chứng duyệt chéo vào báo cáo cá nhân & `TEAM.md`.

## 4. Bằng chứng

- Nhánh cá nhân `baodxd` với các file đã cập nhật: `report/team/bang_loi.md`, `report/team/pilot_plan.yaml`, `report/team/chi_so.md`, `report/team/2A202603858_DoanXuanDuyBao.md`.
- Commit `55cf960` (chuẩn bị), `1695151` (bảng lỗi), `3f7e238` (pilot/chỉ số), `b6df753` (bổ sung thuộc tính event). Chưa có bằng chứng duyệt chéo vì nhóm chưa thực hiện.

## 5. Công cụ AI đã dùng

- Sử dụng trợ lý AI để đọc tài liệu đề bài/hướng dẫn, trích xuất 20 ca lỗi từ file `.docx`, kiểm tra cấu trúc YAML và đối chiếu checklist của rubric.
- Tự kiểm tra bằng cách đối chiếu từng dòng với `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, `CHECKPOINTS.md`, `RUBRIC.md` và `SUBMISSION.md`.

## 6. Tự đánh giá

- Hoàn thành C, D và E1–E2 theo các commit đã nêu; số trong pilot và chỉ số được bàn giao từ code của Hải. Hạn chế còn lại là đồng thuận nhãn ban đầu 60% và dữ liệu phút simulated; giữ nguyên nhãn gốc, bổ sung quy tắc và ưu tiên đo thực tế. Duyệt chéo chưa diễn ra nên chưa tự nhận hoàn thành phần phản biện/hội đồng.
