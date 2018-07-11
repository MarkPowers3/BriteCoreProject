from flask_restful import Resource
from flask import Response, json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from util.alchemy_encoder import Alchemy_Encoder
from orm.risk import Risk
from orm.field import Field
from orm.option import Option


class RiskApi(Resource):
    def get(self, risk_id):

        engine = create_engine('sqlite:///risks.db')
        Session = sessionmaker(engine)

        session = Session()
        risk = session.query(Risk).get(risk_id)
        jsonStr = json.dumps(risk, cls=Alchemy_Encoder(), check_circular=False, indent=4)
        session.close()

        return Response(jsonStr, mimetype='application/json')