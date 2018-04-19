""""普通用户和企业用户登录路由"""
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from jobplus.models import  User,Company,Job,Deliver,Resume
from jobplus.forms import ResumeForm,JobInfoForm,CompanyForm
from flask_login import login_user, logout_user, login_required,current_user
from jobplus.decorators import vister_required,hr_required

user = Blueprint('user', __name__, url_prefix='/user')

#用户登录后的首页路由
@vister_required
@user.route('/vister/<user_id>')
def vister_index(user_id):
    """普通用户帐号信息"""
    resume = Resume.query.filter_by(id=user_id).first()
    if resume:
   # user_id = current_user.id
        user = User.query.filter_by(id=user_id).first()
        return render_template('user/vister_index.html',user=user,resume=resume)
    else:
        redirect(url_for('user.resume',user_id=user_id))
@vister_required
@user.route('/vister/<user_id>/createresume',methods=['GET','POST'])
def resume(user_id):
    """用户创建简历信息"""
    form =ResumeForm()
    if form.validate_on_submit():
        form.create_resume(user_id)
        flash('简历创建成功','success')
        return redirect(url_for('user.vister_index',user_id=user_id))
    return render_template('user/create_resume.html',form=form)


@hr_required
@user.route('/hr/<user_id>')
def hr_index(user_id):
    """企业用户帐号信息"""
    user = User.query.filter_by(id=user_id).first()
    company_id=user.companyid
    company=Company.query.filter_by(id=company_id).first()
    return render_template('user/hr_index.html',user=user,company=company)


@hr_required
@user.route('/hr/<user_id>/resumelist')
def resume_list(user_id):
    """企业用户查看简历"""
    user = User.query.filter_by(id=user_id).first()
    company_id=user.companyid
    delivers=Deliver.query.filter_by(company_id=company_id).all()
    return render_template('/user/check_resume.html',delivers=delivers,user=user)
@hr_required
@user.route('/hr/<user_id>/resumedetail')
def resume_detail(user_id):
    """企业用户查看某一位求职者的简历"""
    resume = Resume.query.filter_by(user_id=user_id).first()
    return render_template('/user/resume_detail.html',resume=resume)

@hr_required
@user.route('/hr/<user_id>/company')
def companyinfo(user_id):
    """企业用户完善企业信息"""

    user = User.query.filter_by(id=user_id).first()
    form = CompanyForm()
    if form.validate_on_submit():
        form.update()
        flash('企业信息创建成功','success')
        return redirect(url_for('user.hr_vister'))

    return render_template('user/hr_index.html',user=user,form=form)
@hr_required
@user.route('/hr/<user_id>/joblist')
def job_list(user_id):
    """"企业用户查看职位列表"""
    user=User.query.filter_by(id=user_id).first()
    company_id=user.companyid
    print(company_id)
    jobs = Job.query.filter_by(company_id=company_id).all() 
    return render_template('user/job_list.html',jobs=jobs,user=user)

@hr_required
@user.route('/hr/<user_id>/jobcreate',methods=['GET','POST'])
def create_job(user_id):
    form =  JobInfoForm()
    if form.validate_on_submit():
        print(form.company_name.data)
        company=Company.query.filter_by(name=form.company_name.data).first()
        company_id=company.id
        form.create_job(company_id)
        flash('创建职位成功', 'success')
        return redirect(url_for('user.hr_index',user_id=user_id))
    return render_template('user/create_job.html', form=form)
