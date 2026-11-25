# Báo cáo cá nhân — NguyenDinhVuHai-2A202603820

## 1. Thông tin thành viên

- Họ tên: Nguyễn Đình Vũ Hải
- MSSV: 2A202603820
- Email: nguyendinhvuhai1234@gmail.com
- Vai trong nhóm: Người kiểm số và giữ bảng chi phí (phần A–B trước giải lao); tiếp quản `src/lab13.py` viết phần D1 và tính 3 chỉ số E (sau giải lao); chạy kiểm tra cuối trên máy thứ hai.

## 2. Phần việc phụ trách

- Kiểm số mô hình chi phí A1–A4 và bảng độ nhạy B1–B4 của Minh; tổng hợp đầy đủ `report/team/bang_chi_phi.md`.
- Tiếp quản `src/lab13.py` sau giải lao: viết hàm tính 5 câu cỡ mẫu D1, kiểm tra power thực tế ở mức 5 điểm, tỉ lệ mở lại trong 7 ngày, và 3 chỉ số E1 (chính, dùng, an toàn).
- Chạy kiểm tra toàn bộ `src/lab13.py` và xác nhận `report/team/pilot_plan.yaml` đọc được bằng `yaml.safe_load` trên máy thứ hai trước khi nộp.

## 3. Đóng góp cụ thể

- Đối chiếu và điền hoàn chỉnh `report/team/bang_chi_phi.md` (A1–A4 và B1–B4), đảm bảo mọi con số từ cột `_simulated` đều có nhãn `simulated` và câu trả lời ngắn ≤ 3 dòng có số liệu.
- Hoàn thiện phần D (`co_mau`, `phan_tich_co_mau`, `in_phan_d`) và phần E (`tinh_chi_so_e`, `in_phan_e`) trong `src/lab13.py` để bàn giao số cho Bảo điền `pilot_plan.yaml` và `chi_so.md`.
- Tự kiểm tra kết quả chạy `src/lab13.py` trên nhánh `haindv` và đối chiếu với công thức trong `docs/du_lieu_va_cong_thuc.md`.

## 4. Bằng chứng

- Nhánh làm việc: `haindv`
- `report/team/bang_chi_phi.md`: hoàn thiện bảng A1–A4, B1–B4 (CPS gốc `4.472 đ` [simulated], top 3 yếu tố nhạy nhất: số ca làm lại `+51,77%`, tỉ lệ xem lại `+40,70%`, lương `+23,12%` [simulated]).
- `src/lab13.py`: bổ sung phần D1 (`1.251` yc/nhóm, `3.103` yc/nhóm ở m=75, giới hạn `1.000` với 20 NV/nhóm và `300` với 6 depot/nhóm, `m ≥ 299` cho MDE 6 điểm với `DE = 6,96`, power `0,64` nếu hiệu ứng thật 5 điểm; tỉ lệ mở lại 7 ngày `4,25%` toàn mẫu / `3,97%` phạm vi) và phần E1 (`82,83%` chính, `27,12%` bỏ qua gợi ý, `4,25%` mở lại).
- Commit `bb17b92` (bảng A), `9f0ccd3` (bảng A–B), `a8bebf9` (code D1/E1 và báo cáo).
- Xác nhận trên máy thứ hai (bản `main` hợp nhất `359e5c6`): đã chạy `python lab13.py` trong `src/.venv` (đạt cả 3 phép thử A1 và in đủ bảng A, B, D1, E1, E2 không lỗi), kiểm tra `yaml.safe_load` trên `report/team/pilot_plan.yaml` (`YAML OK`), và kiểm tra không có từ cấm trong `report/team/`. Nhóm sẵn sàng duyệt chéo Gate 2a.

## 5. Công cụ AI đã dùng

- Dùng trợ lý AI (Antigravity / Gemini) để giải thích cấu trúc bài lab, hỗ trợ cài đặt môi trường `.venv`, định dạng bảng `bang_chi_phi.md`, và gợi ý code phần D–E trong `src/lab13.py`.
- Tự kiểm tra: chạy trực tiếp `src/lab13.py` trong `.venv` trên máy cá nhân, đối chiếu từng con số với công thức trong `docs/du_lieu_va_cong_thuc.md` và ngưỡng sai số ≤ 2% của hướng dẫn lab.

## 6. Tự đánh giá

- Hoàn thành đúng tiến độ các phần việc phụ trách (A–B, D1, E1), bàn giao số liệu sớm để Bảo và Hùng kịp hoàn thiện `pilot_plan.yaml`, `chi_so.md` và `ho_so_launch_v0.md` trước mốc 17:00.
