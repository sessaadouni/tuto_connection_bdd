# tuto_connection_bdd

## Prérequis

- Docker
- Docker-compose
- Python 3.8+

## Installation

```bash
git clone https://github.com/betagouv/tuto_connection_bdd.git
cd tuto_connection_bdd
cp .env.example .env
```

Modifiez le fichier `.env` pour configurer les variables d'environnement.

Créer le dossier `.docker` et placez le fichier de configuration de redis dans ce dossier.

```bash
mkdir .docker
cp .docker-data/redis.conf .docker/redis.conf
```

## Lancement

Lancez les services docker avec la commande suivante :

```bash
docker-compose up -d
```

Vérifiez que les services sont bien lancés avec la commande suivante :

```bash
docker-compose ps
```

Vous devriez voir les services suivants :

```txt
Name                 Command               State           Ports
--------------------------------------------------------------------------------
bdd_redis_1   docker-entrypoint.sh redis   Up      0.0.0.0:6379->6379/tcp
bdd_mongo_1   docker-entrypoint.sh mongod   Up      0.0.0.0:27017->27017/tcp
```

## Utilisation

### Redis

Pour accéder à Redis depuis votre terminal, utilisez la commande suivante :

```bash
docker exec -it bdd-redis-1 redis-cli
```

Vous pouvez maintenant utiliser les commandes Redis.

### MongoDB

Pour accéder à MongoDB depuis votre terminal, utilisez la commande suivante :

```bash
docker exec -it bdd-mongo-1 mongosh
```

Vous pouvez maintenant utiliser les commandes MongoDB.

## Test des Requetes

Pour tester les requêtes, vous pouvez utiliser les scripts suivants :

> Convertir les fichiers TXT en JSON

```bash
python3 to_json.py
```

> Diviser les données en deux parties

```bash
python3 divide_data.py
```

> Insérer les données JSON dans Redis et MongoDB

```bash
python3 redis/insert_to_redis.py
python3 mongo/insert_to_mongo.py
```

> Tester les requêtes avec Redis et MongoDB

```bash
python3 redis/request_redis.py
python3 mongo/request_mongo.py
```

> Jointure avec Redis et MongoDB

```bash
python3 redis/jointure_redis.py
python3 mongo/jointure_mongo.py
```
