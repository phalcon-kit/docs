
Builds the ACL role objects used by PhalconKit permission checks.

The trait combines execution context, identity roles, guest fallback, and
configured role inheritance into one map keyed by role name. Consumers should
use the returned map as the effective role set rather than reading raw user
relations directly.

***

* Full name: `\PhalconKit\Identity\Traits\Acl`

## Methods

### hasAclRole

Check whether the current identity has at least one (or all) of the given ACL roles.

```php
public hasAclRole(array|null $roles = null, bool $or = false): bool
```

This method evaluates the provided role names against the **effective ACL role set**
returned by

- **See:** \PhalconKit\Identity\Traits\getAclRoles(), not just the raw identity roles. As a result:

- Contextual roles such as `ws`, `cli`, and `everyone` are implicitly considered.
- The `guest` role may be present when no explicit identity roles exist.
- Inherited roles are already resolved and included.

Internally, this delegates to
- **See:** \PhalconKit\Identity\Traits\has(), comparing:
- the requested roles (`$roles`)
- against the keys of the computed ACL role map

**Parameters:**

| Parameter | Type            | Description                                                                                                                                                           |
|-----------|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$roles`  | **array\|null** | List of role identifiers to test.
- `null` typically implies a truthy check against defaults,
  depending on {@see \PhalconKit\Identity\Traits\has()} semantics.      |
| `$or`     | **bool**        | Legacy matching mode passed to {@see \PhalconKit\Identity\Traits\has()}:
- `false` (default): at least one role must be present.
- `true`: all roles must be present. |

**Return Value:**

True if the role condition is satisfied, false otherwise.

***
### getAclRoles

Build and return the effective ACL role set for the current identity.

```php
public getAclRoles(array|null $roleList = null): array<string,\Phalcon\Acl\Role>
```

This method computes the **final, authoritative list of ACL roles** used by
permission checks. The resulting role set is not a direct reflection of the
identity’s stored roles; it is a **context-aware, normalized, and expanded**
role map that accounts for execution context and role inheritance.

Resolution rules, applied in order:

1. **Execution-context roles**
   - `ws` is added when running under a WebSocket bootstrap.
   - `cli` is added when running under a console/CLI bootstrap.

2. **Global role**
   - `everyone` is always added, regardless of identity state.

3. **Identity roles**
   - If `$roleList` is provided, it is treated as the authoritative base role list.
   - Otherwise, roles are derived from the current identity via `getRoleList()`.

4. **Guest fallback**
   - If no base roles are resolved, `guest` is added as the sole identity role.

5. **Inherited roles**
   - All roles implied by inheritance rules are automatically added.

The returned array is keyed by role name and contains instantiated ACL `Role`
objects, ensuring uniqueness and preventing duplicate role registration.

**Parameters:**

| Parameter   | Type            | Description                                                                                                                                           |
|-------------|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| `$roleList` | **array\|null** | Optional explicit list of base role identifiers.
When provided, it overrides identity-derived roles
but still participates in inheritance resolution. |

**Return Value:**

Map of role name to ACL Role instance representing
the complete effective ACL role set.

***
