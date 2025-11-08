
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Actions\Rest\FindAction`

## Methods

### getAllAction

Find and expose the resultset.

```php
public getAllAction(): \Phalcon\Http\ResponseInterface
```

* **Warning:** this method is **deprecated**. This means that this method will likely be removed in a future version.
**Return Value:**

The HTTP response that indicates the success of retrieving all records.

**Throws:**

- [`Exception`](../../../../../../Exception.md)

**See Also:**

* findAction()

***
### getAllWithAction

Find with relationships and expose the resultset.

```php
public getAllWithAction(): \Phalcon\Http\ResponseInterface
```

* **Warning:** this method is **deprecated**. This means that this method will likely be removed in a future version.
**Return Value:**

The HTTP response that contains the resultset with the relationships.

**Throws:**

- [`Exception`](../../../../../../Exception.md)

**See Also:**

* findWithAction()

***
### findAction

Find and expose the resultset.

```php
public findAction(): \Phalcon\Http\ResponseInterface
```

This method finds the resultset and exposes it for further processing.

**Return Value:**

The HTTP response that indicates the success of finding and exposing the resultset.

**Throws:**

- [`Exception`](../../../../../../Exception.md)

***
### findWithAction

Find with relationships and expose the resultset.

```php
public findWithAction(): \Phalcon\Http\ResponseInterface
```

This method finds the resultset with relationships and exposes it for further processing.

**Return Value:**

The HTTP response that indicates the success of finding and exposing the resultset.

**Throws:**

- [`Exception`](../../../../../../Exception.md)

***
