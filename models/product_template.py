# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_occasion = fields.Boolean(string="Occasion", default=False)
    order_nb = fields.Integer(string="Numéro d'ordre")
    purchase_date = fields.Date(string="Date d'achat")
    seller = fields.Char(string="Vendeur")
    id_piece = fields.Char(string="Pièce d'identité")
    genre = fields.Char(string="Genre")
    matriculation = fields.Char(string="Immatriculation")
    year = fields.Char(string="Année")
    serial_nb = fields.Char(string="Numéro de série")
    km_counter = fields.Integer(string="Km au compteur")
    purchase_price = fields.Float(string="Prix d'achat")
    purchase_payment_type = fields.Char(string="Mode de réglement")
    sell_date = fields.Date(string="Date de vente")
    buyer_id = fields.Many2one('res.partner', string="Acheteur")
    matriculation_change = fields.Char(string="Changement d'immatriculation")
    warranty = fields.Char(string="Garantie")
    pieces_accessories = fields.Char(string="Pièces et accessoires")
    manpower = fields.Char(string="Main d'oeuvre")
    commission = fields.Char(string="Commission frais divers")
    sell_price = fields.Char(string="Prix de vente")
    sell_payment_type = fields.Char(string="Mode de réglement")