from flask import Blueprint, render_template, request, redirect, url_for
from app import db

# Definir el Blueprint
main_bp = Blueprint('main', __name__)

# Página principal - Lista de usuarios
@main_bp.route('/')
def index():
    return render_template('index.html')