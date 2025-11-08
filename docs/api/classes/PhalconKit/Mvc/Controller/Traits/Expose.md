
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Expose`

## Methods

### expose

Expose properties of an item

```php
public expose(mixed $item, array|null $expose = null): array
```

**Parameters:**

| Parameter | Type            | Description                                                                                                                    |
|-----------|-----------------|--------------------------------------------------------------------------------------------------------------------------------|
| `$item`   | **mixed**       | The item to expose properties for                                                                                              |
| `$expose` | **array\|null** | The array defining which properties to expose (optional).
If not provided, the default $this->getExpose() method will be used. |

**Return Value:**

The exposed properties as an array

***
### listExpose

List entities with specified expose definition

```php
public listExpose(iterable $items, array|null $expose = null): array
```

**Parameters:**

| Parameter | Type            | Description                                                                                                                |
|-----------|-----------------|----------------------------------------------------------------------------------------------------------------------------|
| `$items`  | **iterable**    | The iterable collection of items to be listed                                                                              |
| `$expose` | **array\|null** | The expose definition for the entities (optional)
If not provided, the default $this->getListExpose() method will be used. |

**Return Value:**

The array of exposed entities

***
### exportExpose

Export items with expose definition

```php
public exportExpose(iterable $items, array|null $expose = null): array
```

**Parameters:**

| Parameter | Type            | Description                                                                                                         |
|-----------|-----------------|---------------------------------------------------------------------------------------------------------------------|
| `$items`  | **iterable**    | The items to be exported                                                                                            |
| `$expose` | **array\|null** | The expose definition for the items.
If not provided, the default $this->getExportExpose() definition will be used. |

**Return Value:**

The exported items

***
