#import flask - from package import class
from flask import Flask, render_template
from flask_wtf import CSRFProtect
from flask_bootstrap import Bootstrap5
from flask_mysqldb import MySQL

mysql = MySQL()

#create a function that creates a web application
def create_app():
    app = Flask(__name__)
    app.debug = True
    app.secret_key = 'BetterSecretNeeded123'

    # Enable CSRF Protection
    csrf = CSRFProtect(app)  

    # MySQL configurations
    app.config['MYSQL_HOST']='localhost'
    app.config['MYSQL_USER']='root'
    app.config['MYSQL_PASSWORD']='MySQL@mari0633'
    app.config['MYSQL_DB']='ifn582_assessment3'
    app.config['MYSQL_CURSORCLASS']='DictCursor'

    mysql.init_app(app)

    bootstrap = Bootstrap5(app)
    
    #importing modules here to avoid circular references, register blueprints of routes
    from . import views
    app.register_blueprint(views.bp)

    @app.errorhandler(404) 
    # inbuilt function which takes error as parameter 
    def not_found(e): 
      return render_template("404.html")

    @app.errorhandler(500)
    def internal_error(e):
      return render_template("500.html")
    
    return app