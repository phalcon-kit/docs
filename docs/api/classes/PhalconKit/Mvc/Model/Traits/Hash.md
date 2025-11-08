
***

* Full name: `\PhalconKit\Mvc\Model\Traits\Hash`

## Methods

### hash

Hash a string

```php
public hash(string $string, string|null $salt = null, string|null $workFactor = null): string
```

**Parameters:**

| Parameter     | Type             | Description                                                           |
|---------------|------------------|-----------------------------------------------------------------------|
| `$string`     | **string**       | The string to be hashed                                               |
| `$salt`       | **string\|null** | (optional) The salt value to be appended to the string before hashing |
| `$workFactor` | **string\|null** | (optional) The work factor to determine the hashing cost              |

**Return Value:**

The salted hash value of the input string

***
### checkHash

Checks whether a given hash is valid for a given string.

```php
public checkHash(string|null $hash = null, string|null $string = null, int $maxPassLength): bool
```

**Parameters:**

| Parameter        | Type             | Description                                                       |
|------------------|------------------|-------------------------------------------------------------------|
| `$hash`          | **string\|null** | The hash value to be checked.                                     |
| `$string`        | **string\|null** | The string to be hashed and checked against the given hash value. |
| `$maxPassLength` | **int**          | The maximum length of the password.                               |

**Return Value:**

Returns true if the hash is valid for the string, false otherwise.

***
