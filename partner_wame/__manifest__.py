# -*- coding: utf-8 -*-
{
    'name': 'Partner wa.me',
    "summary": "Enables a button to open wa.me based on the partners phone and mobile.",
    'version': '12.0.1.1.0',
    'author': 'HomebrewSoft',
    'website': 'https://github.com/HomebrewSoft/partner_wame',
    'category': 'Human Resources',
    'license': 'GPL-3',
    'depends': [
        'sms',
    ],
    'data': [
        # security
        # data
        # reports
        # views
        'views/res_partner.xml',
    ],
    'auto_install': True,
    'images': [
        'static/description/images/main_screenshot.png',
        'static/description/images/wame.png',
    ],
}
