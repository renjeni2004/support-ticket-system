
from pathlib import Path

BASE_DIR=Path(__file__).resolve().parent.parent

SECRET_KEY='dev'
DEBUG=True
ALLOWED_HOSTS=[]

INSTALLED_APPS=[
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'rest_framework',
'tickets'
]

MIDDLEWARE=[
'django.middleware.security.SecurityMiddleware',
'django.contrib.sessions.middleware.SessionMiddleware',
'django.middleware.common.CommonMiddleware',
'django.middleware.csrf.CsrfViewMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware',
'django.contrib.messages.middleware.MessageMiddleware'
]

ROOT_URLCONF='supportdesk.urls'

TEMPLATES=[{
'BACKEND':'django.template.backends.django.DjangoTemplates',
'DIRS':[BASE_DIR/'templates'],
'APP_DIRS':True,
}]

WSGI_APPLICATION='supportdesk.wsgi.application'

DATABASES={
'default':{
'ENGINE':'django.db.backends.sqlite3',
'NAME':BASE_DIR/'db.sqlite3'
}
}

STATIC_URL='/static/'
STATICFILES_DIRS=[BASE_DIR/'static']
