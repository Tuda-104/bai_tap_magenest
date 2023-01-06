from odoo import fields, models, api
from odoo.exceptions import ValidationError


class OrderCreationLimit(models.Model):
    _name = 'order.creation.limit'

    staff_name = fields.Many2one('res.users', string='Nhân viên')
    limit = fields.Float(string='Hạn mức', digits=(9, 3))

    @api.constrains('limit')
    def _check_limit(self):
        for rec in self:
            if rec.limit < 0:
                raise ValidationError('!!Lỗi!!')
