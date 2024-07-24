sudo apt update -y
sudo apt install --no-install-recommends php8.3 -y
php -v

sudo apt-get install -y php8.3-cli php8.3-common php8.3-mysql php8.3-zip php8.3-gd php8.3-mbstring php8>php -m

curl -sS https://getcomposer.org/installer -o /tmp/composer-setup.php
HASH=`curl -sS https://composer.github.io/installer.sig`
echo $HASH

php -r "if (hash_file('SHA384', '/tmp/composer-setup.php') === '$HASH') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"

sudo apt install apache2 -y
# sudo ufw app list
# sudo ufw allow 'Apache'
# # sudo ufw allow 22

# # sudo ufw enable
# # sudo ufw status
sudo apt install libapache2-mod-php8.3 -y
sudo apt-get install php-sqlite3 -y

sudo a2enmod php8.3
sudo apt install npm -y

sudo systemctl start apache2

#sudo systemctl status apache2

sudo apt install -y composer 
sudo apt-get install php-xml -y
# sudo apt-get install ext-dom
# sudo apt install composer -y
# sudo mkdir /var/www/test/autotes
