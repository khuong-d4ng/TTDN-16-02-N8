# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import date

class VanBanDen(models.Model):
    _name = 'van_ban_den'
    _description = 'Văn bản đến'
   
    
    company_id = fields.Many2one('res.company', string='Công ty', 
        default=lambda self: self.env.company)

    name = fields.Char(string='Số văn bản', required=True)
    trich_yeu = fields.Text(string='Trích yếu', required=True)
    ngay_van_ban = fields.Date(string='Ngày văn bản', default=fields.Date.today)
    ngay_den = fields.Date(string='Ngày đến', default=fields.Date.today)
    so_den = fields.Char(string='Số đến')
    co_quan_ban_hanh = fields.Char(string='Cơ quan ban hành')
    nguoi_ky = fields.Char(string='Người ký')
    loai_van_ban = fields.Selection([
        ('quyet_dinh', 'Quyết định'),
        ('cong_van', 'Công văn'),
        ('thong_bao', 'Thông báo'),
        ('ke_hoach', 'Kế hoạch'),
        ('bao_cao', 'Báo cáo'),
        ('to_trinh', 'Tờ trình'),
        ('khac', 'Khác'),
    ], string='Loại văn bản', default='cong_van')
    do_khan = fields.Selection([
        ('thuong', 'Thường'),
        ('khan', 'Khẩn'),
        ('hoa_toc', 'Hỏa tốc'),
    ], string='Độ khẩn', default='thuong')
    do_mat = fields.Selection([
        ('binh_thuong', 'Bình thường'),
        ('mat', 'Mật'),
        ('tuyet_mat', 'Tuyệt mật'),
    ], string='Độ mật', default='binh_thuong')
    trang_thai = fields.Selection([
        ('moi', 'Mới'),
        ('dang_xu_ly', 'Đang xử lý'),
        ('da_xu_ly', 'Đã xử lý'),
    ], string='Trạng thái', default='moi')
    file_dinh_kem = fields.Binary(string='File đính kèm')
    file_name = fields.Char(string='Tên file') 