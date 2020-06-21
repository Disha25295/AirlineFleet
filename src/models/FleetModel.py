from marshmallow import fields, Schema

from . import db

class FleetModel(db.Model):

    __tablename__ = 'fleet'

    id = db.Column(db.Integer, primary_key=True)
    parent_airline = db.Column(db.String(50), nullable=False)
    airline = db.Column(db.String(50))
    aircraft_type = db.Column(db.String(50))
    current = db.Column(db.Integer)
    future = db.Column(db.Integer)
    historic = db.Column(db.Integer)
    total = db.Column(db.Integer)
    orders = db.Column(db.Integer)
    unit_cost = db.Column(db.Integer)
    total_cost = db.Column(db.Integer)
    average_cost = db.Column(db.Float)

    def __init__(self,data):
        self.parent_airline = data.get('parent_airline')
        self.airline = data.get('airline')
        self.aircraft_type = data.get('aircraft_type')
        self.current = data.get('current')
        self.future = data.get('future')
        self.historic = data.get('historic')
        self.total = data.get('total')
        self.orders = data.get('orders')
        self.unit_cost = data.get('unit_cost')
        self.total_cost = data.get('total_cost')
        self.average_cost = data.get('average_cost')
        
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self,key,item)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_fleet():
        return FleetModel.query.all()

    @staticmethod
    def get_one_record(id):
        return FleetModel.query.get(id)


    def __repr(self):
        return '<id {}>'.format(self.id)

class FleetSchema(Schema):
    id = fields.Int(dump_only=True)
    parent_airline = fields.Str(required=True)
    airline = fields.Str(required=True)
    aircraft_type = fields.Str(required=True)
    current = fields.Int(required=True)
    future = fields.Int(required=True)
    historic = fields.Int(required=True)
    total = fields.Int(required=True)
    orders = fields.Int(required=True)
    unit_cost = fields.Int(required=True)
    total_cost = fields.Int(required=True)
    average_cost = fields.Float(required=True)
