# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Tỉ lệ yêu cầu có gợi ý hiển thị trên nhóm can thiệp | Số yêu cầu phân biệt của nhóm can thiệp có event `agent_suggestion_shown` chia tổng số yêu cầu nhóm can thiệp | Không cần tính |
| An toàn | Tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu | Số đơn lệch tiền trong `audit_sample_checked` chia tổng số đơn được kiểm tra mẫu hằng tuần | Không cần tính |

Chỉ số chính trong đợt chạy thử là **82,83%** (994/1.200), tỉ lệ bỏ qua gợi ý là **27,12%** (48/177) và tỉ lệ lỗi lọt đến khách là **4,25%** (51/1.200); không viết "trợ lý đã nâng chỉ số" vì đợt chạy thử không có nhóm đối chứng.

## Danh sách event

13 event đề xuất, mỗi event có `trace_id` để nối với trace của agent. Trường chung: `event_id`, `event_at`, `request_id`, `trace_id`; nối với `refund_request_created` để lấy `arm`, `staff_id`, `depot`, loại yêu cầu và bước rollout. Khử trùng theo `event_id`; mỗi chỉ số cấp yêu cầu đếm `request_id` phân biệt.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách / hệ thống phân công | `request_id`, `loai`, `so_tien_vnd`, `arm`, `staff_id`, `depot`, `rollout_stage`, `created_at`, `trace_id` | Khi tạo yêu cầu; bổ sung nhân viên/depot khi phân công, giữ nguyên arm |
| `agent_run_completed` | Agent | `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý của trợ lý hiện ra cho nhân viên |
| `staff_review_decision` | Nhân viên | `quyet_dinh` (`giu`/`sua`/`bo`), `phut_xem_lai`, `trace_id` | Khi nhân viên bấm gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | `phut_lam_lai`, `ly_do`, `trace_id` | Khi nhân viên làm lại xong ca lỗi |
| `refund_ledger_write` | Dịch vụ sổ cái | `refund_id`, `order_id`, `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Sau mỗi lần ghi sổ, kể cả lỗi; phát hiện hai giao dịch thành công cho cùng nghĩa vụ hoàn phí |
| `handoff_to_staff` | Agent | `reason`, `tom_tat`, `trace_id` | Khi agent chuyển yêu cầu sang nhân viên |
| `ticket_closed` | Hệ thống ticket | `closed_at`, `trace_id` | Khi yêu cầu được đóng |
| `ticket_reopened` | Khách | `reopened_at`, `reason`, `trace_id` | Khi khách mở lại yêu cầu |
| `audit_sample_checked` | Kế toán | `audit_id`, `so_tien_da_hoan`, `so_tien_dung`, `price_table_version`, `trace_id` | Khi kiểm tra mẫu đối soát hằng tuần |
| `input_validation_failed` | Giao diện / dịch vụ kiểm tra đầu vào | `field`, `reason`, `trace_id` | Khi đầu vào sai định dạng; đo ngưỡng 2%/ngày trong bảng lỗi |
| `refund_notification_sent` | Dịch vụ thông báo | `message_type`, `refund_id`, `delivery_status`, `trace_id` | Khi gửi thông báo; đối soát thông báo đã hoàn với giao dịch sổ cái thành công |
| `refund_outcome_finalized` | Hệ thống quản lý yêu cầu | `ket_qua` (`thanh_cong`/`lam_lai`/`chuyen_nhan_vien`), `finalized_at`, `reason`, `trace_id` | Khi kết quả yêu cầu đủ theo dõi; giữ lịch sử điều chỉnh nếu đối soát phát hiện sai tiền |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **% yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày:** lấy lần đóng đầu tiên từ `ticket_closed`, yêu cầu `0 <= closed_at - created_at <= 24h` và không có `ticket_reopened` trong khoảng `(closed_at, closed_at + 7 ngày]`; mẫu số là các yêu cầu thuộc cohort đã hoàn tất theo dõi. Yêu cầu không đóng trong 24 giờ là không đạt, không loại khỏi mẫu số.
- **Tỉ lệ bỏ qua gợi ý:** tính từ `agent_suggestion_shown` và `staff_review_decision` (`quyet_dinh` là `sua` hoặc `bo` chia tổng số ca được xem lại).
- **Tỉ lệ mở lại (chỉ báo thay thế cho lỗi lọt):** số yêu cầu phân biệt có `ticket_reopened` trong 7 ngày sau lần đóng đầu chia tổng số yêu cầu cohort đã đủ theo dõi. Không mở lại chưa bảo đảm không sai; đối soát mẫu bổ sung khả năng bắt lỗi ngầm.
- **Tỉ lệ yêu cầu có gợi ý hiển thị trên nhóm can thiệp:** số `request_id` phân biệt có `agent_suggestion_shown` chia tổng yêu cầu `refund_request_created` cùng cohort, lọc `arm = can_thiep`; chỉ số đo mức hiển thị gợi ý.
- **Tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu:** tính từ `audit_sample_checked` (`so_tien_da_hoan != so_tien_dung` chia tổng số bản ghi kiểm tra trong tuần).

