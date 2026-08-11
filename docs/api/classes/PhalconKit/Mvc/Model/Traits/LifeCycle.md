
Provides static query helpers for data-retention lifecycle tasks.

Lifecycle policies are read from `dataLifeCycle.models` and
`dataLifeCycle.policies` in the default PhalconKit config service. The trait
is static because CLI retention tasks call model classes directly when
building delete/obfuscation queries.

Long term, this may belong in a lifecycle-aware model manager. Keeping it as
a trait avoids changing the static API used by existing CLI retention tasks.

***

* Full name: `\PhalconKit\Mvc\Model\Traits\LifeCycle`

## Methods

### prepareLifeCycleQuery

Apply safety defaults to a lifecycle query builder.

```php
public static prepareLifeCycleQuery(\Phalcon\Mvc\Model\Query\BuilderInterface $builder, array<string,mixed>|null $parameters = null): void
```

A model with no resolved policy query should never accidentally match all
records. When parameters are empty, the builder receives a `false`
condition and empty bind arrays so the resulting query is intentionally
empty.

* This method is **static**.
**Parameters:**

| Parameter     | Type                                          | Description                                                             |
|---------------|-----------------------------------------------|-------------------------------------------------------------------------|
| `$builder`    | **\Phalcon\Mvc\Model\Query\BuilderInterface** | Builder that will be executed by the
lifecycle task.                    |
| `$parameters` | **array<string,mixed>\|null**                 | Policy query parameters
resolved from config or supplied by the caller. |

***
### getLifeCyclePolicy

Return the lifecycle policy configured for the current model class.

```php
public static getLifeCyclePolicy(): array<string,mixed>
```

The config maps model class names to policy names under
`dataLifeCycle.models`; the policy payload is then read from
`dataLifeCycle.policies`. Missing mappings return an empty policy.

* This method is **static**.
**Return Value:**

Policy payload for the calling model class.

**Throws:**

When the default DI or config service cannot be
resolved through the PhalconKit DI contract.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
### getLifeCyclePolicyQuery

Return only the lifecycle query portion of the configured policy.

```php
public static getLifeCyclePolicyQuery(): array<string,mixed>|null
```

* This method is **static**.
**Return Value:**

Query definition accepted by Phalcon's
model query builder, or null when no policy query is configured.

**Throws:**

When the lifecycle policy cannot be resolved.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
### getLifeCycleQuery

Build the executable lifecycle query for the current model class.

```php
public static getLifeCycleQuery(array<string,mixed>|null $parameters = null, \Phalcon\Mvc\Model\Query\BuilderInterface|null $builder = null): \Phalcon\Mvc\Model\QueryInterface
```

Callers may pass explicit query parameters or a preconfigured builder for
tests and custom lifecycle workflows. When both are omitted, the
configured policy query is used.

* This method is **static**.
**Parameters:**

| Parameter     | Type                                                | Description                |
|---------------|-----------------------------------------------------|----------------------------|
| `$parameters` | **array<string,mixed>\|null**                       | Query parameters to apply. |
| `$builder`    | **\Phalcon\Mvc\Model\Query\BuilderInterface\|null** | Optional builder override. |

**Return Value:**

Executable query for lifecycle processing.

**Throws:**

When the default DI or models manager service
cannot be resolved through the PhalconKit DI contract.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
### getBuilder

Create a lifecycle query builder for the current model class.

```php
public static getBuilder(array<string,mixed>|null $parameters = null): \Phalcon\Mvc\Model\Query\BuilderInterface
```

The builder is initialized from the provided parameters and forced to use
the calling model class as its `from` model. A top-level `limit` parameter
is applied explicitly because Phalcon's builder parameters do not always
preserve that value when lifecycle tasks construct custom arrays.

* This method is **static**.
**Parameters:**

| Parameter     | Type                          | Description               |
|---------------|-------------------------------|---------------------------|
| `$parameters` | **array<string,mixed>\|null** | Query-builder parameters. |

**Return Value:**

Builder scoped to the calling model class.

**Throws:**

When the default DI or models manager service
cannot be resolved through the PhalconKit DI contract.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
### findLifeCycle

Execute the lifecycle query and return matching records.

```php
public static findLifeCycle(array<string,mixed>|null $parameters = null): mixed
```

If a resultset is returned and the policy parameters include a
`hydration` value, the resultset hydrate mode is updated before returning
it to the caller. Non-resultset query outputs are returned untouched to
preserve native Phalcon behavior.

* This method is **static**.
**Parameters:**

| Parameter     | Type                          | Description                                                  |
|---------------|-------------------------------|--------------------------------------------------------------|
| `$parameters` | **array<string,mixed>\|null** | Query parameters or null to
use the configured policy query. |

**Return Value:**

Query execution result, usually a Phalcon model resultset.

**Throws:**

When the lifecycle query cannot be built because
required DI services are unavailable or incompatible.
- [`ServiceException`](../../../Exception/ServiceException.md)

***
