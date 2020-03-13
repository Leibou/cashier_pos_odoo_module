# _*_ coding: utf-8 _*_
# Author : Khalil-Dev, Ibrahima
{
    #Information sur le module
    'name': "Cashier POS",
    'description': """
        Ce module permet de gerer des caissiers avec l'aide du POS natif de
        Odoo
    """,
    'summary': """
        En collaboration avec le module natif Point of Sale de Odoo, 
        ce module permettra à de nouveaux types d'utilisateurs de Odoo
        nommés caissiers de pouvoir faire des ventes sans avoir à ouvrir 
        de session sur odoo, chose qui devrait être faite après qu'ils soient
        créer et associés à un groupe.
        Mais ce n'est pas l'objectif visé par le client ici, donc il est impératif 
        de créer un nouveau type d'utilisateur "Caissier" pour arriver à ce résultat.
    """,
    'author': "Khalil-Dev",
    'website': "http://khalil-dev.com",
    'company': "SYLVERSYS CONSULTING INTERNATIONAL",
    'category' : 'Sales, Product Management',
    'sequence' : 3,
    'version' : "1.0",
    #Chargement des dépendances du modules : Point Of Sale de Odoo (Module Natif dans les addons)
    'depends' : ["point-of-sale"],

    # Fichiers de données utilisées par ce module
    'data' : [
        "views/cashier_view.xml",
        "views/order_cashier_view.xml",
        "security/cashier_pos_security.xml",
        "security/ir.model.access.csv",

    ],

    # Chargement des éléments statiques
    'js': ["static/src/js/cashier_pos.js",],
    'css': ["static/src/js/cashier_pos.css",],
    'img': ["static/src/js/cashier_pos.js",],
    'qweb' : [
        "static/src/xml/cashier_pos.xml",
    ],

    # Paramètres d'installation du module
    'installable' : True,
    'application': True,
    'autoinstall': False,


}