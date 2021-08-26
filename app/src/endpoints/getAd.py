from flask import request, Response
from flask_restx import Namespace, Resource, fields
import requests
from app.src.db.models.adRequestsSDKDb import findSDK, updateSDKAdRequests, AdRequestsBySDK
from app.src.db.models.adRequestsUserDb import findUser, updateUserAdRequests, AdRequestsByUser
from app.src.utils import Success, NotFound, BadRequest

getAd_api = Namespace('getAd')

getAdModel = getAd_api.model('GetAd', {
    'sdk_version': fields.String(required=True),
    'session_id': fields.String(required=True),
    'platform': fields.String(required=True),
    'user_name': fields.String(required=True),
    'country_code': fields.String(required=True)
})

@getAd_api.route('')
class GetAd(Resource):

    @getAd_api.doc(responses={
        200: 'OK',
        400: 'Bad Request',
        401: 'Unauthorized',
        404: 'Not Found'
    })
    @getAd_api.expect(getAdModel)
    def post(self):

        '''GetAd stats'''
        try:

            sdk_version = request.json.get('sdk_version')
            session_id = request.json.get('session_id')
            platform = request.json.get('platform')
            user_name = request.json.get('user_name')
            country_code = request.json.get('country_code')

            if sdk_version and user_name:
                try:
                    api_url = 'https://6u3td6zfza.execute-api.us-east-2.amazonaws.com/prod/ad/vast'
                    req = requests.get(url=api_url)
                    xml = req.content

                    if findUser(user_name):
                        updateUserAdRequests(user_name)
                    else:
                        AdRequestsByUser(user_name).save()

                    if findSDK(sdk_version):
                        updateSDKAdRequests(sdk_version)
                    else:
                        AdRequestsBySDK(sdk_version).save()

                    resp = Response(response=xml, status=200, mimetype="application/xml")

                    resp.headers["Content-Type"] = "text/xml; charset=utf-8"

                    return resp

                except:
                    return {"message": NotFound.message}, NotFound.status_code
            else:
                return {"message": BadRequest.message}, BadRequest.status_code

        except:
            return {"message": BadRequest.message}, BadRequest.status_code

