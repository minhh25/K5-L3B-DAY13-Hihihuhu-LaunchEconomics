# Phiếu chấm hội đồng Gate 2a — Nhóm A90

- Nhóm chấm: **Hihihuhu — L3B**; người tổng hợp đánh giá: Nguyễn Đình Minh; người giữ phiếu: Vũ Tiến Hùng.
- Nhóm được chấm: **A90 — L3B**, [repo](https://github.com/Tiberu2611/K5-L3B-Day13-A90-LaunchEconomics).
- Phiên bản chấm: nhánh main, commit [a7da2b4](https://github.com/Tiberu2611/K5-L3B-Day13-A90-LaunchEconomics/commit/a7da2b41e20231ece59f6d24578ceb92334513f1), ngày 25/11/2026 (GMT+7).
- Trạng thái: **Đã đọc hồ sơ và kiểm tra code; chưa hỏi–đáp trực tiếp với A90.** Điểm dưới đây là đề xuất để nhóm xác nhận khi duyệt chéo.
- Phạm vi điểm: **C6–C8, tối đa 30 điểm**, theo [RUBRIC.md](../../RUBRIC.md). Phần C1–C5 /70 thuộc chấm đối chiếu của trợ giảng, không cộng vào phiếu này.

## Điểm đề xuất trên hồ sơ

| Tiêu chí | Điểm | Bằng chứng và lý do |
| --- | ---: | --- |
| C6 · Đề xuất khớp bằng chứng | **10/10** | Đề xuất Go có điều kiện cho nội địa + hàng nặng; có số bất lợi và cách xử lý: CPS toàn mẫu 4.472 đ, quốc tế 22.515 đ = 1,88×; xem lại 100% lên 11.743–12.415 đ (simulated); power chỉ 0,64 ở hiệu ứng +5 điểm. Có điều kiện sửa ca 7/20, đo phút thật, chấp nhận MDE +6 điểm và giảm xem lại. [Hồ sơ launch](https://github.com/Tiberu2611/K5-L3B-Day13-A90-LaunchEconomics/blob/a7da2b41e20231ece59f6d24578ceb92334513f1/report/team/ho_so_launch_v0.md#L9), [bảng chi phí](https://github.com/Tiberu2611/K5-L3B-Day13-A90-LaunchEconomics/blob/a7da2b41e20231ece59f6d24578ceb92334513f1/report/team/bang_chi_phi.md). |
| C7 · Số giả lập và phạm vi | **10/10** | Các bảng chi phí, độ nhạy và rủi ro gắn nhãn simulated theo dòng hoặc ghi chú bao phủ bảng; YAML có danh sách đầu vào giả lập. Phạm vi giới hạn nội địa + hàng nặng, loại quốc tế và đối tác bằng số A3; phân biệt dữ liệu chạy thử với bằng chứng tác động có đối chứng. [Phạm vi và đầu vào](https://github.com/Tiberu2611/K5-L3B-Day13-A90-LaunchEconomics/blob/a7da2b41e20231ece59f6d24578ceb92334513f1/report/team/pilot_plan.yaml#L37), [chỉ số](https://github.com/Tiberu2611/K5-L3B-Day13-A90-LaunchEconomics/blob/a7da2b41e20231ece59f6d24578ceb92334513f1/report/team/chi_so.md). |
| C8 · Pilot ra được quyết định | **5/10, tạm thời** | Thiết kế có 20 + 20 nhân viên, ngẫu nhiên theo depot, 5.980 yêu cầu thô/nhánh tương đương 859,20 hiệu dụng; thu mẫu chính 14 ngày, 4 luật dừng có ngưỡng/thời hạn/owner, rollback 30 phút. Tuy nhiên chưa thống nhất mốc bắt đầu cửa sổ mở lại 7 ngày và cách chốt cohort cuối; phần rà soát luật trong chi_so.md vẫn mô tả phiên bản cũ. Chưa đủ căn cứ xác nhận mức 10 điểm về khả năng vận hành/chốt quyết định của toàn bộ hồ sơ. Đây là điểm giữ lại để làm rõ, không phải kết luận thiếu đối chứng hay sai cỡ mẫu. [Lịch](https://github.com/Tiberu2611/K5-L3B-Day13-A90-LaunchEconomics/blob/a7da2b41e20231ece59f6d24578ceb92334513f1/report/team/pilot_plan.yaml#L53), [luật dừng](https://github.com/Tiberu2611/K5-L3B-Day13-A90-LaunchEconomics/blob/a7da2b41e20231ece59f6d24578ceb92334513f1/report/team/pilot_plan.yaml#L98). |
| **Tổng đề xuất** | **25/30** | **Xem xét lại C8 sau khi A90 làm rõ mốc theo dõi và thống nhất tài liệu.** |

**Quyết định đề xuất của hội đồng: Go có điều kiện** cho kế hoạch pilot nội địa + hàng nặng. Các điều kiện và câu hỏi dưới đây cần được giải đáp trước khi chốt duyệt; phiếu không xác nhận pilot đã được phép bắt đầu hay đã có kết quả thực nghiệm.

## Kết quả kiểm tra và điểm mạnh

- Chạy code của A90 từ bản chụp commit nêu trên trong thư mục tạm: kết thúc thành công, 3 phép thử A1 đạt; CSV trùng dữ liệu lab.
- CPS tính lại **4.471,97 đ**, chi phí cả hệ thống **5.864,65 đ/yêu cầu** (simulated); ba yếu tố nhạy nhất là làm lại, xem lại và lương. Bảng B3 xác định giới hạn 2 lần có tổng hệ thống thấp nhất **6.901.220 đ** (simulated).
- D1 khớp **1.251 / 3.103 / 42 người / trần 1.000 / trần 300 / 859 / 299**; phân biệt mẫu thô và hiệu dụng, nêu power 0,64 nếu hiệu ứng thật chỉ +5 điểm.
- E1 khớp **994/1.200 = 82,83%**, **48/177 = 27,12%**, **51/1.200 = 4,25%**. Không suy ra tác động từ đợt chạy thử không có đối chứng.
- YAML đọc được, không còn dấu hỏi ngoài chú thích; 4 luật dừng đủ bốn vế. Bảng nhãn có đồng thuận **16/20 = 80%**; việc kiểm tra này xác nhận tính nhất quán của bảng, không xác nhận quá trình gắn độc lập tại lớp.

## Các điều kiện cần làm rõ hoặc đồng bộ

1. **Chốt mốc theo dõi 7 ngày.** chi_so.md dòng 55 tính từ ngày gửi D; YAML thu yêu cầu đến 27/12/2026, theo dõi đến 03/01/2027 và quyết định 04/01. Nếu cửa sổ mở lại tính sau lần đóng đầu, yêu cầu cuối ngày 27/12 có thể đóng trong ngày 28/12, nên cần theo dõi đến hết 04/01 và quyết định sau đó (ví dụ 05/01), hoặc chốt cutoff giờ cụ thể bảo đảm đủ cửa sổ. Nếu dùng cửa sổ khác, phải định nghĩa và giải thích nhất quán; không tính ca chưa đủ theo dõi là không mở lại. [Nguồn](https://github.com/Tiberu2611/K5-L3B-Day13-A90-LaunchEconomics/blob/a7da2b41e20231ece59f6d24578ceb92334513f1/report/team/chi_so.md#L55).
2. **Cập nhật phần rà soát luật đã lỗi phiên bản.** chi_so.md dòng 81–90 còn ghi các đề xuất chưa áp dụng, cho rằng luật chi phí sẽ kích hoạt sau hai tuần đầu và luật sử dụng thiếu tối thiểu 100 quyết định. YAML dòng 99–105 đã giới hạn luật mở lại từ bước 0,25, chi phí ở bước 0,50 và thêm 100 quyết định. Cần cập nhật bảng rà soát; không kết luận luật hiện tại còn đúng các lỗi đã được sửa. [Rà soát cũ](https://github.com/Tiberu2611/K5-L3B-Day13-A90-LaunchEconomics/blob/a7da2b41e20231ece59f6d24578ceb92334513f1/report/team/chi_so.md#L81), [YAML hiện tại](https://github.com/Tiberu2611/K5-L3B-Day13-A90-LaunchEconomics/blob/a7da2b41e20231ece59f6d24578ceb92334513f1/report/team/pilot_plan.yaml#L98).
3. **Sửa cách viết về 299 yêu cầu/người.** Điều kiện 4 của hồ sơ launch yêu cầu xác nhận đủ 299 trước ngày 14/12; YAML thực tế yêu cầu xác nhận năng lực thu mẫu trước ngày này và chỉ thu mẫu chính 14–27/12. Viết rõ đây là xác nhận năng lực; 5.980 yêu cầu/nhánh phải được thu trong cửa sổ bước 0,50, không lấy đơn hai bước đầu thay thế. [Điều kiện 4](https://github.com/Tiberu2611/K5-L3B-Day13-A90-LaunchEconomics/blob/a7da2b41e20231ece59f6d24578ceb92334513f1/report/team/ho_so_launch_v0.md#L22).

Giữ các điều kiện đã có của A90: xác nhận đủ 40 người/12 depot, ký chấp nhận đánh đổi MDE, chặn ca 7/20 và thay phút simulated bằng số đo thật. Ngưỡng 8.000 đ trong YAML dùng chi phí biến đổi; hồ sơ tóm tắt cũng cần ghi rõ cùng định nghĩa và cùng cửa sổ hai tuần ở bước 0,50.

## Câu hỏi cho đội trình

**Câu hỏi chính:** Với yêu cầu được tạo cuối ngày 27/12 và đóng trong ngày 28/12, nhóm tính cửa sổ mở lại 7 ngày từ mốc nào, chốt dữ liệu lúc nào và có thể quyết định vào 04/01 mà không tính ca chưa đủ theo dõi là thành công không?

**Câu hỏi bổ sung:** Điều kiện đủ 299 yêu cầu/người trước 14/12 là kiểm tra năng lực hay đã thu mẫu; tài liệu nào là phiên bản luật dừng cuối cùng khi chi_so.md và YAML đang khác nhau?

**Câu trả lời của đội trình:** Chưa nhận được; ghi lại câu trả lời thực tế và commit sửa của A90 sau khi trao đổi. Không điền câu trả lời suy đoán thay nhóm.

**Trạng thái chốt điểm:** Đề xuất 25/30 trên hồ sơ tại a7da2b4; chưa có hỏi–đáp trực tiếp và chưa có xác nhận cuối của buổi hội đồng. Chỉ điều chỉnh điểm khi có bằng chứng/giải thích mới, ghi rõ phiên bản được đánh giá lại.
