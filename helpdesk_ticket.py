# -*- coding: utf-8 -*-

from openerp import addons
from openerp import models, fields, api, _
from openerp.exceptions import UserError, RedirectWarning, ValidationError

class helpdesk_ticket(models.Model):
	_inherit = 'helpdesk.ticket'

	team_id = fields.Many2one('helpdesk.team', string="Team")
	ticket_type_id = fields.Many2one('helpdesk.ticket.type', string="Ticket Type")