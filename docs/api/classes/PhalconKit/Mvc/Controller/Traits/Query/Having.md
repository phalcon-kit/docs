
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Having`

## Properties

### having

```php
protected ?\Phalcon\Support\Collection $having
```

***

## Methods

### initializeHaving

Initializes the having property to its default state.

```php
public initializeHaving(): void
```

***
### getHaving

Retrieves the current having collection.

```php
public getHaving(): \Phalcon\Support\Collection|null
```

**Return Value:**

The collection of having, or null if none is set.

***
### setHaving

Sets the having property to the provided collection.

```php
public setHaving(array|\Phalcon\Support\Collection|null $having): void
```

**Parameters:**

| Parameter | Type                                         | Description                                                        |
|-----------|----------------------------------------------|--------------------------------------------------------------------|
| `$having` | **array\|\Phalcon\Support\Collection\|null** | The collection to set as the having property, or null to clear it. |

***
### mergeHaving

Merges the provided having collection with the current having property.

```php
public mergeHaving(array|\Phalcon\Support\Collection $having): void
```

**Parameters:**

| Parameter | Type                                   | Description                                                  |
|-----------|----------------------------------------|--------------------------------------------------------------|
| `$having` | **array\|\Phalcon\Support\Collection** | The collection of having to merge with the current property. |

***
