from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    """Inherits partner, define the fields for the CCA44 FSS project"""

    _inherit = "res.partner"

    accept_project_charter = fields.Boolean("Accept project charter")
    accept_cgv = fields.Boolean("Accept CGV")
    identity_document = fields.Binary("Identity document", attachment=True)
    bank_details_document = fields.Binary("Bank details document", attachment=True)
    sepa_direct_debit_authorization = fields.Binary("SEPA direct debit authorization", attachment=True)
    household_composition_teens = fields.Integer(string="Number of Teens (14-18 years)")
    household_composition_children_under_fourteen = fields.Integer(
        string="Number of Children (-14 years)"
    )
    fss_cca44_comments = fields.Text("Comments")
