
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Actions\Rest\MinimumAction`

## Methods

### minAction

Legacy short alias for `minimumAction()`.

```php
public minAction(): \Phalcon\Http\ResponseInterface
```

***
### minimumAction

Return the minimum value for the configured aggregate column.

```php
public minimumAction(): \Phalcon\Http\ResponseInterface
```

The response variable is named `minimum`. Query preparation is delegated
to the shared query trait so REST filters and policy constraints are
applied consistently.

***
