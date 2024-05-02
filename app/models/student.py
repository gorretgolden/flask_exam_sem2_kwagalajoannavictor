# importing the db
from app.extensions import db




# creating class user and inheriting the model
class Student(db.Model ):
    __tablename__ ='students' 
    # creating an instance
    
    
    id= db.Column(db.Integer, primary_key=True)
    first_name= db.Column(db.String(50), nullable=False)
    last_name= db.Column(db.String(100), nullable=False)
    email= db.Column(db.String(100), nullable=False, unique=True)
    
    
    # creating a constructor so that new instances and new users are tracked
    
    def __init__(self, first_name, last_name, email, password, contact, biography):
        super(Student, self).__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        
        
        

# creating a custom function that concatenates the user's first name and last name
def get_full_name(self):
    
    return f'{self.first_name} {self.last_name}'
    

        
        
    