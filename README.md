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
docker exec -it bdd_redis_1 redis-cli
```

Vous pouvez maintenant utiliser les commandes Redis.

### MongoDB

Pour accéder à MongoDB depuis votre terminal, utilisez la commande suivante :

```bash
docker exec -it bdd_mongo_1 mongosh
```

Vous pouvez maintenant utiliser les commandes MongoDB.
