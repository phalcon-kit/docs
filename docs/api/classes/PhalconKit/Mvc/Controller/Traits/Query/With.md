
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\With`

## Properties

### with

```php
protected ?\Phalcon\Support\Collection $with
```

***

## Methods

### initializeWith

Initializes the relationships.

```php
public initializeWith(): void
```

This method is responsible for initializing the allowed relationship aliases.

***
### setWith

Sets the allowed relationship aliases.

```php
public setWith(\Phalcon\Support\Collection|null $with): void
```

**Parameters:**

| Parameter | Type                                  | Description                                                                   |
|-----------|---------------------------------------|-------------------------------------------------------------------------------|
| `$with`   | **\Phalcon\Support\Collection\|null** | The collection of relationship aliases.
Pass null to allow any relationships. |

***
### getWith

Returns the relationship aliases collection.

```php
public getWith(): \Phalcon\Support\Collection|null
```

This method retrieves the allowed relationship aliases for the model.
If with fields have been set, it returns the collection of relationship aliases.
If no relationship aliases have been set, it returns null.

Note: The relationship aliases are the fields that are allowed to retrieve during queries.

**Return Value:**

The collection of relationship aliases or null everything is allowed.

***
