
Search-based query condition provider.

PURPOSE
-------
This trait is responsible for producing SQL search conditions
based on a free-text `search` parameter and a declarative list
of searchable fields.

It does NOT:
 - Rank results
 - Perform relevance scoring
 - Apply database-specific full-text features

It ONLY:
 - Expands search terms into LIKE expressions
 - Applies strict AND / OR grouping semantics
 - Produces a compiler-safe condition payload

CONDITION CONTRACT
------------------
All conditions produced by this trait MUST follow this shape:

 [
     0 => string  SQL condition fragment (parenthesized),
     1 => array   bind values,
     2 => array   bind types,
 ]

Returning `null` ALWAYS means:
 → "No search restriction should be applied"

This invariant is relied upon by the query compiler.

***

* Full name: `\PhalconKit\Mvc\Controller\Traits\Query\Conditions\SearchConditions`

## Properties

### searchConditions

Registered search condition sets.

```php
protected ?\Phalcon\Support\Collection $searchConditions
```

This collection allows multiple named search strategies
to coexist (e.g. default, advanced, scoped, etc.).

Keys:
 - symbolic identifiers
Values:
 - condition payloads OR lazy builders

***

## Methods

### initializeSearchConditions

Initialize search conditions.

```php
public initializeSearchConditions(): void
```

Called during controller / query bootstrap.

The default search condition is eagerly built to ensure:
 - deterministic behavior
 - no hidden runtime branching

***
### setSearchConditions

Replace the entire search condition collection.

```php
public setSearchConditions(array|\Phalcon\Support\Collection|null $searchConditions): void
```

Used by consumers that want full control over
how search conditions are produced.

**Parameters:**

| Parameter           | Type                                         | Description |
|---------------------|----------------------------------------------|-------------|
| `$searchConditions` | **array\|\Phalcon\Support\Collection\|null** |             |

***
### getSearchConditions

Retrieve the registered search conditions.

```php
public getSearchConditions(): ?\Phalcon\Support\Collection
```

***
### buildDefaultSearchCondition

Build the default search condition.

```php
public buildDefaultSearchCondition(): array|null
```

SEMANTICS
---------
Given:
  search = "foo bar"
  fields = [title, description]

Resulting logic:

  (
    (title LIKE '%%foo%%' OR description LIKE '%%foo%%')
    AND
    (title LIKE '%%bar%%' OR description LIKE '%%bar%%')
  )

This ensures:
 - Every term MUST match at least one field
 - Multiple terms narrow results (AND)

***
### buildSearchTermGroup

Build an OR-group for a single search term.

```php
public buildSearchTermGroup(string $term, array $searchFields, array& $bind, array& $bindTypes): string[]
```

Each enabled searchable field produces:
  field LIKE '%%term%%'

Flattening is required because search fields may be
declared in nested / relational form.

**Parameters:**

| Parameter       | Type       | Description                 |
|-----------------|------------|-----------------------------|
| `$term`         | **string** |                             |
| `$searchFields` | **array**  |                             |
| `$bind`         | **array**  | Accumulator for bind values |
| `$bindTypes`    | **array**  | Accumulator for bind types  |

**Return Value:**

List of SQL expressions

***
### extractSearchTerms

Extract normalized search terms from request parameters.

```php
public extractSearchTerms(): list<string>
```

NORMALIZATION RULES
-------------------
 - Input is treated as free text
 - Whitespace is collapsed
 - Empty tokens are discarded
 - Duplicate terms are removed
 - Original order is preserved

This method is intentionally isolated so that
search tokenization can evolve independently
of SQL generation.

***
