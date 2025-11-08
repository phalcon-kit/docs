# Advanced Configurations

## Advanced `.env` examples

### Database Settings (Master & Slave)

Zemit currently only support MySQL/MariaDB database driver. There is no plan on adapting new databases adapters in the future. Since Phalcon does support many database adapters, nothing stops you from defining your own from your own configuration file.

!!! info "Good to know"
    The Slave Database is only used as a read-only server and will automatically extend the master settings if they are not explicitly defined.

=== "Master Settings"

    ```ini title="Master Database Settings"
    DATABASE_ADAPTER=mysql

    DATABASE_HOST=localhost
    DATABASE_PORT=3306
    DATABASE_DBNAME=database_name
    DATABASE_USERNAME=database_username
    DATABASE_PASSWORD="database_password"
    DATABASE_CHARSET=utf8

    DATABASE_PDO_EMULATE_PREPARES=false
    DATABASE_PDO_STRINGIFY_FETCHES=false

    MYSQL_ATTR_SSL_VERIFY_SERVER_CERT=true
    ```

=== "Slave Settings (Optional)"

    ```ini title="Slave Database Settings"
    DATABASE_READONLY_ENABLE=true

    DATABASE_READONLY_HOST=slave.db.server.tld
    DATABASE_READONLY_PORT=3306
    DATABASE_READONLY_DBNAME=database_name
    DATABASE_READONLY_USERNAME=database_username
    DATABASE_READONLY_PASSWORD="database_password"
    DATABASE_READONLY_CHARSET=utf8
    ```

### Redis Settings

You can use the `redis` Driver for some components such as `session`, `annotation`, `metadata` and `cache`. By default, it will automatically retrieve the default _Redis_ settings which is prefixed with `REDIS_`.

```ini title=".env"
# Using Redis Server for session
SESSION_DRIVER=redis

# Using Redis Server for annotations
ANNOTATIONS_DRIVER=redis

# Using Redis Server for meta-data
METADATA_DRIVER=redis

# Using Redis Server for cache
CACHE_DRIVER=redis

# Default Redis Settings
REDIS_HOST=127.0.0.1
REDIS_PORT=6379
```

It is also possible to overwrite the default redis configuration for each components if you would like to use distinct redis server per component.
If no configuration is defined, the default redis configuration will be used as fallback.

=== "Default Redis"

    ```ini title="Default Redis Settings"
    REDIS_DEFAULT_SERIALIZER=1
    REDIS_LIFETIME=3600
    REDIS_SERIALIZER=
    REDIS_HOST=127.0.0.1
    REDIS_PORT=6379
    REDIS_INDEX=1
    REDIS_AUTH=
    REDIS_PERSISTENT=0
    REDIS_SOCKET=
    ```

=== "Session"

    ```ini title="Session Redis Settings"
    SESSION_DRIVER=redis

    SESSION_REDIS_DEFAULT_SERIALIZER=1
    SESSION_REDIS_LIFETIME=3600
    SESSION_REDIS_SERIALIZER=
    SESSION_REDIS_HOST=127.0.0.1
    SESSION_REDIS_PORT=6379
    SESSION_REDIS_INDEX=1
    SESSION_REDIS_AUTH=
    SESSION_REDIS_PERSISTENT=0
    SESSION_REDIS_SOCKET=
    ```

=== "Cache"

    ```ini title="Cache Redis Settings"
    CACHE_DRIVER=redis

    CACHE_REDIS_DEFAULT_SERIALIZER=1
    CACHE_REDIS_LIFETIME=3600
    CACHE_REDIS_SERIALIZER=
    CACHE_REDIS_HOST=127.0.0.1
    CACHE_REDIS_PORT=6379
    CACHE_REDIS_INDEX=1
    CACHE_REDIS_AUTH=
    CACHE_REDIS_PERSISTENT=0
    CACHE_REDIS_SOCKET=    
    ```

=== "Metadata"

    ```ini title="Metadata Redis Settings"
    METADATA_DRIVER=redis

    METADATA_REDIS_DEFAULT_SERIALIZER=1
    METADATA_REDIS_LIFETIME=3600
    METADATA_REDIS_SERIALIZER=
    METADATA_REDIS_HOST=127.0.0.1
    METADATA_REDIS_PORT=6379
    METADATA_REDIS_INDEX=1
    METADATA_REDIS_AUTH=
    METADATA_REDIS_PERSISTENT=0
    METADATA_REDIS_SOCKET=
    ```

=== "Annotation"

    ```ini title="Annotation Redis Settings"
    ANNOTATION_DRIVER=redis

    ANNOTATION_REDIS_DEFAULT_SERIALIZER=1
    ANNOTATION_REDIS_LIFETIME=3600
    ANNOTATION_REDIS_SERIALIZER=
    ANNOTATION_REDIS_HOST=127.0.0.1
    ANNOTATION_REDIS_PORT=6379
    ANNOTATION_REDIS_INDEX=1
    ANNOTATION_REDIS_AUTH=
    ANNOTATION_REDIS_PERSISTENT=0
    ANNOTATION_REDIS_SOCKET=
    ```
