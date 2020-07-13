from flask import Flask, render_template
import os

app = Flask(__name__, static_folder=os.path.abspath('application/view/static'), template_folder=os.path.abspath('application/view/template'))

from application.controller import a_controller
from application.controller import blog_controller