# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import date

class HoSoVanBan(models.Model):
    _name = 'ho_so_van_ban'
    _description = 'Hồ sơ văn bản'
    
    name = fields.Char(string='Số hồ sơ', required=True)
    ten_ho_so = fields.Char(string='Tên hồ sơ', required=True)
    ma_ho_so = fields.Char(string='Mã hồ sơ')
    thoi_gian_bat_dau = fields.Date(string='Thời gian bắt đầu', default=fields.Date.today)
    thoi_gian_ket_thuc = fields.Date(string='Thời gian kết thúc')
    nguoi_lap = fields.Many2one('res.users', string='Người lập', default=lambda self: self.env.user)
    don_vi = fields.Char(string='Đơn vị')
    
    trang_thai = fields.Selection([
        ('dang_xu_ly', 'Đang xử lý'),
        ('da_hoan_thanh', 'Đã hoàn thành'),
        ('tam_dung', 'Tạm dừng'),
        ('huy_bo', 'Hủy bỏ')
    ], string='Trạng thái', default='dang_xu_ly')
    
    loai_ho_so = fields.Selection([
        ('hanh_chinh', 'Hành chính'),
        ('nhan_su', 'Nhân sự'),
        ('tai_chinh', 'Tài chính'),
        ('du_an', 'Dự án'),
        ('khac', 'Khác')
    ], string='Loại hồ sơ', default='hanh_chinh')
    
    muc_do_bao_mat = fields.Selection([
        ('binh_thuong', 'Bình thường'),
        ('mat', 'Mật'),
        ('tuyet_mat', 'Tuyệt mật')
    ], string='Mức độ bảo mật', default='binh_thuong')
    
    mo_ta = fields.Text(string='Mô tả')
    ghi_chu = fields.Text(string='Ghi chú')
    
    # Sửa lại định nghĩa many2many với relation và column khác nhau
    van_ban_den_ids = fields.Many2many(
        'van_ban_den',
        'ho_so_van_ban_den_rel',  # tên bảng trung gian cho văn bản đến
        'ho_so_id',               # tên cột cho hồ sơ trong bảng trung gian
        'van_ban_den_id',         # tên cột cho văn bản đến trong bảng trung gian
        string='Văn bản đến'
    )
    
    van_ban_di_ids = fields.Many2many(
        'van_ban_di',
        'ho_so_van_ban_di_rel',   # tên bảng trung gian cho văn bản đi
        'ho_so_id',               # tên cột cho hồ sơ trong bảng trung gian
        'van_ban_di_id',          # tên cột cho văn bản đi trong bảng trung gian
        string='Văn bản đi'
    )
    
    file_dinh_kem = fields.Binary(string='File đính kèm')
    file_name = fields.Char(string='Tên file')