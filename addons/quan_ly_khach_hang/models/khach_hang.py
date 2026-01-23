# -*- coding: utf-8 -*-
from odoo import models, fields, api


class KhachHang(models.Model):
    _name = 'quan_ly_khach_hang.khach_hang'
    _description = 'Khách hàng'
    _rec_name = 'ten'

    ma_khach_hang = fields.Char(string='Mã khách hàng', required=True)
    ma_khach_hang_tu_nhap = fields.Boolean(string='Mã khách hàng tự nhập', default=False)
    ten = fields.Char(string='Tên khách hàng', required=True)
    ten_doanh_nghiep = fields.Char(string='Tên doanh nghiệp')
    email = fields.Char(string='Email')
    loai_khach_hang = fields.Selection([
        ('ca_nhan', 'Cá nhân'),
        ('doanh_nghiep', 'Doanh nghiệp'),
    ], string='Loại khách hàng', default='ca_nhan', required=True)
    trang_thai_khach_hang = fields.Selection([
        ('cu', 'Cũ'),
        ('moi', 'Mới'),
    ], string='Trạng thái khách hàng', default='moi', required=True)

    don_hang_ids = fields.One2many(
        'quan_ly_khach_hang.don_hang',
        'khach_hang_id',
        string='Đơn hàng'
    )

    tong_don_cho_xu_ly = fields.Integer(
        string='Tổng đơn hàng đang chờ xử lí',
        compute='_compute_tong_hop_don_hang',
        store=True
    )
    tong_don_da_giao = fields.Integer(
        string='Tổng đơn hàng đã giao',
        compute='_compute_tong_hop_don_hang',
        store=True
    )
    tong_don_da_huy = fields.Integer(
        string='Tổng đơn hàng đã hủy',
        compute='_compute_tong_hop_don_hang',
        store=True
    )
    tong_giao_dich = fields.Float(
        string='Tổng giao dịch',
        compute='_compute_tong_hop_don_hang',
        store=True,
        digits=(16, 2)
    )

    @api.onchange('ten', 'ten_doanh_nghiep')
    def _default_ma_khach_hang(self):
        for record in self:
            if not record.ma_khach_hang_tu_nhap:
                record.ma_khach_hang = record._generate_ma_khach_hang()

    @api.onchange('ma_khach_hang')
    def _onchange_ma_khach_hang(self):
        for record in self:
            if record.ma_khach_hang:
                record.ma_khach_hang_tu_nhap = True

    def _generate_ma_khach_hang(self):
        self.ensure_one()
        ten = (self.ten or '').strip()
        ten_doanh_nghiep = (self.ten_doanh_nghiep or '').strip()
        if not ten and not ten_doanh_nghiep:
            return False
        ma_ten = ''.join(phan[0] for phan in ten.lower().split() if phan)
        ma_dn = ''.join(phan for phan in ten_doanh_nghiep.upper().split() if phan)
        if ma_ten and ma_dn:
            return f"{ma_ten}_{ma_dn}"
        return ma_ten or ma_dn

    @api.model
    def create(self, vals):
        if vals.get('ma_khach_hang'):
            vals['ma_khach_hang_tu_nhap'] = True
        if not vals.get('ma_khach_hang'):
            ten = (vals.get('ten') or '').strip()
            ten_doanh_nghiep = (vals.get('ten_doanh_nghiep') or '').strip()
            ma_ten = ''.join(phan[0] for phan in ten.lower().split() if phan)
            ma_dn = ''.join(phan for phan in ten_doanh_nghiep.upper().split() if phan)
            if ma_ten and ma_dn:
                vals['ma_khach_hang'] = f"{ma_ten}_{ma_dn}"
            else:
                vals['ma_khach_hang'] = ma_ten or ma_dn
            vals['ma_khach_hang_tu_nhap'] = False
        return super().create(vals)

    def write(self, vals):
        if 'ma_khach_hang' in vals:
            vals['ma_khach_hang_tu_nhap'] = True
        return super().write(vals)

    @api.depends('don_hang_ids.trang_thai', 'don_hang_ids.don_gia')
    def _compute_tong_hop_don_hang(self):
        for record in self:
            don_hang = record.don_hang_ids
            don_cho = don_hang.filtered(lambda d: d.trang_thai == 'moi_cho_xu_ly')
            don_giao = don_hang.filtered(lambda d: d.trang_thai == 'da_giao')
            don_huy = don_hang.filtered(lambda d: d.trang_thai == 'da_huy')

            record.tong_don_cho_xu_ly = len(don_cho)
            record.tong_don_da_giao = len(don_giao)
            record.tong_don_da_huy = len(don_huy)
            record.tong_giao_dich = sum(don_giao.mapped('don_gia'))
