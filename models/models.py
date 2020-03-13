from odoo import models, fields
import time

# Création de l'Objet pos_cashier pour gerer les caissiers
class cashier_pos(models.Model):
    _name = 'cashier.pos'
    _order = 'cashier name asc'

    pos_config_id = fields.Many2one('pos.config', string="ID Point de Vente", required=True)
    cashier_name = fields.Char("Caissier", required=True)
    active = fields.Boolean("Status Caissier", help="Si un caissier n'est pas activé, il ne sera pas affiché dans le POS")

    # Valeur par défaut des champs de  l'objet POS_CASHIER "Caissier"
    _defaults = {
        'cashier_name' : '',
        'active': True,
        'pos_config_id' : lambda self,cr,uid,c: self.pool.get('res.users').browse(cr, uid, uid, c).pos_config.id,
    }

    # Régles d'Enregistrement  d'un nouveau Caissier
    _sql_constraints ={(
        'uniq_name',
        'unique(cashier_name, pos_config_id)',
        "Un caissier existe déja avec ce nom dans ce point de vente. Le nom du caissier doit être unique !"),
    }


# Surcharge de l'objet pos.order du module Point de Vente
class inherit_pos_order_for_cashiers(models.Model):
    _name =  'pos.order'
    _inherit = 'pos.order'

    def create_from_ui(self, cr, uid, orders, context=None):
        order_ids =[]
        # Récupération de chaque  id de la commande et les details puis ajout du nom du caissier
        for tmp_order in orders:
            order = tmp_order['data']
            order_id = self.create(cr, uid, {
                'name': order['name'],
                'user_id': order['user_id'] or False,
                'session_id': order['pos_session_id'],
                'lines': order['lines'],
                'pos_references': order['name'],
                'cashier_name': ['cashier_name'],
            }, context)
            # Récuperation des informations de paiements
            for payements in order['statement_id']:
                payement = payements[2]
                sefl.add_payement(cr, uid, order_id, {
                    'amount' : payement['amount'] or 0.0,
                    'payement_date': payement['name'],
                    'statement_id' : payement['statement_id'],
                    'payement_name': payement.get('note', False),
                    'journal': payement['journal_id']
                }, context)
            if order['amount_return']:
                session = sefl.pool.get('pos.session').browse(cr, uid, order['pos_session_id'], context=context)
                cash_journal = session.cash_journal_id
                cash_statement = False
                if not cash_journal:
                    cash_journal_ids = filter(lambda st: st.journal_id.type=='cash', session.statement_ids)
                    if not len(cash_journal_ids):
                        raise
