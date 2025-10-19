#import flask - from package import class
from flask import Flask, render_template, session
from flask_bootstrap import Bootstrap5
from flask_mysqldb import MySQL
from uuid import uuid4
from flask_login import LoginManager, current_user
import os
from MySQLdb.cursors import DictCursor
from project.models import User 

mysql = MySQL()

login_manager = LoginManager()
login_manager.login_view = "main.login"
login_manager.login_message_category = "warning"



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
    app.config['MYSQL_PASSWORD'] = 'Smbrella5991'
    app.config['MYSQL_DB'] = 'sql12802431'
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

    mysql.init_app(app)
    login_manager.init_app(app)
    bootstrap = Bootstrap5(app)
    
    #importing modules here to avoid circular references, register blueprints of routes
    from project import views
    app.register_blueprint(views.bp)
    
                           
    @app.errorhandler(404) 
    # inbuilt function which takes error as parameter 
    def not_found(e): 
      return render_template("404.html")

    @app.errorhandler(500)
    def internal_error(e):
      return render_template("500.html")

  

    return app

 

@login_manager.user_loader
def load_user(user_id: str):

    cur = mysql.connection.cursor(DictCursor)

    if user_id.startswith("p-"):
        pid = user_id.split("p-")[-1]
        cur.execute("SELECT photographer_id AS id, email FROM Photographer WHERE photographer_id=%s", (pid,))
        row = cur.fetchone(); cur.close()
        if not row: return None
        return User(id=f"p-{row['id']}", email=row["email"], role="photographer", photographer_id=row["id"])

    if user_id.startswith("c-"):
        cid = user_id.split("c-")[-1]
        cur.execute("SELECT client_id AS id, email FROM Client WHERE client_id=%s", (cid,))
        row = cur.fetchone(); cur.close()
        if not row: return None
        return User(id=f"c-{row['id']}", email=row["email"], role="client")

    if user_id.startswith("a-"):
        aid = user_id.split("a-")[-1]
        cur.execute("SELECT admin_id AS id, email FROM Admin WHERE admin_id=%s", (aid,))
        row = cur.fetchone(); cur.close()
        if not row: return None
        return User(id=f"a-{row['id']}", email=row["email"], role="admin")

    cur.close()
    return None