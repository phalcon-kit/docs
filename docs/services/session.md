# Session Service

## Session Configuration

### Global Session Configurations

```ini
SESSION_PREFIX=phalcon_kit_session_
SESSION_UNIQUE_ID=phalcon_kit_
SESSION_LIFETIME=3600
```

### Stream File Session

```ini
SESSION_DRIVER=stream
SESSION_STREAM_SAVE_PATH=/tmp
```

### Memcached Session

```ini
SESSION_DRIVER=memcached
SESSION_MEMCACHED_HOST=127.0.0.1
SESSION_MEMCACHED_PORT=11211
SESSION_MEMCACHED_WEIGHT=100
```

### Redis Session

```ini
SESSION_DRIVER=redis
SESSION_REDIS_DEFAULT_SERIALIZER=php
SESSION_REDIS_LIFETIME=3600
SESSION_REDIS_SERIALIZER=
SESSION_REDIS_HOST=127.0.0.1
SESSION_REDIS_PORT=6379
SESSION_REDIS_INDEX=1
SESSION_REDIS_AUTH=
SESSION_REDIS_PERSISTENT=0
SESSION_REDIS_SOCKET=
```

### Noop Session

```ini
SESSION_DRIVER=noop
```

### Session Adapters

=== "stream"

    ```ini
    SESSION_DRIVER=stream
    SESSION_STREAM_ADAPTER=\Phalcon\Session\Adapter\Stream
    ```

=== "memcached"

    ```ini
    SESSION_DRIVER=memcached
    SESSION_STREAM_ADAPTER=\Phalcon\Session\Adapter\Libmemcached
    ```

=== "redis"

    ```ini
    SESSION_DRIVER=redis
    SESSION_STREAM_ADAPTER=\Phalcon\Session\Adapter\Redis
    ```

=== "noop"

    ```ini
    SESSION_DRIVER=noop
    SESSION_STREAM_ADAPTER=\Phalcon\Session\Adapter\Noop
    ```

### Session PHP INI

```ini
SESSION_SAVE_PATH=
SESSION_NAME=PHPSESSID
SESSION_SAVE_HANDLER=files
SESSION_AUTO_START=0
SESSION_GC_PROBABILITY=1
SESSION_GC_DIVISOR=100
SESSION_GC_MAXLIFETIME=1440
SESSION_SERIALIZE_HANDLER=php
SESSION_COOKIE_LIFETIME=0
SESSION_COOKIE_PATH=/
SESSION_COOKIE_DOMAIN=
SESSION_COOKIE_SECURE=1
SESSION_COOKIE_HTTPONLY=1
SESSION_COOKIE_SAMESITE=
SESSION_USE_STRICT_MODE=0
SESSION_USE_COOKIES=1
SESSION_USE_ONLY_COOKIES=1
SESSION_REFERER_CHECK=
SESSION_CACHE_LIMITER=nocache
SESSION_CACHE_EXPIRE=180
SESSION_USE_TRANS_SID=0
SESSION_TRANS_SID_TAGS=a=href,area=href,frame=src,form=
SESSION_TRANS_SID_HOSTS=
SESSION_SID_LENGTH=32
SESSION_SID_BITS_PER_CHARACTER=4
SESSION_UPLOAD_PROGRESS_ENABLED=1
SESSION_UPLOAD_PROGRESS_CLEANUP=1
SESSION_UPLOAD_PROGRESS_PREFIX=phalcon_kit_upload_progress_
SESSION_UPLOAD_PROGRESS_NAME=PHP_SESSION_UPLOAD_PROGRESS
SESSION_UPLOAD_PROGRESS_FREQ=1%
SESSION_UPLOAD_PROGRESS_MIN_FREQ=1
SESSION_LAZY_WRITE=1
SESSION_HASH_FUNCTION=0
SESSION_HASH_BITS_PER_CHARACTER=4
SESSION_ENTROPY_FILE=
SESSION_ENTROPY_LENGTH=0
```

### Session Configuration Object

