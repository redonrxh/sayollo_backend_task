from flask import request
from flask_restx import Namespace, Resource, fields
from app.src.db.models.impressionsUserDb import findUser, updateUserImpressions, ImpressionsByUser
from app.src.db.models.impressionsSDKDb import findSDK, updateSDKImpressions, ImpressionsBySDK
from app.src.utils import Success, NotFound, BadRequest
import json
import requests


impressions_api = Namespace('impressions')

getImpressionsModel = impressions_api.model('Impressions', {
    'sdk_version': fields.String(required=True),
    'session_id': fields.String(required=True),
    'platform': fields.String(required=True),
    'user_name': fields.String(required=True),
    'country_code': fields.String(required=True),
})

@impressions_api.route('')
class Impressions(Resource):

    @impressions_api.doc(responses={
        200: 'OK',
        400: 'Bad Request',
        401: 'Unauthorized',
        404: 'Not Found'
    })
    @impressions_api.expect(getImpressionsModel)
    def post(self):

        '''Get impression stats'''
        try:

            sdk_version = request.json.get('sdk_version')
            session_id = request.json.get('session_id')
            platform = request.json.get('platform')
            user_name = request.json.get('user_name')
            country_code = request.json.get('country_code')
        except:
            return {"message": BadRequest.message}, BadRequest.status_code

        try:
            if findUser(user_name):
                updateUserImpressions(user_name)
            else:
                ImpressionsByUser(user_name).save()

            if findSDK(sdk_version):
                updateSDKImpressions(sdk_version)
            else:
                ImpressionsBySDK(sdk_version).save()

            return {"message": Success.message}, Success.status_code
        except:
            return {"message": NotFound.message}, NotFound.status_code
