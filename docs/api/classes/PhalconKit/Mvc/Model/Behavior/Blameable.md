
Blameable Behavior

Provides a complete audit trail system for models.

Responsibilities:
- Create a single audit entry per create/update operation (audit table)
- Optionally create per-column audit detail entries (audit_detail table)
- Support snapshot-based diffing for updates
- Support runtime and global enable/disable controls
- Prevent recursive auditing of audit tables themselves

Control layers (in order of precedence):
1. SkippableTrait                → disable the behavior entirely
2. Audit toggle                  → enable/disable parent audit rows
3. Audit detail toggle           → enable/disable per-column audit details

This design guarantees:
- Zero overhead when fully disabled
- Deterministic behavior across environments
- Safe runtime toggling (importers, migrations, hot paths)

***

* Full name: `\PhalconKit\Mvc\Model\Behavior\Blameable`
* Parent class: [`Behavior`](https://docs.phalcon.io/latest/api/){:target="_blank"}

## Properties

### parentId

Parent audit ID used to link cascaded/related model changes.

```php
protected static ?int $parentId
```

This is intentionally static to propagate across nested saves.

* This property is **static**.

***

### snapshot

Snapshot of model data before update.

```php
protected ?array $snapshot
```

Populated during beforeUpdate.

***

### changedFields

List of changed fields detected by Phalcon.

```php
protected ?array $changedFields
```

Used to filter unchanged columns on update.

***

### auditClass

Fully-qualified audit model class.

```php
protected string $auditClass
```

***

### auditDetailClass

Fully-qualified audit detail model class.

```php
protected string $auditDetailClass
```

***

### userClass

Fully-qualified user model class.

```php
protected string $userClass
```

***

### auditEnabled

Instance-level audit toggle (parent audit row).

```php
protected bool $auditEnabled
```

Subclasses can redeclare this property to change the default.

***

### auditStaticEnabled

Global audit toggle (parent audit row).

```php
protected static bool $auditStaticEnabled
```

* This property is **static**.

***

### auditDetailEnabled

Instance-level audit detail toggle (per-column rows).

```php
protected bool $auditDetailEnabled
```

Subclasses can redeclare this property to change the default.

***

### auditDetailStaticEnabled

Global audit detail toggle (per-column rows).

```php
protected static bool $auditDetailStaticEnabled
```

* This property is **static**.

***

## Methods

### __construct

Constructor

```php
public __construct(array $options = []): mixed
```

Accepts configuration options to control:
- Model classes
- Initial audit/audit-detail enablement

Audit is opt-in with `auditEnabled => true`. Audit detail remains enabled
by default once audit itself is enabled and can be disabled with
`auditDetailEnabled => false`. Explicit options override subclass
property defaults.

**Parameters:**

| Parameter  | Type      | Description |
|------------|-----------|-------------|
| `$options` | **array** |             |

***

### notify

Receives model lifecycle events.

```php
public notify(string $type, \Phalcon\Mvc\ModelInterface $model): ?bool
```

This method acts as the central gatekeeper and enforces
all enable/disable semantics before any work is done.

Returning null short-circuits the event handling cleanly.

**Parameters:**

| Parameter | Type                            | Description |
|-----------|---------------------------------|-------------|
| `$type`   | **string**                      |             |
| `$model`  | **\Phalcon\Mvc\ModelInterface** |             |

**Throws:**

When the behavior is attached to an incompatible
model instance.
- [`LogicException`](../../../Exception/LogicException.md)

***

### createAudit

Creates a parent audit entry and optional audit detail entries.

```php
public createAudit(string $type, \PhalconKit\Mvc\Model $model): bool
```

- Always creates a single audit row when enabled
- Conditionally creates per-column audit details
- Uses snapshot + changed fields to minimize noise

**Parameters:**

| Parameter | Type                      | Description |
|-----------|---------------------------|-------------|
| `$type`   | **string**                |             |
| `$model`  | **\PhalconKit\Mvc\Model** |             |

**Throws:**

When configured audit classes do not implement the
required audit contracts.
- [`LogicException`](../../../Exception/LogicException.md)

***

### requireBlameableModel

Require the event model to be a PhalconKit model.

```php
protected requireBlameableModel(\Phalcon\Mvc\ModelInterface $model): \PhalconKit\Mvc\Model
```

The audit behavior depends on PhalconKit model helpers such as metadata,
snapshots, attribute reads, and source resolution. This helper keeps the
event handler readable while producing a deterministic framework
exception if the behavior is attached to an incompatible native model.

**Parameters:**

| Parameter | Type                            | Description                               |
|-----------|---------------------------------|-------------------------------------------|
| `$model`  | **\Phalcon\Mvc\ModelInterface** | Model passed by Phalcon's behavior event. |

**Throws:**

When the model does not use PhalconKit's model
base class.
- [`LogicException`](../../../Exception/LogicException.md)

***

### requireAuditRecord

Require the configured audit class to implement the audit contract.

```php
protected requireAuditRecord(mixed $audit): \PhalconKit\Models\Interfaces\AuditInterface&\PhalconKit\Mvc\Model
```

Applications can override the audit model class through behavior options.
This guard reports an invalid override at the framework boundary instead
of failing later while populating audit metadata.

**Parameters:**

| Parameter | Type      | Description                                     |
|-----------|-----------|-------------------------------------------------|
| `$audit`  | **mixed** | Audit record created from the configured class. |

**Throws:**

When the configured audit class is incompatible.
- [`LogicException`](../../../Exception/LogicException.md)

***

### saveAuditRecord

Save the audit record unless audit storage is explicitly absent.

```php
protected saveAuditRecord(\PhalconKit\Models\Interfaces\AuditInterface&\PhalconKit\Mvc\Model $audit): bool
```

Missing audit tables are optional in some applications, so a concrete
`TableNotInDatabase` skips audit creation. The guard is intentionally at
the save boundary so fake/custom audit models that override persistence
still run normally.

**Parameters:**

| Parameter | Type                                                                   | Description |
|-----------|------------------------------------------------------------------------|-------------|
| `$audit`  | **\PhalconKit\Models\Interfaces\AuditInterface&\PhalconKit\Mvc\Model** |             |

***

### requireAuditDetailRecord

Require the configured audit-detail class to implement the detail contract.

```php
protected requireAuditDetailRecord(mixed $detail): \PhalconKit\Models\Interfaces\AuditDetailInterface&\PhalconKit\Mvc\Model
```

**Parameters:**

| Parameter | Type      | Description                                            |
|-----------|-----------|--------------------------------------------------------|
| `$detail` | **mixed** | Audit-detail record created from the configured
class. |

**Throws:**

When the configured audit-detail class is
incompatible.
- [`LogicException`](../../../Exception/LogicException.md)

***

### collectData

Collects snapshot and changed field data prior to update.

```php
protected collectData(\PhalconKit\Mvc\Model $model): bool
```

This method is intentionally lightweight and only runs
when snapshots are available.

**Parameters:**

| Parameter | Type                      | Description |
|-----------|---------------------------|-------------|
| `$model`  | **\PhalconKit\Mvc\Model** |             |

***

### normalizeValue

Normalize a scalar value according to its column type.

```php
protected normalizeValue(mixed $value, ?int $columnType): mixed
```

This method is intentionally conservative:
- null is preserved
- empty string is preserved
- only values belonging to the same semantic domain are collapsed

**Parameters:**

| Parameter     | Type      | Description |
|---------------|-----------|-------------|
| `$value`      | **mixed** |             |
| `$columnType` | **?int**  |             |

***

### normalizeJson

```php
protected normalizeJson(mixed $value): string
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$value`  | **mixed** |             |

***

### ksortRecursive

```php
protected ksortRecursive(array& $array): void
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$array`  | **array** |             |

***

### normalizeArray

Normalize a full row using model column metadata.

```php
protected normalizeArray(array $data, ?array $columnMap, array $columnTypes): array
```

Phalcon models can expose assigned relationships through `toArray()` and
snapshot data. Audit payloads are column snapshots, not response payloads,
so this method keeps only keys that map to real model columns before
normalizing scalar values by database type.

**Parameters:**

| Parameter      | Type       | Description |
|----------------|------------|-------------|
| `$data`        | **array**  |             |
| `$columnMap`   | **?array** |             |
| `$columnTypes` | **array**  |             |

***

### resolveAuditColumnName

Resolve one public/snapshot key to its database column name.

```php
protected resolveAuditColumnName(string|int $key, array<string,string>|null $columnMap, array<string,int> $columnTypes): ?string
```

With a non-empty column map, audit snapshots use mapped attribute names
while data types remain keyed by database column names. Without a map,
the key must already be a metadata column. Unknown keys are treated as
relation or transient payloads and are excluded from audit JSON.

**Parameters:**

| Parameter      | Type                           | Description                                                                       |
|----------------|--------------------------------|-----------------------------------------------------------------------------------|
| `$key`         | **string\|int**                |                                                                                   |
| `$columnMap`   | **array<string,string>\|null** | Database column to model
attribute map, or null when column renaming is disabled. |
| `$columnTypes` | **array<string,int>**          | Database column types from
Phalcon metadata.                                      |

***

### isAuditEnabled

Returns true if audit rows are enabled for this instance and globally.

```php
public isAuditEnabled(): bool
```

***

### enableAudit

Enable audit rows for this instance.

```php
public enableAudit(): void
```

***

### disableAudit

Disable audit rows for this instance.

```php
public disableAudit(): void
```

***

### staticEnableAudit

Enable audit rows globally.

```php
public static staticEnableAudit(): void
```

* This method is **static**.
***

### staticDisableAudit

Disable audit rows globally.

```php
public static staticDisableAudit(): void
```

* This method is **static**.
***

### isAuditDetailEnabled

Returns true if audit detail rows are enabled for this instance and globally.

```php
public isAuditDetailEnabled(): bool
```

***

### enableAuditDetail

Enable audit detail rows for this instance.

```php
public enableAuditDetail(): void
```

***

### disableAuditDetail

Disable audit detail rows for this instance.

```php
public disableAuditDetail(): void
```

***

### staticEnableAuditDetail

Enable audit detail rows globally.

```php
public static staticEnableAuditDetail(): void
```

* This method is **static**.
***

### staticDisableAuditDetail

Disable audit detail rows globally.

```php
public static staticDisableAuditDetail(): void
```

* This method is **static**.
***

## Inherited methods

### getEnabled

Return true if the behavior is enabled
on the current model instance

```php
public getEnabled(): bool
```

***

### setEnabled

Set true to enable the behavior
on the current model instance

```php
public setEnabled(bool $enabled): void
```

**Parameters:**

| Parameter  | Type     | Description |
|------------|----------|-------------|
| `$enabled` | **bool** |             |

***

### getStaticEnabled

Return true if the behavior is enabled
globally for every model instance

```php
public static getStaticEnabled(): bool
```

* This method is **static**.
***

### setStaticEnabled

Set true to enable the behavior
globally for every model instance

```php
public static setStaticEnabled(bool $staticEnabled): void
```

* This method is **static**.
**Parameters:**

| Parameter        | Type     | Description |
|------------------|----------|-------------|
| `$staticEnabled` | **bool** |             |

***

### enable

Enable the behavior
on the current model instance

```php
public enable(): void
```

***

### disable

Disable the behavior
on the current model instance

```php
public disable(): void
```

***

### staticEnable

Enable the behavior
globally for every model instance

```php
public static staticEnable(): void
```

* This method is **static**.
***

### staticDisable

Disable the behavior
globally for every model instance

```php
public static staticDisable(): void
```

* This method is **static**.
***

### isEnabled

Return true if the behavior is enabled
on the current model instance and globally

```php
public isEnabled(): bool
```

***

### isDisabled

Return true if the behavior is enabled
on the current model instance and globally

```php
public isDisabled(): bool
```

***
