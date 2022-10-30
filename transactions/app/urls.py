from .views import app, index, transaction_create, transaction_delete, single_transaction
app.add_url_rule('/', view_func=index, methods=['GET', 'POST'], endpoint='index')
app.add_url_rule('/create', view_func=transaction_create, methods=['GET', 'POST'], endpoint='transaction_create')
app.add_url_rule('/<int:transaction_id>', view_func=single_transaction, methods=['GET', 'POST'], endpoint='single_transaction')
app.add_url_rule('/<int:transaction_id>/delete', view_func=transaction_delete, methods=['GET', 'POST'], endpoint='transaction_delete')

