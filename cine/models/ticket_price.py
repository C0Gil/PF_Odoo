# -*- coding:utf-8 -*-

from odoo import fields, models, api

class TickePrice(models.Model):
    _inherit = 'presupuesto'

    price_of_ticket = fields.Monetary(string='Precio del boleto')
    
    ticket_currency = fields.Many2one(
        comodel_name ="res.currency",
        string="Moneda del ticket",
        default=lambda self: self.env.company.currency_id.id
    )