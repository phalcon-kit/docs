
Abstract contract for fields that may be assigned during save operations.

Save fields protect mass assignment at the REST controller layer. Null keeps
Phalcon model assignment unrestricted, while an empty collection is an
explicit read-only/closed writable-field policy.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\Query\Fields\AbstractSaveFields`

## Methods

### initializeSaveFields

Initialize the save-field policy for REST persistence actions.

```php
public initializeSaveFields(): void
```

* This method is **abstract**.
***
### setSaveFields

Replace the save-field policy.

```php
public setSaveFields(array|\Phalcon\Support\Collection|null $saveFields): void
```

* This method is **abstract**.
**Parameters:**

| Parameter     | Type                                         | Description                                                                                            |
|---------------|----------------------------------------------|--------------------------------------------------------------------------------------------------------|
| `$saveFields` | **array\|\Phalcon\Support\Collection\|null** | Field policy collection, null for
unrestricted assignment, or an empty collection for a closed policy. |

***
### getSaveFields

Return the configured save-field policy.

```php
public getSaveFields(): \Phalcon\Support\Collection|null
```

* This method is **abstract**.
**Return Value:**

Field policy collection or null for unrestricted
assignment.

***
