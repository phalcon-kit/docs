
Remove selected keys from an array at every nesting level.

The function mutates the provided array in place and returns the number of
entries removed. Numeric indexes are not reindexed after removal, matching
PHP's normal `unset()` behavior. Use `$strict = false` only when string and
integer key equivalence is explicitly desired.

***

* Full name: `array_unset_recursive`
* Defined in: `src/Functions/Array.php`

## Parameters

| Parameter  | Type                       | Description                                                |
|------------|----------------------------|------------------------------------------------------------|
| `$array`   | **array<array-key,mixed>** | Array to mutate.                                           |
| `$keyList` | **array<array-key,mixed>** | Keys that should be removed.                               |
| `$strict`  | **bool**                   | Whether key comparisons should use strict type
comparison. |

## Return Value

**int**

Number of entries removed across all nesting levels.
