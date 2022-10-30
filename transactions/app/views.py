from flask import render_template, request, redirect, url_for, flash

from . import app, db

from .models import Transactions
from .forms import TransactionsForm

def index():
    transactions = Transactions.query.all()
    return render_template('index.html', transactions=transactions)

def transaction_create():
    form = TransactionsForm(request.form)
    if request.method == "POST":
        if form.validate_on_submit():
            transactions = Transactions()
            form.populate_obj(transactions)
            db.session.add(transactions)
            db.session.commit()
            flash(f'транзакция №{transactions.id} на сумму {transactions.value} совершена успешно', category='success')
            return redirect(url_for('index'))
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f'{error} ошибка {field}', category='danger')

    return render_template('transaction_create.html', form=form)

def transaction_delete(transaction_id):
    form = TransactionsForm(request.form)

    transactions = Transactions.query.filter_by(id=transaction_id).first()
    if request.method == 'GET':
        return render_template('transaction_delete.html', transactions=transactions, form=form)
    if request.method == 'POST':
        db.session.delete(transactions)
        db.session.commit()
        flash(f'транзакция под номером №{transactions.id} на сумму {transactions.value} удалён')
        return redirect(url_for('index'))


def single_transaction(transaction_id):
    transaction = Transactions.query.filter_by(id=transaction_id).first()
    return render_template('transaction_info.html', transactions=transaction)
