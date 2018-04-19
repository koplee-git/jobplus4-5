import os
import json
from faker import Faker
from jobplus.models import db, User, Company, Job

fake = Faker()


def iter_user_data():
        with open('./scripts/getjob.json','r',encoding="utf-8") as f:
            job_datas = json.load(f)
            for job in job_datas:
                if User.query.filter_by(username=job['job_company']).first():
                    print("ok")
                    continue
                yield User(
                    username=job['job_company'],
                    email=fake.email(),
                    password='123456',
                    role=User.ROLE_VISTER)
def iter_company_data():      
        with open('./scripts/getjob.json','r',encoding="utf-8") as f:
            company_datas = json.load(f)
            for company in company_datas:
                if Company.query.filter_by(name=company['job_company']).first():
                    continue
                if company.get('company_logo'):
                    yield Company(
                        name=company.get('job_company'),
                        location=company.get('job_station'),
                        logo_url='http:'+ company.get('company_logo'),
                        website=fake.url(),
                        description=company.get('company_description'),
                        )
                else:
                    yield Company(
                        name=company.get('job_company'),
                        location=company.get('job_station'),
                        logo_url="http://img01.zhaopin.cn/2012/img/logo.png",
                        website=fake.url(),
                        description=company.get('company_description'),
                        )
def iter_job_data():
        with open('./scripts/getjob.json','r',encoding="utf-8") as f:
            job_datas = json.load(f)
            for job in job_datas:
                if job.get('company_logo'):
                    yield   Job(
                        name=job['job_name'],
                        salary=job['job_salary'],
                        experience=job['job_experence'],
                        location=job['job_station'],
                        degree=job['job_degree'],
                        description=job['job_description'],
                        job_url = 'http:'+job.get('company_logo')
                        )
                else:
                    yield   Job(
                        name=job['job_name'],
                        salary=job['job_salary'],
                        experience=job['job_experence'],
                        location=job['job_station'],
                        degree=job['job_degree'],
                        description=job['job_description'],
                        job_url = "http://img01.zhaopin.cn/2012/img/logo.png"
                        )
def run():
    print("run")
    for job in iter_company_data():
        try:
            print("add")
            #db.session.add(user)
            #db.session.add(company)
            db.session.add(job)
                
        except Exception as e:
           
            print(e)
                
            db.session.rollback()
            
    try:
            
        db.session.commit()
                
    except Exception as e:
            
        print(e)
        db.session.rollback()

if __name__ == "__main__":
    run()
