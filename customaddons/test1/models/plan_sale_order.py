from odoo import models, fields
from odoo.exceptions import UserError


class PlanSaleOrder(models.Model):
    _name = "plan.sale.order"
    _description = 'Plan Sale Order'
    _inherit = ['mail.thread']

    name = fields.Text("Tên", required=True)
    quotation = fields.Many2one('sale.order', readonly=True, store=True)
    infor = fields.Text("Thông tin phương án kinh doanh", required=True)
    state = fields.Selection([
        ('new', 'Tạo mới'),
        ('send', 'Gửi duyệt'),
        ('approve', 'Đã duyệt'),
        ('refuse', 'Từ chối'),
    ], string='Trạng thái báo giá', default='new')
    check_confirm = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No'),
    ], string='Check confirm')
    order_line = fields.One2many('approver.list', 'order_id', string='Order Lines')

    def btn_send(self):
        if self.state == 'new':
            if self.order_line.approver:
                self.state = 'send'
                noti_send = f'({self.create_uid.name}) {fields.Datetime.now()} -> phương án kinh doanh mới đã được gửi.'
                self.message_post(subject='Gửi để duyệt', body=noti_send, mesage_type='notification',
                                  partner_ids=self.order_line.approver.ids)
            else:
                raise UserError('Chưa có người phê duyệt, yêu cầu thêm người phê duyệt')
        else:
            raise UserError('Không thể gửi duyệt kế hoạch kinh doanh này')

    def btn_approve(self):
        if self.check_confirm == 'yes':
            self.state = 'approve'
            noti_approve = f'({self.create_uid.name}) {fields.Datetime.now()} -> phương án kinh doanh mới đã được duyệt.'
            self.message_post(subject='Đã duyệt', body=noti_approve)
        else:
            raise UserError('Tất cả người phê duyệt chưa đồng ý duyệt phương án này.')

    def btn_refuse(self):
        if self.check_confirm == 'no':
            self.state = 'refuse'
            noti_refuse = f'({self.create_uid.name}) {fields.Datetime.now()} -> phương án kinh doanh mới đã bị từ chối, yêu cầu tạo bản khác và gửi duyệt lại.'
            self.message_post(subject='Từ chối duyệt', body=noti_refuse)
        else:
            raise UserError('Tất cả người phê duyệt chưa từ chối duyệt phương án này.')
