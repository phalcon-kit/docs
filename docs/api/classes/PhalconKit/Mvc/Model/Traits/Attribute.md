
This trait provides methods to get and set attributes in a model using the get/set methods

***

* Full name: `\PhalconKit\Mvc\Model\Traits\Attribute`

## Methods

### getAttribute

Returns the value of the specified attribute.

```php
public getAttribute(string $attribute): mixed|null
```

**Parameters:**

| Parameter    | Type       | Description                |
|--------------|------------|----------------------------|
| `$attribute` | **string** | The name of the attribute. |

**Return Value:**

The value of the specified attribute if it exists, otherwise null.

***
### setAttribute

Sets the value of the specified attribute.

```php
public setAttribute(string $attribute, mixed $value): void
```

**Parameters:**

| Parameter    | Type       | Description                            |
|--------------|------------|----------------------------------------|
| `$attribute` | **string** | The name of the attribute.             |
| `$value`     | **mixed**  | The value to be set for the attribute. |

***
