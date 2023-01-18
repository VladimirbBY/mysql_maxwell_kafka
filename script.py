from flask import Response, Flask
from datetime import datetime, timedelta
import os

print("Hello")
app = Flask(__name__)

@app.route("/metrics", methods=["GET"])
def metrics():
    try:
        os.system("Echo Hello")
        os.system('docker exec -it replication mysql -uroot -proot -e "USE  test_temp_env; INSERT INTO info VALUES (NULL,"test");"')
        output_mysql = os.system("docker exec -it replication mysql -uroot -proot -e  'USE  test_temp_env; SELECT json_object('id', id)  FROM info ORDER BY id DESC LIMIT 1;' | awk -F'[^0-9]*' '$0=$2'")
        print(output_mysql)
        output_kafka = os.system('bash -c "docker run --network mysql_maxwell_kafka_default confluentinc/cp-kafkacat kafkacat -b kafka:9092  -t DB_test_temp_env_info  -o -1 -C -q  -p 0 -e" | jq --raw-output .data.id')
        print(output_kafka)

        if output_mysql == output_kafka:
            message = 'connection{Yes="working"} 0'
        elif output_mysql != output_kafka:
            message = 'connection{No="working"} 1'
        return Response(message, mimetype="text/plain")
    except(NameError):
        message = 'connection{Error="working"} 2'
        return Response(message, mimetype="text/plain", status=200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7128, debug=False)

   