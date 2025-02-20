from odoo import http
from odoo.http import request
from werkzeug.utils import redirect

class PersonsController(http.Controller):

    # Display 5 last records from table Persons and display the form
    @http.route('/last/persons', methods=['POST', 'GET'], auth='public', website=True)
    def last_persons(self, **kwargs):
        if request.httprequest.method == "POST":

            # Check existence of birthday
            if not request.params.get("birthday"):
                date = None
            else:
                date = request.params.get("birthday")

            # Check existence of gender
            if request.params.get("sex") == 'none':
                sex = None
            else:
                sex = request.params.get("sex")

            request.env['person'].create({
                "first_name": request.params.get("first_name"),
                "last_name": request.params.get("last_name"),
                "company_id": request.params.get("company_id"),
                "birthday": date,
                "sex": sex,
            })
            return redirect('/last/persons')

        persons = http.request.env['person'].search([],  order='create_date desc', limit=5)
        companies = http.request.env['res.company'].search([])
        return http.request.render('persons16.persons_template', {
            'companies': companies,
            'persons': persons
        })

    # Display all record from table Persons
    @http.route('/all/persons', methods=['GET'], auth='public', website=True)
    def last_persons(self, **kwargs):
        persons = http.request.env['person'].search([])
        return http.request.render('persons16.all_persons_template', {
            'persons': persons,
        })