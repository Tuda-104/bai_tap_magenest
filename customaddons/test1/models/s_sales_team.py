from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SSalesTeam(models.Model):
    _inherit = "crm.team"

    jan = fields.Float("Tháng 1", digits=(9, 3))
    feb = fields.Float("Tháng 2", digits=(9, 3))
    mar = fields.Float("Tháng 3", digits=(9, 3))
    apr = fields.Float("Tháng 4", digits=(9, 3))
    may = fields.Float("Tháng 5", digits=(9, 3))
    jun = fields.Float("Tháng 6", digits=(9, 3))
    jul = fields.Float("Tháng 7", digits=(9, 3))
    aug = fields.Float("Tháng 8", digits=(9, 3))
    sep = fields.Float("Tháng 9", digits=(9, 3))
    oct = fields.Float("Tháng 10", digits=(9, 3))
    nov = fields.Float("Tháng 11", digits=(9, 3))
    dec = fields.Float("Tháng 12", digits=(9, 3))

    @api.constrains('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec')
    def _check_month(self):
        for rec in self:
            if rec.jan <= 0 and rec.feb <= 0 and rec.mar <= 0 and rec.apr <= 0 and rec.may <= 0 and rec.jun <= 0 \
                    and rec.jul <= 0 and rec.aug <= 0 and rec.sep <= 0 and rec.oct <= 0 and rec.nov <= 0 and rec.dec <= 0:
                raise ValidationError("!!!LỖI!!!")
