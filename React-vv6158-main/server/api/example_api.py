from flask_restful import Resource

from flask_restful import request
from flask_restful import reqparse
import json
from .swen_344_db_utils import *

class ExampleApi(Resource):
    def get(self):
    # NOTE: No need to replicate code; use the util function!
       result = exec_get_all("SELECT * FROM people")
       return result

