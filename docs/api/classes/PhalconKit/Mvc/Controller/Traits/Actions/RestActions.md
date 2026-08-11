
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Actions\RestActions`

## Methods

### initializeRestActions

Initialize action-level REST configuration.

```php
public initializeRestActions(): void
```

Query configuration lives in

- **See:** \PhalconKit\Mvc\Controller\Traits\Query::initializeQuery(),
while action traits can expose smaller policy sets that affect only their
response behavior. Count, distinct, and list-count policies are
initialized here so controllers can customize action metadata through the
same lifecycle used by the rest of the REST API layer.

***
