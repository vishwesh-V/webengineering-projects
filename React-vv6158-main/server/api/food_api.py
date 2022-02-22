from flask_restful import Resource

from flask_restful import request
from flask_restful import reqparse
import json
from .swen_344_db_utils import *
from db import *

parser = reqparse.RequestParser()

class FoodApi(Resource):
    def get(self):
       cat = request.args.get('category')
       return get_food_by_category(cat)

    def put(self):
        food_type = request.form['food']
        newData = request.form['data']
        dataChange = request.form['change']
        result = update_food(food_type, newData, dataChange)
        if(result):
            return True
        return False