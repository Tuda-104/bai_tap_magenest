from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SPurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    department = fields.Many2one('hr.department', required=True, string='Phòng ban')
    check_send = fields.Boolean(string='Check send email', default=False)

    def button_confirm(self):
        current_uid = self.env.uid

        id_group_accountant = self.env.cr.execute(
            "SELECT id FROM res_groups WHERE name::text LIKE '%Accountant%';")
        id_group_accountant_result = self.env.cr.fetchall()
        res_groups = self.env['res.groups'].sudo().search([('id', 'in', id_group_accountant_result)])
        res_groups_id = res_groups.mapped('users')
        res_groups_users = res_groups_id.mapped('id')

        employee_line = self.env['order.creation.limit'].search([], limit=1)
        employee = employee_line.mapped('limit')

        for rec in self:
            if rec.amount_total:
                if (rec.amount_total < employee[0]) or (current_uid in res_groups_users):
                    return super(SPurchaseOrder, self).button_confirm()
                else:
                    raise ValidationError('Tổng số tiền đã vượt quá hạn mức. Yêu cầu xác nhận với kế toán viên.')

    def btn_send(self):
        self.message_post(body=f'{self.create_uid.name} -> Xác nhận đã gửi.')
        for rec in self:
            rec.check_send = True
