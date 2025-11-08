
version of sprintf for cases where named arguments are desired (php syntax)

with sprintf: sprintf('second: %%2$s ; first: %%1$s', '1st', '2nd');

with sprintfn: sprintfn('second: %%second$s ; first: %%first$s', array(
 'first' => '1st',
 'second'=> '2nd'
));

***

* Full name: `sprintfn`
* Defined in: `src/Functions/Sprintf.php`

## Parameters

| Parameter | Type       | Description                                                         |
|-----------|------------|---------------------------------------------------------------------|
| `$format` | **string** | sprintf format string, with any number of named arguments           |
| `$args`   | **array**  | array of [ 'arg_name' => 'arg value', ... ] replacements to be made |

## Return Value

**string|false**

result of sprintf call, or bool false on error
