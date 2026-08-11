
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Conditions\FilterConditions`

## Properties

### filterConditions

```php
protected ?\Phalcon\Support\Collection $filterConditions
```

***

## Methods

### initializeFilterConditions

Initializes the filter conditions for the current instance.

```php
public initializeFilterConditions(): void
```

This method sets up the default filter conditions using a predefined collection
and ensures they are properly configured for subsequent operations.

**Return Value:**

This method does not return any value.

**Throws:**

- [`HttpException`](../../../../../Exception/HttpException.md)

***
### setFilterConditions

Sets the filter conditions used for configuring specific query or data processing criteria.

```php
public setFilterConditions(array|\Phalcon\Support\Collection|null $filterConditions): void
```

**Parameters:**

| Parameter           | Type                                         | Description                                                                                |
|---------------------|----------------------------------------------|--------------------------------------------------------------------------------------------|
| `$filterConditions` | **array\|\Phalcon\Support\Collection\|null** | A collection of filter conditions to be applied.
Can be null to clear existing conditions. |

***
### getFilterConditions

Retrieves the collection of filter conditions applied to the current context.

```php
public getFilterConditions(): \Phalcon\Support\Collection|null
```

If no filter conditions are set, this method returns null.

**Return Value:**

The collection of filter conditions, or null if no conditions are set.

***
### defaultFilterCondition

Constructs a SQL filter condition based on the provided filters and allowed fields.

```php
public defaultFilterCondition(array|null $filters = null, array|null $allowedFilters = null, ?string $aliasContext = null, bool $or = false, int $level = 0): array|string|null
```

Supports nested group filters, validation of fields and operators, and handles
both normal and foreign filters, including subqueries and negative operators.

 Responsibilities (and ONLY these):
  - Retrieve and validate raw filters
  - Prepare allowed filter fields
  - Delegate boolean semantics entirely to compileGroup()
  - Return legacy-shaped output

 Explicitly NOT responsible for:
  - Boolean glue decisions
  - Prefix vs infix logic
  - Group normalization
  - Operator semantics

**Parameters:**

| Parameter         | Type            | Description                                                                                                                                                                           |
|-------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$filters`        | **array\|null** | An optional array of filter conditions to apply.
Each filter should include keys like 'field', 'operator',
and optionally 'value' or 'subquery'. Nested groups can
also be specified. |
| `$allowedFilters` | **array\|null** | Optional allowed filter fields for
validation. Null preserves legacy unrestricted filtering; an empty
array denies every field.                                                       |
| `$aliasContext`   | **?string**     | Optional alias context for join-based filters                                                                                                                                         |
| `$or`             | **bool**        | A flag indicating whether the filters should be combined using OR
(true) or AND (false) logic. Defaults to false.                                                                     |
| `$level`          | **int**         |                                                                                                                                                                                       |

**Return Value:**

The constructed SQL filter condition. Returns:
- An array containing the SQL string, binding values, and binding types.
- A string representation of the SQL condition if no bindings are necessary.
- Null if no valid filters are provided.

**Throws:**

If a required property like 'field' or 'operator' is missing,
or if an unauthorized filter field or unsupported operator is used.
- [`HttpException`](../../../../../Exception/HttpException.md)

***
### compileGroup

Compile a group of filters into legacy-compatible SQL.

```php
protected compileGroup(array $filters, bool $or, int $level, array|null $allowedFilters, ?string $aliasContext = null): array|null
```

This is the compiler’s boolean / structural spine.

Responsibilities (and ONLY these):
 - Walk the filter AST (arrays + field nodes)
 - Resolve legacy prefix tokens ("and|or|xor")
 - Enforce boolean boundaries (OR/XOR, group nesting)
 - Route each node to either:
     - SELF / INLINE compilation (self, row-local)
     - EXISTENTIAL compilation (EXISTS / NOT EXISTS)
 - Perform AND-sibling existential coalescing (bucket accumulation)
 - Emit legacy-shaped SQL with exactly-one normalization at group exit

