
The Security trait provides methods to handle security-related functionalities.

***

* Full name: `\PhalconKit\Mvc\Model\Traits\Security`

## Methods

### initializeSecurity

Initializes the security

```php
public initializeSecurity(array|null $options = null): void
```

**Parameters:**

| Parameter  | Type            | Description                                                                                                                                                                          |
|------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$options` | **array\|null** | An optional array of security options. If not provided,
the method will attempt to fetch the options from the options manager.
If no options are found, an empty array will be used. |

***
### setSecurityBehavior

Sets the security behavior

```php
public setSecurityBehavior(\PhalconKit\Mvc\Model\Behavior\Security $securityBehavior): void
```

**Parameters:**

| Parameter           | Type                                        | Description                   |
|---------------------|---------------------------------------------|-------------------------------|
| `$securityBehavior` | **\PhalconKit\Mvc\Model\Behavior\Security** | The security behavior to set. |

***
### getSecurityBehavior

Retrieves the security behavior

```php
public getSecurityBehavior(): \PhalconKit\Mvc\Model\Behavior\Security
```

**Return Value:**

The security behavior instance.

***
