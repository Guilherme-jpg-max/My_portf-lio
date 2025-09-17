from flask import Blueprint, render_template, request, jsonify, send_file, current_app
from app import mail
from .forms import process_contact_form
import os
from .github_utils import get_github_repos


bp = Blueprint("main", __name__)

def get_repos():
    try:
        return get_github_repos()
    except Exception as e:
        print(f"Erro ao buscar repositório: {e}")
        return[]

def render_templates(template_name, **context):
    repos = get_repos()
    return render_template(template_name, repos=repos, **context)

@bp.route("/")
def index():
    return render_templates("index.html", title="Portfólio Guilherme Carlos")


@bp.route("/projects")
def projects():
    return render_templates("index.html", title="Projects", section="projects")


@bp.route("/bout")
def projects():
    return render_templates("index.html", title="bout", section="bout")

@bp.route("/contact", methods=["POST"])
def contact():
    success, msg = process_contact_form(request, mail, os)
    
    if success:
        try:
            mail.send(msg)
            return jsonify({"success": True, "message": "Mensagem enviada com sucesso!"}), 200
        except Exception:
            return jsonify({"success": False, "message": "Ocorreu um erro ao enviar a mensagem. Tente novamente mais tarde."}), 500
    return jsonify({"success": False, "message": "Dados inválidos."}), 400


@bp.route("/skills")
def skills():
    return render_templates("index.html", title="skills", section="skills")