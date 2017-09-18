# -*- coding: utf-8 -*-

from openerp import addons
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError

class helpdesk_ticket_type(models.Model):
    _inherit = 'helpdesk.ticket.type'

    team_id = fields.Many2one('helpdesk.team', string='Team')