Non-responsibilities:
 - Operator normalization (handled by normalizeFilterOperator)
 - Join creation policy (handled by caller / DynamicJoins gate)
 - Existential join building (handled by buildExistsConditionFromField)

Semantic invariants enforced here:
 - OR/XOR always terminates existential accumulation (flush boundary)
 - Group entry/exit always terminates existential accumulation
 - Existential inner predicates are compiled with POSITIVE operators only
 - NOT EXISTS is the ONLY allowed negation mechanism for existential text predicates

**Parameters:**

| Parameter         | Type            | Description                                                                                             |
|-------------------|-----------------|---------------------------------------------------------------------------------------------------------|
| `$filters`        | **array**       | Group payload                                                                                           |
| `$or`             | **bool**        | Current alternation mode (flipped per nesting)                                                          |
| `$level`          | **int**         | Recursion depth (0 = root)                                                                              |
| `$allowedFilters` | **array\|null** | Allowed filter fields. Null preserves
legacy unrestricted filtering; an empty array denies every field. |
| `$aliasContext`   | **?string**     | Optional alias context                                                                                  |

**Return Value:**

['sql'=>string,'bind'=>array,'bindTypes'=>array]

**Throws:**

When a requested filter cannot be processed.
- [`HttpException`](../../../../../Exception/HttpException.md)
When filter configuration is invalid.
- [`LogicException`](../../../../../Exception/LogicException.md)

***
### compileSingleFilterCondition

Compiles a single filter condition into a SQL expression, including bind parameters and bind types.

```php
protected compileSingleFilterCondition(string $fieldBinder, string $operator, array $filter, \Closure $getValue, string $mode = 'self'): array
```

- SQL string (no surrounding AND/OR, caller controls)
- bind array
- bindTypes array

For negative-subquery use, caller passes the *positive* operator.

Responsibilities:
 - Translate **canonical operators** (output of normalizeFilterOperator) into SQL
 - Preserve legacy semantics (especially negative text operators on LEFT JOINs)
 - Remain deterministic and side-effect free

IMPORTANT INVARIANTS:
 - Operator is already normalized and validated
 - Field binder already contains the correct model / join alias
 - This method MUST NOT guess intent

**Parameters:**

| Parameter      | Type         | Description                                                                           |
|----------------|--------------|---------------------------------------------------------------------------------------|
| `$fieldBinder` | **string**   | The field or column placeholder used in the SQL condition.                            |
| `$operator`    | **string**   | The operator to be used in the condition (e.g., '=', 'between', 'in', 'like').        |
| `$filter`      | **array**    | Contains the filtering criteria, including the value(s) to be used for the condition. |
| `$getValue`    | **\Closure** | A closure that generates unique parameter names for binding values in the query.      |
| `$mode`        | **string**   | The semantic scope of the filter condition. Can be 'self' or 'existential'.           |

**Return Value:**

An array containing three elements:
- string The compiled SQL condition as a string.
- array Associative array of bind parameters for the query, with parameter names as keys.
- array Associative array of bind types for each parameter.

***
### getExistentialUniverseField

Reduce a relationship field to its existential "universe":
 - keep relationship chain
 - drop the leaf column
 - keep explicit alias tokens (e.g. [a]) because they denote distinct instances

```php
protected getExistentialUniverseField(string $originalField): string
```

Examples:
- Comment[a].content            => Comment[a]
- RecordUserStatus[c].userId    => RecordUserStatus[c]
- RecordTag[18_a].Tag.label     => RecordTag[18_a].Tag

**Parameters:**

| Parameter        | Type       | Description |
|------------------|------------|-------------|
| `$originalField` | **string** |             |

***
### assembleLegacyGroupSql

Assemble and normalize a group using the legacy prefix-token model.

```php
protected assembleLegacyGroupSql(string[] $fragments, int $level): string
```

**Parameters:**

