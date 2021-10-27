import jwt
from base64 import b64decode
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy