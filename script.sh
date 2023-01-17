#!/bin/bash

time_delay=3

# INSERT INTO info

docker exec -it replication mysql -uroot -proot -e "USE  test_temp_env; INSERT INTO info VALUES (NULL,'test');"

# output from mysql

output_mysql=$(docker exec -it replication mysql -uroot -proot -e  "USE  test_temp_env; SELECT json_object('id', id)  FROM info ORDER BY id DESC LIMIT 1;" | awk -F'[^0-9]*' '$0=$2')

echo Ping $output_mysql #TO DO delete


# output from kafka

sleep $time_delay 

output_kafka=$(bash -c "docker run --network mysql_maxwell_kafka_default confluentinc/cp-kafkacat kafkacat -b kafka:9092  -t DB_test_temp_env_info  -o -1 -C -q  -p 0 -e" | jq --raw-output .data.id)

echo Pong $output_kafka #TO DO delete


if [ "$output_mysql" -eq "$output_kafka" ]
then
  echo 1 >> logs.prom
else
  echo 0 >> logs.prom
fi
