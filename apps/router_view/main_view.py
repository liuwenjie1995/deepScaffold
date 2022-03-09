from flask import Blueprint, render_template, redirect

mainpages = Blueprint('main', __name__)


@mainpages.route('/index')
@mainpages.route('/')
def index():
    return "this is index"
