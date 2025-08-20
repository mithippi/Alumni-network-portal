import os

class Config:
    SECRET_KEY = 'your-secret-key-123'  # Change this to any random string
    SQLALCHEMY_DATABASE_URI = 'sqlite:///alumni.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
