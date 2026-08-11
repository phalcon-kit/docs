
Dump values and terminate execution as an error.

This is the framework's dump-and-die helper. It uses `dump()` for output
formatting, then delegates to `exit_500()` for web response/error status.

***

* Full name: `dd`
* Defined in: `src/Functions/Dump.php`

## Parameters

| Parameter | Type      | Description                           |
|-----------|-----------|---------------------------------------|
| `$params` | **mixed** | Values to inspect before termination. |

## Return Value

**void**
