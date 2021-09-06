#coding=gbk
import os,time,string,random
basedir=os.path.abspath(os.path.dirname(__name__))
BASE_DIR = os.path.dirname(__file__)

class Config:
    SECRET_KEY='lightA0Zr98j/3yX R~XHH!jmN]LWX/,?RTbean'
    PERMANENT_SESSION_LIFETIME=600
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:Mingnisuda2017,@localhost:3306/business'
    CACHE_TYPE = 'simple'

config=Config()