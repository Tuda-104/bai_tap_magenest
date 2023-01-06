from odoo import fields, models, api
from odoo.exceptions import ValidationError


class SHrDepartment(models.Model):
    _inherit = 'hr.department'

    spending_limit = fields.Float('Hạn mức chi tiêu mỗi tháng')
    real_cost = fields.Float(string='Chi tiêu thực tế', compute='_compute_real_cost')
    create_month = fields.Integer('Tháng', compute='_compute_create_month', store=True)

    @api.constrains('spending_limit')
    def _check_spending_limit(self):
        if self.spending_limit:
            if self.spending_limit < 0:
                raise ValidationError("Hạn mức chi tiêu mỗi tháng không được nhỏ hơn 0")

    def _compute_real_cost(self):
        for rec in self:
            if rec.name:
                amount_total = self.env['purchase.order'].search([('department', '=', rec.id)])
                amount_total_department = amount_total.mapped('amount_total')
                rec.real_cost = sum(amount_total_department)

    @api.depends('create_date')
    def _compute_create_month(self):
        for rec in self:
            if rec.create_date:
                create_date = str(rec.create_date)
                create_month = create_date.split("-")
                rec.create_month = create_month[1]
