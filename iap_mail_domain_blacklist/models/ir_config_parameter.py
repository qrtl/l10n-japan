# Copyright 2025 Quartile
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, models
from odoo.addons.iap.tools import iap_tools


class IrConfigParameter(models.Model):
    _inherit = 'ir.config_parameter'

    def set_param(self, key, value):
        if key != 'mail.domain.blacklist':
            return super().set_param(key, value)
        old_values = self.sudo().get_param("mail.domain.blacklist")
        old_set = set(old_values.split(',')) if old_values else set()
        current_set = set(iap_tools._MAIL_DOMAIN_BLACKLIST)
        updated_set = current_set - old_set
        result = super().set_param(key, value)
        new_set = set(value.split(',')) if value else set()
        iap_tools._MAIL_DOMAIN_BLACKLIST = list(updated_set | new_set)
        return result
