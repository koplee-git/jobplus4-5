#coding:utf-8
from jobplus.models import db,User,Resume,Job
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, TextAreaField, IntegerField,SelectField
from wtforms.validators import Length, Email, EqualTo, Required, URL, NumberRange,DataRequired
class LoginForm(FlaskForm):
    email = StringField("邮箱",validators=[Required(),Email()])
    password = PasswordField("密码",validators=[Required(),Length(6,24)])
    remember_me = BooleanField("记住我")
    submit = SubmitField("提交")
    def validata_email(self,field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱未注册')
    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('密码错误')



class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[Required(), Length(3, 24)])
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6, 24)])
    repeat_password = PasswordField('重复密码', validators=[Required(), EqualTo('password')])
    submit = SubmitField('提交') 

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已经存在')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经存在')


    def create_user(self):
        user = User(username=self.username.data,email=self.email.data,password=self.password.data)
        db.session.add(user)
        db.session.commit()
        return user
    def update_user(self, user):
        self.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        return user
    def test(self):
        print("++++++++++")
class CompanyRegisterForm(RegisterForm):
    username = StringField('公司名', validators=[Required(), Length(3, 24)])
    def create_user(self):
        user = User(username=self.username.data,email=self.email.data,password=self.password.data)
        user.is_HR
        db.session.add(user)
        db.session.commit()
        return user
#返回user为了后面扩展，一般创建操作都会返回创建的对象，这里可以不返回user
class JobInfoForm(FlaskForm):
   name = StringField('职位名称',validators=[DataRequired(),Length(3,24)])
   description = StringField('岗位描述',validators=[DataRequired(),Length(1,256)])
   condition = StringField('任职要求',validators=[DataRequired(),Length(1,256)])
   location = StringField('工作地点',validators=[DataRequired(),Length(1,32)])
   company_name = StringField('公司名称',validators=[DataRequired(),Length(3,24)])
   salary = SelectField('薪资范围',choices=[
       ('1','3-6k'),
       ('2','6-9k'),
       ('3','9-15k'),
       ('4','15-25k')])
   experience = SelectField('工作经验',choices=[
       ('1','不限制'),
       ('2','1-3年'),
       ('3','3-5年'),
       ('4','5-10年')])
   degree = SelectField('学历', choices=[
        ('1', '大专'),
        ('2', '本科'),
        ('3', '研究生'),
        ('4', '博士')
        ])
   is_open = SelectField('职位状态',choices=[('10','上线'),('20','下线')])
   submit = SubmitField('提交') 
   def create_job(self,company_id):
       job = Job(name=self.name,salary=self.salary,location=self.location,condition=self.condition,experience=self.experience,degree=self.degree,description=self.description,company_id=company_id)
       db.session.add(job)
       db.session.commit()
       return job
   def update_job(self, job):
        self.populate_obj(job)
        db.session.add(job)
        db.session.commit()
        return job
class ResumeForm(FlaskForm):
    """普通用户简历"""
    username = StringField('姓名', validators=[DataRequired(message=""),Required(), Length(3, 24)])
    gender = SelectField('性别',choices=[('10','男'),('20','女')])
    phone = StringField('手机号码', validators=[DataRequired(),Length(11, 11, )])
    college = StringField('毕业院校', validators=[DataRequired(message='必须填写'),Length(2, 24,)])
    degree = SelectField('学历', choices=[
        ('1', '大专'),
        ('2', '本科'),
        ('3', '研究生'),
        ('4', '博士')
        ])
    major = StringField('专业', validators=[DataRequired(message=''),Length(3, 24, message='专业名称全称')])
    work_year = StringField('工作经验', validators=[DataRequired(),Length(1,256)])
    experience = StringField('工作经验', validators=[DataRequired(),Length(1,256)])
    submit = SubmitField('点击更新')
    def creat_resume(self,user_id):
        resume=Resume(user_id=user_id,name=self.username,gender=self.gender,phone=self.phone,degree=self.degree,work_year=self.work_year,exprience=self.exprience)

        db.session.add(resume)
        db.session.commit()
        return resume
