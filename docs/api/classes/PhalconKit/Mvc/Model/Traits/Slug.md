
***

* Full name: `\PhalconKit\Mvc\Model\Traits\Slug`

## Methods

### initializeSlug

Initializes the slug behavior for the model.

```php
public initializeSlug(array|null $options = null): void
```

**Parameters:**

| Parameter  | Type            | Description                                                                       |
|------------|-----------------|-----------------------------------------------------------------------------------|
| `$options` | **array\|null** | Optional. An array containing the options for the slug behavior. Default is null. |

***
### setSlugBehavior

Sets the slug behavior for the model.

```php
public setSlugBehavior(\PhalconKit\Mvc\Model\Behavior\Transformable $slugBehavior): void
```

**Parameters:**

| Parameter       | Type                                             | Description                                            |
|-----------------|--------------------------------------------------|--------------------------------------------------------|
| `$slugBehavior` | **\PhalconKit\Mvc\Model\Behavior\Transformable** | A Transformable object representing the slug behavior. |

***
### getSlugBehavior

Returns the slug behavior associated with the model.

```php
public getSlugBehavior(): \PhalconKit\Mvc\Model\Behavior\Transformable
```

**Return Value:**

The slug behavior associated with the model.

***
