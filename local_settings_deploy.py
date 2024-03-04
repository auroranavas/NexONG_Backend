import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = ["*"]

# SECRET_KEY = os.environ.get("SECRET_KEY")

SECRET_KEY = "postgres://nexongdb:manosabiertas2024@//cloudsql/ispp-backend:europe-west1:nexongdb/nexongdb"


DEBUG = False

# Modules in use, commented modules that you won't use
MODULES = [
    "nexong",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
# STATICFILES_STORAGE = os.getenv("GS_BUCKET_NAME")
STATICFILES_STORAGE = "ispp-backend_ispp-backend.appspot.com"
"""
BASEURL = "https://{}".format(os.environ.get("RENDER_EXTERNAL_HOSTNAME"))

APIS = {
    "authentication": BASEURL,
    "base": BASEURL,
    "booth": BASEURL,
    "census": BASEURL,
    "mixnet": BASEURL,
    "postproc": BASEURL,
    "store": BASEURL,
    "visualizer": BASEURL,
    "voting": BASEURL,
}
"""
# DATABASE_URL = os.environ.get("DATABASE_URL")
DATABASE_URL = "postgres://nexongdb:manosabiertas2024@//cloudsql/ispp-backend:europe-west1:nexongdb/nexongdb"
DATABASES = {"default": dj_database_url.parse(DATABASE_URL)}

# ALLOWED_ORIGINS = ["https://{}".format(os.environ.get("RENDER_EXTERNAL_HOSTNAME"))]
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = "Strict"
# CSRF_TRUSTED_ORIGINS = ALLOWED_ORIGINS.copy()

# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256
