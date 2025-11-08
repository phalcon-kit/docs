# Cache Service

The `cache` service uses the [Phalcon Cache Component](https://docs.phalcon.io/latest/cache/){:target="_blank"}

## Cache Configurations

```ini
CACHE_DRIVER_CLI=memory
CACHE_DRIVER=memory

# Memory
CACHE_MEMORY_ADAPTER=\Phalcon\Cache\Adapter\Memory

# APCU
CACHE_APCU_ADAPTER=\Phalcon\Cache\Adapter\Apcu

# File
CACHE_STREAM_ADAPTER=\Phalcon\Cache\Adapter\Stream
CACHE_STREAM_DIR=./storage/cache/data/

# Memcached
CACHE_MEMCACHED_ADAPTER=\Phalcon\Cache\Adapter\Libmemcached
CACHE_MEMCACHED_HOST=127.0.0.1
CACHE_MEMCACHED_PORT=11211
CACHE_MEMCACHED_WEIGHT=100

# Redis
CACHE_REDIS_ADAPTER=\Phalcon\Cache\Adapter\Redis
CACHE_REDIS_DEFAULT_SERIALIZER=php
CACHE_REDIS_LIFETIME=3600
CACHE_REDIS_SERIALIZER=
CACHE_REDIS_HOST=127.0.0.1
CACHE_REDIS_PORT=6379
CACHE_REDIS_INDEX=1
CACHE_REDIS_AUTH=
CACHE_REDIS_PERSISTENT=
CACHE_REDIS_SOCKET=

# Global
CACHE_PREFIX=phalcon_kit_cache_
CACHE_LIFETIME=86400
CACHE_DEFAULT_SERIALIZER=Php
```

### Cache Service Provider

```ini
PROVIDER_CACHE=\PhalconKit\Provider\Cache\ServiceProvider
```

### Cache Configurations Object

```php
<?php
new Config([
    'providers' => [
        \PhalconKit\Provider\Cache\ServiceProvider::class => Env::get('PROVIDER_CACHE', \PhalconKit\Provider\Cache\ServiceProvider::class),
    ],
    'cache' => [
        'cli' => Env::get('CACHE_DRIVER_CLI', 'memory'),
        'driver' => Env::get('CACHE_DRIVER', 'memory'),
        'drivers' => [
            'memory' => [
                'adapter' => Env::get('CACHE_MEMORY_ADAPTER', \Phalcon\Cache\Adapter\Memory::class),
            ],
            'apcu' => [
                'adapter' => Env::get('CACHE_APCU_ADAPTER', \Phalcon\Cache\Adapter\Apcu::class),
            ],
            'stream' => [
                'adapter' => Env::get('CACHE_STREAM_ADAPTER', \Phalcon\Cache\Adapter\Stream::class),
                'cacheDir' => Env::get('CACHE_STREAM_DIR', STORAGE_PATH . '/cache/data/'),
            ],
            'memcached' => [
                'adapter' => Env::get('CACHE_MEMCACHED_ADAPTER', \Phalcon\Cache\Adapter\Libmemcached::class),
                'servers' => [
                    [
                        'host' => Env::get('CACHE_MEMCACHED_HOST', Env::get('MEMCACHED_HOST', '127.0.0.1')),
                        'port' => Env::get('CACHE_MEMCACHED_PORT', Env::get('MEMCACHED_PORT', 11211)),
                        'weight' => Env::get('CACHE_MEMCACHED_WEIGHT', Env::get('MEMCACHED_WEIGHT', 100)),
                    ],
                ],
            ],
            'redis' => [
                'adapter' => Env::get('CACHE_REDIS_ADAPTER', \Phalcon\Cache\Adapter\Redis::class),
                'defaultSerializer' => Env::get('CACHE_REDIS_DEFAULT_SERIALIZER', Env::get('REDIS_DEFAULT_SERIALIZER', 'php')),
                'lifetime' => Env::get('CACHE_REDIS_LIFETIME', Env::get('REDIS_LIFETIME', 3600)),
                'serializer' => Env::get('CACHE_REDIS_SERIALIZER', Env::get('REDIS_SERIALIZER', null)),
                'host' => Env::get('CACHE_REDIS_HOST', Env::get('REDIS_HOST', '127.0.0.1')),
                'port' => Env::get('CACHE_REDIS_PORT', Env::get('REDIS_PORT', 6379)),
                'index' => Env::get('CACHE_REDIS_INDEX', Env::get('REDIS_INDEX', 1)),
                'auth' => Env::get('CACHE_REDIS_AUTH', Env::get('REDIS_AUTH', null)),
                'persistent' => Env::get('CACHE_REDIS_PERSISTENT', Env::get('REDIS_PERSISTENT', null)),
                'socket' => Env::get('CACHE_REDIS_SOCKET', Env::get('REDIS_SOCKET', null)),
            ],
        ],
        'default' => [
            'prefix' => Env::get('CACHE_PREFIX', Env::get('GLOBAL_PREFIX', 'phalcon_kit_') . 'cache_'),
            'lifetime' => Env::get('CACHE_LIFETIME', 86400),
            'defaultSerializer' => Env::get('CACHE_DEFAULT_SERIALIZER', 'Php'),
        ],
    ],
]);
```

## Cache Service (`cache`)

!!! info "Cache Service Provider"
    Cache Service Provider (`cache`):
    [`\PhalconKit\Provider\Cache\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Cache/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$cache = $this->cache;

// Retrieving the service from the DI
$cache = $this->di->get('cache');

// Retrieving the service from the getDI()
$cache = $this->getDI()->get('cache');

// Retrieving the service from anywhere
$cache = Di::getDefault()->get('cache');
```
