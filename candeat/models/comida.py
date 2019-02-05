from odoo import models, fields, api

class comida(models.Model):
    _name = 'candeat.comida'
    nombre = fields.Char('Nombre', required=True)
    codigoPlato = fields.Char('Codigo del Plato', required=True)

    def name_get(self):
        res = []
        for record in self:
            name = record.nombre
            res.append((record.id, name))
        return res
