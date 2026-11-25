"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. In kết quả A–B, cỡ mẫu D1 và ba chỉ số E1.
Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist
import pandas as pd
from statsmodels.stats.proportion import proportion_effectsize
from statsmodels.stats.power import NormalIndPower

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CO_DINH_THANG = 40_000_000
YEU_CAU_THANG = 45_000
YEU_CAU_NGAY = 1_500


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# Công thức A1 theo docs/du_lieu_va_cong_thuc.md; giả định các lần chạy độc lập,
# cùng xác suất đúng 0 < p <= 1 và giới hạn k là số nguyên dương.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# CP2 gọi lại hàm này với tham số giá, hệ số và giới hạn chạy đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot_gioi_han = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot_gioi_han, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot_gioi_han, ['phut_xem_lai_simulated',
                               'phut_lam_lai_simulated']] = 0

    tien_token = (runs['tokens_in'] * gia_vao
                  + runs['tokens_out'] * gia_ra) / 1000
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int(reqs['ket_qua'].eq('thanh_cong').sum())
    return dict(
        token=tien_token.sum(), tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai, lam_lai=lam_lai, tong=tong, thanh_cong=thanh_cong,
        cps=tong / thanh_cong if thanh_cong else math.inf,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs)
        if len(reqs) else math.nan,
    )


def in_phan_a(runs, reqs):
    """In các bảng A2–A4 và số đối chiếu để điền báo cáo chi phí."""
    ket_qua = mo_hinh(runs, reqs)
    print('\nA2 · Mô hình chi phí từ trace (chưa gồm chi phí cố định)')
    cac_dong = [
        ('Token (đ)', 'token'),
        ('Tool (đ)', 'tool'),
        ('Trong đó: lần chạy thứ 2 và 3 (đ)', 'chay_lai'),
        ('Xem lại (đ, simulated)', 'xem_lai'),
        ('Làm lại (đ, simulated)', 'lam_lai'),
        ('Tổng chi phí (đ, simulated)', 'tong'),
        ('Số việc thành công', 'thanh_cong'),
        ('Chi phí mỗi việc thành công (đ, simulated)', 'cps'),
        ('Hoá đơn token + tool / yêu cầu (đ)', 'hoa_don_moi_yc'),
    ]
    for nhan, khoa in cac_dong:
        print(f'{nhan:48s} {ket_qua[khoa]:>14,.2f}')
    print(f'CPS / hoá đơn mỗi yêu cầu: '
          f'{ket_qua["cps"] / ket_qua["hoa_don_moi_yc"]:.2f} lần (simulated)')
    print(f'Tỉ trọng làm lại: {ket_qua["lam_lai"] / ket_qua["tong"]:.2%}; '
          f'xem lại: {ket_qua["xem_lai"] / ket_qua["tong"]:.2%} (simulated)')

    # Theo quy ước so sánh của lab: tính cả phần nhân viên làm thay
    # cho mọi yêu cầu không thành công, với mức 12.000 đ/yêu cầu.
    khong_thanh_cong = len(reqs) - ket_qua['thanh_cong']
    he_thong_moi_yc = (ket_qua['tong'] + khong_thanh_cong * BASELINE) / len(reqs)
    print(f'Chi phí cả hệ thống / yêu cầu: {he_thong_moi_yc:,.2f} đ '
          f'= {he_thong_moi_yc / BASELINE:.2f}× nhân viên tự làm (simulated)')

    print('\nA3 · Tách theo loại yêu cầu (CPS chưa gồm chi phí cố định)')
    bang_loai = []
    for loai, nhom in reqs.groupby('loai', sort=False):
        kq_loai = mo_hinh(runs, nhom)
        bang_loai.append({
            'Loại': loai,
            'Số yêu cầu': len(nhom),
            'Thành công': f'{kq_loai["thanh_cong"] / len(nhom):.1%}',
            'Lần chạy/YC': f'{nhom["so_lan_chay"].mean():.2f}',
            'CPS (đ, simulated)': f'{kq_loai["cps"]:,.2f}',
            'CPS/12.000 (simulated)': f'{kq_loai["cps"] / BASELINE:.2f}×',
        })
    print(pd.DataFrame(bang_loai).to_string(index=False))

    print('\nTỉ lệ status=ok theo loại và lần thử (để đánh giá chạy lại):')
    trace_loai = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    ti_le_ok = (trace_loai.assign(ok=trace_loai['status'].eq('ok'))
                .pivot_table(index='loai', columns='attempt', values='ok',
                             aggfunc='mean'))
    print(ti_le_ok.to_string(float_format=lambda gia_tri: f'{gia_tri:.1%}'))

    print('\nA4 · Cộng chi phí cố định cho noi_dia + hang_nang')
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pham_vi = mo_hinh(runs, pham_vi)
    # Mẫu gồm mọi loại yêu cầu: lấy thành công trong phạm vi / toàn bộ mẫu
    # để ngoại suy số việc thành công ở tổng khối lượng công ty mỗi tháng.
    ti_le_thanh_cong_trong_mau = kq_pham_vi['thanh_cong'] / len(reqs)
    print(f'Phạm vi: {len(pham_vi)} yêu cầu, {kq_pham_vi["thanh_cong"]} thành công; '
          f'CPS biến đổi: {kq_pham_vi["cps"]:,.2f} đ (simulated)')
    bang_co_dinh = []
    for khoi_luong in (YEU_CAU_THANG, YEU_CAU_THANG / 2):
        thanh_cong_thang = khoi_luong * ti_le_thanh_cong_trong_mau
        co_dinh_moi_viec = CO_DINH_THANG / thanh_cong_thang
        cps_co_co_dinh = kq_pham_vi['cps'] + co_dinh_moi_viec
        bang_co_dinh.append({
            'Yêu cầu/tháng': f'{khoi_luong:,.0f}',
            'Thành công/tháng': f'{thanh_cong_thang:,.0f}',
            'Cố định/việc (đ)': f'{co_dinh_moi_viec:,.2f}',
            'CPS + cố định (đ, simulated)': f'{cps_co_co_dinh:,.2f}',
            'CPS/12.000 (simulated)': f'{cps_co_co_dinh / BASELINE:.2f}×',
        })
    print(pd.DataFrame(bang_co_dinh).to_string(index=False))
    print('Cột CPS/12.000 ở A3–A4 chỉ so chi phí mỗi việc thành công; '
          'để kết luận tiết kiệm cho công ty phải cộng phần nhân viên làm thay.')


