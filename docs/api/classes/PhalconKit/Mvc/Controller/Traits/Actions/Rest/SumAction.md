
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Actions\Rest\SumAction`

## Methods

### sumAction

Return the sum for the configured aggregate column.

```php
public sumAction(): \Phalcon\Http\ResponseInterface
```

The response variable is named `sum`. Query preparation is delegated to
the shared query trait so filters, permissions, joins, and request state
match the other REST aggregate actions.

***
