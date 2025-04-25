# API REST pour le Processus d'Inscription à l'UDBL

Ce projet implémente une API REST pour gérer le processus d'inscription et la gestion des cotes pour l'Université de Droit de Bukavu (UDBL). Il comprend deux services web distincts construits avec Flask et utilise une base de données SQLite pour le stockage des données.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :

* **Python 3.6+**
* **pip** (le gestionnaire de paquets pour Python)
* **Git** (pour cloner le dépôt)

## Instructions d'Installation et d'Exécution

Suivez ces étapes pour faire fonctionner l'API sur votre machine locale :

1.  **Cloner le dépôt :**

    Si vous avez ce projet sur GitHub, clonez-le dans le répertoire de votre choix en utilisant la commande suivante dans votre terminal :

    ```bash
    git clone <URL_DU_DÉPÔT>
    cd nom_du_répertoire_du_projet
    ```

2.  **Créer et activer un environnement virtuel (recommandé) :**

    Il est recommandé de créer un environnement virtuel pour isoler les dépendances du projet.

    * Sur macOS/Linux :
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * Sur Windows (dans l'invite de commandes) :
        ```bash
        python venv\Scripts\activate
        ```
    * Sur Windows (dans PowerShell) :
        ```powershell
        .\venv\Scripts\Activate.ps1
        ```

    Votre prompt de terminal devrait maintenant être préfixé par `(venv)`.

3.  **Installer les dépendances :**

    Bien que ce projet n'ait qu'une seule dépendance principale pour l'instant, installons Flask dans l'environnement virtuel :

    ```bash
    pip install Flask
    ```

4.  **Initialiser la base de données SQLite :**

    Exécutez les commandes Flask pour créer et initialiser les tables de la base de données SQLite. Assurez-vous d'être toujours dans le répertoire racine du projet et que l'environnement virtuel est activé.

    ```bash
    flask --app app_inscriptions.py initdb
    flask --app app_cotes.py initdb_cotes
    ```

    Ces commandes vont créer le fichier `udbl_db.db` et configurer les tables `candidats` et `cotes_test`. Vous devriez voir des messages de confirmation dans votre terminal.

5.  **Lancer les serveurs web Flask :**

    Vous devrez ouvrir **deux** terminaux (ou utiliser des onglets distincts dans votre terminal) pour exécuter chaque service web séparément. Assurez-vous que l'environnement virtuel est activé dans les deux terminaux.

    * **Dans le premier terminal (pour le service d'inscription - port 5000) :**
        ```bash
        flask --app app_inscriptions.py run --debug --port 5000
        ```

    * **Dans le deuxième terminal (pour le service de gestion des cotes - port 5001) :**
        ```bash
        flask --app app_cotes.py run --debug --port 5001
        ```

    Vous devriez voir des messages indiquant que les serveurs Flask sont en cours d'exécution sur `http://127.0.0.1:5000` et `http://127.0.0.1:5001`. Le mode `--debug` est activé pour faciliter le développement. **N'utilisez pas le serveur de développement en production.**

## Utilisation de l'API

Une fois les serveurs en cours d'exécution, vous pouvez interagir avec l'API en utilisant des clients HTTP comme :

* **Votre navigateur web** (pour les requêtes `GET` simples).
* **`curl`** (en ligne de commande).
* **Postman** ou **Insomnia** (applications de bureau pour tester les APIs).

### Endpoints

Voici les endpoints principaux que nous avons implémentés :

**Service d'inscription (http://127.0.0.1:5000)**

* `POST /inscriptions`: Enregistre un nouveau candidat. Le corps de la requête doit être au format JSON avec les informations du candidat (nom, prenom, email, date\_naissance, telephone).
* `GET /inscriptions/{id}`: Récupère les informations d'un candidat spécifique en utilisant son ID. Remplacez `{id}` par l'identifiant du candidat.

**Service de gestion des cotes (http://127.0.0.1:5001)**

* `POST /cotes`: Enregistre la cote d'un candidat. Le corps de la requête doit être au format JSON avec l'ID du candidat (`candidat_id`), la cote (`cote`), la date du test (`date_test`) et un commentaire (facultatif).
* `GET /cotes/{candidat_id}`: Récupère la cote d'un candidat spécifique en utilisant son `candidat_id`.

### Exemples de requêtes (`curl`)

**Créer une inscription :**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"nom": "Doe", "prenom": "John", "email": "john.doe@example.com", "date_naissance": "2000-01-15", "telephone": "0975008388"}' [http://127.0.0.1:5000/inscriptions](http://127.0.0.1:5000/inscriptions)# udbl_inscription_api
