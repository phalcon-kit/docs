
***

* Full name: `\PhalconKit\Identity\Manager`
* Parent class: [`\PhalconKit\Di\Injectable`](../Di/Injectable.md)
* This class implements:
  [`\PhalconKit\Identity\ManagerInterface`](./ManagerInterface.md),
  [`\PhalconKit\Support\Options\OptionsInterface`](../Support/Options/OptionsInterface.md)

## Methods

### get

Retrieves the identity based on the provided user expose parameter.

```php
public get(array|null $userExpose = null): array
```

**Parameters:**

| Parameter     | Type            | Description                                               |
|---------------|-----------------|-----------------------------------------------------------|
| `$userExpose` | **array\|null** | Optional parameter to specify user-related data exposure. |

**Return Value:**

The resulting identity data array.

***

### getIdentity

Retrieves the identity information based on the provided user expose parameter.

```php
public getIdentity(array|null $userExpose = null): array
```

**Parameters:**

| Parameter     | Type            | Description                                                   |
|---------------|-----------------|---------------------------------------------------------------|
| `$userExpose` | **array\|null** | Optional parameter specifying details for user data exposure. |

**Return Value:**

An associative array containing identity details such as logged-in status, user data, impersonation, roles, and groups.

***

### login

Handles the login process by validating the provided parameters, checking user credentials,
and managing session state. Returns the login status along with any validation messages.

```php
public login(array $params = []): array
```

**Parameters:**

| Parameter | Type      | Description                                                       |
|-----------|-----------|-------------------------------------------------------------------|
| `$params` | **array** | Parameters for login, typically including 'email' and 'password'. |

**Return Value:**

Contains login status, logged-in user information, and validation messages.

***

### logout

Logs out the current user by removing the session identity and returns the login status.

```php
public logout(): array
```

**Return Value:**

An associative array containing the user's login status and identity status after logout.

***

### reset

Resets a user's password or generates a reset token for the user, depending on the input parameters.

```php
public reset(array|null $params = null): array
```

**Parameters:**

