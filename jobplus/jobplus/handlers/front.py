#coding:utf-8
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from jobplus.models import  User
from jobplus.forms import LoginForm,RegisterForm,CompanyRegisterForm
from flask_login import login_user, logout_user, login_required
from jobplus.models import Job
front = Blueprint('front', __name__)

#"""jobplus首页路由"""
@front.route('/')
def index():
    jobs = Job.query.order_by(Job.created_at).limit(9).all()
    companys = User.query.filter(User.role==User.ROLE_HR).order_by(User.created_at.desc()).limit(8)
    return render_template('index.html',
                            jobs=jobs,
                            companys=companys,
                                                     )
#登录时会判断用户的角色

@front.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user, form.remember_me.data)
        if user.is_HR:
            print("______")
            return redirect(url_for("user.hr_index",user_id=user.id))
        elif user.is_admin:
            return redirect(url_for("admin.index"))
        else:
            print("______")
            return redirect(url_for("user.vister_index",user_id=user.id))
    return render_template('login.html', form=form)
    
@front.route('/test',methods=['GET','POST'])
def test():
    return redirect(url_for("admin.index"))

@front.route('/reigster-vister',methods=['GET','POST'])
def register_vister():
    form = RegisterForm()
    if form.validate_on_submit():
        form.create_user()

        flash('注册成功，请登录！', 'success')
        return redirect(url_for('.login'))
    return render_template('register/register_vister.html', form=form)


@front.route('/reigster-hr',methods=['GET','POST'])
def register_hr():
    form = CompanyRegisterForm()
    form.test()
    if form.validate_on_submit():
        form.test()
        form.create_user()
        flash('注册成功，请登录！', 'success')
        return redirect(url_for('.login'))
    return render_template('register/register_hr.html', form=form)


@front.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已经退出登录', 'success')
    return redirect(url_for('.index'))

