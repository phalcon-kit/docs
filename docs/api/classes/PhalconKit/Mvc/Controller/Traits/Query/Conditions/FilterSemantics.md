
***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Conditions\FilterSemantics`

## Methods

### normalizeFilterOperator

Normalize, validate, and canonicalize a filter operator.

```php
public normalizeFilterOperator(string $operator): string
```

This method is the **single normalization boundary** between:
 - untrusted / legacy / frontend-provided operators
 - strict, deterministic, internal query compilation

Design principles:
 - Be tolerant ONLY here
 - Be strict everywhere else
 - Never guess intent
 - Never allow ambiguous mappings

Operator lifecycle:
 1. Frontend sends arbitrary human-readable operator
 2. This method normalizes it into a canonical form
 3. Compiler (compileSingleFilterCondition) assumes correctness

Categories:
 - Native SQL operators        → passed through
 - Extended semantic operators → rewritten later by compiler
 - Unknown / ambiguous         → rejected

**Parameters:**

| Parameter   | Type       | Description                                |
|-------------|------------|--------------------------------------------|
| `$operator` | **string** | Raw operator provided by client / frontend |

**Return Value:**

Canonical operator, or empty string if unsupported

***
### isNegativeOperator

Determines whether an operator represents a syntactic negation.

```php
protected isNegativeOperator(string $operator): bool
```

IMPORTANT:
- This is NOT a semantic classifier
- This MUST NOT be used for EXISTS / NOT EXISTS decisions
- Intended usage: local grouping glue (AND vs OR)

**Parameters:**

| Parameter   | Type       | Description               |
|-------------|------------|---------------------------|
| `$operator` | **string** | The operator to evaluate. |

**Return Value:**

Returns true if the operator is a negative operator, false otherwise.

***
### isTextOperator

Determines whether the given operator represents a **textual pattern predicate**.

```php
protected isTextOperator(string $operator): bool
```

A "text operator" is defined as an operator that:
 - operates on string patterns (LIKE / REGEXP semantics)
 - is NOT atomic over 1-N relations (i.e. cannot be reasoned per joined row)
 - therefore may require existential semantics (EXISTS / NOT EXISTS)
   to preserve correctness when filtering parent entities

This classification is **domain-based**, NOT polarity-based.
It answers WHAT kind of predicate this is — not whether it is negated.

Why this distinction matters:
 - Text predicates can produce false positives / false negatives
   when evaluated inline on LEFT JOINs
 - Scalar predicates (=, !=, IN, etc.) do not suffer from this problem
 - Unary predicates (IS NULL, IS EMPTY, etc.) are row-local and must stay inline

Examples (text operators):
 - contains
 - does not contain
 - starts with
 - does not start with
 - ends with
 - does not end with
 - contains word
 - does not contain word
 - regexp
 - not regexp

Non-examples (NOT text operators):
 - =, !=, <>, IN, NOT IN        (scalar comparisons)
 - is null, is empty, is true  (unary / semantic operators)
 - between                     (range predicate)

Design rules:
 - Caller MUST pass a canonical operator (output of getFilterOperator)
 - This method MUST be deterministic
 - This method MUST NOT infer semantics via substrings
 - This method MUST NOT consider polarity

**Parameters:**

| Parameter   | Type       | Description                             |
|-------------|------------|-----------------------------------------|
| `$operator` | **string** | Canonical operator (already normalized) |

**Return Value:**

True if operator is a textual pattern predicate

***
### isNegativeTextOperator

Determines whether the given operator represents a **negative textual predicate**.

```php
protected isNegativeTextOperator(string $operator): bool
```

A "negative text operator" is defined as:
 - a textual pattern predicate (see isTextOperator)
 - that expresses the *absence* of a pattern rather than its presence

This distinction is CRITICAL for correctness:
 - SQL semantics: `NULL NOT LIKE '%%x%%'` evaluates to NULL (filtered out)
 - Expected semantics: parent rows with NO related child rows
   must still be INCLUDED

Therefore:
 - Inline evaluation of negative text predicates on LEFT JOINs
   is NOT logically equivalent to the intended filter
 - Such predicates often require NOT EXISTS rewrites

Examples (negative text operators):
 - does not contain
 - does not start with
 - does not end with
 - does not contain word
 - not regexp

Non-examples (MUST return false):
 - !=, <>                  (scalar negation, not textual)
 - not in                  (set negation, handled differently)
 - is not null             (explicit NULL semantics already encoded)
 - is not empty            (unary semantic operator)

Design rules:
 - Caller MUST pass a canonical operator (getFilterOperator output)
 - This method MUST be deterministic
 - This method MUST NOT guess negativity via substring checks alone
 - This method MUST NOT classify non-text operators

**Parameters:**

| Parameter   | Type       | Description                             |
|-------------|------------|-----------------------------------------|
| `$operator` | **string** | Canonical operator (already normalized) |

**Return Value:**

True if operator is a negative textual predicate

***
### isNoValueOperator

Determines if the given operator is a "no-value" operator.

```php
protected isNoValueOperator(string $operator, bool $raw = true, bool $extended = true): bool
```

A "no-value" operator does not require an accompanying value for evaluation.
This method supports both raw and extended operator sets based on the provided flags.

**Parameters:**

| Parameter   | Type       | Description                                                                                           |
|-------------|------------|-------------------------------------------------------------------------------------------------------|
| `$operator` | **string** | The operator to be checked, which can include phrases
like 'is null', 'is true', 'is empty', etc.     |
| `$raw`      | **bool**   | Indicates whether to consider raw operators (e.g., 'is null', 'is true').
Defaults to true.           |
| `$extended` | **bool**   | Indicates whether to include extended operators (e.g., 'is empty', 'is not empty').
Defaults to true. |

**Return Value:**

Returns true if the operator is a recognized "no-value" operator based on
the provided flags; otherwise, returns false.

***
### isFilterAllowed

Determines if a given field is allowed to be used as a filter.

```php
public isFilterAllowed(string $field, array|null $allowedFilters): bool
```

This method verifies whether the field is explicitly allowed,
matches dynamic join criteria, or is configured within the allowed filters.

**Parameters:**

| Parameter         | Type            | Description                                                                                                                                       |
|-------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| `$field`          | **string**      | The field to be checked for filter permission.                                                                                                    |
| `$allowedFilters` | **array\|null** | An array of explicitly allowed filters
or filter configurations. Null preserves legacy unrestricted
filtering; an empty array denies every field. |

**Return Value:**

Returns true if the field is allowed to be used as a filter,
otherwise false.

***
### isJoinFilterAllowed

Determines if a join filter is allowed based on the given field and a list of allowed filters.

```php
public isJoinFilterAllowed(string $field, array|null $allowedFilters): bool
```

This method checks the provided field against the allowed filters, optionally
normalizing the field by removing segments wrapped in square brackets.
Associative map entries use the same boolean-like enabled semantics as
other REST collection policies, so config values such as "off", "false",
and "0" disable the key instead of being treated as truthy PHP strings.

**Parameters:**

| Parameter         | Type            | Description                                                                                                                     |
|-------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------|
| `$field`          | **string**      | The field to be checked, potentially including syntax for joins
or relationships (e.g., dot notation or square bracket syntax). |
| `$allowedFilters` | **array\|null** | An array of allowed filters to validate against. Can be null.                                                                   |

**Return Value:**

True if the field is allowed based on the provided filters, false otherwise.

***
