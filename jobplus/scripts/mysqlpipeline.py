import os
import json
from faker import Faker
from jobplus.models import db, User, Company, Job

fake = Faker()


def iter_user_data():
        with open(os.path.join(os.path.dirname(__file__), 'company.json')) as f:
            job_datas = json.load(f)
            for job in job_datas:
                yield User(
                    username=fake.name(),
                    email=fake.email(),
                    password='123456',
                    role=User.ROLE_VISTER)
def iter_company_data():      
        with open(os.path.join(os.path.dirname(__file__), 'company.json')) as f:
            company_datas = json.load(f)
            for company in company_datas:
                yield Company(
                        name=company['name'],
                        location=fake.city_suffix(),
                        logo_url=company['logo_url'],
                        website=fake.url(),
                        description=fake.text(),
                        )
def iter_job_data():
        with  open(os.path.join(os.path.dirname(__file__), 'job.json')) as f:
            job_datas = json.load(f)
            for job in job_datas:
                yield   Job(
                
                        name=job['name'],
                        
                        salary=job['salary'],
                        
                        experience=job['experience'],
                        
                        location=job['location'],
                        
                        degree=job['degree'],
                        
                        description=fake.text(),
                        job_url = job['img_url']
                        )
def run():
    for job in iter_job_data():
        try:
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
