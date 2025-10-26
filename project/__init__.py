# import flask - from package import class
from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from flask_mysqldb import MySQL
from uuid import uuid4
import os

mysql = MySQL()


#create a function that creates a web application
# a web server will run this web application
def create_app():
    app = Flask(__name__,static_folder="static")
    app.debug = True
    app.secret_key = 'BetterSecretNeeded123'
    app.config['UPLOAD_FOLDER'] = os.path.join(app.static_folder, 'img')
    app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    

    # MySQL configurations
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'PASSWORD'
    app.config['MYSQL_DB'] = 'sql12802431'
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

    mysql.init_app(app)
    bootstrap = Bootstrap5(app)
    
    #importing modules here to avoid circular references, register blueprints of routes
    from project import views
    app.register_blueprint(views.bp)
    
    @app.context_processor
    def inject_global_data():
        from project.db import get_all_services
        try:
            services = get_all_services()
        except Exception as e:
            print(f"Error loading services for context: {e}")
            services = []
        return dict(global_services=services)
                           
    @app.errorhandler(404) 
    # inbuilt function which takes error as parameter 
    def not_found(e): 
      return render_template("404.html")

    @app.errorhandler(500)
    def internal_error(e):
      return render_template("500.html")

  

    return app
