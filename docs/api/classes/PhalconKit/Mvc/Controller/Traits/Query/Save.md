
REST persistence trait (controller-side).

Goals:
- Provide a stable `save()` entry point (single + batch)
- Optionally expose controller-mappable `create()` and `update()` helpers
- Enforce forced mode semantics (create must never update, update must never create)
- Keep identity resolution data-driven (row-scoped), not request/global-scoped

Contract:
- Single save: { saved: bool, messages: [], data?: mixed, mode?: 'create'|'update' }
- Batch save:  { saved: bool, messages: [], results: [], stats: } }

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Save`

## Methods

### create

Force CREATE semantics.

```php
public create(): array
```

- Never updates
- Fails if identity is present in payload

**Throws:**

When request payload filtering fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When persistence intent resolution returns an
inconsistent framework state.
- [`LogicException`](../../../../Exception/LogicException.md)

***
### update

Force UPDATE semantics.

```php
public update(): array
```

- Never creates
- Fails if identity is missing or does not resolve

**Throws:**

When request payload filtering fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When persistence intent resolution returns an
inconsistent framework state.
- [`LogicException`](../../../../Exception/LogicException.md)

***
### save

Generic save entry point.

```php
public save(?string $forceMode = null): array
```

Payload shapes:
- Single entity: associative array
- Batch: list of associative arrays

Mode:
- null      => auto (create if no identity, else update if identity resolves)
- 'create'  => force create (no identity allowed)
- 'update'  => force update (identity must resolve)

**Parameters:**

| Parameter    | Type        | Description |
|--------------|-------------|-------------|
| `$forceMode` | **?string** |             |

**Throws:**

When request payload filtering fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}
When persistence intent resolution returns an
inconsistent framework state.
- [`LogicException`](../../../../Exception/LogicException.md)

***
### saveMany

Saves many entities (best-effort).

```php
protected saveMany(array $rows, ?string $forceMode): array
```

Semantics:
- Continues on errors
- Returns per-row results + stats
- Root messages are summary-only (legacy compatibility)

**Parameters:**

| Parameter    | Type        | Description |
|--------------|-------------|-------------|
| `$rows`      | **array**   |             |
| `$forceMode` | **?string** |             |

***
### saveOne

Saves a single entity.

```php
protected saveOne(array $data, ?string $forceMode): array
```

Implementation is intentionally split into small, testable phases:
- resolvePersistenceIntent(): mode + model selection (create/update)
- assignModelFromPayload(): assignment + beforeAssign event
- persistAssignedModel(): save + events + eager loading + expose

**Parameters:**

| Parameter    | Type        | Description |
|--------------|-------------|-------------|
| `$data`      | **array**   |             |
| `$forceMode` | **?string** |             |

**Throws:**

When intent resolution returns no model or an
unsupported persistence mode after reporting no failure.
- [`LogicException`](../../../../Exception/LogicException.md)

***
### requireResolvedPersistenceIntent

Require a successful persistence-intent tuple.

```php
protected requireResolvedPersistenceIntent(string|null $mode, \Phalcon\Mvc\ModelInterface|null $model): array{0: "create"|"update", 1: \Phalcon\Mvc\ModelInterface}
```

`resolvePersistenceIntent()` returns either a REST failure payload or the
internal tuple needed by the rest of the save pipeline. This helper keeps
the orchestration path readable and documents the invariant explicitly:
once no failure was returned, a model instance and one of the two
supported persistence modes must be present.

**Parameters:**

| Parameter | Type                                  | Description                |
|-----------|---------------------------------------|----------------------------|
| `$mode`   | **string\|null**                      | Resolved persistence mode. |
| `$model`  | **\Phalcon\Mvc\ModelInterface\|null** | Resolved target model.     |

**Throws:**

When intent resolution returns no model or an
unsupported persistence mode after reporting no failure.
- [`LogicException`](../../../../Exception/LogicException.md)

***
### resolvePersistenceIntent

Resolves:
- the effective mode ('create'\|'update')
- the target model instance

```php
protected resolvePersistenceIntent(array $data, ?string $forceMode): array
```

Forced mode invariants:
- force 'create': must NOT update; identity is forbidden
- force 'update': must NOT create; identity must resolve to an entity

Returns a 3-tuple: [$mode, $model|null, $failure|null]

**Parameters:**

| Parameter    | Type        | Description |
|--------------|-------------|-------------|
| `$data`      | **array**   |             |
| `$forceMode` | **?string** |             |

***
### findModelByIdentityPayload

Finds an entity using identity extracted from the provided payload.

```php
protected findModelByIdentityPayload(array $payload): ?\Phalcon\Mvc\ModelInterface
```

This is intentionally payload-driven, so batch operations do not rely on controller/global params.

Notes:
- Uses buildIdentityConditionFromData($data) (from IdentityConditions refactor)
- Temporarily overrides the "default" identity condition used by findFirst()
- Restores the previous value afterward to prevent leakage across batch rows

**Parameters:**

| Parameter  | Type      | Description |
|------------|-----------|-------------|
| `$payload` | **array** |             |

***
### assignModelFromPayload

Assigns payload to the model using saveFields/mapFields rules.

```php
protected assignModelFromPayload(\Phalcon\Mvc\ModelInterface $model, array& $data): void
```

- Strips identity fields before assign to prevent accidental PK changes
- Fires rest:beforeAssign with references allowing upstream mutation

**Parameters:**

| Parameter | Type                            | Description |
|-----------|---------------------------------|-------------|
| `$model`  | **\Phalcon\Mvc\ModelInterface** |             |
| `$data`   | **array**                       |             |

***
### persistAssignedModel

Saves the model and returns a canonical REST payload.

```php
protected persistAssignedModel(\Phalcon\Mvc\ModelInterface $model, string $mode): array
```

- Fires rest:beforeSave (may return false to abort)
- Saves model
- Fires rest:afterSave
- Optionally eager-loads relations
- Exposes model

**Parameters:**

| Parameter | Type                            | Description |
|-----------|---------------------------------|-------------|
| `$model`  | **\Phalcon\Mvc\ModelInterface** |             |
| `$mode`   | **string**                      |             |

***
### buildRestSaveFailure

Builds a canonical failure payload for save operations.

```php
protected buildRestSaveFailure(string $message, string $type, int $code, string|array|null $field = null): array
```

Naming is intentionally REST/save-specific (not generic "error") because:
- This trait is used by REST controllers
- The returned shape is part of the REST contract

**Parameters:**

| Parameter  | Type                    | Description                             |
|------------|-------------------------|-----------------------------------------|
| `$message` | **string**              | Human message                           |
| `$type`    | **string**              | Machine-ish type (Phalcon message type) |
| `$code`    | **int**                 | HTTP-ish code (used by action layer)    |
| `$field`   | **string\|array\|null** | Optional field(s) (e.g., PK attributes) |

***
### hasPrimaryKey

Detects whether payload contains identity.

```php
protected hasPrimaryKey(array $data): bool
```

Override when you add:
- composite primary keys
- dynamic key names per model

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$data`   | **array** |             |

***
### stripPrimaryKey

Removes identity fields from the payload so they cannot be mass-assigned.

```php
protected stripPrimaryKey(array& $data): void
```

Override if identity keys differ.

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$data`   | **array** |             |

***
