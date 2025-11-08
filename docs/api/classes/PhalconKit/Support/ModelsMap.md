
Allow to get mapped classes without using magic methods

***

* Full name: `\PhalconKit\Support\ModelsMap`

## Properties

### modelsMap

Store the mapped model classes

```php
public string[] $modelsMap
```

***

## Methods

### getDI

```php
public getDI(): \Phalcon\Di\DiInterface
```

* This method is **abstract**.
***
### getConfig

Retrieve the config from DI

```php
public getConfig(): \PhalconKit\Bootstrap\Config
```

***
### setModelsMap

Set the models mapping or retrieve the mapped models from the config

```php
public setModelsMap(?array $modelsMap = null): void
```

**Parameters:**

| Parameter    | Type       | Description |
|--------------|------------|-------------|
| `$modelsMap` | **?array** |             |

***
### getModelsMap

Get an array of mapped models

```php
public getModelsMap(): array
```

***
### setClassMap

Map a new class

```php
public setClassMap(string $map, string $class): void
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$map`    | **string** |             |
| `$class`  | **string** |             |

***
### removeClassMap

Remove an existing class

```php
public removeClassMap(string $map): void
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$map`    | **string** |             |

***
### getClassMap

Return the class mapping

```php
public getClassMap(string $class): string
```

**Parameters:**

| Parameter | Type       | Description |
|-----------|------------|-------------|
| `$class`  | **string** |             |

***
### getBackupClass

Return the mapped class name of \PhalconKit\Models\Backup::class

```php
public getBackupClass(): string
```

***
### getAuditClass

Return the mapped class name of \PhalconKit\Models\Audit::class

```php
public getAuditClass(): string
```

***
### getAuditDetailClass

Return the mapped class name of \PhalconKit\Models\AuditDetail::class

```php
public getAuditDetailClass(): string
```

***
### getLogClass

Return the mapped class name of \PhalconKit\Models\Log::class

```php
public getLogClass(): string
```

***
### getEmailClass

Return the mapped class name of \PhalconKit\Models\Email::class

```php
public getEmailClass(): string
```

***
### getJobClass

Return the mapped class name of \PhalconKit\Models\Job::class

```php
public getJobClass(): string
```

***
### getFileClass

Return the mapped class name of \PhalconKit\Models\File::class

```php
public getFileClass(): string
```

***
### getSessionClass

Return the mapped class name of \PhalconKit\Models\Session::class

```php
public getSessionClass(): string
```

***
### getFlagClass

Return the mapped class name of \PhalconKit\Models\Flag::class

```php
public getFlagClass(): string
```

***
### getSettingClass

Return the mapped class name of \PhalconKit\Models\Setting::class

```php
public getSettingClass(): string
```

***
### getLangClass

Return the mapped class name of \PhalconKit\Models\Lang::class

```php
public getLangClass(): string
```

***
### getTranslateClass

Return the mapped class name of \PhalconKit\Models\Translate::class

```php
public getTranslateClass(): string
```

***
### getWorkspaceClass

Return the mapped class name of \PhalconKit\Models\Workspace::class

```php
public getWorkspaceClass(): string
```

***
### getWorkspaceLangClass

Return the mapped class name of \PhalconKit\Models\WorkspaceLang::class

```php
public getWorkspaceLangClass(): string
```

***
### getPageClass

Return the mapped class name of \PhalconKit\Models\Page::class

```php
public getPageClass(): string
```

***
### getPostClass

Return the mapped class name of \PhalconKit\Models\Post::class

```php
public getPostClass(): string
```

***
### getTemplateClass

Return the mapped class name of \PhalconKit\Models\Template::class

```php
public getTemplateClass(): string
```

***
### getTableClass

Return the mapped class name of \PhalconKit\Models\Table::class

```php
public getTableClass(): string
```

***
### getProfileClass

Return the mapped class name of \PhalconKit\Models\Profile::class

```php
public getProfileClass(): string
```

***
### getOauth2Class

Return the mapped class name of \PhalconKit\Models\Oauth2::class

```php
public getOauth2Class(): string
```

***
### getUserClass

Return the mapped class name of \PhalconKit\Models\User::class

```php
public getUserClass(): string
```

***
### getUserTypeClass

Return the mapped class name of \PhalconKit\Models\UserType::class

```php
public getUserTypeClass(): string
```

***
### getUserGroupClass

Return the mapped class name of \PhalconKit\Models\UserGroup::class

```php
public getUserGroupClass(): string
```

***
### getUserRoleClass

Return the mapped class name of \PhalconKit\Models\UserRole::class

```php
public getUserRoleClass(): string
```

***
### getUserFeatureClass

Return the mapped class name of \PhalconKit\Models\UserFeature::class

```php
public getUserFeatureClass(): string
```

***
### getRoleClass

Return the mapped class name of \PhalconKit\Models\Role::class

```php
public getRoleClass(): string
```

***
### getRoleRoleClass

Return the mapped class name of \PhalconKit\Models\RoleRole::class

```php
public getRoleRoleClass(): string
```

***
### getRoleFeatureClass

Return the mapped class name of \PhalconKit\Models\RoleFeature::class

```php
public getRoleFeatureClass(): string
```

***
### getGroupClass

Return the mapped class name of \PhalconKit\Models\Group::class

```php
public getGroupClass(): string
```

***
### getGroupRoleClass

Return the mapped class name of \PhalconKit\Models\GroupRole::class

```php
public getGroupRoleClass(): string
```

***
### getGroupTypeClass

Return the mapped class name of \PhalconKit\Models\GroupType::class

```php
public getGroupTypeClass(): string
```

***
### getGroupFeatureClass

Return the mapped class name of \PhalconKit\Models\GroupFeature::class

```php
public getGroupFeatureClass(): string
```

***
### getTypeClass

Return the mapped class name of \PhalconKit\Models\Type::class

```php
public getTypeClass(): string
```

***
### getFeatureClass

Return the mapped class name of \PhalconKit\Models\Feature::class

```php
public getFeatureClass(): string
```

***
