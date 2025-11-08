
Flush Cache on changes

***

* Full name: `\PhalconKit\Mvc\Model\Traits\Cache`

## Properties

### preventFlushCache

Set true to avoid flushing cache for the current instance

```php
public bool $preventFlushCache
```

***
### flushModelsCacheBlackList

Whitelisted classes to not force global cache flush on change

```php
public array $flushModelsCacheBlackList
```

***

## Methods

### initializeCache

Initializing Cache

```php
public initializeCache(): void
```

***
### addFlushCacheBehavior

Adding Cache Behavior

```php
public addFlushCacheBehavior(?array $flushModelsCacheBlackList = null): void
```

**Parameters:**

| Parameter                    | Type       | Description |
|------------------------------|------------|-------------|
| `$flushModelsCacheBlackList` | **?array** |             |

***
### isInstanceOf

Check whether the current instance is any of the classes

```php
public isInstanceOf(array $classes = [], ?\Phalcon\Mvc\ModelInterface $that = null): bool
```

**Parameters:**

| Parameter  | Type                             | Description |
|------------|----------------------------------|-------------|
| `$classes` | **array**                        |             |
| `$that`    | **?\Phalcon\Mvc\ModelInterface** |             |

***
