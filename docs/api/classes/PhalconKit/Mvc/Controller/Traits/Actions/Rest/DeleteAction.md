
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Actions\Rest\DeleteAction`

## Methods

### deleteAction

Delete the first record matching the prepared REST query.

```php
public deleteAction(): \Phalcon\Http\ResponseInterface
```

The action returns 404 when no entity matches. On success or failure it
exposes the attempted entity, the boolean delete result, and model
messages so clients can display domain validation or delete errors.

***
