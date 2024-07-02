# -*- coding: utf-8 -*-
from odoo import models, fields, api

class FlotaInc(models.Model):
    _name = 'flota_inc.flota_inc'
    _description = 'Flota Incupasaje'

    marca = fields.Char()
    modelo = fields.Char()
    placa = fields.Char()
    chofer = fields.Many2one('hr.employee', string='Chofer',
    domain="[('job_id.name', '=', 'Chofer')]")
    anio = fields.Char(string="Año")

class FlotaGranja(models.Model):
    _name = 'flota_granja.flota_granja'
    _description = 'Flota Granja San José'

    marca = fields.Char()
    modelo = fields.Char()
    placa = fields.Char()
    chofer = fields.Many2one('hr.employee', string='Chofer', tracking=True)
    anio = fields.Char(string="Año")

class FlotaYuluc(models.Model):
    _name = 'flota_yuluc.flota_yuluc'
    _description = 'Flota Granja Yuluc'

    marca = fields.Char()
    modelo = fields.Char()
    placa = fields.Char()
    chofer = fields.Many2one('hr.employee', string='Chofer', tracking=True)
    anio = fields.Char(string="Año")
