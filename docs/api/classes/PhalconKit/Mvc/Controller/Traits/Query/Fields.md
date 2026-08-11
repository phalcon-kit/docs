
Groups REST field-policy initialization for query controllers.

The individual subtraits own their storage and merge behavior. This trait
keeps the request lifecycle compact by initializing all public field
policies before conditions, ordering, and persistence logic consume them.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Fields`

## Methods

### initializeFields

Initialize every REST field-policy collection for the current request.

```php
public initializeFields(): void
```

Concrete controllers can override the specific `initialize*Fields()`
method they own instead of replacing this aggregate method. That keeps
event ordering stable while still allowing resource-specific policies.

***
