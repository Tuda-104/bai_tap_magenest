from odoo import fields, models


class OrderCreation(models.Model):
    _name = 'order.creation'

    order_name = fields.Char('Đơn hạn mức')
    order_creation_staff_id = fields.Many2many('order.creation.limit', 'order_creation_rel', 'order_creation_staff_id',
                                               'staff_name', string='Nhân viên')
