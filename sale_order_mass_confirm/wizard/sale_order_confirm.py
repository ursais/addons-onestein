# -*- coding: utf-8 -*-
# Copyright 2016 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, api

from datetime import datetime
import logging
_logger = logging.getLogger(__name__)


class SaleOrderConfirmWizard(models.TransientModel):
    _name = "sale.order.confirm.wizard"
    _description = "Wizard - Sale Order Confirm"

    @api.multi
    def confirm_sale_orders(self):
        _logger.info("\n\n***Start Mass Order Confirmation.")
        start_time = datetime.now()
        self.ensure_one()
        active_ids = self._context.get('active_ids')
        orders = self.env['sale.order'].browse(active_ids)
        order_cnt = 1
        for order in orders:
            _logger.info("\n%s. Confirming Order:  %s\n" % (str(order_cnt), order.name))
            order_cnt += 1
            if order.state in ['draft', 'sent']:
                order.action_confirm()
            self.env.cr.commit()
        _logger.info("\n\n***End Mass Order Confirmation %s\n\n" % str(datetime.now()-start_time) )
