# Web Server Setup

## Serve your application

### Using PHP’s Built-in Web Server (Development or Demos Only)
For **development or demonstration purposes**, you can utilize PHP's built-in web server. Please note that this server is primarily intended for application development and testing in controlled environments. It's not suitable as a full-featured web server for production use.

To start the server, run the following command in your terminal:

```shell
php -S 0.0.0.0:8000 ./public/index.php
```

This command will serve your application on http://localhost:8000, 
allowing you to access the Phalcon Kit Frontend module directly from your browser. Keep in mind:

- The PHP built-in server handles only one request at a time, operating in a single-threaded mode. This means that if one request is blocked, other requests will have to wait.
- For comprehensive details and best practices about using PHP's built-in web server, please consult the [Official PHP documentation](https://www.php.net/manual/en/features.commandline.webserver.php){:target="_blank"}.

Remember, for production environments, it's recommended to use a more robust web server like Apache or Nginx,
which are designed to handle multiple simultaneous requests and offer a wider range of features for web application deployment.

### Using a Full-Featured Web Server (Development or Production)

To make your application accessible on the public internet, it's essential to deploy it using a robust,
production-ready web server. Options such as Apache or Nginx are excellent choices for this purpose,
offering enhanced functionality and the ability to handle multiple simultaneous requests efficiently.