Pilot chỉ tính tác động chính ở bước 0,50 (20 nhân viên mỗi nhánh), cùng cửa sổ thời gian và phạm vi cho hai nhánh. Ngày quyết định dự kiến **20/01/2027** sau khi cohort cuối đủ 7 ngày theo dõi; không coi yêu cầu chưa đủ theo dõi là thành công. Định nghĩa và cách khử trùng được chốt trước pilot; các giá trị tính thử phía trên lấy trực tiếp từ cờ kết quả của CSV.

**Đo các luật dừng CP4:**

| Chỉ số / sự cố | Event và cách tính | Thời điểm / phạm vi áp dụng | Người phụ trách |
| --- | --- | --- | --- |
| Hoàn trùng hoặc báo hoàn sai | Đối soát `refund_ledger_write` theo `order_id` và nghĩa vụ hoàn phí, nối `refund_notification_sent` theo `refund_id`/`trace_id`; phát hiện giao dịch trùng hoặc thông báo đã hoàn khi sổ cái không thành công | Mọi bước 4/10/20 người; cảnh báo ngay, tắt trong 30 phút | Giám đốc vận hành LogiX-VN |
| Trần mở lại > 6% | Dùng `ticket_closed`, `ticket_reopened`, `refund_request_created`; số yêu cầu mở lại / số yêu cầu cohort đã đủ theo dõi | Đánh giá hằng ngày, mọi bước; chưa đủ 7 ngày thì chưa xác nhận an toàn để tăng bước | Giám đốc vận hành LogiX-VN |
| Chênh mở lại ≥ 2 điểm phần trăm | Tỉ lệ mở lại can thiệp trừ đối chứng, cùng phạm vi và cửa sổ theo dõi | Chỉ từ bước ít nhất 10 người dùng trợ lý, đối chứng 20; vi phạm 3 lần đánh giá hằng ngày liên tiếp thì dừng | Giám đốc vận hành LogiX-VN |
| CPS biến đổi > 8.000 đ | Token/tool của mọi `agent_run_completed` + phút thực tế từ `staff_review_decision`, `staff_rework_completed` × 2.000 đ, chia số `refund_outcome_finalized` thành công cùng cohort; không cộng cố định | Theo tuần đủ theo dõi, vi phạm 2 tuần liên tiếp; không có thành công thì CPS vô hạn, kết quả chưa đủ theo dõi thì chưa tăng bước | PM trợ lý hoàn phí |
| Bỏ qua gợi ý > 40% | `staff_review_decision`: số yêu cầu quyết định sửa/bỏ chia số yêu cầu được xem lại | Theo tuần; phỏng vấn 5 nhân viên trong 3 ngày, chưa xử lý thì chưa tăng bước; mẫu số 0 ghi chưa có dữ liệu | Trưởng nhóm CSKH |

## E2 · Rủi ro kinh tế

Các dòng độ nhạy lấy số từ `bang_chi_phi.md`; kịch bản cố định theo số người được tính thêm bằng `kinh_te_rollout` trong `src/lab13.py`. Các giá trị chi phí đều có nhãn simulated.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,77%, lên **6.787 đ/việc** (simulated) | Tỉ lệ làm lại theo tuần > 7% | Thu hẹp về `noi_dia`, rà 20 `trace_id` làm lại gần nhất | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | **11.743 đ = 0,98×** với 9 phút làm lại/ca; lên **12.415 đ = 1,03×** nếu làm lại 15,3 phút/ca (simulated) | Tỉ lệ yêu cầu được xem lại > 50% cuối bước rollout 0,25 | Giảm tỉ lệ xem lại theo bậc khi tỉ lệ sửa + bỏ < 15% | Trưởng nhóm CSKH |
| Khối lượng chỉ đạt một nửa kế hoạch | Chi phí cố định 40 triệu đ/tháng tăng từ 1.185 đ lên 2.370 đ/việc; CPS phạm vi pilot tăng từ 4.599 đ (0,38×) lên **5.784 đ (0,48×)** (simulated) | Số việc thành công theo tuần < 50% kế hoạch | Dừng mở rộng pilot, rà soát lại chi phí cố định và điều kiện chuyển giao | PM trợ lý hoàn phí |
| Pilot ít người gánh toàn bộ 40 triệu đ/tháng | Với 4/10/20 người và việc phân bổ đều, CPS biến đổi khoảng **3.414 đ**, CPS cộng cố định lần lượt khoảng **15.266 / 8.155 / 5.784 đ** (simulated) | Theo dõi riêng CPS biến đổi và cố định/việc ở từng bước; so số việc thành công thực tế với dự toán | Ngưỡng dừng 8.000 đ chỉ xét CPS biến đổi; PM duyệt lại ngân sách/hợp đồng khi cố định cao, không coi cố định cao là chất lượng agent giảm | PM trợ lý hoàn phí |

Kịch bản cuối giả định pilot chịu toàn bộ cố định, cơ cấu loại yêu cầu và năng suất chia đều giữ như mẫu. Đây là chi phí mỗi việc agent thành công, chưa cộng nhân viên làm thay. Với 4 người, ngoại suy **3.375 việc thành công/tháng**, cố định **11.852 đ/việc** (simulated); phải ghi giả định khi trình hội đồng, không suy ra từ số CPS này rằng agent vi phạm ngưỡng biến đổi 8.000 đ.
