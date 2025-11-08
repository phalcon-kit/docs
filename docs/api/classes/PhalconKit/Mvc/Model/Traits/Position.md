
The Position trait is used to manage the position behavior of an object.

It provides methods to initialize the position behavior set and retrieve
the position behavior object, and reorder the object's position in a list.

***

* Full name: `\PhalconKit\Mvc\Model\Traits\Position`

## Methods

### initializePosition

Initializes the position behavior for the current object.

```php
public initializePosition(array|null $options = null): void
```

Sets the position options and sets the position behavior accordingly.

**Parameters:**

| Parameter  | Type            | Description                                                                                                 |
|------------|-----------------|-------------------------------------------------------------------------------------------------------------|
| `$options` | **array\|null** | The options for the position behavior.
If not provided, the default position behavior options will be used. |

**Throws:**

- [`Exception`](../../../../Exception.md)

***
### setPositionBehavior

Sets the position behavior for the current object.

```php
public setPositionBehavior(\PhalconKit\Mvc\Model\Behavior\Position $positionBehavior): void
```

**Parameters:**

| Parameter           | Type                                        | Description                      |
|---------------------|---------------------------------------------|----------------------------------|
| `$positionBehavior` | **\PhalconKit\Mvc\Model\Behavior\Position** | The position behavior to be set. |

***
### getPositionBehavior

Retrieves the position behavior attached to the current object.

```php
public getPositionBehavior(): \PhalconKit\Mvc\Model\Behavior\Position
```

**Return Value:**

The position behavior object.

**Throws:**

if the position behavior is not found.
- [`Exception`](../../../../Exception.md)

***
### reorder

Reorders the current object's position in the list.

```php
public reorder(int|null $position = null, string|null $positionField = null): bool
```

- Update position+1 done using afterSave event

**Parameters:**

| Parameter        | Type             | Description                                                                                            |
|------------------|------------------|--------------------------------------------------------------------------------------------------------|
| `$position`      | **int\|null**    | The new position for the object. If not provided, the default behavior's position field will be used.  |
| `$positionField` | **string\|null** | The field on which the position is stored. If not provided, the default behavior's field will be used. |

**Return Value:**

Returns true if the reorder operation was successful, false otherwise.

**Throws:**

- [`Exception`](../../../../Exception.md)

***
