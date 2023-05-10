import flask
import base64
import util

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'Hello!'


@app.route('/bank_statement', methods=['POST'])
def bank_statement():
    """
    Обрабатывать запросы на /bank_statement и возвращать результат
    :return: Json data
    """
    data = flask.request.json
    statement = base64.b64decode(data['base64-bank_statement'])

    text = util.read_pdf(statement=statement)

    # TODO: необходимо обработать полученную банковскую выписку и получить информацию о транзакциях
    transactions = []

    # TODO: возвращать обработанные данные в виде JSON
    return flask.jsonify({'personal_info': {'name': 'Person', 'passport': '123'},
                          'transactions': transactions})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
