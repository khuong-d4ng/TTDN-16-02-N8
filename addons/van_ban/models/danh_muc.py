# -*- coding: utf-8 -*-
from odoo import models, fields

class DonVi(models.Model):
    _name = 'van_ban.don_vi'
    _description = 'Đơn vị'
    _order = 'sequence,id'

    name = fields.Char(string='Tên đơn vị', required=True)
    ma_don_vi = fields.Char(string='Mã đơn vị', required=True)
    sequence = fields.Integer(string='Thứ tự', default=10)
    active = fields.Boolean(string='Đang hoạt động', default=True)
    ghi_chu = fields.Text(string='Ghi chú')

class ChucVu(models.Model):
    _name = 'van_ban.chuc_vu'
    _description = 'Chức vụ'
    _order = 'sequence,id'

    name = fields.Char(string='Tên chức vụ', required=True)
    ma_chuc_vu = fields.Char(string='Mã chức vụ', required=True)
    sequence = fields.Integer(string='Thứ tự', default=10)
    active = fields.Boolean(string='Đang hoạt động', default=True)
    ghi_chu = fields.Text(string='Ghi chú')

class LoaiVanBan(models.Model):
    _name = 'van_ban.loai_van_ban'
    _description = 'Loại văn bản'
    _order = 'sequence,id'

    name = fields.Char(string='Tên loại văn bản', required=True)
    ma_loai = fields.Char(string='Mã loại', required=True)
    sequence = fields.Integer(string='Thứ tự', default=10)
    active = fields.Boolean(string='Đang hoạt động', default=True)
    ghi_chu = fields.Text(string='Ghi chú')

class DoMat(models.Model):
    _name = 'van_ban.do_mat'
    _description = 'Độ mật'
    _order = 'sequence,id'

    name = fields.Char(string='Tên độ mật', required=True)
    ma_do_mat = fields.Char(string='Mã độ mật', required=True)
    sequence = fields.Integer(string='Thứ tự', default=10)
    active = fields.Boolean(string='Đang hoạt động', default=True)
    ghi_chu = fields.Text(string='Ghi chú')

class DoKhan(models.Model):
    _name = 'van_ban.do_khan'
    _description = 'Độ khẩn'
    _order = 'sequence,id'

    name = fields.Char(string='Tên độ khẩn', required=True)
    ma_do_khan = fields.Char(string='Mã độ khẩn', required=True)
    sequence = fields.Integer(string='Thứ tự', default=10)
    active = fields.Boolean(string='Đang hoạt động', default=True)
    ghi_chu = fields.Text(string='Ghi chú')