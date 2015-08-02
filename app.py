#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request
import csv
import time

app = Flask(__name__)

marcas = [
    {
        'codigo': u'201113844',
        'tiempo': u'11:04:00 15/07/2015',
        'lugar': u'ML004',
        'ip': u'157.253.0.2',
        'ipaccesspoint': u'157.253.0.1',
        'ruido': u'1',
        'luz': u'2',
        'musica': u'JBalvin',
        'temperatura': u'20',
        'humedad': u'30',
        'grupo': u'201116404',
        'infoAdd': u'-'
    },
    {
        'codigo': u'201116404',
        'tiempo': u'11:04:00 15/07/2015',
        'lugar': u'ML009',
        'ip': u'157.253.0.3',
        'ipaccesspoint': u'157.253.0.1',
        'ruido': u'1',
        'luz': u'2',
        'musica': u'JBalvin',
        'temperatura': u'20',
        'humedad': u'30',
        'grupo': u'201113844',
        'infoAdd': u'-'
    }
]

@app.route('/api/marcas', methods=['GET'])
def get_marcas():
    return jsonify({'marcas': marcas})

#Para llamar:
#curl -i -H "Content-Type: application/json" -X POST -d '{"codigo":"201116404","tiempo":"11:04:00 15/07/2015",    "lugar": "ML009","ip":"157.253.0.3","ipaccesspoint": "157.253.0.1","ruido":"1","luz":"2","musica":"JBalvin", "temperatura":"20","humedad":"30","grupo": "201113844","infoAdd":"-"}' http://157.253.235.102:5000/api/marcas


@app.route('/api/marcas', methods=['POST'])
def create_marca():
    if not request.json or not 'codigo' in request.json:
        abort(400)
    marca = {
        'codigo': request.json['codigo'],
        'tiempo': request.json.get('tiempo', ""),
        'lugar': request.json.get('lugar', ""),
        'ip': request.json.get('ip', ""),
        'ipaccesspoint': request.json.get('ipaccesspoint', ""),
        'ruido': request.json.get('ruido', ""),
        'luz': request.json.get('luz', ""),
        'musica': request.json.get('musica', ""),
        'temperatura': request.json.get('temperatura', ""),
        'humedad': request.json.get('humedad', ""),
        'grupo': request.json.get('grupo', ""),
        'infoAdd': request.json.get('infoAdd', "")
    }
    #marcas.append(marca)
    f = open('bd.csv', 'a')
    try:
	writer = csv.writer(f)
	writer.writerow( (
	request.json['codigo'], 
	request.json.get('tiempo', ""),
        request.json.get('lugar', ""),
        request.json.get('ip', ""),
        request.json.get('ipaccesspoint', ""),
        request.json.get('ruido', ""),
        request.json.get('luz', ""),
        request.json.get('musica', ""),
        request.json.get('temperatura', ""),
        request.json.get('humedad', ""),
        request.json.get('grupo', ""),
        request.json.get('infoAdd', ""),
	time.strftime("%c")
	) )
    finally:
    	f.close()
    return jsonify({'marca': marca}), 201

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(host= '157.253.195.165',port=80)
