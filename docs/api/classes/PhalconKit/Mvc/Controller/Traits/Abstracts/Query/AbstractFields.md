
Abstract contract that groups all REST field-policy collections.

These policies control which model fields can cross the public REST boundary
for exposure, filtering, mapping, ordering, saving, and searching. Keeping
the contracts grouped makes controller initialization predictable while still
letting each policy expose its own focused getter/setter methods.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\Query\AbstractFields`

## Methods

### initializeFields

Initialize expose, filter, map, order, save, and search field policies.

```php
public initializeFields(): void
```

* This method is **abstract**.
***
