# -*- coding: utf-8 -*-
from odoo import http

# class XaymaPersonnalisaton(http.Controller):
#     @http.route('/xayma_personnalisaton/xayma_personnalisaton/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xayma_personnalisaton/xayma_personnalisaton/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('xayma_personnalisaton.listing', {
#             'root': '/xayma_personnalisaton/xayma_personnalisaton',
#             'objects': http.request.env['xayma_personnalisaton.xayma_personnalisaton'].search([]),
#         })

#     @http.route('/xayma_personnalisaton/xayma_personnalisaton/objects/<model("xayma_personnalisaton.xayma_personnalisaton"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xayma_personnalisaton.object', {
#             'object': obj
#         })