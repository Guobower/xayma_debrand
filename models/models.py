# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Sle_order(models.Model):
    _inherit = 'stock.warehouse'
    capaciteStockage = fields.Integer("Capacité de stockage de volume (en m3)")


# class xayma_personnalisaton(models.Model):
#     _name = 'xayma_personnalisaton.xayma_personnalisaton'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100