from odoo import models, fields
from datetime import date


class SIndicatorEvaluation(models.Model):
    _inherit = 'indicator.evaluation'

    actual_revenue_difference = fields.Float('Chênh lệch', digits=(9, 3),
                                             compute='_compute_actual_revenue_difference')

    def _compute_actual_revenue_difference(self):
        current_month = date.today().month
        for rec in self:
            if rec.actual_revenue:
                month_sales_result = self.env['crm.team'].search([('id', 'in', rec.sale_order_id.mapped('id'))])
                month_sales = month_sales_result.mapped(lambda res: (res.jan, res.feb,
                                                                     res.mar, res.apr, res.may,
                                                                     res.jun, res.jul, res.aug,
                                                                     res.sep, res.oct,
                                                                     res.nov, res.dec))
                rec.actual_revenue_difference = rec.actual_revenue - month_sales[0][current_month - 1]