# ---------- Nhiệm vụ B · Độ nhạy và chi phí cả hệ thống ----------
def phan_tich_do_nhay(runs, reqs):
    """Tính B1–B4 từ dữ liệu; các chi phí có dùng thời gian simulated.

    B1–B3 dùng toàn bộ mẫu. B4 chỉ xét noi_dia + hang_nang,
    xem lại một lần cho mỗi yêu cầu có ít nhất một run status=ok.
    Các kịch bản B chưa cộng chi phí cố định.
    """
    goc = mo_hinh(runs, reqs)
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=GIA_VAO * 2, gia_ra=GIA_RA * 2),
        'Giá token giảm một nửa': dict(gia_vao=GIA_VAO / 2, gia_ra=GIA_RA / 2),
        'Tỉ lệ xem lại gấp đôi': dict(he_so_xem_lai=2),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi': dict(he_so_lam_lai=2),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%': dict(luong_phut=LUONG_PHUT * 1.25),
        'Chỉ cho chạy tối đa 2 lần': dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần': dict(max_lan_chay=1),
    }
    b1 = []
    for ten, tham_so in kich_ban.items():
        cps = mo_hinh(runs, reqs, **tham_so)['cps']
        b1.append(dict(kich_ban=ten, cps=cps,
                       thay_doi_pct=(cps / goc['cps'] - 1) * 100))

    cps_cap = mo_hinh(runs, reqs, gia_vao=GIA_VAO * 2,
                      gia_ra=GIA_RA * 2, he_so_xem_lai=2)['cps']
    b2 = dict(cps=cps_cap, thay_doi_pct=(cps_cap / goc['cps'] - 1) * 100)
    # So các kịch bản tăng chi phí để mỗi yếu tố chỉ xuất hiện một lần.
    xep_hang = sorted((dong for dong in b1 if dong['thay_doi_pct'] > 0),
                      key=lambda dong: dong['thay_doi_pct'], reverse=True)[:3]

    b3 = []
    for gioi_han in (1, 2, 3):
        kq = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        khong_thanh_cong = len(reqs) - kq['thanh_cong']
        b3.append(dict(gioi_han=gioi_han, tong=kq['tong'],
                       khong_thanh_cong=khong_thanh_cong,
                       he_thong=kq['tong'] + khong_thanh_cong * BASELINE,
                       cps=kq['cps']))

    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    trace = runs[runs['request_id'].isin(pham_vi['request_id'])]
    so_xem_lai = trace.loc[trace['status'].eq('ok'), 'request_id'].nunique()
    so_lam_lai = int(pham_vi['ket_qua'].eq('lam_lai').sum())
    kq_pham_vi = mo_hinh(runs, pham_vi)
    token_tool = kq_pham_vi['token'] + kq_pham_vi['tool']
    tien_xem_lai = so_xem_lai * 5 * LUONG_PHUT
    # Theo hướng dẫn B4: trung bình trên các ca làm lại của TOÀN BỘ mẫu,
    # làm tròn một chữ số thập phân trước khi tính kịch bản độ nhạy.
    phut_tb = round(reqs.loc[reqs['ket_qua'].eq('lam_lai'),
                             'phut_lam_lai_simulated'].mean(), 1)
    b4 = []
    for phut_lam_lai in (9, phut_tb):
        tien_lam_lai = so_lam_lai * phut_lam_lai * LUONG_PHUT
        tong = token_tool + tien_xem_lai + tien_lam_lai
        cps = tong / kq_pham_vi['thanh_cong']
        # So sánh với nhân viên tự làm trên cùng mẫu số yêu cầu.
        khong_thanh_cong = len(pham_vi) - kq_pham_vi['thanh_cong']
        he_thong_moi_yc = (tong + khong_thanh_cong * BASELINE) / len(pham_vi)
        phut_xem_hoa_von = (BASELINE * kq_pham_vi['thanh_cong']
                            - token_tool - tien_lam_lai) / (so_xem_lai * LUONG_PHUT)
        b4.append(dict(phut_lam_lai=phut_lam_lai, so_yeu_cau=len(pham_vi),
                       so_xem_lai=so_xem_lai, so_lam_lai=so_lam_lai,
                       thanh_cong=kq_pham_vi['thanh_cong'], token_tool=token_tool,
                       xem_lai=tien_xem_lai, lam_lai=tien_lam_lai, tong=tong,
                       cps=cps, so_voi_nhan_vien=cps / BASELINE,
                       phut_xem_hoa_von=phut_xem_hoa_von,
                       he_thong_moi_yc=he_thong_moi_yc))
    return dict(goc=goc, b1=b1, b2=b2, xep_hang=xep_hang, b3=b3, b4=b4)


