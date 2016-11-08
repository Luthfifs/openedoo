from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
import json
from datetime import datetime, date
import datetime


Base = declarative_base()

class od_session(Base):
	__tablename__ = 'od_user_session'
	session_id = Column(Integer, primary_key=True,autoincrement=True)
	user_id = Column(Integer)
	token_session = Column(Text())
	created = Column(DateTime())
	def __init__(self,session_id,user_id,token_session,created):
		self.session_id = session_id
		self.user_id = user_id
		self.token_session = token_session
		self.created = created

class od_users(Base):
	__tablename__ = 'od_user'
	user_id = Column(Integer,primary_key=True,autoincrement=True)
	username = Column(String(16))
	password = Column(String(16))
	access_token = Column(Text())
	public_key = Column(Text())
	private_key = Column(Text())
	status = Column(Integer)
	role = Column(String(64))
	created = Column(DateTime())
	last_login = Column(DateTime())
	user_profile = Column(Text())
	user_profile_asd = Column(Text())
	def __init__(self,user_id, username,password,access_token,public_key,private_key,status,role,created,last_login,user_profile,user_profile_asd):
		self.user_id = user_id
		self.username = username
		self.password = password
		self.access_token = access_token
		self.public_key = public_key
		self.private_key = private_key
		self.status = status
		self.role = role
		self.created = created
		self.last_login = last_login
		self.user_profile = user_profile
		self.user_profile_asd = user_profile_asd
'''	def __repr__(self):
		return "<User(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)>" % (self.user_id, self.username, self.password, self.access_token,self.public_key,self.private_key,self.status,self.role,self.created,self.last_login,self.device,self.user_profile)
'''
def db_create():
	engine = create_engine('mysql://root:ayambakar@localhost:3306/db_baru')
	metadata = MetaData(bind=engine)
	auto_map = automap_base()
	Base.metadata.create_all(engine)

db_create()