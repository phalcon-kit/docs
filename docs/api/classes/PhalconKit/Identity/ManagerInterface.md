
***

* Full name: `\PhalconKit\Identity\ManagerInterface`
* Parent interfaces:
  [`\PhalconKit\Identity\Traits\Interfaces\AclInterface`](./Traits/Interfaces/AclInterface.md),
  [`\PhalconKit\Identity\Traits\Interfaces\ImpersonationInterface`](./Traits/Interfaces/ImpersonationInterface.md),
  [`\PhalconKit\Identity\Traits\Interfaces\JwtInterface`](./Traits/Interfaces/JwtInterface.md),
  [`\PhalconKit\Identity\Traits\Interfaces\Oauth2Interface`](./Traits/Interfaces/Oauth2Interface.md),
  [`\PhalconKit\Identity\Traits\Interfaces\RoleInterface`](./Traits/Interfaces/RoleInterface.md),
  [`\PhalconKit\Identity\Traits\Interfaces\SessionInterface`](./Traits/Interfaces/SessionInterface.md),
  [`\PhalconKit\Identity\Traits\Interfaces\UserInterface`](./Traits/Interfaces/UserInterface.md)

## Inherited methods

### getUser

```php
public getUser(bool $as = false, ?bool $force = null): ?\PhalconKit\Models\Interfaces\UserInterface
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$as`     | **bool**  |             |
| `$force`  | **?bool** |             |

***

### setUser

```php
public setUser(?\PhalconKit\Models\Interfaces\UserInterface $user): void
```

**Parameters:**

| Parameter | Type                                             | Description |
|-----------|--------------------------------------------------|-------------|
| `$user`   | **?\PhalconKit\Models\Interfaces\UserInterface** |             |

***

### getUserAs

```php
public getUserAs(): ?\PhalconKit\Models\Interfaces\UserInterface
```

***

### setUserAs

```php
public setUserAs(?\PhalconKit\Models\Interfaces\UserInterface $user): void
```

**Parameters:**

| Parameter | Type                                             | Description |
|-----------|--------------------------------------------------|-------------|
| `$user`   | **?\PhalconKit\Models\Interfaces\UserInterface** |             |

***

### getUserId

```php
public getUserId(bool $as = false): ?int
```

**Parameters:**

| Parameter | Type     | Description |
|-----------|----------|-------------|
| `$as`     | **bool** |             |

***

### getUserAsId

```php
public getUserAsId(): ?int
```

***

### getRoleList

```php
public getRoleList(): array
```

***

### getGroupList

```php
public getGroupList(): array
```

***

### getTypeList

```php
public getTypeList(): array
```

***

### isLoggedIn

```php
public isLoggedIn(bool $as = false, bool $force = false): bool
```

**Parameters:**

| Parameter | Type     | Description |
|-----------|----------|-------------|
| `$as`     | **bool** |             |
| `$force`  | **bool** |             |

***

### isLoggedInAs

```php
public isLoggedInAs(bool $force = false): bool
```

**Parameters:**

| Parameter | Type     | Description |
|-----------|----------|-------------|
| `$force`  | **bool** |             |

***

### findUserById

```php
public findUserById(int $id): ?\PhalconKit\Models\Interfaces\UserInterface
```

**Parameters:**

| Parameter | Type    | Description |
|-----------|---------|-------------|
| `$id`     | **int** |             |

***

### findUserByEmail

```php
public findUserByEmail(string $string): ?\PhalconKit\Models\Interfaces\UserInterface
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$string` | **string** |             |

***

### getSessionKey

```php
public getSessionKey(bool $refresh = false): string
```

**Parameters:**

| Parameter  | Type     | Description |
|------------|----------|-------------|
| `$refresh` | **bool** |             |

***

### removeSessionIdentity

```php
public removeSessionIdentity(): void
```

***

### setSessionIdentity

```php
public setSessionIdentity(array $identity): void
```

**Parameters:**

| Parameter   | Type      | Description |
|-------------|-----------|-------------|
| `$identity` | **array** |             |

***

### getSessionIdentity

```php
public getSessionIdentity(): array
```

***

### hasSessionIdentity

```php
public hasSessionIdentity(): bool
```

***

### getKey

```php
public getKey(): ?string
```

***

### hasRole

```php
public hasRole(?array $roles = null, bool $or = false, bool $inherit = true): bool
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$roles`   | **?array** |             |
| `$or`      | **bool**   |             |
| `$inherit` | **bool**   |             |

***

### has

```php
public has(array|string|null $needles = null, array $haystack = [], bool $or = false): bool
```

**Parameters:**

| Parameter   | Type                    | Description |
|-------------|-------------------------|-------------|
| `$needles`  | **array\|string\|null** |             |
| `$haystack` | **array**               |             |
| `$or`       | **bool**                |             |

***

### getInheritedRoleList

```php
public getInheritedRoleList(array $roleIndexList = []): array
```

**Parameters:**

| Parameter        | Type      | Description |
|------------------|-----------|-------------|
| `$roleIndexList` | **array** |             |

***

### oauth2

```php
public oauth2(string $provider, string $providerUuid, string $accessToken, ?string $refreshToken = null, ?array $meta = []): array
```

**Parameters:**

| Parameter       | Type        | Description |
|-----------------|-------------|-------------|
| `$provider`     | **string**  |             |
| `$providerUuid` | **string**  |             |
| `$accessToken`  | **string**  |             |
| `$refreshToken` | **?string** |             |
| `$meta`         | **?array**  |             |

***

### getJwt

```php
public getJwt(bool $refresh = false): array
```

**Parameters:**

| Parameter  | Type     | Description |
|------------|----------|-------------|
| `$refresh` | **bool** |             |

***

### getClaim

```php
public getClaim(bool $refresh = false, bool $force = false): array
```

**Parameters:**

| Parameter  | Type     | Description |
|------------|----------|-------------|
| `$refresh` | **bool** |             |
| `$force`   | **bool** |             |

***

### setClaim

```php
public setClaim(array $claim): void
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$claim`  | **array** |             |

***

### getJwtToken

```php
public getJwtToken(string $id, array $data = [], array $options = []): string
```

**Parameters:**

| Parameter  | Type       | Description |
|------------|------------|-------------|
| `$id`      | **string** |             |
| `$data`    | **array**  |             |
| `$options` | **array**  |             |

***

### getClaimFromToken

```php
public getClaimFromToken(string $token, ?string $claim = null): array
```

**Parameters:**

| Parameter | Type        | Description |
|-----------|-------------|-------------|
| `$token`  | **string**  |             |
| `$claim`  | **?string** |             |

***

### getClaimFromAuthorization

```php
public getClaimFromAuthorization(array $authorization): array
```

**Parameters:**

| Parameter        | Type      | Description |
|------------------|-----------|-------------|
| `$authorization` | **array** |             |

***

### loginAs

```php
public loginAs(array $params = []): array
```

**Parameters:**

| Parameter | Type      | Description |
|-----------|-----------|-------------|
| `$params` | **array** |             |

***

### logoutAs

```php
public logoutAs(): array
```

***

### getAclRoles

```php
public getAclRoles(?array $roleList = null): array
```

**Parameters:**

| Parameter   | Type       | Description |
|-------------|------------|-------------|
| `$roleList` | **?array** |             |

***
