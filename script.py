from flask import Response, Flask, render_template
import os
import subprocess

print("Hello")
app = Flask(__name__)

@app.route("/metrics", methods=["GET"])
def metrics():
    try:
        os.system('docker exec -it replication mysql -uroot -proot -e "USE  test_temp_env; INSERT INTO info VALUES (NULL,"test");"')
        output_mysql = subprocess.check_output("docker exec -it replication mysql -uroot -proot -e  'USE  test_temp_env; SELECT json_object('id', id)  FROM info ORDER BY id DESC LIMIT 1;' | awk -F'[^0-9]*' '$0=$2'", shell=True)
        output_kafka = subprocess.check_output('bash -c "docker run --network mysql_maxwell_kafka_default confluentinc/cp-kafkacat kafkacat -b kafka:9092  -t DB_test_temp_env_info  -o -1 -C -q  -p 0 -e" | jq --raw-output .data.id', shell=True)
        print(output_mysql, "*"*50)
        print(output_kafka, "*"*50)
        if str(output_mysql.decode()) == str(output_kafka.decode()):
            message = 'connection 1'
        elif output_mysql != output_kafka:
            message = 'connection 0'
        return Response(message, mimetype="text/plain")
    except(NameError):
        message = 'connection 2'
        return Response(message, mimetype="text/plain", status=200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7128, debug=False)

   