| Parameter    | Type         | Description                                                                                          |
|--------------|--------------|------------------------------------------------------------------------------------------------------|
| `$fragments` | **string[]** | Each fragment is already prefixed with "and\|or\|xor"
OR is a nested group's already-normalized SQL. |
| `$level`     | **int**      | Recursion depth (0 = root).                                                                          |

***
### optimizeOperatorAndValue

Optimizes operator / value pairs based on value semantics.

```php
protected optimizeOperatorAndValue(string $operator, mixed $value): array{string, mixed}
```

This method performs **safe semantic rewrites** where intent
is unambiguous and SQL correctness would otherwise be violated.

Examples:
 - contains + int      → =
 - contains + int[]    → in
 - does not contain + int   → !=
 - does not contain + int[] → not in

IMPORTANT:
 - This method MUST be side-effect free
 - It MUST NOT guess intent
 - It MUST preserve meaning for strings

**Parameters:**

| Parameter   | Type       | Description                             |
|-------------|------------|-----------------------------------------|
| `$operator` | **string** | Canonical operator (already normalized) |
| `$value`    | **mixed**  | Raw filter value                        |

**Return Value:**

Optimized operator and value

***
### buildExistsConditionFromField

Build a correlated EXISTS / NOT EXISTS subquery condition from a relationship field.

```php
protected buildExistsConditionFromField(string $field, string $condition, bool $negated = false): array{conditions: string, bind: array, bindTypes: array}
```

This method is a PURE SQL emitter:
 - it does NOT decide semantics
 - it does NOT infer polarity
 - it only materializes an existential path

Polarity (EXISTS vs NOT EXISTS) is controlled explicitly by the caller.

Assumptions:
 - getJoinsDefinitionFromField() returns joins ordered deepest → shallowest
 - joins may contain payload blocks (new join format)
 - $condition already references join aliases, not the root model

**Parameters:**

| Parameter    | Type       | Description                                  |
|--------------|------------|----------------------------------------------|
| `$field`     | **string** | Relationship field used to resolve joins     |
| `$condition` | **string** | Predicate applied inside the subquery        |
| `$negated`   | **bool**   | Whether to emit NOT EXISTS instead of EXISTS |

**Throws:**

- [`HttpException`](../../../../../Exception/HttpException.md)

***
### getFilterScope

Determines the semantic scope of a filter.

```php
protected getFilterScope(array $filter, string|null $aliasContext): string
```

Scope is a FIRST-CLASS semantic decision.
It MUST be resolved BEFORE any SQL is generated.

There are only two valid scopes:

 - "self"
     Predicate is row-local to the root model.
     Safe for inline SQL.

 - "existential"
     Predicate quantifies over related rows.
     MUST be expressed via EXISTS / NOT EXISTS.

This method is the SINGLE SOURCE OF TRUTH for that decision.

Hard rules (ANY => existential):
 ------------------------------------------------------------
 1. Field contains an explicit relationship alias
      Example: RecordUserStatus[a].userId

 2. Field is foreign (contains ".") AND operator is textual
      Text predicates on 1-N relations are never row-local.

 3. Filter explicitly requests subquery semantics
      (legacy / backward compatibility)

What this method MUST NOT do:
 - Guess intent
 - Inspect joins
 - Inspect SQL mode
 - Inspect grouping context

**Parameters:**

| Parameter       | Type             | Description                                |
|-----------------|------------------|--------------------------------------------|
| `$filter`       | **array**        | Raw filter payload                         |
| `$aliasContext` | **string\|null** | Current alias universe (null = root model) |

**Return Value:**

Either "self" or "existential"

**Throws:**

If scope cannot be determined deterministically
- [`LogicException`](../../../../../Exception/LogicException.md)

***
### resolveGroupCarrierLogic

Determine the effective logic token of a group node.

```php
protected resolveGroupCarrierLogic(array $group): ?string
```

Legacy rule:
- If the first concrete field inside the group has an explicit "logic",
  that logic applies to the group as a whole.
