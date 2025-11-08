# Models Service

The `models` service uses the [Phalcon Models Component](https://docs.phalcon.io/latest/models/){:target="_blank"}

## Configurations

```ini
MODEL_BACKUP=\PhalconKit\Models\Backup
MODEL_AUDIT=\PhalconKit\Models\Audit
MODEL_AUDIT_DETAIL=\PhalconKit\Models\AuditDetail
MODEL_LOG=\PhalconKit\Models\Log
MODEL_EMAIL=\PhalconKit\Models\Email
MODEL_JOB=\PhalconKit\Models\Job
MODEL_FILE=\PhalconKit\Models\File
MODEL_SESSION=\PhalconKit\Models\Session
MODEL_FLAG=\PhalconKit\Models\Flag
MODEL_SETTING=\PhalconKit\Models\Setting
MODEL_LANG=\PhalconKit\Models\Lang
MODEL_TRANSLATE=\PhalconKit\Models\Translate
MODEL_TRANSLATE_FIELD=\PhalconKit\Models\TranslateField
MODEL_TRANSLATE_TABLE=\PhalconKit\Models\TranslateTable
MODEL_WORKSPACE=\PhalconKit\Models\Workspace
MODEL_WORKSPACE_LANG=\PhalconKit\Models\WorkspaceLang
MODEL_PAGE=\PhalconKit\Models\Page
MODEL_POST=\PhalconKit\Models\Post
MODEL_TEMPLATE=\PhalconKit\Models\Template
MODEL_TABLE=\PhalconKit\Models\Table
MODEL_FIELD=\PhalconKit\Models\Field
MODEL_OAUTH_2=\PhalconKit\Models\Oauth2
MODEL_PROFILE=\PhalconKit\Models\Profile
MODEL_USER=\PhalconKit\Models\User
MODEL_USER_TYPE=\PhalconKit\Models\UserType
MODEL_USER_GROUP=\PhalconKit\Models\UserGroup
MODEL_USER_ROLE=\PhalconKit\Models\UserRole
MODEL_USER_FEATURE=\PhalconKit\Models\UserFeature
MODEL_ROLE=\PhalconKit\Models\Role
MODEL_ROLE_ROLE=\PhalconKit\Models\RoleRole
MODEL_ROLE_FEATURE=\PhalconKit\Models\RoleFeature
MODEL_GROUP=\PhalconKit\Models\Group
MODEL_GROUP_ROLE=\PhalconKit\Models\GroupRole
MODEL_GROUP_TYPE=\PhalconKit\Models\GroupType
MODEL_GROUP_FEATURE=\PhalconKit\Models\GroupFeature
MODEL_TYPE=\PhalconKit\Models\Type
MODEL_FEATURE=\PhalconKit\Models\Feature
```

### Models Service Provider

```ini
PROVIDER_MODELS=\PhalconKit\Provider\Models\ServiceProvider
```

### Models Configurations Object

```php
<?php
new Config([
    'providers' => [
        \PhalconKit\Provider\Models\ServiceProvider::class => Env::get('PROVIDER_MODELS', \PhalconKit\Provider\Models\ServiceProvider::class),
    ],
    'models' => [
        \PhalconKit\Models\Backup::class => Env::get('MODEL_BACKUP', \PhalconKit\Models\Backup::class),
        \PhalconKit\Models\Audit::class => Env::get('MODEL_AUDIT', \PhalconKit\Models\Audit::class),
        \PhalconKit\Models\AuditDetail::class => Env::get('MODEL_AUDIT_DETAIL', \PhalconKit\Models\AuditDetail::class),
        \PhalconKit\Models\Log::class => Env::get('MODEL_LOG', \PhalconKit\Models\Log::class),
        \PhalconKit\Models\Email::class => Env::get('MODEL_EMAIL', \PhalconKit\Models\Email::class),
        \PhalconKit\Models\Job::class => Env::get('MODEL_JOB', \PhalconKit\Models\Job::class),
        \PhalconKit\Models\File::class => Env::get('MODEL_FILE', \PhalconKit\Models\File::class),
        \PhalconKit\Models\Session::class => Env::get('MODEL_SESSION', \PhalconKit\Models\Session::class),
        \PhalconKit\Models\Flag::class => Env::get('MODEL_FLAG', \PhalconKit\Models\Flag::class),
        \PhalconKit\Models\Setting::class => Env::get('MODEL_SETTING', \PhalconKit\Models\Setting::class),
        \PhalconKit\Models\Lang::class => Env::get('MODEL_LANG', \PhalconKit\Models\Lang::class),
        \PhalconKit\Models\Translate::class => Env::get('MODEL_TRANSLATE', \PhalconKit\Models\Translate::class),
        \PhalconKit\Models\TranslateField::class => Env::get('MODEL_TRANSLATE_FIELD', \PhalconKit\Models\TranslateField::class),
        \PhalconKit\Models\TranslateTable::class => Env::get('MODEL_TRANSLATE_TABLE', \PhalconKit\Models\TranslateTable::class),
        \PhalconKit\Models\Workspace::class => Env::get('MODEL_WORKSPACE', \PhalconKit\Models\Workspace::class),
        \PhalconKit\Models\WorkspaceLang::class => Env::get('MODEL_WORKSPACE_LANG', \PhalconKit\Models\WorkspaceLang::class),
        \PhalconKit\Models\Page::class => Env::get('MODEL_PAGE', \PhalconKit\Models\Page::class),
        \PhalconKit\Models\Post::class => Env::get('MODEL_POST', \PhalconKit\Models\Post::class),
        \PhalconKit\Models\Template::class => Env::get('MODEL_TEMPLATE', \PhalconKit\Models\Template::class),
        \PhalconKit\Models\Table::class => Env::get('MODEL_TABLE', \PhalconKit\Models\Table::class),
        \PhalconKit\Models\Field::class => Env::get('MODEL_FIELD', \PhalconKit\Models\Field::class),
        \PhalconKit\Models\Oauth2::class => Env::get('MODEL_OAUTH_2', \PhalconKit\Models\Oauth2::class),
        \PhalconKit\Models\Profile::class => Env::get('MODEL_PROFILE', \PhalconKit\Models\Profile::class),
        \PhalconKit\Models\User::class => Env::get('MODEL_USER', \PhalconKit\Models\User::class),
        \PhalconKit\Models\UserType::class => Env::get('MODEL_USER_TYPE', \PhalconKit\Models\UserType::class),
        \PhalconKit\Models\UserGroup::class => Env::get('MODEL_USER_GROUP', \PhalconKit\Models\UserGroup::class),
        \PhalconKit\Models\UserRole::class => Env::get('MODEL_USER_ROLE', \PhalconKit\Models\UserRole::class),
        \PhalconKit\Models\UserFeature::class => Env::get('MODEL_USER_FEATURE', \PhalconKit\Models\UserFeature::class),
        \PhalconKit\Models\Role::class => Env::get('MODEL_ROLE', \PhalconKit\Models\Role::class),
        \PhalconKit\Models\RoleRole::class => Env::get('MODEL_ROLE_ROLE', \PhalconKit\Models\RoleRole::class),
        \PhalconKit\Models\RoleFeature::class => Env::get('MODEL_ROLE_FEATURE', \PhalconKit\Models\RoleFeature::class),
        \PhalconKit\Models\Group::class => Env::get('MODEL_GROUP', \PhalconKit\Models\Group::class),
        \PhalconKit\Models\GroupRole::class => Env::get('MODEL_GROUP_ROLE', \PhalconKit\Models\GroupRole::class),
        \PhalconKit\Models\GroupType::class => Env::get('MODEL_GROUP_TYPE', \PhalconKit\Models\GroupType::class),
        \PhalconKit\Models\GroupFeature::class => Env::get('MODEL_GROUP_FEATURE', \PhalconKit\Models\GroupFeature::class),
        \PhalconKit\Models\Type::class => Env::get('MODEL_TYPE', \PhalconKit\Models\Type::class),
        \PhalconKit\Models\Feature::class => Env::get('MODEL_FEATURE', \PhalconKit\Models\Feature::class),
    ],
]);
```

## Models Service (`models`)

!!! info "Models Service Provider"
    Models Service Provider (`models`):
    [`\PhalconKit\Provider\Models\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Models/ServiceProvider.php){:target="_blank"}

```php
<?php
// Retrieving the service from an Injectable
$models = $this->models;

// Retrieving the service from the DI
$models = $this->di->get('models');

// Retrieving the service from the getDI()
$models = $this->getDI()->get('models');

// Retrieving the service from anywhere
$models = Di::getDefault()->get('models');
```
