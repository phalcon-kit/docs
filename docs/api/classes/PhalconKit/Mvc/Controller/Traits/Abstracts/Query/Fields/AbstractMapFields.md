
Abstract contract for public-field to model-field mapping.

Map fields let REST controllers accept stable public payload names while
assigning different model attributes. Null disables mapping and leaves
payload keys unchanged.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\Query\Fields\AbstractMapFields`

## Methods

### initializeMapFields

Initialize the assignment field-map policy.

```php
public initializeMapFields(): void
```

* This method is **abstract**.
***
### setMapFields

Replace the assignment field-map policy.

```php
public setMapFields(array|\Phalcon\Support\Collection|null $mapFields): void
```

* This method is **abstract**.
**Parameters:**

| Parameter    | Type                                         | Description                                                 |
|--------------|----------------------------------------------|-------------------------------------------------------------|
| `$mapFields` | **array\|\Phalcon\Support\Collection\|null** | Field map collection or null to disable
assignment mapping. |

***
### getMapFields

Return the configured assignment field-map policy.

```php
public getMapFields(): \Phalcon\Support\Collection|null
```

* This method is **abstract**.
**Return Value:**

Field map collection or null when mapping is
disabled.

***
