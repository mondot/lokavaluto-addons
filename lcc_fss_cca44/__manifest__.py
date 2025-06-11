# Copyright 20204 Boris Gallet ()
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "lcc_fss_cca44",  # TODO : rename cca44_base
    "version": "16.0.1.0.0",
    "author": "Elabore",
    "website": "https://elabore.coop",
    "maintainer": "Quentin Mondot",
    "license": "AGPL-3",
    "category": "Tools",
    "summary": "specificities for food social security project near Nantes (named CCA 44)",
    # any module necessary for this one to work correctly
    "depends": [
        "lcc_fss_base",
    ],
    "qweb": [],
    "external_dependencies": {
        "python": [],
    },
    # always loaded
    "data": [
        "views/res_partner_view.xml"
    ],
    # only loaded in demonstration mode
    "demo": [],
    "js": [],
    "css": [],
    "installable": True,
    # Install this module automatically if all dependency have been previously
    # and independently installed.  Used for synergetic or glue modules.
    "auto_install": False,
    "application": False,
}
