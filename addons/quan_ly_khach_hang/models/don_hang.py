# -*- coding: utf-8 -*-
from odoo import models, fields


class DonHang(models.Model):
    _name = 'quan_ly_khach_hang.don_hang'
    _description = 'Đơn hàng'
    _rec_name = 'ten_don_hang'

    ten_don_hang = fields.Char(string='Tên đơn hàng', required=True)
    khach_hang_id = fields.Many2one(
        'quan_ly_khach_hang.khach_hang',
        string='Khách hàng',
        required=True
    )

    ten_khach_hang = fields.Char(
        string='Tên khách hàng',
        related='khach_hang_id.ten',
        store=True,
        readonly=True
    )
    ma_khach_hang = fields.Char(
        string='Mã khách hàng',
        related='khach_hang_id.ma_khach_hang',
        store=True,
        readonly=True
    )
    ten_doanh_nghiep = fields.Char(
        string='Tên doanh nghiệp',
        related='khach_hang_id.ten_doanh_nghiep',
        store=True,
        readonly=True
    )
    email = fields.Char(
        string='Email',
        related='khach_hang_id.email',
        store=True,
        readonly=True
    )

    don_gia = fields.Float(string='Đơn giá', digits=(16, 2), required=True)
    trang_thai = fields.Selection([
        ('moi_cho_xu_ly', 'Mới (chờ xử lí)'),
        ('da_giao', 'Đã giao'),
        ('da_huy', 'Đã hủy'),
    ], string='Trạng thái', default='moi_cho_xu_ly', required=True)
    ngay_tao_don = fields.Date(
        string='Ngày tạo đơn',
        default=fields.Date.context_today,
        required=True
    )
    han_ban_giao = fields.Date(string='Hạn bàn giao')
