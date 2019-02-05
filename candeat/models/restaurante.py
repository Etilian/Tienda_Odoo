from odoo import models, fields, api

class Restaurante(models.Model):
    _name = 'candeat.restaurante'
    nombre = fields.Char('Nombre', required=True)
    direccion = fields.Char('Dirección', required=True)
    telefono = fields.Char('Teléfono', required=True)
    comida = fields.Many2many('candeat.comida')

    def name_get(self):
        res = []
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res


