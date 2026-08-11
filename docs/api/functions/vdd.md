
Dump values through native `var_dump()` and terminate execution.

This helper is intentionally lower-level than `dd()`: it bypasses the
Phalcon debug dumper so edge cases involving object debug handlers,
resources, or raw PHP output can be inspected directly.

***

* Full name: `vdd`
* Defined in: `src/Functions/Dump.php`

## Parameters

| Parameter | Type      | Description                           |
|-----------|-----------|---------------------------------------|
| `$params` | **mixed** | Values to inspect before termination. |

## Return Value

**void**
