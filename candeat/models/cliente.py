from odoo import models, fields, api

class Cliente(models.Model):
    _name = 'candeat.cliente'
    nombre = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellidos', required=True)
    telefono = fields.Char('Teléfono', required=True)
    direccion = fields.Char('Dirección', required=True)
    restaurante = fields.Many2one('candeat.restaurante', 'Restaurante')
    comida = fields.Many2one('candeat.comida', 'Comida')

