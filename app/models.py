from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from .import login_manager,db
from datetime import datetime