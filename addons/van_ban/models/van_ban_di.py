# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import date

class VanBanDi(models.Model):
    _name = 'van_ban_di'
    _description = 'Văn bản đi'
    
    company_id = fields.Many2one('res.company', string='Công ty', 
        default=lambda self: self.env.company)
    
    name = fields.Char(string='Số văn bản', required=True)
    trich_yeu = fields.Text(string='Trích yếu', required=True)
    ngay_van_ban = fields.Date(string='Ngày văn bản', default=fields.Date.today)
    ngay_gui = fields.Date(string='Ngày gửi', default=fields.Date.today)
    so_di = fields.Char(string='Số đi')
    noi_nhan = fields.Text(string='Nơi nhận')
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
        ('du_thao', 'Dự thảo'),
        ('cho_duyet', 'Chờ duyệt'),
        ('da_duyet', 'Đã duyệt'),
        ('da_gui', 'Đã gửi'),
    ], string='Trạng thái', default='du_thao')
    file_dinh_kem = fields.Binary(string='File đính kèm')
    file_name = fields.Char(string='Tên file') 