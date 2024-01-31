#!/usr/bin/env bash
#I just replaced the conf with the defult one
sudo sed -i "s/sites-enabled/sites-available/" /etc/nginx/nginx.conf
sudo service nginx restart
