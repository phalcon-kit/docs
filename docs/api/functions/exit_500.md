
Terminate execution with a 500 Internal Server Error response code.

In web SAPIs, the response code is set to 500 when headers are still
mutable. In CLI/phpdbg the helper simply exits with status code 1. This is
intended for debugging helpers and unrecoverable bootstrap failures, not
for normal exception/control-flow handling.

***

* Full name: `exit_500`
* Defined in: `src/Functions/Dump.php`

## Parameters

This function has no parameters.

## Return Value

**void**
