{
    'name': 'Persons',
    'version': '1.0',
    'category': 'Website',
    'description': """This is a module for rendering and creating persons""",
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'views/persons.xml',
        'views/website_menu.xml',
        'views/last_persons.xml',
        'views/all_persons.xml',
    ],
    'license': 'LGPL-3',
}
