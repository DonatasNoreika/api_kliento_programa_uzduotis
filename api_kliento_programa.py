from flask import Flask, render_template, redirect, url_for
import requests
import json
import forms

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfgsfdgsdfgsdfgsdf'

@app.route('/', methods=['GET'])
def index():
    return gauti_visas_prekes()

@app.route('/prekes', methods=['GET'])
def gauti_visas_prekes():
    r = requests.get('http://127.0.0.1:8000/preke')
    prekiu_sarasas = json.loads(r.text)
    print(prekiu_sarasas)
    return render_template("prekes.html", prekiu_sarasas=prekiu_sarasas)

@app.route("/nauja_preke", methods=["GET", "POST"])
def nauja_preke():
    forma = forms.PrekeForm()
    if forma.validate_on_submit():
        preke = {
            "pavadinimas": forma.pavadinimas.data,
            "kaina": forma.kaina.data,
            "kiekis": forma.kiekis.data
        }
        r = requests.post('http://127.0.0.1:8000/preke', json=preke)
        return redirect(url_for('gauti_visas_prekes'))
    return render_template("nauja_preke.html", form=forma)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
