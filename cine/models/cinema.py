# -*- coding:utf-8 -*-

import logging
from odoo import models, fields
from odoo.exceptions import UserError

logger = logging.getLogger(__name__)


class Cinema(models.Model):
    _name = 'cinema'

    name = fields.Char(string='Cine', required=True)
    
    address_id = fields.Many2one('res.partner', string='Contactos')

    address_categories = fields.Many2one(
        comodel_name="res.partner.category",
        string="Categoria Cine",
        default=lambda self: self.env.ref('cine.category_cinema')
    )

    movie_ids = fields.Many2many(
        comodel_name='presupuesto', 
        string='Películas',
        domain=[('state','=','aprobado')]
    )

    details_ids = fields.One2many(
        comodel_name='cinema.details',
        inverse_name='id_cinema',
        string='Detalles'
    )

    state = fields.Selection(selection=[
        ('borrador', 'Borrador'),
        ('aprobado', 'Aprobado'),
        ('cancelado', 'Cancelado'),
    ], string='Estados', copy=False)


    def unlink(self):
        for record in self:
            if record._name == 'cinema':
                record.state = 'cancelado'
                super(Cinema, record).unlink()                                  


class CinemaDetails(models.Model):
    _name = 'cinema.details'

    id_cinema = fields.Many2one(
        comodel_name = 'cinema',
        string = 'Cine'
    )

    name = fields.Many2one(
        comodel_name = 'theater',
        string='Sala de Cine'
    )
    
    num_theater = fields.Char(string='Numero de sala', related='name.seq_theater')
    
    movie = fields.Many2one(
        comodel_name='presupuesto',
        string='Pelicula',
        related='name.movie_ids'
    )
    
    ticket_price = fields.Monetary(string='Precio', related='name.tck_price')
    
    currency_id = fields.Many2one(
        comodel_name = 'res.currency',
        string = 'Moneda',
        related='name.currency_id')

