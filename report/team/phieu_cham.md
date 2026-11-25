# Phiếu chấm hội đồng Gate 2a — Nhóm A90

- Nhóm chấm: **Hihihuhu — L3B**; người tổng hợp đánh giá: Nguyễn Đình Minh; người giữ phiếu: Vũ Tiến Hùng.
- Nhóm được chấm: **A90 — L3B**, [repo](https://github.com/Tiberu2611/K5-L3B-Day13-A90-LaunchEconomics).
- Phiên bản chấm: nhánh main, commit [a7da2b4](https://github.com/Tiberu2611/K5-L3B-Day13-A90-LaunchEconomics/commit/a7da2b41e20231ece59f6d24578ceb92334513f1), ngày 25/11/2026 (GMT+7).
- Trạng thái: **Đã nhận câu trả lời bằng văn bản của A90 qua Minh; chờ commit đồng bộ tài liệu.** Ngày 25/11/2026 kiểm tra lại nhánh main vẫn ở `a7da2b4`; chưa có bản sửa mới để xác nhận các thay đổi đã áp dụng.
- Phạm vi điểm: **C6–C8, tối đa 30 điểm**, theo [RUBRIC.md](../../RUBRIC.md). Phần C1–C5 /70 thuộc chấm đối chiếu của trợ giảng, không cộng vào phiếu này.

## Điểm đề xuất trên phiên bản đã kiểm tra

| Tiêu chí | Điểm | Bằng chứng và lý do |
| --- | ---: | --- |
| C6 · Đề xuất khớp bằng chứng | **10/10** | Đề xuất Go có điều kiện cho nội địa + hàng nặng; có số bất lợi và cách xử lý: CPS toàn mẫu 4.472 đ, quốc tế 22.515 đ = 1,88×; xem lại 100% lên 11.743–12.415 đ (simulated); power chỉ 0,64 ở hiệu ứng +5 điểm. Có điều kiện sửa ca 7/20, đo phút thật, chấp nhận MDE +6 điểm và giảm xem lại. [Hồ sơ launch](https://github.com/Tiberu2611/K5-L3B-Day13-A90-LaunchEconomics/blob/a7da2b41e20231ece59f6d24578ceb92334513f1/report/team/ho_so_launch_v0.md#L9), [bảng chi phí](https://github.com/Tiberu2611/K5-L3B-Day13-A90-LaunchEconomics/blob/a7da2b41e20231ece59f6d24578ceb92334513f1/report/team/bang_chi_phi.md). |
| C7 · Số giả lập và phạm vi | **10/10** | Các bảng chi phí, độ nhạy và rủi ro gắn nhãn simulated theo dòng hoặc ghi chú bao phủ bảng; YAML có danh sách đầu vào giả lập. Phạm vi giới hạn nội địa + hàng nặng, loại quốc tế và đối tác bằng số A3; phân biệt dữ liệu chạy thử với bằng chứng tác động có đối chứng. [Phạm vi và đầu vào](https://github.com/Tiberu2611/K5-L3B-Day13-A90-LaunchEconomics/blob/a7da2b41e20231ece59f6d24578ceb92334513f1/report/team/pilot_plan.yaml#L37), [chỉ số](https://github.com/Tiberu2611/K5-L3B-Day13-A90-LaunchEconomics/blob/a7da2b41e20231ece59f6d24578ceb92334513f1/report/team/chi_so.md). |
| C8 · Pilot ra được quyết định | **5/10, tạm thời** | Thiết kế có 20 + 20 nhân viên, ngẫu nhiên theo depot, 5.980 yêu cầu thô/nhánh tương đương 859,20 hiệu dụng; thu mẫu chính 14 ngày, 4 luật dừng có ngưỡng/thời hạn/owner, rollback 30 phút. Phản hồi bằng văn bản đã làm rõ mốc closed_at, dời quyết định sang 05/01 và xác nhận YAML là nguồn luật dừng chính thức. Tuy nhiên bản main đã kiểm tra vẫn chưa cập nhật lịch và các mô tả cũ, nên tạm giữ 5 điểm cho phiên bản này; có thể nâng lên 10 sau khi xác minh commit đồng bộ. Đây không phải kết luận thiếu đối chứng hay sai cỡ mẫu. [Lịch](https://github.com/Tiberu2611/K5-L3B-Day13-A90-LaunchEconomics/blob/a7da2b41e20231ece59f6d24578ceb92334513f1/report/team/pilot_plan.yaml#L53), [luật dừng](https://github.com/Tiberu2611/K5-L3B-Day13-A90-LaunchEconomics/blob/a7da2b41e20231ece59f6d24578ceb92334513f1/report/team/pilot_plan.yaml#L98). |
| **Tổng đề xuất** | **25/30** | **Đã giải đáp về nguyên tắc; xem xét nâng C8 lên 10 sau khi kiểm tra commit đồng bộ tài liệu.** |

**Quyết định đề xuất của hội đồng: Go có điều kiện** cho kế hoạch pilot nội địa + hàng nặng. A90 đã giải đáp các câu hỏi bên dưới; cần áp dụng các sửa đổi vào repo trước khi chốt lại C8. Phiếu không xác nhận pilot đã được phép bắt đầu hay đã có kết quả thực nghiệm.

## Kết quả kiểm tra và điểm mạnh

- Chạy code của A90 từ bản chụp commit nêu trên trong thư mục tạm: kết thúc thành công, 3 phép thử A1 đạt; CSV trùng dữ liệu lab.
- CPS tính lại **4.471,97 đ**, chi phí cả hệ thống **5.864,65 đ/yêu cầu** (simulated); ba yếu tố nhạy nhất là làm lại, xem lại và lương. Bảng B3 xác định giới hạn 2 lần có tổng hệ thống thấp nhất **6.901.220 đ** (simulated).
- D1 khớp **1.251 / 3.103 / 42 người / trần 1.000 / trần 300 / 859 / 299**; phân biệt mẫu thô và hiệu dụng, nêu power 0,64 nếu hiệu ứng thật chỉ +5 điểm.
- E1 khớp **994/1.200 = 82,83%**, **48/177 = 27,12%**, **51/1.200 = 4,25%**. Không suy ra tác động từ đợt chạy thử không có đối chứng.
- YAML đọc được, không còn dấu hỏi ngoài chú thích; 4 luật dừng đủ bốn vế. Bảng nhãn có đồng thuận **16/20 = 80%**; việc kiểm tra này xác nhận tính nhất quán của bảng, không xác nhận quá trình gắn độc lập tại lớp.

## Các điểm phát hiện ở phiên bản a7da2b4

1. **Chốt mốc theo dõi 7 ngày.** chi_so.md dòng 55 tính từ ngày gửi D; YAML thu yêu cầu đến 27/12/2026, theo dõi đến 03/01/2027 và quyết định 04/01. Nếu cửa sổ mở lại tính sau lần đóng đầu, yêu cầu cuối ngày 27/12 có thể đóng trong ngày 28/12, nên cần theo dõi đến hết 04/01 và quyết định sau đó (ví dụ 05/01), hoặc chốt cutoff giờ cụ thể bảo đảm đủ cửa sổ. Nếu dùng cửa sổ khác, phải định nghĩa và giải thích nhất quán; không tính ca chưa đủ theo dõi là không mở lại. [Nguồn](https://github.com/Tiberu2611/K5-L3B-Day13-A90-LaunchEconomics/blob/a7da2b41e20231ece59f6d24578ceb92334513f1/report/team/chi_so.md#L55).
2. **Cập nhật phần rà soát luật đã lỗi phiên bản.** chi_so.md dòng 81–90 còn ghi các đề xuất chưa áp dụng, cho rằng luật chi phí sẽ kích hoạt sau hai tuần đầu và luật sử dụng thiếu tối thiểu 100 quyết định. YAML dòng 99–105 đã giới hạn luật mở lại từ bước 0,25, chi phí ở bước 0,50 và thêm 100 quyết định. Cần cập nhật bảng rà soát; không kết luận luật hiện tại còn đúng các lỗi đã được sửa. [Rà soát cũ](https://github.com/Tiberu2611/K5-L3B-Day13-A90-LaunchEconomics/blob/a7da2b41e20231ece59f6d24578ceb92334513f1/report/team/chi_so.md#L81), [YAML hiện tại](https://github.com/Tiberu2611/K5-L3B-Day13-A90-LaunchEconomics/blob/a7da2b41e20231ece59f6d24578ceb92334513f1/report/team/pilot_plan.yaml#L98).
3. **Sửa cách viết về 299 yêu cầu/người.** Điều kiện 4 của hồ sơ launch yêu cầu xác nhận đủ 299 trước ngày 14/12; YAML thực tế yêu cầu xác nhận năng lực thu mẫu trước ngày này và chỉ thu mẫu chính 14–27/12. Viết rõ đây là xác nhận năng lực; 5.980 yêu cầu/nhánh phải được thu trong cửa sổ bước 0,50, không lấy đơn hai bước đầu thay thế. [Điều kiện 4](https://github.com/Tiberu2611/K5-L3B-Day13-A90-LaunchEconomics/blob/a7da2b41e20231ece59f6d24578ceb92334513f1/report/team/ho_so_launch_v0.md#L22).

Giữ các điều kiện đã có của A90: xác nhận đủ 40 người/12 depot, ký chấp nhận đánh đổi MDE, chặn ca 7/20 và thay phút simulated bằng số đo thật. Ngưỡng 8.000 đ trong YAML dùng chi phí biến đổi; hồ sơ tóm tắt cũng cần ghi rõ cùng định nghĩa và cùng cửa sổ hai tuần ở bước 0,50.

## Câu hỏi cho đội trình

**Câu hỏi chính:** Với yêu cầu được tạo cuối ngày 27/12 và đóng trong ngày 28/12, nhóm tính cửa sổ mở lại 7 ngày từ mốc nào, chốt dữ liệu lúc nào và có thể quyết định vào 04/01 mà không tính ca chưa đủ theo dõi là thành công không?

**Trả lời của A90:**

- **Mốc tính:** nhóm tính cửa sổ 7 ngày từ `closed_at` (thời điểm đóng lần đầu), đúng với định nghĩa "đóng trong 24 giờ và không mở lại trong 7 ngày sau khi đóng". Ca chưa đủ 7 ngày theo dõi không được tính là thành công; quy tắc này đã có ở `pilot_plan.yaml` dòng 35 và 81, còn dòng 65 quy định thiếu theo dõi thì kết luận chưa đủ bằng chứng.
- **Hội đồng bắt đúng:** bản a7da2b4 chưa ghi rõ mốc `closed_at`, và `chi_so.md` dòng 55 còn viết D + 7 tính từ ngày gửi. Yêu cầu tạo cuối ngày 27/12 có thể đóng đến cuối ngày 28/12, nên cửa sổ kết thúc cuối ngày 04/01/2027. Mốc `follow_up_end: 2027-01-03` hụt 1 ngày vì nhóm cộng 7 ngày từ 27/12 mà quên 24 giờ chờ đóng. Vì vậy **không thể quyết định vào 04/01**.
- **Cách xử lý:** nhóm tiếp thu và sẽ sửa thống nhất `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md` và `group_report.md`:
  - `follow_up_end: 2027-01-04` (hết ngày, giờ Asia/Bangkok); chốt dữ liệu lúc 00:00 ngày 2027-01-05.
  - `decision_date: 2027-01-05`; lần phân tích tác động duy nhất cũng chuyển sang ngày này.
  - `chi_so.md` dòng 55: yêu cầu gửi ngày D chỉ chắc chắn đủ dữ liệu sau 24 giờ chờ đóng + 7 ngày theo dõi.
- **Kết quả:** mọi yêu cầu của bước 0.50 (14–27/12) đóng trong 24 giờ đều đủ 7 ngày theo dõi trước khi quyết định. Yêu cầu không đóng trong 24 giờ là không đạt chỉ số chính và vẫn nằm trong mẫu số.

**Câu hỏi bổ sung:** Điều kiện đủ 299 yêu cầu/người trước 14/12 là kiểm tra năng lực hay đã thu mẫu; tài liệu nào là phiên bản luật dừng cuối cùng khi chi_so.md và YAML đang khác nhau?

**Trả lời của A90:**

- **299 yêu cầu/người trước 14/12:** đây là **kiểm tra năng lực tải**, không phải đã thu đủ 299 mẫu (`pilot_plan.yaml` dòng 64). Trước bước 0.50, Trưởng nhóm CSKH xác nhận tải đủ điều kiện đạt ít nhất 299 / 14 ≈ 21,4 yêu cầu/nhân viên/ngày; nhóm sẽ ghi rõ cách kiểm tra là dùng lưu lượng thực tế ở bước 0.10–0.25. Mẫu chính chỉ thu trong 14–27/12 (dòng 61), không lấy đơn hai bước đầu thay thế. Hết 27/12 chưa đủ 299/người thì kết luận chưa đủ bằng chứng, không tự gia hạn (dòng 65). Nhóm sẽ sửa Điều kiện 4 của `ho_so_launch_v0.md` thành "kiểm tra năng lực tải".
- **Phiên bản luật dừng cuối cùng:** `report/team/pilot_plan.yaml` là bản chính thức duy nhất. Mục "Rà soát luật dừng" cuối `chi_so.md` là nhật ký góp ý của Thành viên 3 cho Thành viên 2. Cả ba góp ý đã vào YAML: (a) luật 3 chỉ chấm ở bước 0.50 và dùng phút đo thật (dòng 103); (b) luật 1 không chấm ở bước 0.10 (dòng 99–100); (c) luật 4 đòi ít nhất 100 quyết định (dòng 105). Nhóm quên cập nhật trạng thái "đã áp dụng" trong `chi_so.md` và sẽ commit đồng bộ.

## Nhận xét sau phản hồi bằng văn bản

| Điểm phản biện | Đánh giá câu trả lời | Bằng chứng còn cần xác minh |
| --- | --- | --- |
| Mốc theo dõi 7 ngày | **Giải thích phù hợp:** tính từ lần đóng đầu; yêu cầu không đóng trong 24 giờ vẫn là không đạt và nằm trong mẫu số. Theo dõi hết 04/01, chốt lúc 00:00 ngày 05/01 rồi quyết định ngày 05/01 giải quyết khoảng thiếu một ngày. | Commit sửa follow_up_end, decision_date, mốc phân tích duy nhất và mô tả chỉ số ở các file liên quan. |
| 299 yêu cầu/người | **Giải thích phù hợp:** trước 14/12 chỉ xác nhận năng lực tải tối thiểu khoảng 21,4 yêu cầu/người/ngày trong 14 ngày; mẫu chính chỉ thu 14–27/12. Không lấy đơn hai bước trước thay mẫu chính, không đủ thì chưa kết luận. | Hồ sơ launch ghi rõ kiểm tra năng lực tải thay vì đã có đủ mẫu trước bước đo chính; nhất quán với YAML. |
| Phiên bản luật dừng | **Giải thích phù hợp:** YAML là nguồn chính thức; ba góp ý đã được đưa vào YAML từ bản đã kiểm tra. Vấn đề còn lại là mục rà soát trong chi_so.md chưa được đồng bộ. | Commit đổi trạng thái góp ý đã áp dụng, cập nhật bảng rà soát và tóm tắt luật ở hồ sơ launch/báo cáo nhóm. |

**Kết luận sau phản hồi:** Chấp nhận phần giải thích về nguyên tắc; ba điểm phản biện đã được trả lời. Chưa xác nhận tài liệu đã sửa vì câu trả lời nêu sẽ sửa và sẽ commit, trong khi nhánh main vẫn ở a7da2b4 tại lượt kiểm tra này.

**Trạng thái chốt điểm:** Tạm giữ **25/30** cho phiên bản đã kiểm tra (C6: 10, C7: 10, C8: 5), **Go có điều kiện**. Sau khi nhận và xác minh commit đồng bộ đúng các nội dung trên, đề xuất nâng **C8 lên 10/10, tổng 30/30**; đây là phương án có điều kiện, chưa phải điểm đã chốt. Ghi rõ commit được kiểm tra lại trước khi đổi điểm.

**Bước tiếp theo:** Minh gửi lại A90 yêu cầu cung cấp link commit/PR đã sửa; khi nhận được thì đối chiếu nội dung trước khi cập nhật điểm. Phần trả lời của A90 phía trên được lưu theo nội dung Minh đã cung cấp.
