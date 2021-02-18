# Copyright 2020 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "Indonesia's PPh 21 Taxform Related Configuration and Computation",
    "version": "8.0.1.1.0",
    "category": "localization",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia,OpenSynergy Indonesia,"
    "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "l10n_id_taxform",
        "account",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/ptkp_category_data.xml",
        "views/ptkp_views.xml",
        "views/pph_21_biaya_jabatan_views.xml",
        "views/pph_21_npwp_rate_modifier_views.xml",
        "views/pph_21_rate_views.xml",
        "views/res_partner_views.xml",
    ],
    "demo": [
        "demo/pph_21_biaya_jabatan_demo.xml",
        "demo/pph_21_npwp_rate_modifier_demo.xml",
        "demo/pph_21_rate_demo.xml",
        "demo/ptkp_demo.xml",
    ],
}
