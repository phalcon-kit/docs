
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Distinct`

## Properties

### distinct

```php
protected ?\Phalcon\Support\Collection $distinct
```

***

## Methods

### initializeDistinct

Initialize the distinct parameter for the query.

```php
public initializeDistinct(): void
```

**Throws:**

If an error occurs during filtering
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
### setDistinct

Sets the distinct collection.

```php
public setDistinct(\Phalcon\Support\Collection|null $distinct): void
```

**Parameters:**

| Parameter   | Type                                  | Description                     |
|-------------|---------------------------------------|---------------------------------|
| `$distinct` | **\Phalcon\Support\Collection\|null** | The distinct collection to set. |

***
### getDistinct

Gets the distinct collection.

```php
public getDistinct(): \Phalcon\Support\Collection|null
```

**Return Value:**

The distinct collection, if set; otherwise, null.

***
