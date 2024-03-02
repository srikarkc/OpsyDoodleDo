#!/usr/bin/env bash

# Update package list
sudo apt-get update

# Install Apache2
sudo apt-get install -y apache2

# Remove the default index.html
sudo rm /var/www/html/index.html

# Create a new index.html file
echo 'Hello, World!' | sudo tee /var/www/html/index.html
