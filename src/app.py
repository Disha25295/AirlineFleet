from flask import Flask

from .config import app_config

from .views.FleetView import fleet_api

from .models import db
def create_app(env):

    app = Flask(__name__)


    app.config.from_object(app_config[env])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    app.register_blueprint(fleet_api)

    @app.route('/', methods = ['GET'])
    def index():

        return 'Congratulations. workin'

    return app  




