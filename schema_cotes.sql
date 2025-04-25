DROP TABLE IF EXISTS cotes_test;

CREATE TABLE cotes_test (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidat_id INTEGER NOT NULL,
    cote REAL,
    date_test TEXT NOT NULL,
    commentaire TEXT,
    FOREIGN KEY (candidat_id) REFERENCES candidats(id)
);