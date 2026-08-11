
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Actions\Rest\MaximumAction`

## Methods

### maxAction

Legacy short alias for `maximumAction()`.

```php
public maxAction(): \Phalcon\Http\ResponseInterface
```

***
### maximumAction

Return the maximum value for the configured aggregate column.

```php
public maximumAction(): \Phalcon\Http\ResponseInterface
```

The response variable is named `maximum`. Query preparation is delegated
to the shared query trait so REST filters and policy constraints are
applied consistently.

***
