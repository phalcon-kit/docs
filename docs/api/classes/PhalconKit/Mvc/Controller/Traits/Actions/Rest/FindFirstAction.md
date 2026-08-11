
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Actions\Rest\FindFirstAction`

## Methods

### getAction

Legacy alias for `findFirstAction()`.

```php
public getAction(): \Phalcon\Http\ResponseInterface
```

* **Warning:** this method is **deprecated**. This means that this method will likely be removed in a future version.
***
### getWithAction

Legacy alias for `findFirstWithAction()`.

```php
public getWithAction(): \Phalcon\Http\ResponseInterface
```

* **Warning:** this method is **deprecated**. This means that this method will likely be removed in a future version.
***
### findFirstAction

Find, expose, and return the first record matching the prepared query.

```php
public findFirstAction(): \Phalcon\Http\ResponseInterface
```

The action returns 404 when no entity matches. On success, `data` holds
the exposed model payload.

***
### findFirstWithAction

Find the first matching record with configured eager-loaded relations.

```php
public findFirstWithAction(): \Phalcon\Http\ResponseInterface
```

The action returns 404 when no entity matches. On success, `data` holds
the exposed model payload. If the client sends no `with` parameter, the
controller's default eager-load graph is used. If the client sends
`with`, only the requested, controller-approved subset is loaded.

**Throws:**

When request parameter filtering fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When a requested relationship is not allowed.
- [`HttpException`](../../../../../Exception/HttpException.md)

***
