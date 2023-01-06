from odoo import models, fields, api


class IndicatorEvaluation(models.Model):
    _name = 'indicator.evaluation'

    sale_order_id = fields.Many2one('crm.team', string='Nhóm bán hàng')
    actual_revenue = fields.Float(string='Doanh thu thực tế', compute='_compute_actual_revenue')
    report_month = fields.Integer('Tháng', store=True)
    month_revenue = fields.Float('Chỉ tiêu doanh thu theo tháng', compute='_compute_month_revenue', store=True)

    def _compute_actual_revenue(self):
        for rec in self:
            if rec.sale_order_id:
                amount_untaxed_opportunity = self.env['sale.order'].search(
                    [('team_id', 'in', rec.sale_order_id.mapped('id'))])
                amount_untaxed = amount_untaxed_opportunity.mapped('amount_untaxed')
                rec.actual_revenue = sum(amount_untaxed)

    @api.depends('report_month')
    def _compute_month_revenue(self):
        for rec in self:
            if rec.report_month:
                month_sales_result = self.env['crm.team'].search([('id', 'in', rec.sale_order_id.mapped('id'))])
                month_sales = month_sales_result.mapped(lambda res: (res.jan, res.feb, res.mar, res.apr, res.may,
                                                                     res.jun, res.jul, res.aug, res.sep, res.oct,
                                                                     res.nov, res.dec))
                rec.month_revenue = month_sales[0][rec.report_month - 1]
