# Team

## Thông tin nhóm

- Tên nhóm: Hihihuhu
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-Hihihuhu-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo: https://github.com/minhh25/K5-L3B-DAY13-Hihihuhu-LaunchEconomics
- Quyền truy cập: public, đã kiểm tra khi rà soát bài nộp.
- Nhánh nộp: `main` sau khi merge PR; nhánh hoàn thiện hồ sơ: `minhnd`.
- Phiên bản A–E đã tích hợp: `2b91cac`; các thay đổi hoàn thiện hồ sơ tiếp tục qua PR từ `minhnd`. Commit nộp là commit cuối trên `main` trước deadline, tra bằng `git log -1 --format=%H main`.

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
| 1 | Nguyễn Đình Minh | 2A202603867 | nguyenminh25112k4@gmail.com | [minhh25](https://github.com/minhh25) | Viết code A–B trước giải lao; kiểm số sau giải lao; điều phối tích hợp và nộp bài |
| 2 | Nguyễn Đình Vũ Hải | 2A202603820 | nguyendinhvuhai1234@gmail.com | [HaiVuuu](https://github.com/HaiVuuu) | Kiểm số và giữ bảng chi phí A–B; viết code D1 và tính chỉ số E sau giải lao |
| 3 | Đoàn Xuân Duy Bảo | 2A202603858 | doanxuanduybao96@gmail.com | [CapybaraSlayer96](https://github.com/CapybaraSlayer96) | Gắn nhãn 1; phụ trách bảng lỗi, kế hoạch pilot và đặc tả event |
| 4 | Vũ Tiến Hùng | 2A202603882 | hungvu.education@gmail.com | [hungvueducation-hash](https://github.com/hungvueducation-hash) | Gắn nhãn 2 kiêm giữ hồ sơ; tổng hợp launch v0, báo cáo nhóm và phiếu duyệt chéo |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

**Luân phiên code:** Minh viết A–B trước giải lao; Hải tiếp quản `src/lab13.py` sau giải lao, tự chạy lại mô hình chi phí, hoàn thiện phần B còn thiếu rồi viết D1 và tính chỉ số E. Minh chuyển sang kiểm tra công thức và kết quả. Hai người bàn giao trước khi cùng sửa một file.

## Phân công theo phase

Giờ dưới đây theo lịch mẫu trong [CHECKPOINTS.md](CHECKPOINTS.md); nếu coach đổi giờ thì giữ nguyên thứ tự. Bảng này lưu kế hoạch phân công; đóng góp thực tế và bằng chứng được tổng hợp ở các mục cá nhân bên dưới. Nhóm xác nhận chưa duyệt chéo Gate 2a.

| Phase / mốc | Minh | Hải | Bảo | Hùng | Đầu ra / điều kiện bàn giao |
| --- | --- | --- | --- | --- | --- |
| Chuẩn bị · 14:00–14:10 | Kiểm tra repo nhóm, môi trường và cách chạy trong `src/` | Đọc cấu trúc hai CSV, bảng giá và cách tính chi phí | Đọc yêu cầu A–E, lập danh sách điều kiện hoàn thành | Kiểm tra mẫu hồ sơ, mở hồ sơ launch để điền dần | Đủ vai; môi trường sẵn sàng; mọi người biết file phụ trách |
| A / CP1 · 14:10–14:53 | Viết A1, `mo_hinh`, A3 theo loại và A4 chi phí cố định | Tính tay đối chiếu ít nhất một khoản; điền bảng A2–A4 trong `bang_chi_phi.md` | Soát phạm vi loại yêu cầu, mẫu số thành công và chi phí chuyển nhân viên | Ghi kết luận A vào hồ sơ launch, giữ nhãn `simulated` | Ba phép thử A1 đạt; đủ bảng A2–A4; Hải kiểm số của Minh |
| B / CP2 · 14:53–15:20 | Viết 9 kịch bản B1, cặp B2, so sánh B3 và xem lại 100% B4 | Điền bảng B; xếp hạng yếu tố; viết câu trả lời ngắn có số | Kiểm tra lập luận giới hạn chạy lại và giả định xem lại/làm lại | Ghi rủi ro kinh tế từ B và cập nhật hồ sơ launch | `bang_chi_phi.md` đủ A–B; ghi rõ chi phí cả hệ thống và giả định B4 |
| C / CP3 · 15:35–16:08 | Kiểm tra lại A–B, hỗ trợ Hải đối chiếu mô hình | Tiếp quản code, tự chạy mô hình chi phí và hoàn thiện B còn thiếu | Gắn độc lập đủ 20 ca trong 8 phút; sau đó tổng hợp bảng lỗi và 5 cách khắc phục | Gắn độc lập đủ 20 ca trong 8 phút; sau đó cùng Bảo so nhãn, ghi đồng thuận và quy tắc phân biệt | `bang_loi.md` lưu hai bộ nhãn gốc; đồng thuận mục tiêu ≥ 16/20; đủ 5 loại lỗi |
| D / CP4 · 16:08–16:36 | Kiểm tra D1, cỡ mẫu hiệu dụng, đánh đổi và ngưỡng dừng so với dữ liệu | Viết code tính đủ 5 câu D1 và tỉ lệ mở lại hiện tại; bàn giao số cho Bảo | Chủ trì D2 và điền `pilot_plan.yaml`: phạm vi, phân nhóm, rollout, luật dừng, rollback | Kiểm tra owner, ngày quyết định, trạng thái giả lập và tính nhất quán với hồ sơ launch | YAML đủ trường, không còn dấu hỏi; đọc được; ≥ 3 luật dừng đủ 4 vế |
| E / CP5 · 16:36–17:00 | Đối chiếu số giữa các file, cùng nhóm chốt đề xuất có căn cứ | Tính 3 chỉ số có sẵn, bàn giao công thức và kết quả cho Bảo | Tổng hợp `chi_so.md`: 3 chỉ số tính thử, thêm 2 chỉ số đề xuất, ≥ 6 event có `trace_id`, ≥ 2 rủi ro kinh tế | Hoàn thiện `ho_so_launch_v0.md` một trang, đủ 7 mục, trạng thái và vai trò phụ trách | Hồ sơ sẵn sàng lúc 17:00; đề xuất Go / Go có điều kiện / No-go khớp bằng chứng |
| Gate 2a · 17:00–17:45 | Đại diện trình bày; trả lời về chi phí và phạm vi | Trả lời về độ nhạy, cỡ mẫu và chỉ số | Trả lời về lỗi, pilot và luật dừng | Ghi nhận phản biện; điền `phieu_cham.md` từ đánh giá thực tế của cả nhóm | Cả 4 người đọc và chấm nhóm được phân công; có quyết định, lý do và câu hỏi |
| Hoàn tất · 17:45–18:00 | Tích hợp thay đổi, kiểm tra file nộp, commit và push | Chạy code từ đầu đến cuối trên máy thứ hai; kiểm tra YAML và các bảng | Soát yêu cầu rubric, event, luật dừng và nhãn `simulated` | Tổng hợp `group_report.md`, nhắc mọi người hoàn thiện báo cáo cá nhân và cập nhật bằng chứng trong `TEAM.md` | Đủ hồ sơ, báo cáo và đóng góp; mỗi người tự nộp link repo trên LMS trước 23h59 GMT+7 ngày lab |

### Quy tắc phối hợp

- Bảo và Hùng gắn nhãn độc lập, không trao đổi trong 8 phút đầu CP3; giữ nguyên hai bộ nhãn ban đầu sau khi so nhãn. Nếu đồng thuận dưới 80%, viết lại định nghĩa trước khi đi tiếp.
- Trong thời gian gắn nhãn độc lập, Hùng tập trung gắn nhãn; việc cập nhật hồ sơ tiếp tục sau đó.
- Mỗi file có một người tổng hợp chính: `src/lab13.py` Minh rồi Hải; `bang_chi_phi.md` Hải; `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md` Bảo; `ho_so_launch_v0.md`, `phieu_cham.md`, `group_report.md` Hùng. Người kiểm tra góp ý trước khi người giữ file tích hợp.
- Minh kiểm số sau giải lao; Hải kiểm số trước giải lao. Bảo kiểm tra điều kiện hoàn thành; Hùng kiểm tra hồ sơ đủ bằng chứng, trạng thái và người phụ trách.
- Mọi con số phải lấy từ code của nhóm hoặc phép tính tay có cách tính; số dựa vào cột `_simulated` ghi nhãn `simulated`. Các câu trả lời trong hồ sơ giữ ngắn, có số theo yêu cầu đề bài.
- Cả nhóm phải giải thích được chi phí, giới hạn chạy lại, cỡ mẫu theo cụm và lý do đề xuất cuối.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Mỗi người copy mẫu `report/team/MSSV_HoTen.md` thành file cá nhân đúng tên dưới đây và tự ghi công cụ AI đã dùng, cách kiểm tra, kết quả và bằng chứng. Giữ nguyên file mẫu.

## Nguyễn Đình Minh — 2A202603867

### Phần việc phụ trách

- Chủ trì code A–B; kiểm tra số và tích hợp sau giải lao; trình bày Gate 2a; đóng gói và push bài.
- Báo cáo cá nhân: `report/team/2A202603867_NguyenDinhMinh.md`.

### Đóng góp cụ thể

- Đã hoàn thiện các hàm A1, mô hình chi phí A2–A4 và code B1–B4; chạy kiểm tra với dữ liệu lab và bộ nhỏ tính tay, bàn giao cho Hải.
- Đã rà soát bản tích hợp A–E, bổ sung báo cáo cá nhân, tổng hợp báo cáo nhóm và đóng góp, hoàn thiện lịch/cỡ mẫu/luật dừng pilot, đối chiếu hồ sơ với `SUBMISSION.md`. Chưa trình bày Gate 2a vì nhóm chưa duyệt chéo.
- Đã hoàn thiện CP4–CP5 theo slide bổ sung: luật dừng theo bước 4/10/20 người, CPS biến đổi tách cố định; bổ sung ngoại suy thời gian thu mẫu, bảng kinh tế rollout, 13 event, 4 rủi ro và đồng bộ hồ sơ launch. Điểm và quyết định hội đồng vẫn chưa có.

### Bằng chứng

- Commit `99971af` (phân công), `6d98671` (A), `43891a3` (B); `src/lab13.py` chạy đủ A–B–D–E, A1 đạt. Báo cáo cá nhân ghi cách kiểm tra và các kết quả; phần hoàn thiện cuối thể hiện trong diff/PR nhánh `minhnd`.

## Nguyễn Đình Vũ Hải — 2A202603820

### Phần việc phụ trách

- Chủ trì kiểm số và bảng chi phí A–B; tiếp quản code sau giải lao; tính D1 và chỉ số E; chạy kiểm tra trên máy thứ hai.
- Báo cáo cá nhân: `report/team/2A202603820_NguyenDinhVuHai.md`.

### Đóng góp cụ thể

- Đã hoàn thiện bảng chi phí A–B; viết `co_mau`, `phan_tich_co_mau`, `in_phan_d`, `tinh_chi_so_e`, `in_phan_e`; bàn giao kết quả D1/E1 cho Bảo.
- Báo cáo cá nhân ghi nhận đã chạy code trên nhánh `haindv`; lần chạy lại bản hoàn thiện cuối trên máy thứ hai còn cần xác nhận.

### Bằng chứng

- Commit `bb17b92` (bảng A), `9f0ccd3` (bảng A–B), `a8bebf9` (code D1/E1 và báo cáo). Các file `bang_chi_phi.md`, `src/lab13.py`, báo cáo cá nhân lưu số và cách đối chiếu.

## Đoàn Xuân Duy Bảo — 2A202603858

### Phần việc phụ trách

- Gắn nhãn 1; chủ trì bảng lỗi, kế hoạch pilot, đặc tả chỉ số/event và tổng hợp rủi ro kinh tế.
- Báo cáo cá nhân: `report/team/2A202603858_DoanXuanDuyBao.md`.

### Đóng góp cụ thể

- Đã tổng hợp hai bộ nhãn, tính đồng thuận ban đầu 12/20 = 60%, viết lại định nghĩa và quy tắc cho 8 ca lệch, hoàn thiện 5 cách khắc phục.
- Đã hoàn thiện pilot từ D1 của Hải và chỉ số/event/rủi ro từ A–B, E1; bước duyệt chéo còn chưa diễn ra.

### Bằng chứng

- Commit `55cf960`, `1695151` (bảng lỗi), `3f7e238` (pilot và chỉ số), `b6df753` (event); hai bộ nhãn gốc nằm trong `bang_loi.md`, nhãn Hùng đối chiếu tại `nhan_doc_lap_hung.md`.

## Vũ Tiến Hùng — 2A202603882

### Phần việc phụ trách

- Gắn nhãn 2 kiêm giữ hồ sơ; chủ trì hồ sơ launch v0, ghi phiếu duyệt chéo và tổng hợp báo cáo nhóm.
- Báo cáo cá nhân: `report/team/2A202603882_VuTienHung.md`.

### Đóng góp cụ thể

- Đã dựng khung hồ sơ, báo cáo nhóm và phiếu chấm; lưu bộ nhãn độc lập 20 ca; điền hồ sơ launch đủ 7 mục và đề xuất Go có điều kiện từ số A–E.
- Minh tổng hợp tiếp báo cáo nhóm, cập nhật trạng thái phiếu và rút gọn hồ sơ trong lượt hoàn thiện cuối; Hùng giữ vai trò ghi nhận duyệt chéo khi hoạt động diễn ra.

### Bằng chứng

- Commit `77bc5b9` (khung hồ sơ), `e10274c` (số A–B), `889ff11` (nhãn gốc), `e80cd63` (launch đủ 7 mục); báo cáo cá nhân và `nhan_doc_lap_hung.md`. Phiếu chấm đang ghi đúng trạng thái chưa duyệt, chưa có điểm hay phản biện thực tế.
