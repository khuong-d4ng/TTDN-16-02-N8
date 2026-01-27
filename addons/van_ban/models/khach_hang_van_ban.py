# -*- coding: utf-8 -*-
from odoo import models, fields, api


class KhachHangVanBan(models.Model):
    """Mở rộng model KhachHang để thêm liên kết với văn bản đến"""
    _inherit = 'quan_ly_khach_hang.khach_hang'

    # Văn bản đến liên quan
    van_ban_den_ids = fields.One2many(
        'van_ban_den',
        'khach_hang_id',
        string='Văn bản đến'
    )

    tong_van_ban_moi = fields.Integer(
        string='Tổng văn bản mới',
        compute='_compute_tong_hop_van_ban',
        store=True
    )
    tong_van_ban_dang_xu_ly = fields.Integer(
        string='Tổng văn bản đang xử lý',
        compute='_compute_tong_hop_van_ban',
        store=True
    )
    tong_van_ban_da_xu_ly = fields.Integer(
        string='Tổng văn bản đã xử lý',
        compute='_compute_tong_hop_van_ban',
        store=True
    )

    @api.depends('van_ban_den_ids.trang_thai')
    def _compute_tong_hop_van_ban(self):
        for record in self:
            van_ban = record.van_ban_den_ids
            vb_moi = van_ban.filtered(lambda v: v.trang_thai == 'moi')
            vb_dang_xu_ly = van_ban.filtered(lambda v: v.trang_thai == 'dang_xu_ly')
            vb_da_xu_ly = van_ban.filtered(lambda v: v.trang_thai == 'da_xu_ly')

            record.tong_van_ban_moi = len(vb_moi)
            record.tong_van_ban_dang_xu_ly = len(vb_dang_xu_ly)
            record.tong_van_ban_da_xu_ly = len(vb_da_xu_ly)