For detailed guidance on setting up a Phalcon application with these web servers,
please refer to the [Phalcon Webserver Documentation](https://docs.phalcon.io/latest/webserver-setup/){:target="_blank"}.
This resource provides comprehensive instructions and best practices for various server configurations.

#### Option 1: Configuring Apache
Here's a basic configuration example for setting up your Phalcon Kit application with Apache 2.4 and PHP-FPM 8.2:

- Your Apache virtual host needs to be configured to point to the /public/ directory of your Phalcon Kit project.
- Customize the `ServerName`, `ServerAlias`, `DocumentRoot` and other directives to align with your needs.

```apacheconf
<VirtualHost *:80>
    ServerName domain.tld
    ServerAlias www.domain.tld
    DocumentRoot /path/to/app/public
    
    <Directory /path/to/app/public>
        Options -Indexes +FollowSymLinks +MultiViews
        AllowOverride All
        Require all granted
    </Directory>
    
    <FilesMatch \.(php|phar)$>
        SetHandler "proxy:unix:/var/opt/remi/php84/run/php-fpm/www.sock|fcgi://localhost"
    </FilesMatch>
</VirtualHost>

<VirtualHost *:443>
    ServerName domain.tld
    ServerAlias www.domain.tld
    DocumentRoot /path/to/app/public
    
    <Directory /path/to/app/public>
        Options -Indexes +FollowSymLinks +MultiViews
        AllowOverride All
        Require all granted
    </Directory>
    
    <FilesMatch \.(php|phar)$>
        SetHandler "proxy:unix:/var/opt/remi/php84/run/php-fpm/www.sock|fcgi://localhost"
    </FilesMatch>
    
    SetEnv HTTPS on
    SetEnv HTTP_X_FORWARDED_PROTO https
</VirtualHost>
```

Remember to replace domain.tld and /path/to/app/public with your actual domain and project directory path.
If you're using PHP-FPM, you may need additional configuration specific to your setup.

##### Url Rewriting

To ensure that your Phalcon Kit application routes requests correctly, it's essential to set up URL rewriting 
rules in Apache. This involves creating .htaccess files in both the root directory of your application
and the public subdirectory.

**Root Directory .htaccess**

In the root directory of your Phalcon Kit application, create an .htaccess file with the following content. 
This configuration redirects all traffic to the public folder, maintaining a clean URL structure and 
enhancing security by hiding the internal directory structure.

```apacheconf title="/path/to/app/.htaccess"
<IfModule mod_rewrite.c>
    RewriteEngine on
    RewriteRule   ^$ public/    [L]
    RewriteRule   ((?s).*) public/$1 [L]
</IfModule>
```

This file should be placed at the root of your Phalcon Kit application (/path/to/app/.htaccess).

**Public Directory .htaccess**

In the public directory, where your frontend files reside, you'll need another .htaccess file. 
This file rewrites URLs to route requests through the index.php entry script, enabling friendly 
URLs and routing functionality provided by Phalcon Kit and Phalcon.

```apacheconf title="/path/to/app/public/.htaccess"
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond   %{REQUEST_FILENAME} !-d
    RewriteCond   %{REQUEST_FILENAME} !-f
    RewriteRule   ^((?s).*)$ index.php?_url=/$1 [QSA,L]
</IfModule>
```

Place this file inside the public directory (/path/to/app/public/.htaccess). It ensures that non-existing 
file or directory requests are correctly passed to index.php, allowing Phalcon Kit to handle the routing.

!!! note "Important Notes"
    - Ensure that the `mod_rewrite` module is enabled in your Apache configuration. This module is required for URL rewriting to work.
    - The use of `.htaccess` files requires that the `AllowOverride` directive in your main Apache configuration is set to `All` for the directory where your Phalcon Kit application resides.

These rewriting rules are crucial for the correct functioning of your application, especially
if you are using SEO-friendly URLs or routing beyond the basic setup.

By configuring these `.htaccess` files correctly, you enhance both the functionality and security
of your Phalcon Kit application when hosted on an Apache server.

This example offers a starting point. Depending on your server environment and specific requirements,
additional configuration might be necessary.

#### Option 2: Configuring Nginx

Below is a basic Nginx configuration example for hosting a Phalcon Kit project. This configuration assumes 
you are using PHP-FPM to process PHP files. Modify the server_name and root directives to suit your
domain and project directory.

```nginx
server {
    listen      80;
    server_name   default;

    ssl on;
    ssl_session_timeout  5m;
    ssl_protocols  SSLv2 SSLv3 TLSv1;
    ssl_ciphers  ALL:!ADH:!EXPORT56:RC4+RSA:+HIGH:+MEDIUM:+LOW:+SSLv2:+EXP;
    ssl_prefer_server_ciphers   on;

    ssl_certificate        /var/nginx/certs/default.cert;
    ssl_certificate_key    /var/nginx/certs/default.key;

    root /path/to/app/public;
    index index.php index.html index.htm;

    charset utf-8;
    client_max_body_size 100M;
    fastcgi_read_timeout 1800;

    location / {
        # Matches URLS `$_GET['_url']`
        try_files $uri $uri/ /index.php?_url=$uri&$args;
    }

    location ~ [^/]\.php(/|$) {
        # try_files $uri =404;

        fastcgi_pass  unix:/var/run/php/php8.4-fpm.sock;
        fastcgi_index /index.php;
        include fastcgi_params;
        fastcgi_split_path_info ^(.+?\.php)(/.*)$;
        
        if (!-f $document_root$fastcgi_script_name) {
            return 404;
        }

        fastcgi_param PATH_INFO       $fastcgi_path_info;
        fastcgi_param PATH_TRANSLATED $document_root$fastcgi_path_info;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
    }

    location ~ /\.ht {
        deny all;
    }

    location ~* \.(js|css|png|jpg|jpeg|gif|ico)$ {
        expires       max;
        log_not_found off;
        access_log    off;
    }
}
```

Make sure to replace `domain.tld` with your actual domain and `/path/to/app/public` with the correct path 
to your Phalcon Kit project's public directory. The `fastcgi_pass` directive should be adjusted according to your PHP-FPM setup.

This example provides a basic starting point for Nginx configuration. Depending on your server environment,
additional tweaks or settings might be necessary for optimal performance and security. Always consult the
[official Nginx documentation](https://docs.nginx.com/nginx/admin-guide/web-server/){:target="_blank"} 
for more detailed setup instructions and best practices.
