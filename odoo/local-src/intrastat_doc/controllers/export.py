from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import content_disposition, ensure_db


class StockPickingController(http.Controller):

    @http.route('/download/stockpicking/<string:document_type>',
                type='http', auth='user')
    def intrastat_doc_download(self,  document_type, id, filename=None, **kw):
        """ Return the packing-list or the commercial-invoice documents
            in an Excel format, for a specific stock-picking whose id is passed
            in parameters.
        """
        ensure_db()
        env = request.env
        file_content = ''
        stock_pick = env['stock.picking'].browse([int(id)]).exists()
        if len(stock_pick):
            file_content = stock_pick.get_intrastat_doc(document_type)
        return request.make_response(
                file_content,
                [('Content-Type', 'application/octet-stream'),
                 ('Content-Disposition', content_disposition(filename))])
