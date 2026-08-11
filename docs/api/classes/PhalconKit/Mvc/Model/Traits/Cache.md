
Registers model-cache flushing behavior for mutable models.

By default the trait installs after-event actions that clear the shared
`modelsCache` service when a save/update changed data, or when create,
delete, restore, and reorder events change record visibility/order.
Session and audit models are blacklisted during initialization to avoid
flushing global model caches for high-volume infrastructure records.

Known limitation: cache invalidation is coarse-grained. Granular cache keys,
whitelist rules, and pre-warming need an explicit cache policy contract
before this trait can safely delete only selected entries.

***

* Full name: `\PhalconKit\Mvc\Model\Traits\Cache`

## Properties

### preventFlushCache

Whether cache flushing is disabled for this model instance.

```php
public bool $preventFlushCache
```

Set this to true before initialization or before calling
`addFlushCacheBehavior()` to skip installing the flush behavior for the
current instance.

***
### flushModelsCacheBlackList

Model classes that should not trigger global model-cache clearing.

```php
public array<int,class-string|object|string> $flushModelsCacheBlackList
```

The list is populated with core session/audit classes during
initialization and can be extended by applications before calling
`addFlushCacheBehavior()`.

***

## Methods

### initializeCache

Initialize model cache invalidation for the current model.

```php
public initializeCache(): void
```

The `models` service supplies framework model class mappings used for
the default blacklist. After the blacklist is prepared, the trait adds
the flush behavior unless this model instance or class is excluded.

**Throws:**

When the models service cannot be resolved
through the PhalconKit DI contract.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
### addFlushCacheBehavior

Add an after-event behavior that clears the shared models cache.

```php
public addFlushCacheBehavior(array<int,class-string|object|string>|null $flushModelsCacheBlackList = null): void
```

The behavior is skipped when `preventFlushCache` is true or the current
model is an instance of one of the blacklisted classes. Cache clearing is
attempted only when snapshots indicate that persisted data changed.

**Parameters:**

| Parameter                    | Type                                              | Description                                                                              |
|------------------------------|---------------------------------------------------|------------------------------------------------------------------------------------------|
| `$flushModelsCacheBlackList` | **array<int,class-string\|object\|string>\|null** |
Classes that should not receive the flush behavior. Defaults to the
instance blacklist. |

**Throws:**

When the modelsCache service cannot be resolved
through the PhalconKit DI contract.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
### isInstanceOf

Check whether a model instance belongs to any configured class.

```php
public isInstanceOf(array<int,mixed> $classes = [], \Phalcon\Mvc\ModelInterface|null $that = null): bool
```

This helper supports cache blacklist checks while allowing tests or
callers to pass an explicit instance. Invalid values are ignored instead
of being passed to `instanceof`, because a malformed application-provided
blacklist entry should not turn cache-behavior initialization into a PHP
fatal error.

**Parameters:**

| Parameter  | Type                                  | Description                                                           |
|------------|---------------------------------------|-----------------------------------------------------------------------|
| `$classes` | **array<int,mixed>**                  | Class names, objects, or ignored
malformed values to compare against. |
| `$that`    | **\Phalcon\Mvc\ModelInterface\|null** | Optional model instance to inspect.
Defaults to the current model.    |

**Return Value:**

True when the model is an instance of at least one class.

***
