from peewee import *
from envparse import env

env.read_envfile()
env.read_envfile('.env')

db_host = env.str('mysql_database_host')
<<<<<<< HEAD
db_user = env.str('mysql_username')
db_password = env.str('mysql_password')
=======
db_user = env.str('mysql_database_gsu1_username')
db_password = env.str('mysql_database_gsu1_password')
>>>>>>> 6ab409b6cbf5693675d6cdfdd182f434573965f5
db_name = env.str('mysql_database_name')

db = MySQLDatabase(host=db_host, user=db_user, password=db_password, database=db_name)

db.connect()


class BaseModel(Model):
	class Meta:
		database = db