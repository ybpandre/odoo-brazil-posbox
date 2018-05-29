# -*- coding: utf-8 -*-
import openerp.addons.hw_proxy.controllers.main as hw_proxy
from openerp import http
from .sat import Sat


class SatDriver(hw_proxy.Proxy):

    # TODO: Temos um problema quando o sat é iniciado depois do POS
    # @http.route('/hw_proxy/status_json', type='json', auth='none', cors='*')
    # def status_json(self):
    #     if not hw_proxy.drivers['satcfe'].device:
    #         hw_proxy.drivers['satcfe'].get_device()
    #     return self.get_status()

    @http.route('/hw_proxy/init/', type='json', auth='none', cors='*')
    def init(self, json):
        hw_proxy.drivers['satcfe'] = Sat(**json)
        return True

    @http.route('/hw_proxy/enviar_cfe_sat/', type='json', auth='none', cors='*')
    def enviar_cfe_sat(self, json):
        res = hw_proxy.drivers['satcfe'].action_call_sat('send', json)
        print ('RESPOSTA: ', res)
        return res

    @http.route('/hw_proxy/cancelar_cfe/', type='json', auth='none', cors='*')
    def cancelar_cfe(self, json):
        return hw_proxy.drivers['satcfe'].action_call_sat('cancel', json)

    @http.route('/hw_proxy/reprint_cfe/', type='json', auth='none', cors='*')
    def reprint_cfe(self, json):
        return hw_proxy.drivers['satcfe'].action_call_sat('reprint', json)
