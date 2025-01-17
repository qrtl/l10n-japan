# Copyright 2025 Quartile
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.addons.iap.tools import iap_tools

iap_tools._MAIL_DOMAIN_BLACKLIST = iap_tools._MAIL_DOMAIN_BLACKLIST | {"outlook.jp"}
