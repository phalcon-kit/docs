
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Actions\Rest\NewAction`

## Methods

### newAction

Build and expose a new unsaved model instance.

```php
public newAction(): \Phalcon\Http\ResponseInterface
```

Request parameters are assigned through the configured save/map fields so
clients can inspect default values and server-side assignment behavior
before submitting a create request.

***
