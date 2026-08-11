
Abstract contract for query result cache options.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\Query\AbstractCache`

## Methods

### initializeCacheConfig

Initialize the full cache option collection.

```php
public initializeCacheConfig(): void
```

* This method is **abstract**.
***
### initializeCacheKey

Initialize the cache key for the current query.

```php
public initializeCacheKey(): void
```

* This method is **abstract**.
***
### initializeCacheLifetime

Initialize the cache lifetime for the current query.

```php
public initializeCacheLifetime(): void
```

* This method is **abstract**.
***
### setCacheKey

Replace the computed cache key.

```php
public setCacheKey(?string $cacheKey): void
```

* This method is **abstract**.
**Parameters:**

| Parameter   | Type        | Description |
|-------------|-------------|-------------|
| `$cacheKey` | **?string** |             |

***
### getCacheKey

Return the computed cache key.

```php
public getCacheKey(): ?string
```

* This method is **abstract**.
***
### setCacheLifetime

Replace the cache lifetime, in seconds.

```php
public setCacheLifetime(?int $cacheLifetime): void
```

* This method is **abstract**.
**Parameters:**

| Parameter        | Type     | Description |
|------------------|----------|-------------|
| `$cacheLifetime` | **?int** |             |

***
### getCacheLifetime

Return the cache lifetime, in seconds.

```php
public getCacheLifetime(): ?int
```

* This method is **abstract**.
***
### setCacheConfig

Replace the Phalcon `cache` find-option collection.

```php
public setCacheConfig(array|\Phalcon\Support\Collection|null $cacheConfig): void
```

* This method is **abstract**.
**Parameters:**

| Parameter      | Type                                         | Description |
|----------------|----------------------------------------------|-------------|
| `$cacheConfig` | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getCacheConfig

Return the Phalcon `cache` find-option collection.

```php
public getCacheConfig(): ?\Phalcon\Support\Collection
```

* This method is **abstract**.
***
