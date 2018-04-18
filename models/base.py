from peewee import *
from envparse import env

env.read_envfile()
env.read_envfile('.env')

db_host = env.str('mysql_database_host')
db_user = env.str('mysql_database_gsu1_username')
db_password = env.str('mysql_database_gsu1_password')
db_name = env.str('mysql_database_name')

db = MySQLDatabase(host=db_host, user=db_user, password=db_password, database=db_name)

db.connect()


class BaseModel(Model):
	class Meta:
		database = db