def in_phan_b(ket_qua):
    """In bảng B1–B4 để đối chiếu và bàn giao cho người giữ bảng chi phí."""
    print('\nB · Các chi phí và mức thay đổi dưới đây là simulated, chưa gồm cố định.')
    print('\nB1 · Đổi từng yếu tố')
    print(f'CPS gốc: {ket_qua["goc"]["cps"]:,.2f} đ (simulated)')
    print(f'{"Kịch bản":32s} {"CPS (đ, simulated)":>19s} {"Thay đổi (%)":>15s}')
    for dong in ket_qua['b1']:
        print(f'{dong["kich_ban"]:32s} {dong["cps"]:>19,.2f} '
              f'{dong["thay_doi_pct"]:>+15.2f}')

    print('\nB2 · Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi')
    print(f'CPS: {ket_qua["b2"]["cps"]:,.2f} đ; '
          f'thay đổi {ket_qua["b2"]["thay_doi_pct"]:+.2f}% (simulated)')
    print('Mô hình cộng tuyến tính: tác động của cặp bằng tổng hai tác động riêng.')
    print('Ba yếu tố ảnh hưởng mạnh nhất trong các kịch bản tăng chi phí:')
    for hang, dong in enumerate(ket_qua['xep_hang'], 1):
        print(f'{hang}. {dong["kich_ban"]}: +{dong["thay_doi_pct"]:.2f}% (simulated)')

    print('\nB3 · Giới hạn chạy lại (chi phí là simulated)')
    bang_gioi_han = pd.DataFrame(ket_qua['b3']).rename(columns={
        'gioi_han': 'Tối đa lần chạy', 'tong': 'Tổng trợ lý (đ)',
        'khong_thanh_cong': 'Không thành công', 'he_thong': 'Cả hệ thống (đ)',
        'cps': 'CPS (đ)',
    })
    print(bang_gioi_han.to_string(index=False, float_format=lambda so: f'{so:,.2f}'))
    re_nhat = min(ket_qua['b3'], key=lambda dong: dong['he_thong'])
    cps_thap_nhat = min(ket_qua['b3'], key=lambda dong: dong['cps'])
    print(f'Cả hệ thống rẻ nhất: {re_nhat["gioi_han"]} lần chạy '
          f'({re_nhat["he_thong"]:,.2f} đ, simulated).')
    print(f'CPS thấp nhất: {cps_thap_nhat["gioi_han"]} lần chạy '
          f'({cps_thap_nhat["cps"]:,.2f} đ, simulated).')
    print(f'Giới hạn {cps_thap_nhat["gioi_han"]} lần đẩy thêm '
          f'{cps_thap_nhat["khong_thanh_cong"] - re_nhat["khong_thanh_cong"]} '
          'yêu cầu sang nhân viên so với phương án rẻ nhất cho cả hệ thống.')

    print('\nB4 · Xem lại 100% với noi_dia + hang_nang (simulated)')
    dau = ket_qua['b4'][0]
    print(f'{dau["so_yeu_cau"]} yêu cầu; {dau["so_xem_lai"]} có run ok, '
          f'mỗi yêu cầu xem lại 5 phút; {dau["so_lam_lai"]} ca làm lại; '
          f'{dau["thanh_cong"]} việc thành công.')
    print(f'Token + tool: {dau["token_tool"]:,.2f} đ; '
          f'xem lại: {dau["xem_lai"]:,.2f} đ (simulated).')
    for dong in ket_qua['b4']:
        print(f'Làm lại {dong["phut_lam_lai"]:.1f} phút/ca: '
              f'tiền làm lại {dong["lam_lai"]:,.2f} đ; tổng {dong["tong"]:,.2f} đ; '
              f'CPS {dong["cps"]:,.2f} đ = {dong["so_voi_nhan_vien"]:.2f}× '
              '12.000 đ (simulated).')
        print(f'  Hoà vốn theo CPS: xem lại ≤ {dong["phut_xem_hoa_von"]:.2f} phút/ca; '
              f'cả hệ thống / yêu cầu: {dong["he_thong_moi_yc"]:,.2f} đ '
              '(đã cộng nhân viên làm thay, simulated).')
    print('Kịch bản thứ hai dùng phút làm lại trung bình toàn mẫu, làm tròn 1 chữ số '
          'thập phân (simulated). Pilot cần đo thời gian xem lại/làm lại thực tế '
          'và mức có thể giảm xem lại an toàn.')


