from odoo import models, fields


class SSHrDepartment(models.Model):
    _inherit = 'hr.department'

    real_cost_difference = fields.Float(string='Chênh lệch', compute='_compute_real_cost_difference')

    def _compute_real_cost_difference(self):
        for rec in self:
            rec.real_cost_difference = 0
            if rec.spending_limit:
                rec.real_cost_difference = rec.spending_limit - rec.real_cost
