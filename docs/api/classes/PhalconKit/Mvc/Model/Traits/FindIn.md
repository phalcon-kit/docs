
Provides small `IN (...)` helpers for models with an integer `id` column.

The current trait intentionally exposes only `findInById()`. More generic
`findIn*` variants need field validation, bind-type inference, and clear
naming rules before they become public model API.

***

* Full name: `\PhalconKit\Mvc\Model\Traits\FindIn`

## Methods

### findInById

```php
public static findInById(array $idList = []): \Phalcon\Mvc\Model\ResultsetInterface
```

* This method is **static**.
**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$idList` | **array** |             |

***
