# Báo cáo cá nhân — Vũ Tiến Hùng-2A202603882

## 1. Thông tin thành viên

- Họ tên: Vũ Tiến Hùng
- MSSV: 2A202603882
- Email: hungvu.education@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 2 kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- Giữ và chủ trì `ho_so_launch_v0.md` (7 mục, đề xuất cuối).
- Gắn nhãn độc lập 20 ca lỗi ở CP3, cùng Bảo so nhãn.
- Ghi `phieu_cham.md` (duyệt chéo Gate 2a) và tổng hợp `group_report.md`.

## 3. Đóng góp cụ thể

- Đã làm: dựng khung `ho_so_launch_v0.md`, điền mục 1, 2, 3, 7 từ số A–B trong `bang_chi_phi.md`, ghi nhãn *simulated*.
- Đã lưu đủ 20 nhãn độc lập trong `nhan_doc_lap_hung.md`; Bảo tổng hợp hai bộ nhãn với đồng thuận ban đầu 12/20 = 60%, giữ nguyên nhãn gốc.
- Đã hoàn thiện hồ sơ launch đủ 7 mục và đề xuất Go có điều kiện từ kết quả A–E (commit `e80cd63`). Minh tiếp tục tổng hợp báo cáo nhóm và rà soát hồ sơ trong lượt hoàn thiện cuối.
- Chưa ghi kết quả duyệt chéo vì nhóm xác nhận chưa thực hiện hoạt động này.

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- Nhánh `hungvt`: commit `77bc5b9` (khung hồ sơ), `e10274c` (điền mục 1, 2, 3, 7).
- Bộ nhãn độc lập ban đầu: commit `889ff11`, [nhan_doc_lap_hung.md](nhan_doc_lap_hung.md), đối chiếu cột người gắn nhãn 2 trong [bang_loi.md](bang_loi.md).
- Hồ sơ launch đủ 7 mục: commit `e80cd63`; [phieu_cham.md](phieu_cham.md) ghi trạng thái chưa duyệt chéo, chưa có kết quả hội đồng.

## 5. Công cụ AI đã dùng

- Claude Code (Anthropic): soạn khung các file hồ sơ, đọc `bang_chi_phi.md` để chép số vào hồ sơ, đối chiếu số giữa các file, so nhánh Git của các thành viên.
- Cơ sở đối chiếu: số chi phí từ `bang_chi_phi.md`, D1 từ `pilot_plan.yaml`, chỉ số/event từ `chi_so.md`; nhãn gốc đối chiếu với bảng lỗi. Lượt rà soát tích hợp của Minh kiểm tra lại các liên kết số liệu này.

## 6. Tự đánh giá

Hoàn thành bộ nhãn và hồ sơ launch theo vai trò giữ hồ sơ, cung cấp bằng chứng ở các commit trên. Đồng thuận ban đầu 60% còn thấp, nên cần tiếp tục kiểm tra định nghĩa lỗi; không đổi nhãn gốc để nâng tỉ lệ. Hồ sơ nêu rõ chi phí simulated và đánh đổi power 0,64 ở hiệu ứng +5 điểm. Phần hội đồng và hỏi–đáp còn chờ duyệt chéo thực tế.
