
Dump values in a CLI-safe or browser-safe representation.

CLI and phpdbg output is encoded as pretty JSON so command-line debugging
stays readable without HTML. Web output uses Phalcon's debug dumper to
preserve type details in a browser-friendly format. This helper does not
terminate execution; use `dd()` or `vdd()` for dump-and-die behavior.

***

* Full name: `dump`
* Defined in: `src/Functions/Dump.php`

## Parameters

| Parameter | Type      | Description        |
|-----------|-----------|--------------------|
| `$params` | **mixed** | Values to inspect. |

## Return Value

**void**
