USE_LOCAL_DB = False

SECRET_KEY = 'longrandomstring'

ADMINS = (
	('Who Ever', 'is@responsib.le'),
)

DATABASES = {
	'default': {
		'ENGINE':	'django.contrib.gis.db.backends.postgis',
		'HOST':		'db', #biogames_postgis
		'PORT':		'5432',
		'NAME':		'postgres',
		#'NAME':		'postgres',
		'USER':		'postgres',
		'PASSWORD':	'secret',
		'ATOMIC_REQUESTS': True,
	}
}
