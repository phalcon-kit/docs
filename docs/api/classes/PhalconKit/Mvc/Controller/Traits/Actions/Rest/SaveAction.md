
REST save / create / update actions.

Responsibilities:
- Delegate persistence to the Save trait
- Translate save results into correct HTTP semantics

Non-responsibilities:
- No persistence logic
- No validation logic
- No inference of entity-level errors

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Actions\Rest\SaveAction`

## Methods

### saveAction

Generic save endpoint.

```php
public saveAction(): \Phalcon\Http\ResponseInterface
```

- Auto-detects creation vs. update
- Supports single or batch payloads
- Backward compatible entry point

**Throws:**

When request payload filtering fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When persistence intent resolution returns an
inconsistent framework state.
- [`LogicException`](../../../../../Exception/LogicException.md)

***
### createAction

Explicitly create endpoint.

```php
public createAction(): \Phalcon\Http\ResponseInterface
```

- Forces creation semantics
- Single entity success → 201 Created
- Batch semantics unchanged (200 / 207 / 422)

**Throws:**

When request payload filtering fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When persistence intent resolution returns an
inconsistent framework state.
- [`LogicException`](../../../../../Exception/LogicException.md)

***
### updateAction

Explicit update endpoint.

```php
public updateAction(): \Phalcon\Http\ResponseInterface
```

- Forces update semantics
- Success → 200 OK

**Throws:**

When request payload filtering fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When persistence intent resolution returns an
inconsistent framework state.
- [`LogicException`](../../../../../Exception/LogicException.md)

***
### respondFromSaveResult

Normalizes a save() result into a REST response.

```php
protected respondFromSaveResult(array $ret): \Phalcon\Http\ResponseInterface
```

Rules enforced here:

Single entity:
- 200 OK → success
- 400 Bad Req → malformed input without validation/domain messages
- 422 Unprocessable → validation/domain failure with messages

Batch:
- 200 OK → all entities saved
- 207 Multi → mixed success / failure
- 422 Unprocessable → all entities failed

**Parameters:**

| Parameter | Type      | Description                                      |
|-----------|-----------|--------------------------------------------------|
| `$ret`    | **array** | Result returned by save(), create(), or update() |

***
### getSaveActionFailureStatusCode

Resolve the HTTP status code for a failed single-entity save.

```php
protected getSaveActionFailureStatusCode(array $ret): int
```

Model, validation, and domain-rule failures normally include messages and
map to 422 Unprocessable Entity. Framework-generated REST failures use
Phalcon message codes for request problems such as invalid create/update
intent, missing targets, forbidden operations, or conflicts; those
explicit 4xx codes are preserved so the action layer does not collapse
them into validation responses. 5xx responses should come from thrown
exceptions or explicit controller error handling, not model messages.

A failure without messages is treated as a malformed request because the
persistence layer could not provide a domain-specific reason for the
rejection.

**Parameters:**

| Parameter | Type      | Description                |
|-----------|-----------|----------------------------|
| `$ret`    | **array** | Single-entity save result. |

***
