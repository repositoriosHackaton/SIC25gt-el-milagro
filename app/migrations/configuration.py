import os
class Config:
    SQLALCHEMY_DATABASE_URI ="mssql+pyodbc://douglas:1234@DOU-BASIC/Ejemplo?driver=ODBC+Driver+17+for+SQL+Server"
    SQLALCHEMY_TRACK_MODIFICATIONS = False