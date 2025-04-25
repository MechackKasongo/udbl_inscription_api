DROP TABLE IF EXISTS candidats;

CREATE TABLE candidats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    date_naissance TEXT,
    email TEXT UNIQUE,
    telephone TEXT,
    statut TEXT DEFAULT 'Nouveau',
    date_inscription TEXT DEFAULT CURRENT_TIMESTAMP
);