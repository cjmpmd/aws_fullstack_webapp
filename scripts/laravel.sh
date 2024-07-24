#!/bin/bash

APP_NAME="myapp"  # Your Laravel application's name
APP_DIR="/var/www/myapp"
PHP_VERSION="8.3" # Adjust to your PHP version (e.g., 8.0)

# Check if directory exists and create
if [ -d "" ]; then
    echo "Directory '' already exists. Please choose a different name or location."
    exit 1
fi

# Create directory and navigate
#  mkdir /var/www/myapp
# cd /var/www/myapp



# Install Laravel (replace "laravel/laravel" if you have a custom repo)
 composer create-project laravel/laravel /var/www/myapp 9.5 --prefer-dist

# Set permissions (replace `www-data` if your Apache user is different)

cd /var/www/myapp
chown -R www-data:www-data bootstrap/cache
chown -R www-data:www-data storage
chmod -R 775 storage
chmod -R 775 bootstrap/cache

#  chown -R www-data:www-data /var/www/myapp
#  chmod -R 755 /var/www/myapp/storage /var/www/myapp/bootstrap/cache

# Generate application key (essential for security)
 php artisan key:generate

# Run database migrations (optional, if you have a database set up)
# php artisan migrate

# Install Laravel Breeze (authentication scaffolding, optional)
    

#  php artisan ui bootstrap
#  php artisan ui bootstrap --auth
 
# php artisan ui bootstrap
# php artisan ui vue
# php artisan ui react

# php artisan ui bootstrap --auth
# php artisan ui vue --auth
# php artisan ui react --auth

# npm install
# npm run dev
# npm build


# Install additional packages (tailwindcss)
# npm install
# npm run build

# Display success message
echo "Laravel 9 application '$APP_NAME' created successfully in '$APP_DIR'."



NEW_CONFIG_FILE="my_new_config.conf"  # Name of your new configuration file
OLD_CONFIG_FILE="000-default.conf"    # Name of the configuration file to disable (adjust if needed)
CONFIG_DIR="/etc/apache2/sites-available" # Directory where configuration files are stored

# 1. Create the new configuration file
sudo bash -c "cat > $CONFIG_DIR/$NEW_CONFIG_FILE <<EOF
# Your Apache configuration content here
<VirtualHost *:80>
        #ServerName www.example.com

        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/myapp/public

           <Directory /var/www/myapp/public>
                Options Indexes FollowSymLinks
                AllowOverride All
                Require all granted
            </Directory>


        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

</VirtualHost>
EOF"

# 2. Disable the old configuration file
sudo a2dissite "$OLD_CONFIG_FILE"

# 3. Enable the new configuration file
sudo a2ensite "$NEW_CONFIG_FILE"

# 4. Test the configuration (optional)
apache2ctl configtest

 a2dismod mpm_event 
 a2dismod mpm_worker
 a2enmod php8.3

 systemctl restart apache2

 rm /var/www/myapp/resources/views/welcome.blade.php

sudo bash -c "cat > /var/www/myapp/resources/views/welcome.blade.php <<EOF
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Hallo</title>
</head>
<body>
    <h6>Working on it!</h6>
    
</body>
</html>
EOF"


# cd /var/www/myapp
# php artisan migrate
# php artisan optimize:clear

#  rm myscript.sh  # Make it executable


