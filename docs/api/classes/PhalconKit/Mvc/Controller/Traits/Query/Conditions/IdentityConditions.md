
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Conditions\IdentityConditions`

## Properties

### identityConditions

```php
protected ?\Phalcon\Support\Collection $identityConditions
```

***

## Methods

### initializeIdentityConditions

```php
public initializeIdentityConditions(): void
```

***
### setIdentityConditions

```php
public setIdentityConditions(?\Phalcon\Support\Collection $identityConditions): void
```

**Parameters:**

| Parameter             | Type                             | Description |
|-----------------------|----------------------------------|-------------|
| `$identityConditions` | **?\Phalcon\Support\Collection** |             |

***
### getIdentityConditions

```php
public getIdentityConditions(): ?\Phalcon\Support\Collection
```

***
### defaultIdentityCondition

Builds the identity condition based on the current user's identity and role.

```php
public defaultIdentityCondition(): array|string|null
```

**Return Value:**

Returns an array with the following elements:
- If identity columns are empty, returns null.
- If no identity is found, returns ['false'].
- If the current user role is a super admin, returns ['true'].
- If identity conditions are found, returns an array with the following elements:
  - The condition string formed by joining the columns with 'or' operators.
  - An array of bind values for the condition.
  - An array of bind types for the condition.

***
### getIdentityColumns

Retrieves the identity columns of the current model.

```php
public getIdentityColumns(): array
```

**Return Value:**

The identity columns.

***
