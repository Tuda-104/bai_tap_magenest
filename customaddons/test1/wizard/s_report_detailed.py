from odoo import models, fields, _
from datetime import date


class SReportDetailed(models.Model):
    _name = 's.report.detailed'

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
            context = {
                'name': _("Báo cáo chi tiết"),
                'view_mode': 'tree',
                'res_model': 'crm.lead',
                'type': 'ir.actions.act_window',
                'view_id': self.env.ref('crm.crm_case_tree_view_oppor').id,
                'target': 'current',
                'domain': [('sale_team_id', 'in', sale_order_id), ('create_month', '=', self.report_month), ],
                'context': {'create': False, 'edit': False, 'delete': False}
            }
        else:
            context = {
                'name': _("Báo cáo chi tiết"),
                'view_mode': 'tree',
                'res_model': 'crm.lead',
                'type': 'ir.actions.act_window',
                'view_id': self.env.ref('crm.crm_case_tree_view_oppor').id,
                'target': 'current',
                'context': {'create': False, 'edit': False, 'delete': False}
            }
        return context
