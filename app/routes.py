from flask import Blueprint, request, jsonify
from .models import Destination, Itinerary, Expense, db

bp = Blueprint('api', __name__)

@bp.route('/destinations', methods=['GET', 'POST'])
def destinations():
    if request.method == 'GET':
        destinations = Destination.query.all()
        return jsonify([destination.serialize() for destination in destinations])

    if request.method == 'POST':
        data = request.json
        new_destination = Destination(**data)
        db.session.add(new_destination)
        db.session.commit()
        return jsonify(new_destination.serialize()), 201

# Define similar routes for Itinerary and Expense

