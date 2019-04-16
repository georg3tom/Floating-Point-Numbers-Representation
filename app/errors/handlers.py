from flask import Blueprint,render_template

errors=Blueprint('erros',__name__)


@errors.app_errorhandler(404)
def error404(error):
    return render_template('errors/404.html'),404

@errors.app_errorhandler(500)
def error500(error):
    return render_template('errors/500.html'),500
