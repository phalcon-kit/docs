
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Bind`

## Properties

### bind

```php
protected ?\Phalcon\Support\Collection $bind
```

***
### bindTypes

```php
protected ?\Phalcon\Support\Collection $bindTypes
```

***

## Methods

### initializeBind

Initializes the bindings.

```php
public initializeBind(): void
```

This method is responsible for initializing the necessary binding data for the queries.

***
### initializeBindTypes

Initializes the binding types.

```php
public initializeBindTypes(): void
```

This method is responsible for initializing the necessary bind types for the queries.

***
### setBind

Sets the fields for binding data.

```php
public setBind(\Phalcon\Support\Collection|null $bind): void
```

**Parameters:**

| Parameter | Type                                  | Description                                                                |
|-----------|---------------------------------------|----------------------------------------------------------------------------|
| `$bind`   | **\Phalcon\Support\Collection\|null** | The collection of field bindings.
Pass null to disable the field bindings. |

***
### getBind

Returns the bind data.

```php
public getBind(): \Phalcon\Support\Collection|null
```

This method retrieves the bind fields for the model.
If bind fields have been set, it returns the collection of bind fields.
If no bind fields have been set, it returns null.

Note: The bind fields are the fields that are allowed to be used within database queries.

**Return Value:**

The collection of bindings or null if binding is disabled.

***
### setBindTypes

Sets the fields for binding data.

```php
public setBindTypes(\Phalcon\Support\Collection|null $bindTypes): void
```

**Parameters:**

| Parameter    | Type                                  | Description                                                              |
|--------------|---------------------------------------|--------------------------------------------------------------------------|
| `$bindTypes` | **\Phalcon\Support\Collection\|null** | The collection of binding types.
Pass null to disable the binding types. |

***
### getBindTypes

Returns the binding types.

```php
public getBindTypes(): \Phalcon\Support\Collection|null
```

This method retrieves the binding types for the query.
If bind binding types have been set, it returns the collection of binding types.
If no binding types have been set, it returns null.

Note: The binding types are the types for the fields used within database queries.

**Return Value:**

The collection of bindings or null if binding types is disabled.

***
