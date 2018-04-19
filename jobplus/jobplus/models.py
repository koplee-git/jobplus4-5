#coding:utf-8
from flask_login import UserMixin,current_user
from flask_sqlalchemy import SQLAlchemy
from flask import url_for
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
db=SQLAlchemy()
class Base(db.Model):

    __abstract__ = True
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)
class User(Base,UserMixin):
    __tablename__ = 'user'
    ROLE_VISTER = 10
    ROLE_HR = 20
    ROLE_ADMIN = 30
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(128), unique=True, index=True, nullable=False)
##用户名 可以公司名或者用户名字
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
##注册邮箱，用户用户登录
    _password = db.Column('password', db.String(256), nullable=False)
    role = db.Column(db.SmallInteger, default=ROLE_VISTER)
    company_id = db.Column(db.Integer,db.ForeignKey('company.id'),nullable=True)
    def __repr__(self):
        return "<User:{}>".format(self.username)
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,orig_password):
        self._password = generate_password_hash(orig_password)
    def check_password(self,password):
        return check_password_hash(self._password,password)
    @property
    def is_HR(self):
        return self.role == self.ROLE_HR
    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN
    @property
    def companyid(self):
        company=Company.query.filter_by(name=self.username).first()
        self.company_id=company.id
        return self.company_id

class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer,primary_key=True)
    logo_url = db.Column(db.String(256),nullable=True)
    name = db.Column(db.String(32),nullable=True)
    website = db.Column(db.String(32),nullable=True)
    description = db.Column(db.String(256),nullable=True)
    location = db.Column(db.String(32),nullable=True)
    user =db.relationship('User',backref='company')
class Job(Base):
        __tablename__ = 'job'
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(256))
        salary = db.Column(db.String(128), nullable=False)
        location = db.Column(db.String(256))
        condition = db.Column(db.String(256),nullable=True)
        experience = db.Column(db.String(256))
        degree = db.Column(db.String(256))
        description = db.Column(db.String(128))
        is_fulltime = db.Column(db.Boolean, default=True)
        is_open = db.Column(db.Boolean, default=True)
        company_id = db.Column(db.Integer, db.ForeignKey('company.id', ondelete='CASCADE'))
        job_url = db.Column(db.String(256),nullable=True)
        company = db.relationship('Company', uselist=False)
        def __repr__(self):
             return '<Job {}>'.format(self.name)
        @property 
        def current_user_is_applied(self):
            d = Deliver.query.filter_by(job_id=self.id,user_id=current_user.id).first()
            return (d is not None)
class Resume(Base):
    __tablename__ = "resume"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    name = db.Column(db.String(24))
    gender = db.Column(db.String(24))
    phone = db.Column(db.Integer)
    college = db.Column(db.String(24))
    degree = db.Column(db.String(24))
    major = db.Column(db.String(24))
    work_year = db.Column(db.Integer)
    description = db.Column(db.String(1024))
class Deliver(Base):
    __tablename__ ='deliver'
    STATUS_WAITING=1
    STATUS_REJECT=2
    STATUS_APPCEPT=3
    
    id =  db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id',ondelete='SET NULL'))
    job_id = db.Column(db.Integer,db.ForeignKey('job.id',ondelete='SET NULL'))
    company_id = db.Column(db.String(24))
    status=db.Column(db.SmallInteger,default=STATUS_WAITING)
    response = db.Column(db.String(256))

    @property
    def user(self):
        return User.query.get(self.user_id)
    @property
    def job(self):
        return Job.query.get(self.job_id)
