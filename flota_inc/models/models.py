# -*- coding: utf-8 -*-
from odoo import models, fields, api

class FlotaInc(models.Model):
    _name = 'flota_inc.flota_inc'
    _description = 'Flota Incupasaje'

    marca = fields.Char()
    modelo = fields.Char()
    placa = fields.Char()
    chofer = fields.Many2one('hr.employee', string='Chofer', tracking=True)
    anio = fields.Char(string="Año")

class Employee(models.Model):
    _inherit = 'hr.employee'

    name = fields.Char(string="Nombre")
    work_phone = fields.Char(string="Teléfono del Trabajo")
    work_email = fields.Char(string="Correo del Trabajo")
    company_id = fields.Many2one('res.company', string="Compañía")
    department_id = fields.Many2one('hr.department', string="Departamento")

    job_id = fields.Many2one('hr.job', string="Puesto de Trabajo")

class HrExpense(models.Model):
    _inherit = 'hr.expense'

    employee_id = fields.Many2one('hr.employee', string="Empleado")
