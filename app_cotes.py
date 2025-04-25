from flask import Flask, request, jsonify
import sqlite3

app_cotes = Flask(__name__)
DATABASE = 'udbl_db.db' # Utilisation de la même base de données

def get_db_cotes():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db_cotes():
    with app_cotes.app_context():
        db = get_db_cotes()
        with app_cotes.open_resource('schema_cotes.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
    print('Table des cotes initialisée.')

@app_cotes.cli.command('initdb_cotes')
def initdb_cotes_command():
    """Initialise la table des cotes."""
    init_db_cotes()

@app_cotes.route('/cotes', methods=['POST'])
def enregistrer_cote():
    data = request.get_json()
    candidat_id = data.get('candidat_id')
    cote = data.get('cote')
    date_test = data.get('date_test')
    commentaire = data.get('commentaire')

    if candidat_id is None or cote is None or date_test is None:
        return jsonify({'error': 'ID du candidat, cote et date du test sont requis'}), 400

    db = get_db_cotes()
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO cotes_test (candidat_id, cote, date_test, commentaire) VALUES (?, ?, ?, ?)",
                       (candidat_id, cote, date_test, commentaire))
        db.commit()
        cote_id = cursor.lastrowid
        return jsonify({'id': cote_id, 'message': 'Cote enregistrée'}), 201
    except sqlite3.IntegrityError as e:
        return jsonify({'error': f'Erreur lors de l\'enregistrement de la cote: {e}'}), 400
    finally:
        db.close()

@app_cotes.route('/cotes/<int:candidat_id>', methods=['GET'])
def get_cote_candidat(candidat_id):
    db = get_db_cotes()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM cotes_test WHERE candidat_id = ?", (candidat_id,))
    cote_info = cursor.fetchone()
    db.close()

    if cote_info:
        return jsonify(dict(cote_info)), 200
    return jsonify({'error': 'Cote non trouvée pour ce candidat'}), 404

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    from multiprocessing import Process

    p1 = Process(target=app.run, kwargs={'debug': True, 'port': 5000})
    p2 = Process(target=app_cotes.run, kwargs={'debug': True, 'port': 5001})

    p1.start()
    p2.start()

    p1.join()
    p2.join()