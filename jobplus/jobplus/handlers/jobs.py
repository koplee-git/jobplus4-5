""" 职位详情，职位列表"""
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from jobplus.models import  User,Job,Deliver,db
from jobplus.forms import LoginForm,RegisterForm,CompanyRegisterForm
from flask_login import login_user, logout_user, login_required
from jobplus.decorators import vister_required

jobs = Blueprint('jobs',__name__,url_prefix='/jobs')

@jobs.route('/')
def job_list():
    page = request.args.get('page',default=1,type=int)
    pagination = Job.query.paginate(
        page=page,
        per_page = current_app.config['INDEX_PER_PAGE'],
         error_out = False
         )
    return render_template('job/index.html',pagination=pagination)
    

@jobs.route('/job/<int:job_id>')
def job_detail(job_id):
    job=Job.query.get_or_404(job_id)
    return render_template('job/job_detail.html',job=job)
@vister_required
@jobs.route('/job/<user_id>/<job_id>/deliver')
def deliver(user_id,job_id):
    job = Job.query.get_or_404(job_id)

    deliver=Deliver(user_id=user_id,job_id=job.id,company_id=job.company_id)
    db.session.add(deliver)
    db.session.commit()
    flash('投递成功', 'success')
    return render_template('job/job_detail.html',job=job)
