
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Actions\Rest\IndexAction`

## Methods

### indexAction

Forward an index request to the REST action that matches the HTTP method.

```php
public indexAction(): \Phalcon\Http\ResponseInterface
```

POST/PUT/PATCH requests are forwarded to `save`, DELETE requests to
`delete`, and GET requests to either `find` or `findFirst` depending on
whether an integer `id` parameter is present.

**Throws:**

When request forwarding fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When request parameter filtering fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
### restForwarding

Execute the method/id based REST forwarding decision.

```php
protected restForwarding(): bool
```

Returns true when a forward was performed and false when the request
method is not handled by the generic index endpoint.

**Throws:**

When request forwarding fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When request parameter filtering fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
