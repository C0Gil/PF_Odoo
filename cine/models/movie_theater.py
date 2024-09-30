# -*- coding:utf-8 -*-

from odoo import models, fields, api

class Theater(models.Model):
    _name = 'theater'

    name = fields.Char(string='Nombre', required=True)
    seq_theater = fields.Char(string="Numero de sala", copy=False, readonly=True)

    movie_ids = fields.Many2one(
        comodel_name='presupuesto', 
        string='Películas',
        domain=[('state','=','aprobado')]
    )

    tck_price = fields.Monetary(string='Precio', related='movie_ids.price_of_ticket')
    
    currency_id = fields.Many2one(
        comodel_name = 'res.currency',
        string = 'Moneda',
        related='movie_ids.currency_id')

    @api.model
    def create(self, variables):
        sequence_obj = self.env['ir.sequence']
        correlative = sequence_obj.next_by_code('sequence.movie.theaters')
        variables['seq_theater'] = correlative
        return super(Theater, self).create(variables)

    def copy(self, default=None):
        if self._name == 'theater':
            default = dict(default or {})
            default['name'] = self.name + '(copia)'
            return super(Theater, self).copy(default)
