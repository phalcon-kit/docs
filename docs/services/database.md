# Database Service

## Introduction

The components under the `\Phalcon\Db` namespace are the ones responsible for powering the `\Phalcon\Mvc\Model` class - the `Model` in `MVC` for the framework. It consists of an independent high-level abstraction layer for database systems completely written in C.

This component allows for a lower level database manipulation than using traditional models.

## Database Configurations (`.env`)

### Basic Database Configurations

```ini
DATABASE_HOST=localhost
DATABASE_DBNAME=database
DATABASE_USERNAME=username
DATABASE_PASSWORD=password
```

### Database Configurations
```ini
DATABASE_HOST=localhost
DATABASE_PORT=3306
DATABASE_DBNAME=database
DATABASE_USERNAME=username
DATABASE_PASSWORD=password
DATABASE_CHARSET=utf8
```

### Database Options
```ini
DATABASE_CHARSET=utf8
DATABASE_SQL_MODE=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION
DATABASE_EMULATE_PREPARES=false
DATABASE_STRINGIFY_FETCHES=false
DATABASE_SSL_VERIFY_SERVER_CERT=true
DATABASE_USE_BUFFERED_QUERY=true
```

### Database Adapter / Dialect
```ini
# Optional, you can set your own adapter and dialect classes
DATABASE_MYSQL_ADAPTER=\Zemit\Db\Adapter\Pdo\Mysql
DATABASE_MYSQL_DIALECT=\Zemit\Db\Dialect\Mysql
```

### Database Driver

=== "`mysql`"
    
    ```ini
    # Database Driver to "mysql"
    DATABASE_DRIVER=mysql
    ```

=== "`postgresql`"
    
    ```ini
    # Database Driver to "postgresql"
    # Not officially supported by Zemit
    DATABASE_DRIVER=postgresql
    ```

=== "`sqlite`"
    
    ```ini
    # Database Driver to "sqlite"
    # Not officially supported by Zemit
    DATABASE_DRIVER=sqlite
    ```

### Readonly Slave
```ini
DATABASE_READONLY_ENABLE=true
```

### Readonly Configurations
```ini
DATABASE_READONLY_HOST=localhost
DATABASE_READONLY_PORT=3306
DATABASE_READONLY_DBNAME=database
DATABASE_READONLY_USERNAME=username
DATABASE_READONLY_PASSWORD=username
DATABASE_READONLY_CHARSET=utf8
```

### Database Service Provider
```ini
PROVIDER_DATABASE=\Zemit\Provider\Database\ServiceProvider
PROVIDER_DATABASE_READ_ONLY=\Zemit\Provider\DatabaseReadOnly\ServiceProvider
```

### Database Configuration Object
```php
<?php
new Config([
    'providers' => [
        \Zemit\Provider\Database\ServiceProvider::class => Env::get('PROVIDER_DATABASE', \Zemit\Provider\Database\ServiceProvider::class),
        \Zemit\Provider\DatabaseReadOnly\ServiceProvider::class => Env::get('PROVIDER_DATABASE_READ_ONLY', \Zemit\Provider\DatabaseReadOnly\ServiceProvider::class),
    ],
    'database' => [
        'default' => Env::get('DATABASE_ADAPTER', 'mysql'),
        'drivers' => [
            'mysql' => [
                'adapter' => Env::get('DATABASE_MYSQL_ADAPTER', \Zemit\Db\Adapter\Pdo\Mysql::class),
                'dialectClass' => Env::get('DATABASE_MYSQL_DIALECT', \Zemit\Db\Dialect\Mysql::class),
                'host' => Env::get('DATABASE_HOST', 'localhost'),
                'port' => Env::get('DATABASE_PORT', 3306),
                'dbname' => Env::get('DATABASE_DBNAME', ''),
                'username' => Env::get('DATABASE_USERNAME', 'root'),
                'password' => Env::get('DATABASE_PASSWORD', ''),
                'charset' => Env::get('DATABASE_CHARSET', 'utf8'),
                'options' => [
                    PDO::MYSQL_ATTR_INIT_COMMAND => 'SET NAMES ' . Env::get('DATABASE_CHARSET', 'utf8') .
                    ', sql_mode = \'' . Env::get('DATABASE_SQL_MODE', 'STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION') . '\'',
                    PDO::ATTR_EMULATE_PREPARES => Env::get('DATABASE_EMULATE_PREPARES', false), // https://stackoverflow.com/questions/10113562/pdo-mysql-use-pdoattr-emulate-prepares-or-not
                    PDO::ATTR_STRINGIFY_FETCHES => Env::get('DATABASE_STRINGIFY_FETCHES', false),
                    PDO::MYSQL_ATTR_SSL_VERIFY_SERVER_CERT => Env::get('DATABASE_SSL_VERIFY_SERVER_CERT', true),
                    PDO::MYSQL_ATTR_USE_BUFFERED_QUERY => Env::get('DATABASE_USE_BUFFERED_QUERY', true),
                ],
                'readonly' => [
                    'enable' => Env::get('DATABASE_READONLY_ENABLE', false),
                    'host' => Env::get('DATABASE_READONLY_HOST', null),
                    'port' => Env::get('DATABASE_READONLY_PORT', null),
                    'dbname' => Env::get('DATABASE_READONLY_DBNAME', null),
                    'username' => Env::get('DATABASE_READONLY_USERNAME', null),
                    'password' => Env::get('DATABASE_READONLY_PASSWORD', null),
                    'charset' => Env::get('DATABASE_READONLY_CHARSET', null),
                ],
            ],
        ],
    ],
]);
```

## Database Service (`db`)

!!! info "Database Service Provider"
Database Service Provider (`db`): [`\Zemit\Provider\Database\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Database/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$db = $this->db;

// Retrieving the service from the DI
$db = $this->di->get('db');

// Retrieving the service from anywhere
$db = Di::getDefault()->get('db');
```
