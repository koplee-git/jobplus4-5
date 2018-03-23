""" 企业列表 企业详情"""
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from jobplus.models import  User,Company
from jobplus.forms import LoginForm,RegisterForm,CompanyRegisterForm
from flask_login import login_user, logout_user, login_required

companys = Blueprint('companys',__name__,url_prefix='/companys')

@companys.route('/')
def company_list():
    page = request.args.get('page',default=1,type=int)
    pagination = Company.query.paginate(
        page=page,
        per_page = current_app.config['INDEX_PER_PAGE'],
         error_out = False
                                    )

    return render_template('company/index.html',pagination=pagination)
