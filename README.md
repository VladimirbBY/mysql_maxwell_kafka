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

### Textfile Collector

The textfile collector is similar to the Pushgateway, in that it allows exporting of statistics from batch jobs. It can also be used to export static metrics, such as what role a machine has. The Pushgateway should be used for service-level metrics. The textfile module is for metrics that are tied to a machine.

To use it, set the --collector.textfile.directory flag on the node_exporter commandline. The collector will parse all files in that directory matching the glob *.prom using the text format. Note: Timestamps are not supported.

To atomically push completion time for a cron job:

echo my_batch_job_completion_time $(date +%s) > /path/to/directory/my_batch_job.prom.$$
mv /path/to/directory/my_batch_job.prom.$$ /path/to/directory/logs.prom

To statically set roles for a machine using labels:

echo 'role{role="application_server"} 1' > /path/to/directory/role.prom.$$
mv /path/to/directory/role.prom.$$ /path/to/directory/role.prom



##  Step 4 Run script

./sсript.sh 
