USE_LOCAL_DB = False

SECRET_KEY = 'longrandomstring'

ADMINS = (
	('Who Ever', 'clemens.klug@uni-bamberg.de'),
)

DATABASES = {
	'default': {
		'ENGINE':	'django.contrib.gis.db.backends.postgis',
		'HOST':		'db', #biogames_postgis
		'PORT':		'5432',
		'NAME':		'biogames',
		#'NAME':		'postgres',
		'USER':		'postgres',
		'PASSWORD':	'secret',
		'ATOMIC_REQUESTS': True,
	}
}
