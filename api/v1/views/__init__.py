#!/usr/bin/python3
"""bleuprint"""
from flask import Blueprint


simple_page = Blueprint('app_views', __name__,
                        url_prefix='/api/v1')

from api.v1.views import app_views
from api.v1.views.index import *
