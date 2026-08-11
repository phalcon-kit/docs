
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Actions\Rest\RestoreAction`

## Methods

### restoreAction

Restore the first soft-deleted entity matching the prepared REST query.

```php
public restoreAction(): \Phalcon\Http\ResponseInterface
```

The action returns 404 when no entity matches. The configured model must
implement `SoftDeleteInterface`; on completion the response exposes the
attempted entity, the restore result, and model messages.

**Throws:**

When the configured model does not support soft
deletes.
- [`LogicException`](../../../../../Exception/LogicException.md)

***
### requireSoftDeleteEntity

Require the current REST entity to support soft-delete restoration.

```php
protected requireSoftDeleteEntity(\Phalcon\Mvc\ModelInterface $entity): \Phalcon\Mvc\ModelInterface&\PhalconKit\Mvc\Model\Interfaces\SoftDeleteInterface
```

The action can be composed into any REST controller, but it is valid only
for models that expose PhalconKit's soft-delete contract. A helper keeps
the action body focused on the workflow while converting an invalid
controller/model pairing into a stable framework exception.

**Parameters:**

| Parameter | Type                            | Description                         |
|-----------|---------------------------------|-------------------------------------|
| `$entity` | **\Phalcon\Mvc\ModelInterface** | Entity returned by the query layer. |

**Throws:**

When the configured model does not support soft
deletes.
- [`LogicException`](../../../../../Exception/LogicException.md)

***
