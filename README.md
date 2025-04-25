# API REST pour le Processus d'Inscription à l'UDBL

Ce travail implémente une API REST pour gérer le processus d'inscription et la gestion des cotes pour l'Université de Don Bosco de Lubumbashi (UDBL). Il comprend deux services web construits avec Flask et utilise une base de données SQLite pour le stockage des données.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine car le test et la consommation de l'api sont faits en local :

### A installer :

* Python 3.6+
* pip (le gestionnaire de paquets pour Python)
* Git (pour cloner le dépôt)
* Postman (recommandé pour tester l'API) - [https://www.postman.com/downloads/](https://www.postman.com/downloads/)
* `curl` (généralement préinstallé sur la plupart des systèmes d'exploitation)

## Instructions d'Installation et d'Exécution

Suivez ces étapes pour faire fonctionner l'API sur votre machine locale :

1.  **Cloner le dépôt :**

    Si vous avez ce projet sur GitHub, clonez-le dans le répertoire de votre choix en utilisant la commande suivante dans votre terminal (pour mon cas je suis sur Linux) :

    ```bash
    git clone <URL_DU_DÉPÔT>
    cd nom_du_répertoire_du_projet
    ```

2.  **Créer et activer un environnement virtuel (recommandé) :**

    Il est préférable de créer un environnement virtuel pour isoler les dépendances du projet dans le dossier où vous avez mis le travail.

    * sur macOS/Linux :
        ```bash
        # Exécuter ça dans le terminal:
        python3 -m venv venv
        source venv/bin/activate
        ```
    * Sur Windows (dans l'invite de commandes) :
        ```bash
        # Exécuter ça dans le terminal:
        python venv\Scripts\activate
        ```
    * Si vous l'exécutez (dans PowerShell) :
        ```powershell
        .\venv\Scripts\Activate.ps1
        ```

    Votre prompt de terminal devrait maintenant être préfixé par `(venv)`.

3.  **Installer les dépendances :**

    Installons Flask dans l'environnement virtuel en exécutant cette commande toujours dans le terminal :

    ```bash
    pip install Flask
    ```

4.  **Initialiser la base de données SQLite :**

    Exécutez les commandes Flask pour créer et initialiser les tables de la base de données SQLite. Assurez-vous d'être toujours dans le répertoire racine du projet et que l'environnement virtuel est activé.

    Exécutez ces deux commandes :

    ```bash
    flask --app app_inscriptions.py initdb
    flask --app app_cotes.py initdb_cotes
    ```

    Ces commandes vont créer le fichier `udbl_db.db` et configurer les tables `candidats` et `cotes_test`. Vous devriez voir des messages de confirmation dans votre terminal.

5.  **Lancer les serveurs web Flask :**

    Vous devrez ouvrir deux terminaux pour exécuter chaque service web séparément. Assurez-vous que l'environnement virtuel est activé dans les deux terminaux toujours à la racine du travail du projet.

    * Dans le premier terminal (pour le service d'inscription - port 5000) :
        ```bash
        flask --app app_inscriptions.py run --debug --port 5000
        ```

    * Dans le deuxième terminal (pour le service de gestion des cotes - port 5001) :
        ```bash
        flask --app app_cotes.py run --debug --port 5001
        ```

    Vous devriez voir des messages indiquant que les serveurs Flask sont en cours d'exécution sur `http://127.0.0.1:5000` et `http://127.0.0.1:5001`. Le mode `--debug` est activé pour faciliter le développement. **N'utilisez pas le serveur de développement en production.**

## Utilisation de l'API

Une fois les serveurs en cours d'exécution, vous pouvez interagir avec l'API en utilisant des clients HTTP comme :

* le navigateur web (pour les requêtes `GET` simples).
* `curl` (en ligne de commande).
* Postman.

### Endpoints

Voici les endpoints principaux que nous avons implémentés :

**Service d'inscription (http://127.0.0.1:5000)**

* `POST /inscriptions`: Enregistre un nouveau candidat. Le corps de la requête doit être au format JSON avec les informations du candidat (nom, prenom, email, date\_naissance, telephone).

    **Exemple avec `curl` pour créer une inscription :**

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"nom": "Ilunga", "prenom": "John", "email": "john.Ilunga@gmail.com", "date_naissance": "2000-01-15", "telephone": "0975008388"}' [http://127.0.0.1:5000/inscriptions](http://127.0.0.1:5000/inscriptions)
    ```

    **Exemple avec Postman pour créer une inscription :**
    * Sélectionnez la méthode `POST`.
    * Entrez l'URL `http://127.0.0.1:5000/inscriptions`.
    * Dans l'onglet "Body", choisissez "raw" et le format "JSON".
    * Collez le corps de la requête JSON ci-dessus.
    * Cliquez sur "Send".

* `GET /inscriptions/{id}`: Récupère les informations d'un candidat spécifique en utilisant son ID. Remplacez `{id}` par l'identifiant du candidat.

    **Exemple avec `curl` pour récupérer l'inscription avec l'ID 1 :**

    ```bash
    curl [http://127.0.0.1:5000/inscriptions/1](http://127.0.0.1:5000/inscriptions/1)
    ```

    **Exemple avec Postman pour récupérer l'inscription avec l'ID 1 :**
    * Sélectionnez la méthode `GET`.
    * Entrez l'URL `http://127.0.0.1:5000/inscriptions/1`.
    * Cliquez sur "Send".

**Service de gestion des cotes (http://127.0.0.1:5001)**

* `POST /cotes`: Enregistre la cote d'un candidat. Le corps de la requête doit être au format JSON avec l'ID du candidat (`candidat_id`), la cote (`cote`), la date du test (`date_test`) et un commentaire (facultatif).

    **Exemple avec `curl` pour enregistrer une cote pour le candidat avec l'ID 2 :**

    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"candidat_id": 2, "cote": 15.5, "date_test": "2025-05-10", "commentaire": "Bonne performance"}' [http://127.0.0.1:5001/cotes](http://127.0.0.1:5001/cotes)
    ```

    **Exemple avec Postman pour enregistrer une cote pour le candidat avec l'ID 2 :**
    * Sélectionnez la méthode `POST`.
    * Entrez l'URL `http://127.0.0.1:5001/cotes`.
    * Dans l'onglet "Body", choisissez "raw" et le format "JSON".
    * Collez le corps de la requête JSON ci-dessus (en ajustant `candidat_id`, `cote`, etc.).
    * Cliquez sur "Send".

* `GET /cotes/{candidat_id}`: Récupère la cote d'un candidat spécifique en utilisant son `candidat_id`.

    **Exemple avec `curl` pour récupérer la cote du candidat avec l'ID 2 :**

    ```bash
    curl [http://127.0.0.1:5001/cotes/2](http://127.0.0.1:5001/cotes/2)
    ```

    **Exemple avec Postman pour récupérer la cote du candidat avec l'ID 2 :**
    * Sélectionnez la méthode `GET`.
    * Entrez l'URL `http://127.0.0.1:5001/cotes/2`.
    * Cliquez sur "Send".

## Arrêter les serveurs

Pour arrêter les serveurs Flask, retournez dans les terminaux où ils sont en 
cours d'exécution et appuyez sur `Ctrl + C`.

