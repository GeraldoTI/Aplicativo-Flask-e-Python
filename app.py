from flask import Flask, render_template, request, jsonify, make_response
import csv
import io

app = Flask(__name__)

# Lista para armazenar as tags
tags = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_tag', methods=['POST'])
def add_tag():
    tag = request.form.get('tag')
    if tag and tag not in tags:
        tags.append(tag)
    return jsonify(tags)

@app.route('/get_tags', methods=['GET'])
def get_tags():
    return jsonify(tags)

@app.route('/export_csv', methods=['GET'])
def export_csv():
    # Cria uma resposta para download do CSV
    si = io.StringIO()
    cw = csv.writer(si)
    cw.writerow(['Tags'])  # Cabeçalho do CSV
    for tag in tags:
        cw.writerow([tag])
    
    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=tags.csv"
    output.headers["Content-type"] = "text/csv"
    return output

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Permite acesso externo
