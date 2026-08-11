
Abstract contract for identity-based query conditions.

Identity conditions are responsible for constraining queries
based on explicit identity data (typically primary keys or
model-defined identity columns).

IDENTITY CONDITION CONTRACT
---------------------------
All identity condition builders MUST return:

 - null        → no identity constraint applied
 - array       → [sql, bindValues, bindTypes]

Returning any other shape is invalid and may break
the query compiler.

IMPORTANT
---------
Identity conditions:
 - Are NOT authorization rules
 - Are NOT implicit
 - Are NOT required to exist

Consumers decide how absence of identity affects semantics.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Abstracts\Query\Conditions\AbstractIdentityConditions`

## Methods

### initializeIdentityConditions

Initialize identity conditions.

```php
public initializeIdentityConditions(): void
```

Called during controller / query bootstrap.

* This method is **abstract**.
***
### setIdentityConditions

Replace the identity condition collection.

```php
public setIdentityConditions(array|\Phalcon\Support\Collection|null $identityConditions): void
```

Allows higher-level components to override
identity semantics entirely.

* This method is **abstract**.
**Parameters:**

| Parameter             | Type                                         | Description |
|-----------------------|----------------------------------------------|-------------|
| `$identityConditions` | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getIdentityConditions

Retrieve the registered identity conditions.

```php
public getIdentityConditions(): ?\Phalcon\Support\Collection
```

* This method is **abstract**.
***
### defaultIdentityCondition

Build the default identity condition.

```php
public defaultIdentityCondition(): array|string|null
```

This method is expected to:
- Pull identity data from request / parameters
- Apply identity column constraints
- Return a compiler-safe payload

* This method is **abstract**.
**Return Value:**

Identity condition payload or null if none applies

***
### buildIdentityConditionFromData

Build an identity condition from arbitrary data.

```php
public buildIdentityConditionFromData(array $data, array|null $columns = null): array|null
```

Implementations MUST:
 - Ignore missing or null values
 - Generate bind-safe equality predicates
 - AND-coalesce all applicable predicates

Failure modes MUST be silent:
 - No identity columns → null
 - No usable data      → null

* This method is **abstract**.
**Parameters:**

| Parameter  | Type            | Description                        |
|------------|-----------------|------------------------------------|
| `$data`    | **array**       | Input data (e.g. request params)   |
| `$columns` | **array\|null** | Optional explicit identity columns |

**Return Value:**

Identity condition payload

***
### getIdentityColumns

Return the identity columns for the current model.

```php
public getIdentityColumns(): array
```

Default implementations usually return:
 - Primary key attributes

Override for:
 - Composite identity models
 - Natural-key identity semantics

* This method is **abstract**.
***
