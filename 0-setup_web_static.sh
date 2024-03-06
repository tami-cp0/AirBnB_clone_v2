#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

if ! service nginx status &> /dev/null; then
    apt-get update
    apt-get -y install nginx
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
    touch "/data/web_static/releases/test/index.html"
fi

if [ -L "/data/web_static/current" ]; then
    rm -f "/data/web_static/current" && ln -s "/data/web_static/releases/test/" "/data/web_static/current"
fi

chown -R ubuntu:ubuntu "/data/"

sed -i 's,server {,server {\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n,g' /etc/nginx/sites-enabled/default

service nginx restart