```php
<?php
new Config([
    'session' => [
        'driver' => Env::get('SESSION_DRIVER', 'stream'),
        'drivers' => [
            'stream' => [
                'adapter' => Env::get('SESSION_STREAM_ADAPTER', \Phalcon\Session\Adapter\Stream::class),
                'savePath' => Env::get('SESSION_STREAM_SAVE_PATH', '/tmp'),
            ],
            'memcached' => [
                'adapter' => Env::get('SESSION_MEMCACHED_ADAPTER', \Phalcon\Session\Adapter\Libmemcached::class),
                'servers' => [
                    [
                        'host' => Env::get('SESSION_MEMCACHED_HOST', Env::get('MEMCACHED_HOST', '127.0.0.1')),
                        'port' => Env::get('SESSION_MEMCACHED_PORT', Env::get('MEMCACHED_PORT', 11211)),
                        'weight' => Env::get('SESSION_MEMCACHED_WEIGHT', Env::get('MEMCACHED_WEIGHT', 100)),
                    ],
                ],
                'client' => [],
            ],
            'redis' => [
                'adapter' => Env::get('SESSION_REDIS_ADAPTER', \Phalcon\Session\Adapter\Redis::class),
                'defaultSerializer' => Env::get('SESSION_REDIS_DEFAULT_SERIALIZER', Env::get('REDIS_DEFAULT_SERIALIZER', 'php')),
                'lifetime' => Env::get('SESSION_REDIS_LIFETIME', Env::get('REDIS_LIFETIME', 3600)),
                'serializer' => Env::get('SESSION_REDIS_SERIALIZER', Env::get('REDIS_SERIALIZER', null)),
                'host' => Env::get('SESSION_REDIS_HOST', Env::get('REDIS_HOST', '127.0.0.1')),
                'port' => Env::get('SESSION_REDIS_PORT', Env::get('REDIS_PORT', 6379)),
                'index' => Env::get('SESSION_REDIS_INDEX', Env::get('REDIS_INDEX', 1)),
                'auth' => Env::get('SESSION_REDIS_AUTH', Env::get('REDIS_AUTH', null)),
                'persistent' => Env::get('SESSION_REDIS_PERSISTENT', Env::get('REDIS_PERSISTENT', 0)),
                'socket' => Env::get('SESSION_REDIS_SOCKET', Env::get('REDIS_SOCKET', null)),
            ],
            'noop' => [
                'adapter' => Env::get('SESSION_NOOP_ADAPTER', \Phalcon\Session\Adapter\Noop::class),
            ],
        ],
        'default' => [
            'prefix' => Env::get('SESSION_PREFIX', Env::get('GLOBAL_PREFIX', 'phalcon_kit_') . 'session_'),
            'uniqueId' => Env::get('SESSION_UNIQUE_ID', Env::get('GLOBAL_PREFIX', 'phalcon_kit_')),
            'lifetime' => Env::get('SESSION_LIFETIME', 3600),
        ],
        'ini' => [
            'session.save_path' => Env::get('SESSION_SAVE_PATH', ''),
            'session.name' => Env::get('SESSION_NAME', 'PHPSESSID'),
            'session.save_handler' => Env::get('SESSION_SAVE_HANDLER', 'files'),
            'session.auto_start' => Env::get('SESSION_AUTO_START', '0'),
            'session.gc_probability' => Env::get('SESSION_GC_PROBABILITY', '1'),
            'session.gc_divisor' => Env::get('SESSION_GC_DIVISOR', '100'),
            'session.gc_maxlifetime' => Env::get('SESSION_GC_MAXLIFETIME', '1440'),
            'session.serialize_handler' => Env::get('SESSION_SERIALIZE_HANDLER', 'php'),
            'session.cookie_lifetime' => Env::get('SESSION_COOKIE_LIFETIME', '0'),
            'session.cookie_path' => Env::get('SESSION_COOKIE_PATH', '/'),
            'session.cookie_domain' => Env::get('SESSION_COOKIE_DOMAIN', ''),
            'session.cookie_secure' => Env::get('SESSION_COOKIE_SECURE', '1'),
            'session.cookie_httponly' => Env::get('SESSION_COOKIE_HTTPONLY', '1'),
            'session.cookie_samesite' => Env::get('SESSION_COOKIE_SAMESITE', ''),
            'session.use_strict_mode' => Env::get('SESSION_USE_STRICT_MODE', '0'),
            'session.use_cookies' => Env::get('SESSION_USE_COOKIES', '1'),
            'session.use_only_cookies' => Env::get('SESSION_USE_ONLY_COOKIES', '1'),
            'session.referer_check' => Env::get('SESSION_REFERER_CHECK', ''),
            'session.cache_limiter' => Env::get('SESSION_CACHE_LIMITER', 'nocache'),
            'session.cache_expire' => Env::get('SESSION_CACHE_EXPIRE', '180'),
            'session.use_trans_sid' => Env::get('SESSION_USE_TRANS_SID', '0'),
            'session.trans_sid_tags' => Env::get('SESSION_TRANS_SID_TAGS', 'a=href,area=href,frame=src,form='),
            'session.trans_sid_hosts' => Env::get('SESSION_TRANS_SID_HOSTS', $_SERVER['HTTP_HOST'] ?? ''),
            'session.sid_length' => Env::get('SESSION_SID_LENGTH', '32'),
            'session.sid_bits_per_character' => Env::get('SESSION_SID_BITS_PER_CHARACTER', '4'),
            'session.upload_progress.enabled' => Env::get('SESSION_UPLOAD_PROGRESS_ENABLED', '1'),
            'session.upload_progress.cleanup' => Env::get('SESSION_UPLOAD_PROGRESS_CLEANUP', '1'),
            'session.upload_progress.prefix' => Env::get('SESSION_UPLOAD_PROGRESS_PREFIX', Env::get('GLOBAL_PREFIX', 'phalcon_kit_') . 'upload_progress_'),
            'session.upload_progress.name' => Env::get('SESSION_UPLOAD_PROGRESS_NAME', 'PHP_SESSION_UPLOAD_PROGRESS'),
            'session.upload_progress.freq' => Env::get('SESSION_UPLOAD_PROGRESS_FREQ', '1%'),
            'session.upload_progress.min_freq' => Env::get('SESSION_UPLOAD_PROGRESS_MIN_FREQ', '1'),
            'session.lazy_write' => Env::get('SESSION_LAZY_WRITE', '1'),
            'session.hash_function' => Env::get('SESSION_HASH_FUNCTION', '0'),
            'session.hash_bits_per_character' => Env::get('SESSION_HASH_BITS_PER_CHARACTER', '4'),
            'session.entropy_file' => Env::get('SESSION_ENTROPY_FILE', ''),
            'session.entropy_length' => Env::get('SESSION_ENTROPY_LENGTH', '0'),
        ],
    ],
]);
```

## Session Service (`session`)

!!! info "Session Service Provider"
    Session Service Provider (`session`):
    [`\Zemit\Provider\Session\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Session/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$session = $this->session;

// Retrieving the service from the DI
$session = $this->di->get('session');

// Retrieving the service from the getDI()
$session = $this->getDI()->get('session');

// Retrieving the service from anywhere
$session = Di::getDefault()->get('session');
```
