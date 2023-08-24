"""
测试模拟声明式配置文件
"""

SECRET_KEY = 'fake-key'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django_quanttide_hr',
    "tests",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3"
    }
}