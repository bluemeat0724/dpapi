from flask import Blueprint

api = Blueprint('api_1_0',__name__)

from app.api_1_0 import sheets_operations,apptool,rolling_operation,universitydata,enterprisedata,governmentdata,industrydata,screendatamanage

