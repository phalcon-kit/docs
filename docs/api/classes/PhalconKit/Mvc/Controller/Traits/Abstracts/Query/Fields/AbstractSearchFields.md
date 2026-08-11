
Abstract contract for fields that may participate in text search.

Search fields are opt-in: null means no search field list was configured,
while a non-null collection defines exactly which fields the public `search`
request parameter can target.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\Query\Fields\AbstractSearchFields`

## Methods

### initializeSearchFields

Initialize the search-field policy for the current controller/action.

```php
public initializeSearchFields(): void
```

* This method is **abstract**.
***
### setSearchFields

Replace the search-field policy.

```php
public setSearchFields(array|\Phalcon\Support\Collection|null $searchFields): void
```

* This method is **abstract**.
**Parameters:**

| Parameter       | Type                                         | Description                                                             |
|-----------------|----------------------------------------------|-------------------------------------------------------------------------|
| `$searchFields` | **array\|\Phalcon\Support\Collection\|null** | Field policy collection or null when
search should remain unconfigured. |

***
### getSearchFields

Return the configured search-field policy.

```php
public getSearchFields(): \Phalcon\Support\Collection|null
```

* This method is **abstract**.
**Return Value:**

Field policy collection or null when search is
unconfigured.

***
