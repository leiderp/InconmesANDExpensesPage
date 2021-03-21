from sqlalchemy import Column, Integer, String, Date, Float,ForeignKey
from sqlalchemy.orm import relationship
from aplicacion.index import db

class Users(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False)
    password = Column(String(200),nullable=False)
    incomes = relationship("Incomes", cascade ="all, delete-orphan", backref="Users",lazy=True)
    expenses = relationship("Expenses", cascade ="all, delete-orphan", backref="Users",lazy=True)
    
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)

class Incomes(db.Model):
    __tablename__ = 'incomes'
    id = Column(Integer,primary_key=True)
    date = Column(Date,nullable=False)
    description = Column(String(200), nullable=False)
    amount = Column(Float,nullable=False)
    userId = Column(Integer,ForeignKey('users.id'),nullable=False)
    
class Expenses(db.Model):
    __tablename__ = 'expenses'
    id = Column(Integer,primary_key=True)
    date = Column(Date,nullable=False)
    description = Column(String(200), nullable=False)
    amount = Column(Float,nullable=False)
    userId = Column(Integer,ForeignKey('users.id'),nullable=False) 