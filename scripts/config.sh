
#!/bin/bash

NEW_CONFIG_FILE="my_new_config.conf"  # Name of your new configuration file
OLD_CONFIG_FILE="000-default.conf"    # Name of the configuration file to disable (adjust if needed)
CONFIG_DIR="/etc/apache2/sites-available" # Directory where configuration files are stored

# 1. Create the new configuration file
sudo bash -c "cat > $CONFIG_DIR/$NEW_CONFIG_FILE <<EOF
# Your Apache configuration content here
<VirtualHost *:80>
        # The ServerName directive sets the request scheme, hostname and port that
        # the server uses to identify itself. This is used when creating
        # redirection URLs. In the context of virtual hosts, the ServerName
        # specifies what hostname must appear in the request's Host: header to
        # match this virtual host. For the default virtual host (this file) this
        # value is not decisive as it is used as a last resort host regardless.
        # However, you must set it for any further virtual host explicitly.
        #ServerName www.example.com

        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/myapp/public

        # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
        # error, crit, alert, emerg.
        # It is also possible to configure the loglevel for particular
        # modules, e.g.
        #LogLevel info ssl:warn

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        # For most configuration files from conf-available/, which are
        # enabled or disabled at a global level, it is possible to
        # include a line for only one particular virtual host. For example the
        # following line enables the CGI configuration for this host only
        # after it has been globally disabled with "a2disconf".
        #Include conf-available/serve-cgi-bin.conf
</VirtualHost>
EOF"

# 2. Disable the old configuration file
sudo a2dissite "$OLD_CONFIG_FILE"

# 3. Enable the new configuration file
sudo a2ensite "$NEW_CONFIG_FILE"

# 4. Test the configuration (optional)
apache2ctl configtest