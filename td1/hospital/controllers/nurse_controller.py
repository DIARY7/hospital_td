# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from datetime import datetime, timedelta

class RondController(http.Controller):

    @http.route('/hospital/my-week-rondes', auth='user', website=True)
    def my_week_rondes(self, **kw):
        user = request.env.user
        nurse = request.env['hospital.staff.nurse'].sudo().search([('user_id', '=', user.id)], limit=1)

        # if not nurse:
        #     return request.render('your_module_name.no_nurse')

        today = datetime.today()
        start_of_week = today - timedelta(days=today.weekday())  # lundi
        end_of_week = start_of_week + timedelta(days=6)           # dimanche

        rondes = request.env['hospital.rond'].sudo().search([
            ('nurse_id', '=', nurse.id),
            ('date_of_rond', '>=', start_of_week),
            ('date_of_rond', '<=', end_of_week),
        ])

        return request.render('hospital.template_week_rondes', {
            'nurse': nurse,
            'rondes': rondes,
            'start': start_of_week.strftime("%d/%m/%Y"),
            'end': end_of_week.strftime("%d/%m/%Y")
        })

    @http.route('/hospital/my-week-rondes/pdf', type='http', auth='user')
    def my_week_rondes_pdf(self, **kwargs):
        user = request.env.user
        nurse = request.env['hospital.staff.nurse'].sudo().search([('user_id', '=', user.id)], limit=1)

        if not nurse:
            return request.not_found()

        # Récupérer les dates de début et fin de la semaine depuis les paramètres
        start_date = kwargs.get('start')
        end_date = kwargs.get('end')

        # Filtrer les rondes pour la semaine en cours
        domain = [
            ('nurse_id', '=', nurse.id),
            ('date_of_rond', '>=', start_date),
            ('date_of_rond', '<=', end_date)
        ]
        rondes = request.env['hospital.rond'].sudo().search(domain)

        if not rondes:
            return request.not_found("Aucune ronde trouvée pour cette période")

        # Préparer les données pour le rapport
        data = {
            'doc_ids': rondes.ids,
            'docs': rondes,
            'nurse': nurse,
            'start': start_date,
            'end': end_date
        }

        # Méthode spécifique pour Odoo 18
        pdf_content = request.env['ir.actions.report'].sudo()._render_qweb_pdf(
            'hospital.report_week_rondes_pdf',  # Nom du template QWeb
            rondes.ids,  # IDs des documents
            data=data  # Données supplémentaires
        )

        return request.make_response(
            pdf_content[0],  # Le contenu PDF est le premier élément du tuple retourné
            headers=[
                ('Content-Type', 'application/pdf'),
                ('Content-Disposition', f'attachment; filename="rondes_semaine_{start_date}_au_{end_date}.pdf"')
            ]
        )