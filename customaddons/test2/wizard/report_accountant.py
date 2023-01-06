from odoo import models, fields, _
from datetime import date


class ReportAccountant(models.Model):
    _name = 'report.accountant'

    report_month = fields.Selection([
        ('1', 'Tháng 1'), ('2', 'Tháng 2'), ('3', 'Tháng 3'),
        ('4', 'Tháng 4'), ('5', 'Tháng 5'), ('6', 'Tháng 6'),
        ('7', 'Tháng 7'), ('8', 'Tháng 8'), ('9', 'Tháng 9'),
        ('10', 'Tháng 10'), ('11', 'Tháng 11'), ('12', 'Tháng 12'),
    ], string='Tháng', default='0', required=True)
    department_id = fields.Many2many('hr.department', string='Phòng ban')

    def btn_export(self):
        department_name = self.department_id.mapped('name')
        if self.report_month and self.department_id:
            context = {
                'name': _("Detail Report"),
                'view_mode': 'tree',
                'res_model': 'hr.department',
                'type': 'ir.actions.act_window',
                'view_id': self.env.ref('hr.view_department_tree').id,
                'target': 'current',
                'domain': [('create_month', '=', self.report_month), ('name', 'in', department_name)],
                'context': {'create': False, 'edit': False, 'delete': False}
            }
        else:
            context = {
                'name': _("Detail Report"),
                'view_mode': 'tree',
                'res_model': 'hr.department',
                'type': 'ir.actions.act_window',
                'view_id': self.env.ref('hr.view_department_tree').id,
                'target': 'current',
                'context': {'create': False, 'edit': False, 'delete': False}
            }
        return context
