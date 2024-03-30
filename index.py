import json
from flask import Flask, Response, jsonify, request, abort
import requests as req
import socket

app = Flask(__name__)


@app.route('/converte-moedas', methods=['POST'])
def converte_moedas_route() -> tuple[Response, int]:
    try:
        hostname = socket.gethostname()
        body = json.loads(request.data)
        valor = body['valor']
        try:
            float(valor)
        except ValueError:
            raise ValueError("É obrigatório que o valor enviado seja um número.")
        cotacao_euro_e_dolar = resgata_cotacao_euro_e_dolar()
        return jsonify({
            "conversao": {
                "real": valor,
                "dolar": calcula_valor_em_real(valor, cotacao_euro_e_dolar["cotacao_dolar"]),
                "euro": calcula_valor_em_real(valor, cotacao_euro_e_dolar["cotacao_euro"]),
                "maquina": hostname,
            }
        }), 200
    except ValueError as e:
        return abort(400, e)
    except Exception as e:
        return abort(500, e)


def calcula_valor_em_real(valor: float, cotacao: float) -> float:
    return valor * cotacao


def resgata_cotacao_euro_e_dolar() -> dict[str, float]:
    response = req.get(
        'https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL')
    response_json = json.loads(response.content)
    cotacao_dolar = response_json['USDBRL']['high']
    cotacao_euro = response_json['EURBRL']['high']
    return {
        "cotacao_dolar": float(cotacao_dolar),
        "cotacao_euro": float(cotacao_euro)
    }


if __name__ == '__main__':
    app.run(port=5000)
