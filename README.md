# NPI
Documentation
Pour lancer le projet, vous devez le déployer via les commandes Docker Compose :


docker-compose build
docker-compose up -d
Une fois que les services Python et MySQL sont lancés, rendez-vous dans le conteneur Python :

Vous devez avoir un fichier .env à la racine du projet, comme dans .exemple.env.
docker-compose exec <service_name> /bin/bash
Puis, lancez la commande suivante :

python3 /app/classs/database/migrations/001.py
pour exécuter les migrations de la base de données.


Une fois la migration achevée, et le .env créer. Vous pouvez vous rendre à l'adresse :

http://localhost:8000/{calcul}

Le calcul doit être comme dans cet exemple : "3,55,9,:,sin,*". Les éléments sont séparés par des , sans espace. Pour la division, utilisez les : Ne pas utiliser le /, sinon il sera considéré comme une route.

http://localhost:8000/download

Pour télécharger un CSV contenant la totalité des opérations effectuées.