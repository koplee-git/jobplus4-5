from flask import Blueprint, render_template, request, current_app, redirect, url_for, flash
from jobplus.decorators import admin_required
from jobplus.models import User,db,Job,Company
from jobplus.forms import RegisterForm,JobInfoForm
from flask_login import current_user
admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('/')
@admin_required
def index():
    return render_template('admin/admin_base.html')


@admin.route('/users')
@admin_required
def user():
    page = request.args.get('page', default=1, type=int)
    pagination = User.query.paginate(
        page=page,
        per_page=current_app.config['ADMIN_PER_PAGE'],
        error_out=False
    )
    return render_template('admin/user_list.html', pagination=pagination)

@admin.route('/jobs')
@admin_required
def job():
    page = request.args.get('page',default=1,type=int)
    pagination = Job.query.paginate(
        page=page,
        per_page=current_app.config['ADMIN_PER_PAGE'],
        error_out=False
    )
    return render_template('admin/job_list.html', pagination=pagination)


@admin.route('/users/create',methods=['GET','POST'])
@admin_required
def create_user():
    form =  RegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('创建用户成功', 'success')
        return redirect(url_for('admin.user'))
    return render_template('admin/create_user.html', form=form)

@admin.route('/jobs/create',methods=['GET','POST'])
@admin_required
def create_job():
    form =  JobInfoForm()
    if form.validate_on_submit():
        company=Company.query.filter_by(name=form.company_name.data).first()
        company_id=company.id
        print("+++++++++++++++++++++")
        print(company_id)
        print("+++++++++++++++++++++")
        form.create_job(company_id)
        flash('创建用户成功', 'success')
        return redirect(url_for('admin.job'))
    return render_template('admin/create_job.html', form=form)

@admin.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
@admin_required
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    form =RegisterForm(obj=user)
    if form.validate_on_submit():
        form.update_user(user)
        flash('用户更新成功', 'success')
        return redirect(url_for('admin.user'))
    return render_template('admin/edit_user.html', form=form, user=user)


@admin.route('/jobs/<int:job_id>/edit', methods=['GET', 'POST'])
@admin_required
def edit_job(job_id):
    job = Job.query.get_or_404(job_id)
    form =JobInfoForm(obj=job)
    if form.validate_on_submit():
        form.update_job(job)
        flash('职位更新成功', 'success')
        return redirect(url_for('admin.job'))
    return render_template('admin/edit_job.html', form=form, job=job)

@admin.route('/users/<int:user_id>/delete',methods=['GET','POST'])
@admin_required
def delete_user(user_id):
    if current_user.id == user_id:
        flash('不能删除自己','success')
        return redirect(url_for('admin.user'))
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('删除成功','success')
    return redirect(url_for('admin.user'))

@admin.route('/jobs/<int:job_id>/delete',methods=['GET','POST'])
@admin_required
def delete_job(job_id):
    job = Job.query.get_or_404(job_id)
    db.session.delete(job)
    db.session.commit()
    flash('删除成功','success')
    return redirect(url_for('admin.job'))

@admin.route('/jobs/<int:job_id>/able',methods=['GET','POST'])
@admin_required
def able_job(job_id):
    job = Job.query.get_or_404(job_id)
    if job.is_open:
        job.is_open=False
        flash('下线成功','success')
    else:
        job.is_open=True
        flash('上线成功','success')
    db.session.add(job)
    db.session.commit()
    return redirect(url_for('admin.job'))
