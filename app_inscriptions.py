from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'udbl_db.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Pour accéder aux colonnes par nom
    return conn

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initialise la base de données."""
    init_db()
    print('Base de données initialisée.')

@app.route('/inscriptions', methods=['POST'])
def create_inscription():
    data = request.get_json()
    nom = data.get('nom')
    prenom = data.get('prenom')
    email = data.get('email')
    # ... Récupérer les autres données

    if not nom or not prenom or not email:
        return jsonify({'error': 'Nom, prénom et email sont requis'}), 400

    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO candidats (nom, prenom, email) VALUES (?, ?, ?)", (nom, prenom, email))
        db.commit()
        candidat_id = cursor.lastrowid
        return jsonify({'id': candidat_id, 'message': 'Inscription réussie'}), 201
    except sqlite3.IntegrityError as e:
        return jsonify({'error': f'Erreur lors de l\'inscription: {e}'}), 400
    finally:
        db.close()

@app.route('/inscriptions/<int:candidat_id>', methods=['GET'])
def get_inscription(candidat_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM candidats WHERE id = ?", (candidat_id,))
    candidat = cursor.fetchone()
    db.close()

    if candidat:
        return jsonify(dict(candidat)), 200
    return jsonify({'error': 'Candidat non trouvé'}), 404

if __name__ == '__main__':
    app.run(debug=True)