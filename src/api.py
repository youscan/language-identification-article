from flask_restplus import Resource, Api
import os
import ast
from .classifier import cld2_prediction, ft_prediction
import traceback


api = Api(
    title='Mention Language Classification API',
    description='Mention Language Classification API',
    prefix=os.getenv('API_PREFIX', ''),
    doc=os.getenv('API_PREFIX', '/'))

ns = api.namespace('langindentification', description='Language analyzer')
parser = api.parser()

parser.add_argument(
    'texts',
    required=True,
    help="""{
        "texts": [
            "之前推荐过BUCC自己的糖果",
            "nə baxırsan siçan?",
            "Эксклюзивная, Современная игра на бумаге сделал сам  Своими руками(HD)"
        ]
    }
    """,
    location='json'
    )


@ns.route('/cld2')
class LangIndentification_cld2(Resource):
    @ns.doc(parser=parser)
    def post(self):
        try:
            args = parser.parse_args()
            mentions = ast.literal_eval(args["texts"])
            if len(mentions) > 0:
                result = {"results": cld2_prediction(mentions)}
            else:
                result = {"results": []}

            return result, 200
        except:
            result = {"error_code": traceback.format_exc()}
            return result, 500


@ns.route('/ft')
class LangIndentification_ft(Resource):
    @ns.doc(parser=parser)
    def post(self):
        try:
            args = parser.parse_args()
            mentions = ast.literal_eval(args["texts"])
            if len(mentions) > 0:
                result = {"results": ft_prediction(mentions)}
            else:
                result = {"results": []}

            return result, 200
        except:
            result = {"error_code": traceback.format_exc()}
            return result, 500


@ns.route('/healthcheck')
class Healthcheck(Resource):
    def get(self):
        return '', 200
