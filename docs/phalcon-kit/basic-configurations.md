# Basic Configuration

The Configuration component in Zemit Core is a flexible and powerful tool for managing and accessing your application's configuration settings. It provides a default class with predefined values that can be customized to fit your needs, and also allows you to load environment variables from a .env file. The Configuration component is decoupled into multiple sections, making it easy to organize and manage your settings. With the Configuration component, you can easily control and adjust your application's configuration within the Zemit Core framework.

!!! info "Good to know"
    `\Zemit\Support\Env` is using _vlucas Dotenv_ library behind the scene to load and prepare environment variables from the .env file, please refer yourself to the official [Dotenv documentation](https://github.com/vlucas/phpdotenv){:target="_blank"}.

## Basic `.env` example

```ini title=".env"
# Enable Debug
APP_DEBUG=true

# Enable Profiler
APP_PROFILER=true

# Enable Send Email
APP_SEND_EMAIL=true

# Use SMTP
MAILER_DRIVER=smtp
MAILER_SMTP_HOST=smtp.server.tld
MAILER_SMTP_PORT=465
MAILER_SMTP_ENCRYPTION=tls
MAILER_SMTP_USERNAME=username
MAILER_SMTP_PASSWORD="smtp_password"
MAILER_FROM_EMAIL=email@server.tld
MAILER_FROM_NAME="App Name"

# Enable APCU Cache
APP_CACHE=true
METADATA_DRIVER=apcu
CACHE_DRIVER=apcu

# Set Global Security Salt
SECURITY_SALT="my_app_salt"

# Set Master Database Configuration
DATABASE_HOST=localhost
DATABASE_DBNAME=database_name
DATABASE_USERNAME=database_username
DATABASE_PASSWORD="database_password"

# Add a new Slave Database
DATABASE_READONLY_ENABLE=true
DATABASE_READONLY_HOST=slave.db.server.tld

# Set Custom Authorization Header
IDENTITY_AUTHORIZATION_HEADER=X-Authorization

# Set Localisation
LOCALE_DEFAULT=fr
LOCALE_ALLOWED=fr,en,es
LOCALE_MODE=session_geoip
LOCALE_SESSION_KEY=my_app_local
TRANSLATE_LOCALE=fr_CA.utf8
TRANSLATE_DEFAULT_PATH=./app/Locales/

# Set Redis Server
REDIS_HOST=redis.server.tld
REDIS_PORT=6379
```

## Basic `Config` example

Because we are using `\Phalcon\Config\Config` which extends the Collection class, you can refer yourself to the official [Phalcon Configuration documentation](https://docs.phalcon.io/latest/config) as well as the [Phalcon Collection documentation](https://docs.phalcon.io/latest/support-collection) for more information.

Create a new `Config` class that should look similar to this below:

### Simple example using `Config`

```php
<?php
use \Zemit\Bootstrap\Config;

$config = Config([
    'app' => [
        'version' => '1.0.0',
        'debug' => true,
    ],
]);

return $config;
```

### Simple example mixing `.env` and `Config`

```php
<?php
use \Zemit\Bootstrap\Config;
use \Zemit\Support\Env;

$config = Config([
    'app' => [
        // forcing a value
        'version' => '1.0.0',
        
        // .env value will be used and fallback to false
        'debug' => Env::get('APP_DEBUG', false),
    ],
]);

return $config;
```



## Advanced `Config` example

```php
<?php
namespace App\Config;

use Zemit\Utils\Env;

class Config extends Zemit\Bootstrap\Config
{
    public function __construct(array $data = [], bool $insensitive = true)
    {
        parent::__construct([
            'app' => [
                // override whatever variable you want
                'version' => Env::get('APP_VERSION', '0.0.1')
                
                // add custom configs wherever you want
                'customKey' => Env::get('APP_CUSTOM_KEY', 'default-value')
                // ...
            ],
            
            // creating a new custom config
            'custom' => [
                'key' => Env::get('CUSTOM_KEY', 'default-value')
                // ...
            ],
        ], $insensitive);
        
        if (!empty($data)) {
            $this->merge(new PhalconConfig($data, $insensitive));
        }
    }
}
```
