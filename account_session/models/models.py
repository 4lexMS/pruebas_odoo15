# -*- coding: utf-8 -*-

from odoo import models, fields, api


class account_session(models.Model):
    _inherit = 'account.bank.statement'
    nombre = ""
