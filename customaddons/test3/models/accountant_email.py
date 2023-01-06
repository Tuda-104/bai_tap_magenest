from odoo import fields, models, api


class AccountantEmail(models.Model):
    _name = 'accountant.email'

    def send_email(self):
        accountant_ids = self.env.ref('test2.groups_accountant').users.ids

        res_users = self.env['res.users'].sudo().search([('id', 'in', accountant_ids)])
        res_users_partner_id = res_users.mapped('partner_id.id')

        res_partner = self.env['res.partner'].sudo().search([('id', 'in', res_users_partner_id)])
        email_accountant = res_partner.mapped('email')

        indicator_evaluation = self.env['indicator.evaluation'].search([])
        sale_team_name = indicator_evaluation.mapped('sale_order_id.name')
        real_revenue = indicator_evaluation.mapped('actual_revenue')
        real_revenue_difference = indicator_evaluation.mapped('actual_revenue_difference')

        hr_department = self.env['hr.department'].search([])
        department_name = hr_department.mapped('name')
        real_cost = hr_department.mapped('real_cost')
        real_cost_difference = hr_department.mapped('real_cost_difference')

        ctx = {}
        ctx['sale_team_name'] = sale_team_name
        ctx['real_revenue'] = real_revenue
        ctx['real_revenue_difference'] = real_revenue_difference
        ctx['department_name'] = department_name
        ctx['real_cost'] = real_cost
        ctx['real_cost_difference'] = real_cost_difference
        ctx['email_to'] = ';'.join(map(lambda x: x, email_accountant))
        ctx['email_from'] = self.env.user.company_id.email
        template = self.env.ref('test3.email_template')
        template.with_context(ctx).send_mail(self.id, force_send=True, raise_exception=False)

