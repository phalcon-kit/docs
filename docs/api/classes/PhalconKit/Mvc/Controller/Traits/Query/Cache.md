
This trait provides methods for caching data for the query.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Cache`

## Properties

### cacheConfig

This variable holds the configuration settings for caching.

```php
public \Phalcon\Support\Collection|null $cacheConfig
```

***
### cacheKey

The cache key used for storing data in the cache.

```php
public string|null $cacheKey
```

***
### cacheLifetime

The lifetime of the cache data in seconds.

```php
public int|null $cacheLifetime
```

***

## Methods

### initializeCacheConfig

Initializes the cache.

```php
public initializeCacheConfig(): void
```

This method initializes the cache by setting the cache key and lifetime.

**Throws:**

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
### initializeCacheLifetime

Initializes the cache lifetime.

```php
public initializeCacheLifetime(): void
```

This method retrieves the 'lifetime' parameter using `getParam()` method,
applies the 'FILTER_ABSINT' filter to it, and then sets the cache lifetime
using `setCacheLifetime()` method with the filtered value.

**Throws:**

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
### initializeCacheKey

Initializes the cache key.

```php
public initializeCacheKey(): void
```

This method constructs and sets a unique cache key by combining the model name,
user identity, cache lifetime, and parameters.

***
### setCacheLifetime

Sets the cache lifetime.

```php
public setCacheLifetime(int|null $cacheLifetime): void
```

**Parameters:**

| Parameter        | Type          | Description         |
|------------------|---------------|---------------------|
| `$cacheLifetime` | **int\|null** | The cache lifetime. |

***
### getCacheLifetime

Retrieves the cache lifetime.

```php
public getCacheLifetime(): int|null
```

**Return Value:**

The cache lifetime.

***
### setCacheKey

Sets the cache key.

```php
public setCacheKey(string|null $cacheKey): void
```

**Parameters:**

| Parameter   | Type             | Description    |
|-------------|------------------|----------------|
| `$cacheKey` | **string\|null** | The cache key. |

***
### getCacheKey

Retrieves the cache key.

```php
public getCacheKey(): string|null
```

**Return Value:**

The cache key.

***
### setCacheConfig

Set the cache config collection for the query.

```php
public setCacheConfig(\Phalcon\Support\Collection|null $cacheConfig): void
```

**Parameters:**

| Parameter      | Type                                  | Description                                      |
|----------------|---------------------------------------|--------------------------------------------------|
| `$cacheConfig` | **\Phalcon\Support\Collection\|null** | The cache config collection, or null to disable. |

***
### getCacheConfig

Retrieves the cache collection for the query.

```php
public getCacheConfig(): \Phalcon\Support\Collection|null
```

**Return Value:**

The cache config collection, or null if no cache is set.

***
