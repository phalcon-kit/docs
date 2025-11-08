# Models Service

The `models` service uses the [Phalcon Models Component](https://docs.phalcon.io/latest/models/){:target="_blank"}

## Configurations

```ini
MODEL_BACKUP=\Zemit\Models\Backup
MODEL_AUDIT=\Zemit\Models\Audit
MODEL_AUDIT_DETAIL=\Zemit\Models\AuditDetail
MODEL_LOG=\Zemit\Models\Log
MODEL_EMAIL=\Zemit\Models\Email
MODEL_JOB=\Zemit\Models\Job
MODEL_FILE=\Zemit\Models\File
MODEL_SESSION=\Zemit\Models\Session
MODEL_FLAG=\Zemit\Models\Flag
MODEL_SETTING=\Zemit\Models\Setting
MODEL_LANG=\Zemit\Models\Lang
MODEL_TRANSLATE=\Zemit\Models\Translate
MODEL_TRANSLATE_FIELD=\Zemit\Models\TranslateField
MODEL_TRANSLATE_TABLE=\Zemit\Models\TranslateTable
MODEL_WORKSPACE=\Zemit\Models\Workspace
MODEL_WORKSPACE_LANG=\Zemit\Models\WorkspaceLang
MODEL_PAGE=\Zemit\Models\Page
MODEL_POST=\Zemit\Models\Post
MODEL_TEMPLATE=\Zemit\Models\Template
MODEL_TABLE=\Zemit\Models\Table
MODEL_FIELD=\Zemit\Models\Field
MODEL_OAUTH_2=\Zemit\Models\Oauth2
MODEL_PROFILE=\Zemit\Models\Profile
MODEL_USER=\Zemit\Models\User
MODEL_USER_TYPE=\Zemit\Models\UserType
MODEL_USER_GROUP=\Zemit\Models\UserGroup
MODEL_USER_ROLE=\Zemit\Models\UserRole
MODEL_USER_FEATURE=\Zemit\Models\UserFeature
MODEL_ROLE=\Zemit\Models\Role
MODEL_ROLE_ROLE=\Zemit\Models\RoleRole
MODEL_ROLE_FEATURE=\Zemit\Models\RoleFeature
MODEL_GROUP=\Zemit\Models\Group
MODEL_GROUP_ROLE=\Zemit\Models\GroupRole
MODEL_GROUP_TYPE=\Zemit\Models\GroupType
MODEL_GROUP_FEATURE=\Zemit\Models\GroupFeature
MODEL_TYPE=\Zemit\Models\Type
MODEL_FEATURE=\Zemit\Models\Feature
```

### Models Service Provider

```ini
PROVIDER_MODELS=\Zemit\Provider\Models\ServiceProvider
```

### Models Configurations Object

```php
<?php
new Config([
    'providers' => [
        \Zemit\Provider\Models\ServiceProvider::class => Env::get('PROVIDER_MODELS', \Zemit\Provider\Models\ServiceProvider::class),
    ],
    'models' => [
        \Zemit\Models\Backup::class => Env::get('MODEL_BACKUP', \Zemit\Models\Backup::class),
        \Zemit\Models\Audit::class => Env::get('MODEL_AUDIT', \Zemit\Models\Audit::class),
        \Zemit\Models\AuditDetail::class => Env::get('MODEL_AUDIT_DETAIL', \Zemit\Models\AuditDetail::class),
        \Zemit\Models\Log::class => Env::get('MODEL_LOG', \Zemit\Models\Log::class),
        \Zemit\Models\Email::class => Env::get('MODEL_EMAIL', \Zemit\Models\Email::class),
        \Zemit\Models\Job::class => Env::get('MODEL_JOB', \Zemit\Models\Job::class),
        \Zemit\Models\File::class => Env::get('MODEL_FILE', \Zemit\Models\File::class),
        \Zemit\Models\Session::class => Env::get('MODEL_SESSION', \Zemit\Models\Session::class),
        \Zemit\Models\Flag::class => Env::get('MODEL_FLAG', \Zemit\Models\Flag::class),
        \Zemit\Models\Setting::class => Env::get('MODEL_SETTING', \Zemit\Models\Setting::class),
        \Zemit\Models\Lang::class => Env::get('MODEL_LANG', \Zemit\Models\Lang::class),
        \Zemit\Models\Translate::class => Env::get('MODEL_TRANSLATE', \Zemit\Models\Translate::class),
        \Zemit\Models\TranslateField::class => Env::get('MODEL_TRANSLATE_FIELD', \Zemit\Models\TranslateField::class),
        \Zemit\Models\TranslateTable::class => Env::get('MODEL_TRANSLATE_TABLE', \Zemit\Models\TranslateTable::class),
        \Zemit\Models\Workspace::class => Env::get('MODEL_WORKSPACE', \Zemit\Models\Workspace::class),
        \Zemit\Models\WorkspaceLang::class => Env::get('MODEL_WORKSPACE_LANG', \Zemit\Models\WorkspaceLang::class),
        \Zemit\Models\Page::class => Env::get('MODEL_PAGE', \Zemit\Models\Page::class),
        \Zemit\Models\Post::class => Env::get('MODEL_POST', \Zemit\Models\Post::class),
        \Zemit\Models\Template::class => Env::get('MODEL_TEMPLATE', \Zemit\Models\Template::class),
        \Zemit\Models\Table::class => Env::get('MODEL_TABLE', \Zemit\Models\Table::class),
        \Zemit\Models\Field::class => Env::get('MODEL_FIELD', \Zemit\Models\Field::class),
        \Zemit\Models\Oauth2::class => Env::get('MODEL_OAUTH_2', \Zemit\Models\Oauth2::class),
        \Zemit\Models\Profile::class => Env::get('MODEL_PROFILE', \Zemit\Models\Profile::class),
        \Zemit\Models\User::class => Env::get('MODEL_USER', \Zemit\Models\User::class),
        \Zemit\Models\UserType::class => Env::get('MODEL_USER_TYPE', \Zemit\Models\UserType::class),
        \Zemit\Models\UserGroup::class => Env::get('MODEL_USER_GROUP', \Zemit\Models\UserGroup::class),
        \Zemit\Models\UserRole::class => Env::get('MODEL_USER_ROLE', \Zemit\Models\UserRole::class),
        \Zemit\Models\UserFeature::class => Env::get('MODEL_USER_FEATURE', \Zemit\Models\UserFeature::class),
        \Zemit\Models\Role::class => Env::get('MODEL_ROLE', \Zemit\Models\Role::class),
        \Zemit\Models\RoleRole::class => Env::get('MODEL_ROLE_ROLE', \Zemit\Models\RoleRole::class),
        \Zemit\Models\RoleFeature::class => Env::get('MODEL_ROLE_FEATURE', \Zemit\Models\RoleFeature::class),
        \Zemit\Models\Group::class => Env::get('MODEL_GROUP', \Zemit\Models\Group::class),
        \Zemit\Models\GroupRole::class => Env::get('MODEL_GROUP_ROLE', \Zemit\Models\GroupRole::class),
        \Zemit\Models\GroupType::class => Env::get('MODEL_GROUP_TYPE', \Zemit\Models\GroupType::class),
        \Zemit\Models\GroupFeature::class => Env::get('MODEL_GROUP_FEATURE', \Zemit\Models\GroupFeature::class),
        \Zemit\Models\Type::class => Env::get('MODEL_TYPE', \Zemit\Models\Type::class),
        \Zemit\Models\Feature::class => Env::get('MODEL_FEATURE', \Zemit\Models\Feature::class),
    ],
]);
```

## Models Service (`models`)

!!! info "Models Service Provider"
    Models Service Provider (`models`):
    [`\Zemit\Provider\Models\ServiceProvider`](https://github.com/phalcon-kit/core/blob/master/src/Provider/Models/ServiceProvider.php){:target="_blank"}

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
