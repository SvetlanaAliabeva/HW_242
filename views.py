from typing import Union

from flask import Blueprint, request, jsonify, Response
from marshmallow import ValidationError

from builder import build_query
from models import BatchRequestSchema

main_bp = Blueprint('main', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query() -> Response | tuple[Response, int]:
    # TODO: Принять запрос от пользователя
    data: dict = request.json

    # TODO: Обработать запрос, валидировать значения
    try:
        BatchRequestSchema().load(data)
    except ValidationError as error:
       return jsonify(error.messages), 400

    # TODO: Выполнить запрос
    result = None
    for query in data['queries']:
        result = build_query(
            cmd=query['cmd'],
            value=query['value'],
            file_name=data['file_name'],
            data=result,
            )

    return jsonify(result)

