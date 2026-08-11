
Format a string with named placeholders backed by `vsprintf()`.

Named placeholders use PHP's positional syntax with a symbolic name in
place of the numeric position. The names are rewritten to numeric
positions before calling `vsprintf()`.

Example:
```php
sprintfn('second: %%second$s ; first: %%first$s', [
    'first' => '1st',
    'second' => '2nd',
]);
```

***

* Full name: `sprintfn`
* Defined in: `src/Functions/Sprintf.php`

## Parameters

| Parameter | Type                    | Description                                          |
|-----------|-------------------------|------------------------------------------------------|
| `$format` | **string**              | Sprintf format string containing named placeholders. |
| `$args`   | **array<string,mixed>** | Replacement values keyed by placeholder
name.        |

## Return Value

**string|false**

Formatted string, or false after emitting a warning
when a named placeholder has no matching argument.