# ---------- Nhiệm vụ D · Cỡ mẫu và tỉ lệ mở lại hiện tại ----------
def co_mau(p1, p2, alpha=0.05, power=0.80):
    """Cỡ mẫu mỗi nhóm khi so sánh hai tỉ lệ p1, p2 (kiểm định hai phía)."""
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil(
        (za * math.sqrt(2 * pb * (1 - pb))
         + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2
        / (p2 - p1) ** 2
    )


def phan_tich_co_mau(reqs, p1=0.70, mde_5=0.05, mde_6=0.06,
                     alpha=0.05, power=0.80, icc=0.02,
                     m_hien_tai=75, c_nhan_vien=20, c_depot=6):
    """Tính 5 câu D1, power thực tế nếu hiệu ứng thật là 5 điểm, và tỉ lệ mở lại 7 ngày."""
    n_5 = co_mau(p1, p1 + mde_5, alpha=alpha, power=power)
    de_75 = 1 + (m_hien_tai - 1) * icc
    n_75 = math.ceil(n_5 * de_75)
    nv_moi_nhom = math.ceil(n_75 / m_hien_tai)

    eff_max_nv = c_nhan_vien / icc
    eff_max_depot = c_depot / icc

    n_6 = co_mau(p1, p1 + mde_6, alpha=alpha, power=power)
    m_min_6 = math.ceil(n_6 * (1 - icc) / (c_nhan_vien - n_6 * icc))
    de_6 = 1 + (m_min_6 - 1) * icc

    # Power khi thiết kế cho 6 điểm (n_eff = n_6) nhưng tác động thật chỉ 5 điểm
    es_5 = proportion_effectsize(p1 + mde_5, p1)
    power_neu_5 = NormalIndPower().power(effect_size=es_5, nobs1=n_6,
                                         alpha=alpha, ratio=1.0)

    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    mo_lai_toan_mau = reqs['mo_lai_trong_7_ngay'].mean()
    mo_lai_pham_vi = pham_vi['mo_lai_trong_7_ngay'].mean()
    yeu_cau_moi_nguoi_ngay = YEU_CAU_NGAY / (2 * c_nhan_vien)
    ti_trong_pham_vi = len(pham_vi) / len(reqs)

    return dict(
        n_5=n_5, de_75=de_75, n_75=n_75, nv_moi_nhom=nv_moi_nhom,
        eff_max_nv=eff_max_nv, eff_max_depot=eff_max_depot,
        n_6=n_6, m_min_6=m_min_6, de_6=de_6, power_neu_5=power_neu_5,
        n_raw_6=c_nhan_vien * m_min_6,
        n_eff_6=c_nhan_vien * m_min_6 / de_6,
        ngay_thu_mau_toan_bo=math.ceil(m_min_6 / yeu_cau_moi_nguoi_ngay),
        ngay_thu_mau_pham_vi=math.ceil(
            m_min_6 / (yeu_cau_moi_nguoi_ngay * ti_trong_pham_vi)),
        mo_lai_toan_mau=mo_lai_toan_mau,
        so_mo_lai_toan_mau=int(reqs['mo_lai_trong_7_ngay'].sum()),
        n_toan_mau=len(reqs),
        mo_lai_pham_vi=mo_lai_pham_vi,
        so_mo_lai_pham_vi=int(pham_vi['mo_lai_trong_7_ngay'].sum()),
        n_pham_vi=len(pham_vi),
    )


def in_phan_d(kq):
    """In kết quả D1 và tỉ lệ mở lại 7 ngày hiện tại."""
    print('\nD1 · Cỡ mẫu pilot (p1=0,70; alpha=0,05; power=0,80; ICC=0,02)')
    print(f'a) Chia theo yêu cầu (MDE +5 điểm): {kq["n_5"]:,} yêu cầu/nhóm')
    print(f'b) Theo nhân viên, m=75 (DE={kq["de_75"]:.2f}): '
          f'{kq["n_75"]:,} yêu cầu/nhóm → {kq["nv_moi_nhom"]} nhân viên/nhóm '
          f'(tổng {kq["nv_moi_nhom"] * 2} > 40: không đủ người)')
    print(f'c) 20 nhân viên/nhóm: cỡ mẫu hiệu dụng tối đa = '
          f'{kq["eff_max_nv"]:,.0f} < {kq["n_5"]:,} (không đạt 5 điểm)')
    print(f'd) 6 depot/nhóm: cỡ mẫu hiệu dụng tối đa = '
          f'{kq["eff_max_depot"]:,.0f} < {kq["n_5"]:,} (không đạt)')
    print(f'e) MDE +6 điểm ({kq["n_6"]:,}/nhóm), 20 nhân viên/nhóm: '
          f'm ≥ {kq["m_min_6"]} yêu cầu/người (DE={kq["de_6"]:.2f})')
    print(f'   Lưu ý bất lợi: nếu tác động thật chỉ +5 điểm với n={kq["n_6"]}, '
          f'power còn {kq["power_neu_5"]:.2f}')
    print(f'   Cần {kq["n_raw_6"]:,} yêu cầu thô/nhóm, tương đương '
          f'{kq["n_eff_6"]:,.2f} quan sát hiệu dụng; chỉ thu ở bước 20 người.')
    print(f'   Ước tính thu mẫu với 1.500 yêu cầu/ngày, chia đều cho 40 người: '
          f'{kq["ngay_thu_mau_toan_bo"]} ngày nếu toàn bộ loại yêu cầu; '
          f'{kq["ngay_thu_mau_pham_vi"]} ngày nếu chỉ noi_dia + hang_nang '
          '(giả định cơ cấu mẫu giữ nguyên). Sau đó vẫn cần cửa sổ theo dõi 7 ngày.')
    print(f'Tỉ lệ mở lại trong 7 ngày hiện tại: '
          f'toàn mẫu {kq["mo_lai_toan_mau"]:.2%} '
          f'({kq["so_mo_lai_toan_mau"]}/{kq["n_toan_mau"]}); '
          f'phạm vi noi_dia+hang_nang {kq["mo_lai_pham_vi"]:.2%} '
          f'({kq["so_mo_lai_pham_vi"]}/{kq["n_pham_vi"]})')


# ---------- Nhiệm vụ E · Chỉ số và rủi ro chi phí ở từng bước rollout ----------
def kinh_te_rollout(runs, reqs):
    """Ngoại suy theo 40 nhân viên, phân bổ đều việc và cơ cấu mẫu giữ nguyên.

    Giả định cả 40 triệu đ/tháng được phân bổ cho bước pilot đang xét.
    CPS biến đổi dùng cho luật dừng 8.000 đ; cố định được theo dõi riêng.
    """
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq = mo_hinh(runs, pham_vi)
    bang = []
    for so_nguoi in (4, 10, 20):
        thanh_cong_thang = (YEU_CAU_THANG * so_nguoi / 40
                            * kq['thanh_cong'] / len(reqs))
        co_dinh_moi_viec = CO_DINH_THANG / thanh_cong_thang
        bang.append(dict(so_nguoi=so_nguoi, thanh_cong_thang=thanh_cong_thang,
                         cps_bien_doi=kq['cps'], co_dinh_moi_viec=co_dinh_moi_viec,
                         cps_day_du=kq['cps'] + co_dinh_moi_viec))
    return bang


def tinh_chi_so_e(reqs):
    """Tính 3 chỉ số (chính, dùng, an toàn) trên 1.200 yêu cầu chạy thử."""
    chinh_mask = (reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    bo_qua_mask = xem['quyet_dinh_xem_lai'].isin(['sua', 'bo'])
    an_toan_mask = reqs['mo_lai_trong_7_ngay'] == 1
    return dict(
        chinh=chinh_mask.mean(),
        chinh_tu=int(chinh_mask.sum()),
        chinh_mau=len(reqs),
        bo_qua=bo_qua_mask.mean(),
        bo_qua_tu=int(bo_qua_mask.sum()),
        bo_qua_mau=len(xem),
        an_toan=an_toan_mask.mean(),
        an_toan_tu=int(an_toan_mask.sum()),
        an_toan_mau=len(reqs),
    )


def in_phan_e(kq):
    """In 3 chỉ số E1 (lưu ý chưa có đối chứng nên không kết luận nâng chỉ số)."""
    print('\nE1 · Ba chỉ số tính thử trên 1.200 yêu cầu (chỉ số trong đợt chạy thử)')
    print(f'- Chính (% đóng trong 24h và không mở lại 7 ngày): '
          f'{kq["chinh"]:.2%} ({kq["chinh_tu"]}/{kq["chinh_mau"]})')
    print(f'- Dùng (tỉ lệ bỏ qua gợi ý = (sua+bo)/được xem lại): '
          f'{kq["bo_qua"]:.2%} ({kq["bo_qua_tu"]}/{kq["bo_qua_mau"]})')
    print(f'- An toàn (% mở lại trong 7 ngày): '
          f'{kq["an_toan"]:.2%} ({kq["an_toan_tu"]}/{kq["an_toan_mau"]})')


def in_kinh_te_rollout(bang):
    print('\nE2 · Cố định khi pilot còn ít người (chi phí simulated)')
    print('Phạm vi noi_dia + hang_nang; ngoại suy đều việc, '
          'cả 40 triệu đ/tháng được phân bổ cho pilot; chưa tính nhân viên làm thay.')
    print(pd.DataFrame(bang).rename(columns={
        'so_nguoi': 'Người dùng', 'thanh_cong_thang': 'Thành công/tháng',
        'cps_bien_doi': 'CPS biến đổi (đ)', 'co_dinh_moi_viec': 'Cố định/việc (đ)',
        'cps_day_du': 'CPS + cố định (đ)',
    }).to_string(index=False, float_format=lambda so: f'{so:,.2f}'))
    print('Ngưỡng dừng 8.000 đ chỉ dùng CPS biến đổi; '
          'chi phí cố định dùng để đánh giá ngân sách/hợp đồng riêng.')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    in_phan_a(runs, reqs)
    in_phan_b(phan_tich_do_nhay(runs, reqs))
    in_phan_d(phan_tich_co_mau(reqs))
    in_phan_e(tinh_chi_so_e(reqs))
    in_kinh_te_rollout(kinh_te_rollout(runs, reqs))
