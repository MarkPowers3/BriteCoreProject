from flask_restful import Resource
from flask import json, Response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from util.alchemy_encoder import Alchemy_Encoder
from orm.risk import Risk

class RisksApi(Resource):
    def get(self):
        return self.get_risks()

    def get_risks(self):

        engine = create_engine('sqlite:///risks.db')
        Session = sessionmaker(engine)
        session = Session()

        risks = session.query(Risk).all()
        jsonStr = json.dumps(risks, cls=Alchemy_Encoder(), check_circular=False, indent=4)
        session.close()

        return Response(jsonStr, mimetype='application/json')