| Parameter | Type            | Description                                                                                                                                                                                                                                                                                                          |
|-----------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$params` | **array\|null** | Parameters including email, token,
password, and password confirmation for the reset operation.
- 'email': The user's email address.
- 'token': An optional reset token for password update.
- 'password': The new password to set (relevant with token).
- 'passwordConfirm': The confirmation of the new password. |

**Return Value:**

An array containing the following keys:
- 'saved': A boolean indicating whether the save operation was successful.
- 'sent': A boolean indicating whether the reset token email was sent successfully.
- 'messages': A collection of validation or processing messages.

**Throws:**

- [`Exception`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### collectList

Collects and returns a list of entities from the specified property of the model, keyed by a method from each entity.

```php
private collectList(\PhalconKit\Mvc\ModelInterface|null $model, string $property, string $keyMethod = 'getKey'): array
```

**Parameters:**

| Parameter    | Type                                     | Description                                                                           |
|--------------|------------------------------------------|---------------------------------------------------------------------------------------|
| `$model`     | **\PhalconKit\Mvc\ModelInterface\|null** | The model containing the property with the list of entities.                          |
| `$property`  | **string**                               | The name of the property in the model that holds the list of entities.                |
| `$keyMethod` | **string**                               | The name of the method in each entity used to generate the key. Defaults to 'getKey'. |

**Return Value:**

An associative array of entities, keyed by the specified method from each entity.

***

## Inherited methods

### getUser

Return the current user or impersonated user object based on the session

```php
public getUser(bool $as = false, bool|null $force = null): \PhalconKit\Models\Interfaces\UserInterface|null
```

**Parameters:**

| Parameter | Type           | Description                                                        |
|-----------|----------------|--------------------------------------------------------------------|
| `$as`     | **bool**       | Flag to indicate whether to get the user as another user           |
| `$force`  | **bool\|null** | Flag to indicate whether to force the retrieval of the user object |

**Return Value:**

The user object or null if session is not available

***

### setUser

Set the current user or impersonated user instance.

```php
public setUser(\PhalconKit\Models\Interfaces\UserInterface|null $user): void
```

**Parameters:**

| Parameter | Type                                                  | Description                                                 |
|-----------|-------------------------------------------------------|-------------------------------------------------------------|
| `$user`   | **\PhalconKit\Models\Interfaces\UserInterface\|null** | The user instance to set or null to unset the current user. |

***

### getUserAs

Retrieve the original user when impersonating

```php
public getUserAs(): \PhalconKit\Models\Interfaces\UserInterface|null
```

**Return Value:**

The user instance or null if not available.

***

### setUserAs

Set the original user instance when impersonating

```php
public setUserAs(\PhalconKit\Models\Interfaces\UserInterface|null $user): void
```

**Parameters:**

| Parameter | Type                                                  | Description                                 |
|-----------|-------------------------------------------------------|---------------------------------------------|
| `$user`   | **\PhalconKit\Models\Interfaces\UserInterface\|null** | The user instance to set, or null to unset. |

***

### getUserId

Retrieves the current/impersonated user or the original user ID.

```php
public getUserId(bool $as = false): int|null
```

**Parameters:**

| Parameter | Type     | Description                                                                                      |
|-----------|----------|--------------------------------------------------------------------------------------------------|
| `$as`     | **bool** | Determines whether to retrieve the original user (true) or the current/impersonated one (false). |

**Return Value:**

Returns the user ID as an integer if available, or null if the user is not set.

***

### getUserAsId

Retrieves the original user ID when impersonating.

```php
public getUserAsId(): int|null
```

**Return Value:**

Returns the user ID as an integer if available, or null otherwise.

***

### getRoleList

Retrieves the list of roles associated with the current identity.

```php
public getRoleList(): array
```

**Return Value:**

Returns an array of roles. If no roles are set, returns an empty array.

***

### getGroupList

Retrieves the list of groups associated with the current identity.

```php
public getGroupList(): array
```

**Return Value:**

Returns an array of group identifiers or an empty array if no groups are found.

***

### getTypeList

Retrieves the list of types associated with the current identity.

```php
public getTypeList(): array
```

**Return Value:**

Returns an array of types. If no types are found, returns an empty array.

***

### isLoggedIn

Checks if the user is currently logged in.

```php
public isLoggedIn(bool $as = false, bool $force = false): bool
```

**Parameters:**

| Parameter | Type     | Description                                                                                   |
|-----------|----------|-----------------------------------------------------------------------------------------------|
| `$as`     | **bool** | Determines whether to check the original user (true) or the current/impersonated one (false). |
| `$force`  | **bool** | Forces a fresh check ignoring cached user session data when set to true.                      |

**Return Value:**

Returns true if the user is logged in, false otherwise.

***

### isLoggedInAs

Checks if the user is logged in and impersonating another user.

```php
public isLoggedInAs(bool $force = false): bool
```

**Parameters:**

| Parameter | Type     | Description                                           |
|-----------|----------|-------------------------------------------------------|
| `$force`  | **bool** | Determines whether to enforce a specific login check. |

**Return Value:**

Returns true if the user is logged in based on the condition, otherwise false.

***

### findUserById

Finds and retrieves a user by their unique identifier.

```php
public findUserById(int $id): \PhalconKit\Models\Interfaces\UserInterface|null
```

**Parameters:**

| Parameter | Type    | Description                                        |
|-----------|---------|----------------------------------------------------|
| `$id`     | **int** | The unique identifier of the user to be retrieved. |

**Return Value:**

Returns the user instance if found, or null if no user exists with the specified identifier.

***

### findUserByEmail

Finds and retrieves a user by their email address.

```php
public findUserByEmail(string $string): \PhalconKit\Models\Interfaces\UserInterface|null
```

**Parameters:**

| Parameter | Type       | Description                                  |
|-----------|------------|----------------------------------------------|
| `$string` | **string** | The email address of the user to search for. |

**Return Value:**

Returns a UserInterface instance if a user with the specified email is found, or null if no user matches the email.

***

### getSessionKey

Retrieves the session key, optionally appending a refresh suffix.

```php
public getSessionKey(bool $refresh = false): string
```

**Parameters:**

| Parameter  | Type     | Description                                                           |
|------------|----------|-----------------------------------------------------------------------|
| `$refresh` | **bool** | Indicates whether to append the '-refresh' suffix to the session key. |

**Return Value:**

The retrieved session key, with or without the refresh suffix.

***

### removeSessionIdentity

Removes the session identity associated with the current instance, if a valid key exists.

```php
public removeSessionIdentity(): void
```

***

### setSessionIdentity

Sets the session identity by storing the provided identity data in the session.

```php
public setSessionIdentity(array $identity): void
```

**Parameters:**

| Parameter   | Type      | Description                                                                      |
|-------------|-----------|----------------------------------------------------------------------------------|
| `$identity` | **array** | An associative array representing the identity data to be stored in the session. |

***

### getSessionIdentity

Retrieves the session identity from the session storage.

```php
public getSessionIdentity(): array
```

**Return Value:**

An associative array representing the identity data retrieved from the session. Returns an empty array if no data is found.

***

### hasSessionIdentity

Checks if a session identity exists by verifying the presence of a valid key and its association in the session.

```php
public hasSessionIdentity(): bool
```

**Return Value:**

Returns true if a session identity exists; otherwise, false.

***

### getKey

Retrieves the 'key' value from the claim array if it exists, or returns null.

```php
public getKey(): string|null
```

**Return Value:**

The 'key' value from the claim array, or null if not found.

***

### hasRole

Determines if the current user has the specified roles.

```php
public hasRole(array|null $roles = null, bool $or = false, bool $inherit = true): bool
```

**Parameters:**

| Parameter  | Type            | Description                                                                                            |
|------------|-----------------|--------------------------------------------------------------------------------------------------------|
| `$roles`   | **array\|null** | List of roles to check against.                                                                        |
| `$or`      | **bool**        | If true, checks if the user has at least one of the roles. If false, checks if the user has all roles. |
| `$inherit` | **bool**        | If true, includes inherited roles in the check.                                                        |

**Return Value:**

True if the user satisfies the role conditions, false otherwise.

***

### has

Check if the needles meet the haystack using nested arrays
Reversing ANDs and ORs within each nested subarray

```php
public has(array|string|null $needles = null, array $haystack = [], bool $or = false): bool
```

$this->has(['dev', 'admin'], $this->getUser()->getRoles(), true); // 'dev' OR 'admin'
$this->has(['dev', 'admin'], $this->getUser()->getRoles(), false); // 'dev' AND 'admin'

$this->has(['dev', 'admin'], $this->getUser()->getRoles()); // 'dev' AND 'admin'
$this->has([['dev', 'admin']], $this->getUser()->getRoles()); // 'dev' OR 'admin'
$this->has([[['dev', 'admin']]], $this->getUser()->getRoles()); // 'dev' AND 'admin'

**Parameters:**

| Parameter   | Type                    | Description                                              |
|-------------|-------------------------|----------------------------------------------------------|
| `$needles`  | **array\|string\|null** | Needles to match and meet the rules                      |
| `$haystack` | **array**               | Haystack array to search into                            |
| `$or`       | **bool**                | True to force with "OR" , false to force "AND" condition |

**Return Value:**

Return true or false if the needles rules are being met

***

### getInheritedRoleList

Retrieves a list of inherited roles based on the provided role indices.

```php
public getInheritedRoleList(array $roleIndexList = []): array
```

The method processes the given role indices, determines their inherited roles
recursively, and returns a unique and flattened list of all inherited roles.

**Parameters:**

| Parameter        | Type      | Description                                                                      |
|------------------|-----------|----------------------------------------------------------------------------------|
| `$roleIndexList` | **array** | The list of role indices to process for inheritance. Defaults to an empty array. |

**Return Value:**

An array containing the unique list of all inherited roles.

***

### oauth2

OAuth2 authentication

```php
public oauth2(string $provider, string $providerUuid, string $accessToken, string|null $refreshToken = null, array|null $meta = []): array
```

**Parameters:**

| Parameter       | Type             | Description                                             |
|-----------------|------------------|---------------------------------------------------------|
| `$provider`     | **string**       | The OAuth2 provider                                     |
| `$providerUuid` | **string**       | The UUID associated with the provider                   |
| `$accessToken`  | **string**       | The access token provided by the provider               |
| `$refreshToken` | **string\|null** | The refresh token provided by the provider (optional)   |
| `$meta`         | **array\|null**  | Additional metadata associated with the user (optional) |

**Return Value:**

Returns an array with the following keys:
- 'saved': Indicates whether the OAuth2 entity was saved successfully
- 'loggedIn': Indicates whether the user is currently logged in
- 'loggedInAs': Indicates the user that is currently logged in
- 'messages': An array of validation messages

**Throws:**

- [`Exception`](../../Exception.md)

***

### getJwt

Generates a new JWT and refresh token based on the specified claim and configuration.

```php
public getJwt(bool $refresh = false): array
```

If the claim does not have a key or is refreshed, it creates a new key and updates the session if enabled.

**Parameters:**

| Parameter  | Type     | Description                                                                                      |
|------------|----------|--------------------------------------------------------------------------------------------------|
| `$refresh` | **bool** | Indicates whether to refresh the claim by generating a new key and invalidating previous tokens. |

**Return Value:**

Contains the generated JWT, refresh token, and a flag indicating if the claim was refreshed.

**Throws:**

- [`\Phalcon\Encryption\Security\Exception|\Phalcon\Encryption\Security\JWT\Exceptions\ValidatorException`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### getClaim

Retrieves the claim using different authentication methods such as JWT, Authorization Header, or Session.

```php
public getClaim(bool $refresh = false, bool $force = false): array
```

If the claim is cached and not forced to refresh, it returns the cached claim.

**Parameters:**

| Parameter  | Type     | Description                                                      |
|------------|----------|------------------------------------------------------------------|
| `$refresh` | **bool** | Determines whether to attempt refreshing the claim if available. |
| `$force`   | **bool** | Forces bypassing the cached claim and retrieving a new one.      |

**Return Value:**

The claim data or an empty array if no claim is found.

***

### setClaim

Sets the claim information for the current instance.

```php
public setClaim(array $claim): void
```

**Parameters:**

| Parameter | Type      | Description            |
|-----------|-----------|------------------------|
| `$claim`  | **array** | The claim data to set. |

***

### getJwtToken

Generates a JWT (JSON Web Token) using the provided identifier, payload data, and additional options.

```php
public getJwtToken(string $id, array $data = [], array $options = []): string
```

**Parameters:**

| Parameter  | Type       | Description                                                                                                                     |
|------------|------------|---------------------------------------------------------------------------------------------------------------------------------|
| `$id`      | **string** | The unique identifier for the JWT, typically representing a specific user or session.                                           |
| `$data`    | **array**  | An associative array containing the payload data to be encoded in the JWT.                                                      |
| `$options` | **array**  | An associative array of options for the token such as issuer, audience, subject, etc. Defaults will be applied if not provided. |

**Return Value:**

The generated JWT token as a string.

**Throws:**

- [`ValidatorException`](https://docs.phalcon.io/latest/api/){:target="_blank"}

***

### getClaimFromToken

Extracts claims from a provided JWT token after validating it.

```php
public getClaimFromToken(string $token, string|null $claim = null): array
```

**Parameters:**

| Parameter | Type             | Description                                           |
|-----------|------------------|-------------------------------------------------------|
| `$token`  | **string**       | The JWT token to parse and validate.                  |
| `$claim`  | **string\|null** | An optional identifier to validate the token against. |

**Return Value:**

The claims extracted from the token, or an empty array if no valid claims are found.

***

### getClaimFromAuthorization

Extracts claim information from the authorization header if it follows the Bearer token format.

```php
public getClaimFromAuthorization(array $authorization): array
```

**Parameters:**

| Parameter        | Type      | Description                                                           |
|------------------|-----------|-----------------------------------------------------------------------|
| `$authorization` | **array** | The authorization header split into an array with the type and token. |

**Return Value:**

The claim information extracted from the token or an empty array if extraction fails.

***

### getJsonRawBody

Retrieves the raw JSON body from the request.

```php
private getJsonRawBody(): \stdClass
```

If the body is not valid JSON, an empty stdClass object is returned.

**Return Value:**

The raw JSON body as an object or an empty stdClass object if the input is invalid.

***

### loginAs

Allows an admin or developer to log in as another user based on their user ID.

```php
public loginAs(array $params = []): array
```

Validates the provided parameters to ensure the presence and numericality of the user ID.
Also handles the scenario where the user attempts to return to their original session.

**Parameters:**

| Parameter | Type      | Description                                                                                      |
|-----------|-----------|--------------------------------------------------------------------------------------------------|
| `$params` | **array** | Associative array containing the key 'userId', which represents the ID of the user to log in as. |

**Return Value:**

An array containing the validation messages, login status, and login-as status:
- 'messages': Validation messages, if any.
- 'loggedIn': Boolean indicating whether the user is logged in under their original session.
- 'loggedInAs': Boolean indicating whether the user is logged in as another user.

***

### logoutAs

Logs out from a session where the user was logged in (impersonating)
as another user, reverting back to the original session identity.

```php
public logoutAs(): array
```

If the current session identity includes an 'asUserId', the identity
is updated to the corresponding 'userId'.

**Return Value:**

An array containing the user's login status after reverting:
- 'loggedIn': Boolean indicating whether the original user is logged in.
- 'loggedInAs': Boolean indicating whether the session is currently logged in as another user.

***

### getAclRoles

Return the list of ACL roles
- role `ws` is automatically added if the bootstrap mode is websocket/ws
- role `cli` is automatically added if the bootstrap mode is console/cli
- role `everyone` is automatically added to everyone at all time
- role `guest` is automatically added only if no role was found
- inherited roles are automatically added from the base roles

```php
public getAclRoles(array|null $roleList = null): array
```

**Parameters:**

| Parameter   | Type            | Description |
|-------------|-----------------|-------------|
| `$roleList` | **array\|null** |             |

***

### __construct

Constructs a new instance of the class.

```php
public __construct(array|null $options = null): mixed
```

**Parameters:**

| Parameter  | Type            | Description                                                                    |
|------------|-----------------|--------------------------------------------------------------------------------|
| `$options` | **array\|null** | An optional array of options to initialize the instance with. Default is null. |

***

### initializeOptions

Initializes the options for the object.

```php
public initializeOptions(array|null $options = null): void
```

**Parameters:**

| Parameter  | Type            | Description                                                          |
|------------|-----------------|----------------------------------------------------------------------|
| `$options` | **array\|null** | The options to be initialized. If null, an empty array will be used. |

***

### initialize

Initializes the object.

```php
public initialize(): void
```

This method is responsible for performing any necessary setup or initialization tasks for the object.
It does not accept any parameters and does not return a value.

***

### setOptions

Sets the options for the object.

```php
public setOptions(array $options, bool $merge = false): void
```

**Parameters:**

| Parameter  | Type      | Description                                                                    |
|------------|-----------|--------------------------------------------------------------------------------|
| `$options` | **array** | The array of options to be set.                                                |
| `$merge`   | **bool**  | Whether to merge the existing options with the new options. Defaults to false. |

***

### getOptions

Retrieves all options.

```php
public getOptions(): array
```

**Return Value:**

An array containing all the options.

***

### setOption

Sets the value of the option specified by the given key.

```php
public setOption(string $key, mixed $value = null, bool $merge = false): void
```

**Parameters:**

| Parameter | Type       | Description                                                                         |
|-----------|------------|-------------------------------------------------------------------------------------|
| `$key`    | **string** | The key of the option.                                                              |
| `$value`  | **mixed**  | The value to be set for the option.                                                 |
| `$merge`  | **bool**   | Whether to merge the new value with an existing value if the option already exists. |

***

### getOption

Retrieves the value of the option specified by the given key.

```php
public getOption(string $key, mixed $default = null): mixed
```

**Parameters:**

| Parameter  | Type       | Description                                                    |
|------------|------------|----------------------------------------------------------------|
| `$key`     | **string** | The key of the option.                                         |
| `$default` | **mixed**  | The default value to be returned if the option does not exist. |

**Return Value:**

The value of the option specified by the key, or the default value if the option does not exist.

***

### hasOption

Checks if the option specified by the given key exists.

```php
public hasOption(string $key): bool
```

**Parameters:**

| Parameter | Type       | Description            |
|-----------|------------|------------------------|
| `$key`    | **string** | The key of the option. |

**Return Value:**

Returns true if the option exists, false otherwise.

***

### removeOption

Remove an option by key

```php
public removeOption(string $key): void
```

Removes the option with the given key from the options array.

**Parameters:**

| Parameter | Type       | Description                         |
|-----------|------------|-------------------------------------|
| `$key`    | **string** | The key of the option to be removed |

***

### resetOptions

Reset all options to their default values
- Uses the defaultOptions property to set the options

```php
public resetOptions(): void
```

***

### clearOptions

Clear all options

```php
public clearOptions(): void
```

This method clears all the options stored in the class.
After calling this method, the options array will be empty.

***
