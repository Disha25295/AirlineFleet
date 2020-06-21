from flask import request, json, Response, Blueprint
from ..models.FleetModel import FleetModel, FleetSchema


fleet_api = Blueprint('fleet', __name__)
fleet_schema = FleetSchema()
fleets_schema = FleetSchema(many=True)

@fleet_api.route('/fleet', methods = ['POST'])
def create():

    req_data =  request.get_json()
    data = fleet_schema.load(req_data)
    error = None

    if error :
        return custom_response(error,400)

    
    plane = FleetModel(data)
    plane.save()
    my_plane = fleet_schema.dump(plane)
    return custom_response(my_plane, 201)

@fleet_api.route('/fleet', methods = ['GET'])
def read():

    all_data = FleetModel.get_fleet()
    print("+++++++++++++++++++++++++++++++")
    print(all_data)
    ser = fleet_schema.dump(all_data, many=True)
    return custom_response(ser, 200)

def custom_response(res,status_code):
    return Response(
        mimetype = "application/json",
        response = json.dumps(res),
        status = status_code
    )