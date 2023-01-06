from odoo import models, fields, _
from datetime import date


class ReportIndicatorEvaluation(models.Model):
    _name = 's.report.indicator.evaluation'

    report_month = fields.Selection([
        ('0', date.today().strftime('%B')),
        ('1', 'Tháng 1'), ('2', 'Tháng 2'), ('3', 'Tháng 3'),
        ('4', 'Tháng 4'), ('5', 'Tháng 5'), ('6', 'Tháng 6'),
        ('7', 'Tháng 7'), ('8', 'Tháng 8'), ('9', 'Tháng 9'),
        ('10', 'Tháng 10'), ('11', 'Tháng 11'), ('12', 'Tháng 12')
    ], string='Tháng', default='0', required=True)
    sale_order_id = fields.Many2many('crm.team', string='Nhóm bán hàng')

    def btn_export(self):
        if self.report_month and self.sale_order_id:
            if self.report_month == '0':
                self.report_month = str(date.today().month)
            sale_order_id = self.sale_order_id.mapped('id')
            self.env['indicator.evaluation'].sudo().search([]).unlink()
            for id in sale_order_id:
                self.env['indicator.evaluation'].sudo().create({
                    'sale_order_id': id,
                    'report_month': int(self.report_month)
                })
            context = {
                'name': _("Báo cáo đánh giá chỉ tiêu"),
                'view_mode': 'tree',
                'res_model': 'indicator.evaluation',
                'type': 'ir.actions.act_window',
                'view_id': self.env.ref('test1.indicator_evaluation_view_tree').id,
                'target': 'current',
                'domain': [('sale_order_id', 'in', sale_order_id), ('report_month', '=', int(self.report_month))],
                'context': {'create': False, 'edit': False, 'delete': False}
            }

        else:
            context = {
                'name': _("Báo cáo đánh giá chỉ tiêu"),
                'view_mode': 'tree',
                'res_model': 'indicator.evaluation',
                'type': 'ir.actions.act_window',
                'view_id': self.env.ref('test1.indicator_evaluation_view_tree').id,
                'target': 'current',
                'context': {'create': False, 'edit': False, 'delete': False}
            }
        return context
