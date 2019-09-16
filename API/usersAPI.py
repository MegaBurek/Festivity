import flask
from flask import request
from flask import session
from flask import jsonify
from API.db_connection import connection



def login(username, password):
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE username=%s AND password=%s"
            cursor.execute(sql, (username, password))
            user = cursor.fetchone()

            if user is not None:
                return True

            return False