from flask import Flask, Blueprint
from app.extensions import db,migrate
from flask_sqlalchemy import SQLAlchemy

from app.controllers.student.student import student


# Setting up an application factory function and everything must be within the function
def create_app():
    app = Flask(__name__)
    
    
      
    app.config.from_object('config.Config')
    # enables us import our Config class
    # enables us to work with the application without showing our configuration
    # defining the class
    
    # Initialising the third-party libraries. we pass in the app and db
    db.init_app (app) 
    migrate.init_app(app, db)
    
    
    
    # working with migrations
    
    # importing and registering models
    from app.models.student import Student
    
   
    # testing whether the application works
    @app.route('/')
    def home():
        return "Students API setup"
 # # registering blueprints
     # registering the blueprint auth
#    routes for protected resources
   
    app.register_blueprint(Student)
    
    
   
   

    return app

    

