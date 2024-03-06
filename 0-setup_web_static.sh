#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

if ! service nginx status &> /dev/null; then
    apt-get update
    apt-get -y install nginx
    service nginx start
fi

if [ ! -d "/data/" ]; then
    mkdir "/data/"
fi

if [ ! -d "/data/web_static/" ]; then
    mkdir "/data/web_static/"
fi

if [ ! -d "/data/web_static/releases/" ]; then
    mkdir "/data/web_static/releases/"
fi

if [ ! -d "/data/web_static/shared/" ]; then
    mkdir "/data/web_static/shared/"
fi

if [ ! -d "/data/web_static/releases/test/" ]; then
    mkdir "/data/web_static/releases/test/"
fi

if [ ! -e "/data/web_static/releases/test/index.html" ]; then
    echo "Hello World!" > "/data/web_static/releases/test/index.html"
fi

ln -sf "/data/web_static/releases/test/" "/data/web_static/current"

chown -HR ubuntu:ubuntu "/data/"

sed -i 's,server_name _;,server_name _;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n,g' /etc/nginx/sites-enabled/default

nginx -s reload
