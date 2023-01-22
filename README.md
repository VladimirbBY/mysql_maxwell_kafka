# mysql+maxwell+kafka test

## Step 1 clone files:

config.properties   
docker-compose.yaml   
master.cnf   
script.sh   

## Step 2 create Env

docker-compose up -d  

docker exec -it kafka kafka-topics --create --bootstrap-server kafka:9092 --replication-factor 1 --partitions 1 --topic topic_test

docker exec -it replication mysql -uroot -proot -e "CREATE DATABASE IF NOT EXISTS test_temp_env; USE test_temp_env; CREATE TABLE IF NOT EXISTS info(id INT PRIMARY KEY AUTO_INCREMENT, test VARCHAR(50) NOT NULL DEFAULT '');"

restart docker-compose up -d  

## Step 3 monitoring

Use Prometeus сonfiguration example:   

prometheus.yml


##  Step 4 Run script

./sсript.py 

## TO DO
