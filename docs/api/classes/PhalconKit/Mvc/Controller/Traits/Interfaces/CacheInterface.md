
Contract for REST query cache-key helpers.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Interfaces\CacheInterface`

## Methods

### getCacheKey

Build a cache key for the current query parameters.

```php
public getCacheKey(array<string,mixed>|null $params = null): ?string
```

**Parameters:**

| Parameter | Type                          | Description                                                                                 |
|-----------|-------------------------------|---------------------------------------------------------------------------------------------|
| `$params` | **array<string,mixed>\|null** | Optional request/query
parameters. Implementations use current controller params when null. |

***
