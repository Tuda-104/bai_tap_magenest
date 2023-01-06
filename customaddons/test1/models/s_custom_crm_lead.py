from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SCustomCrmLead(models.Model):
    _inherit = 'crm.lead'

    minimum_revenue = fields.Float("Doanh thu tối thiểu (trước VAT)", digits=(9, 3))
    actual_revenue = fields.Float(string='Doanh thu thực tế', compute='_compute_actual_revenue')
    check_priority = fields.Boolean(string='Check Priority', default=True, compute='_compute_check_priority',
                                    store=True)
    create_month = fields.Integer('Create Month', compute='_compute_create_month', store=True)
    sale_team_id = fields.Many2one('crm.team', string="Nhóm bán hàng", required=False)
    all_quotation = fields.Integer('all_quotation', compute='_compute_all_quotation', store=False)

    @api.constrains('minimum_revenue')
    def _check_money(self):
        for rec in self:
            if rec.minimum_revenue <= 0:
                raise ValidationError("!!!LỖI!!!")

    def _compute_all_quotation(self):
        for rec in self:
            if rec.id:
                all_quotation = self.env['sale.order'].search_count([('opportunity_id', '=', rec.id)])
                rec.all_quotation = all_quotation

    @api.depends('priority')
    def _compute_check_priority(self):
        for rec in self:
            if rec.priority == '3':
                rec.check_priority = False
            else:
                rec.check_priority = True

    def btn_lost(self):
        return super(SCustomCrmLead, self).action_set_lost()

    def _compute_actual_revenue(self):
        for rec in self:
            if rec.id:
                amount_total = self.env['sale.order'].search([('opportunity_id', '=', rec.id)])
                amount_total_opportunity = amount_total.mapped('amount_total')
                rec.actual_revenue = sum(amount_total_opportunity)

    @api.depends('create_date')
    def _compute_create_month(self):
        for rec in self:
            if rec.create_date:
                create_date = str(rec.create_date)
                create_month = create_date.split("-")
                rec.create_month = create_month[1]
