#!/bin/bash

echo Hello!

# INSERT INTO info

docker exec -it replication mysql -uroot -proot -e "USE k8s_temp_env; INSERT INTO info VALUES (NULL,'test','10-01-2021','20-01-2021','active', 'user-test, user-test');"

# SELECT from info

docker exec -it replication mysql -uroot -proot -e "USE k8s_temp_env; SELECT id  FROM info ORDER BY id DESC LIMIT 1;"

# kafka-console-consumer

#docker exec -it kafka kafka-console-consumer --topic DB_k8s_temp_env_info --from-beginning --bootstrap-server kafka:9092 --timeout-ms 4000

#docker exec -it kafka kafka-console-consumer --topic DB_k8s_temp_env_info --from-beginning --bootstrap-server kafka:9092 --timeout-ms 6000 | head -n 1 | jq .data.id

x=$(docker exec -it kafka kafka-console-consumer --topic DB_k8s_temp_env_info --from-beginning --bootstrap-server kafka:9092 --timeout-ms 6000 | head -n 1 | jq .data.id)
echo Privet $x

#docker exec -it kafka kafka-console-consumer --topic DB_k8s_temp_env_info --from-beginning --bootstrap-server kafka:9092 --timeout-ms 6000 | tail -n 5 | jq .data.id
