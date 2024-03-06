#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

if ! service nginx status &> /dev/null; then
    apt-get update
    apt-get -y install nginx
    service nginx start
fi

if [ ! -d "/data/web_static/shared/" ]; then
    mkdir -p "/data/web_static/shared/"
fi

if [ ! -d "/data/web_static/releases/test/" ]; then
    mkdir -p "/data/web_static/releases/test/"
fi

echo "Hello World!" > "/data/web_static/releases/test/index.html"

ln -sf "/data/web_static/releases/test/" "/data/web_static/current"

chown -hR ubuntu:ubuntu "/data/"

sed -i 's,server_name _;,server_name _;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t\tindex index.html;\n\t}\n,g' /etc/nginx/sites-enabled/default

service nginx restart
