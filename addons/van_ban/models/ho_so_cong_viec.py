# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import date

class HoSoCongViec(models.Model):
    _name = 'ho_so_cong_viec'
    _description = 'Hồ sơ công việc'
    
    name = fields.Char(string='Mã công việc', required=True)
    ten_cong_viec = fields.Char(string='Tên công việc', required=True)
    mo_ta = fields.Text(string='Mô tả công việc')
    
    nguoi_giao = fields.Many2one('res.users', string='Người giao', default=lambda self: self.env.user, readonly=True)
    nguoi_thuc_hien = fields.Many2many('res.users', 'ho_so_cong_viec_thuc_hien_rel', 'cong_viec_id', 'user_id', string='Người thực hiện', readonly=True)
    nguoi_phoi_hop = fields.Many2many('res.users', 'ho_so_cong_viec_phoi_hop_rel', 'cong_viec_id', 'user_id', string='Người phối hợp', readonly=True)
    
    ngay_giao = fields.Date(string='Ngày giao', default=fields.Date.today)
    han_hoan_thanh = fields.Date(string='Hạn hoàn thành')
    ngay_hoan_thanh = fields.Date(string='Ngày hoàn thành')
    
    muc_do_uu_tien = fields.Selection([
        ('thap', 'Thấp'),
        ('trung_binh', 'Trung bình'),
        ('cao', 'Cao'),
        ('rat_cao', 'Rất cao')
    ], string='Mức độ ưu tiên', default='trung_binh')
    
    trang_thai = fields.Selection([
        ('moi', 'Mới'),
        ('dang_thuc_hien', 'Đang thực hiện'),
        ('cho_xac_nhan', 'Chờ xác nhận'),
        ('hoan_thanh', 'Hoàn thành'),
        ('tam_dung', 'Tạm dừng'),
        ('huy', 'Hủy')
    ], string='Trạng thái', default='moi')
    
    tien_do = fields.Float(string='Tiến độ (%)', default=0)
        
    van_ban_lien_quan_ids = fields.Many2many(
        'van_ban_den',
        'ho_so_cong_viec_van_ban_den_rel',
        'cong_viec_id',
        'van_ban_id',
        string='Văn bản đến liên quan'
    )
    
    ket_qua = fields.Text(string='Kết quả thực hiện')
    nhan_xet = fields.Text(string='Nhận xét')
    
    file_dinh_kem = fields.Binary(string='File đính kèm')
    file_name = fields.Char(string='Tên file')
    
    @api.onchange('trang_thai')
    def _onchange_trang_thai(self):
        if self.trang_thai == 'hoan_thanh':
            self.ngay_hoan_thanh = fields.Date.today()
            self.tien_do = 100
        elif self.trang_thai == 'moi':
            self.tien_do = 0