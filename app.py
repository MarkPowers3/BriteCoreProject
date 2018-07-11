from flask import Flask, render_template, redirect, safe_join, send_from_directory
from flask_restful import Api
from flask_cors import CORS
from restful.risk_api import RiskApi
from restful.risks_api import RisksApi

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/risk*/*": {"origins": "*"}})


api.add_resource(RisksApi, '/risks')
api.add_resource(RiskApi, '/risk/<risk_id>')


if __name__ == '__main__':
    app.run(debug=True, port = 5000)