- Otherwise, the group has no intrinsic logic.

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$group`  | **array** |             |

***
### resolveFilterLogicToken

Resolve the logical token ("and" \| "or" \| "xor") that prefixes the current fragment.

```php
protected resolveFilterLogicToken(array $node, int $index, bool $or): string
```

IMPORTANT CORRECTION:
 - At ROOT level (level=0), the fallback logic for index 0 MUST be "and".
   This prevents the compiler from generating:
       (primary constraints) OR (rest...)
   which collapses the filter set to “all rows matching the first constraint”.

Legacy behavior preserved:
 - Explicit payload "logic" always wins.
 - Nested alternation ($or toggling) remains unchanged for index >= 1
   and for non-root groups.

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$node`   | **array** |             |
| `$index`  | **int**   |             |
| `$or`     | **bool**  |             |

***
### getBindTypeFromRawValue

Retrieves the bind type based on the raw value.

```php
public getBindTypeFromRawValue(mixed|null $rawValue = null): int
```

**Parameters:**

| Parameter   | Type            | Description                                   |
|-------------|-----------------|-----------------------------------------------|
| `$rawValue` | **mixed\|null** | The raw value to determine the bind type for. |

**Return Value:**

The bind type based on the raw value. Possible values are:
- Column::BIND_PARAM_STR: If the raw value is a string or an array.
- Column::BIND_PARAM_INT: If the raw value is an integer.
- Column::BIND_PARAM_BOOL: If the raw value is a boolean.
- Column::BIND_PARAM_DECIMAL: If the raw value is a float or a double.
- Column::BIND_PARAM_NULL: If the raw value is null or its type is not recognized.

***
### toPositiveOperator

Convert a canonical NEGATIVE operator into its POSITIVE equivalent.

```php
protected toPositiveOperator(string $operator): string
```

This method is used EXCLUSIVELY for existential compilation.

CONTRACT:
 - Input MUST be a canonical operator (normalizeFilterOperator output)
 - Input MUST represent a negative semantic operator
 - Output MUST be the positive equivalent

This method MUST NOT:
 - guess intent
 - rewrite non-negative operators
 - accept unknown operators

**Parameters:**

| Parameter   | Type       | Description |
|-------------|------------|-------------|
| `$operator` | **string** |             |

**Throws:**

if operator cannot be safely converted
- [`LogicException`](../../../../../Exception/LogicException.md)

***
### splitField

Returns:
  - originalField: user-provided field (trimmed)
  - joinName:      portion before last dot, or null
  - fieldName:     portion after last dot (or whole)
  - joinAlias:     mapped alias (dynamicJoinsMapping), or joinName

```php
protected splitField(string $field): array{0: string, 1: string|null, 2: string, 3: string|null}
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$field`  | **string** |             |

***
### hasFiltersFieldsParams

Check whether the current request filters contain one or more of the specified fields.

```php
public hasFiltersFieldsParams(array|string|null $fields = null, bool $or = false): bool
```

Supports nested AND/OR logic - each nested array inverts the operator.

Examples:
  hasFiltersParams('status')                      // checks if "status" filter exists
  hasFiltersParams(['status', 'type'], true)      // "status" OR "type"
  hasFiltersParams(['status', 'type'])            // "status" AND "type"
  hasFiltersParams([['status', 'type']])          // "status" OR "type"
  hasFiltersParams([[['status', 'type']]])        // "status" AND "type"

**Parameters:**

| Parameter | Type                    | Description                                                                 |
|-----------|-------------------------|-----------------------------------------------------------------------------|
| `$fields` | **array\|string\|null** | List of fields to check against. If null, checks if "filters" param exists. |
| `$or`     | **bool**                | If true, matches at least one (OR). If false, matches all (AND).            |

**Return Value:**

True if the filters satisfy the condition, false otherwise.

**Throws:**

When request parameter filtering fails.
- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***
