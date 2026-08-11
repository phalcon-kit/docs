
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Actions\Rest\ReorderAction`

## Methods

### reorderAction

Reorder the first entity matching the prepared REST query.

```php
public reorderAction(): \Phalcon\Http\ResponseInterface
```

The action returns 404 when no entity matches. The configured model must
implement `PositionInterface`; on completion the response exposes the
attempted entity, the reorder result, and model messages.

**Throws:**

When request parameter filtering fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When the configured model does not support
positional reordering.
- [`LogicException`](../../../../../Exception/LogicException.md)

***
### requirePositionEntity

Require the current REST entity to support positional reordering.

```php
protected requirePositionEntity(\Phalcon\Mvc\ModelInterface $entity): \Phalcon\Mvc\ModelInterface&\PhalconKit\Mvc\Model\Interfaces\PositionInterface
```

`reorderAction()` is opt-in controller composition. This helper keeps the
action workflow compact while turning a wrong model/controller pairing
into a clear PhalconKit logic exception instead of a disabled assertion or
late method-call error.

**Parameters:**

| Parameter | Type                            | Description                         |
|-----------|---------------------------------|-------------------------------------|
| `$entity` | **\Phalcon\Mvc\ModelInterface** | Entity returned by the query layer. |

**Throws:**

When the configured model does not support
positional reordering.
- [`LogicException`](../../../../../Exception/LogicException.md)

***
