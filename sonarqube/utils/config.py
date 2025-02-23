API_COMPONENTS_SHOW_ENDPOINT = "/api/components/show"

API_PROJECTS_BULK_DELETE_ENDPOINT = "/api/projects/bulk_delete"
API_PROJECTS_SEARCH_ENDPOINT = "/api/projects/search"
API_PROJECTS_CREATE_ENDPOINT = "/api/projects/create"
API_PROJECTS_DELETE_ENDPOINT = "/api/projects/delete"
API_PROJECTS_UPDATE_VISIBILITY_ENDPOINT = "/api/projects/update_visibility"
API_PROJECTS_UPDATE_KEY_ENDPOINT = "/api/projects/update_key"
API_PROJECTS_UPDATE_DEFAULT_VISIBILITY_ENDPOINT = 'api/projects/update_default_visibility'

API_APPLICATIONS_ADD_PROJECT_ENDPOINT = "/api/applications/add_project"
API_APPLICATIONS_REMOVE_PROJECT_ENDPOINT = "/api/applications/remove_project"
API_APPLICATIONS_SHOW_ENDPOINT = "/api/applications/show"
API_APPLICATIONS_CREATE_ENDPOINT = "/api/applications/create"
API_APPLICATIONS_DELETE_ENDPOINT = "/api/applications/delete"
API_APPLICATIONS_UPDATE_ENDPOINT = "/api/applications/update"
API_APPLICATIONS_CREATE_BRANCH_ENDPOINT = "/api/applications/create_branch"
API_APPLICATIONS_DELETE_BRANCH_ENDPOINT = "/api/applications/delete_branch"
API_APPLICATIONS_UPDATE_BRANCH_ENDPOINT = "/api/applications/update_branch"
API_APPLICATIONS_SET_TAGS_ENDPOINT = "/api/applications/set_tags"

API_USERS_SEARCH_ENDPOINT = "/api/users/search"
API_USERS_CREATE_ENDPOINT = "/api/users/create"
API_USERS_UPDATE_ENDPOINT = "/api/users/update"
API_USERS_CHANGE_PASSWORD_ENDPOINT = "/api/users/change_password"
API_USERS_GROUPS_ENDPOINT = "/api/users/groups"
API_USERS_DEACTIVATE_ENDPOINT = "/api/users/deactivate"
API_USERS_UPDATE_LOGIN_ENDPOINT = "/api/users/update_login"

API_USER_GROUPS_SEARCH_ENDPOINT = "/api/user_groups/search"
API_USER_GROUPS_CREATE_ENDPOINT = "/api/user_groups/create"
API_USER_GROUPS_DELETE_ENDPOINT = "/api/user_groups/delete"
API_USER_GROUPS_UPDATE_ENDPOINT = "/api/user_groups/update"
API_USER_GROUPS_USERS_ENDPOINT = "/api/user_groups/users"
API_USER_GROUPS_ADD_USER_ENDPOINT = "/api/user_groups/add_user"
API_USER_GROUPS_REMOVE_USER_ENDPOINT = "/api/user_groups/remove_user"

API_PERMISSIONS_ADD_GROUP_ENDPOINT = "/api/permissions/add_group"
API_PERMISSIONS_REMOVE_GROUP_ENDPOINT = "/api/permissions/remove_group"
API_PERMISSIONS_ADD_USER_ENDPOINT = "/api/permissions/add_user"
API_PERMISSIONS_REMOVE_USER_ENDPOINT = "/api/permissions/remove_user"
API_PERMISSIONS_APPLY_TEMPLATE_ENDPOINT = "/api/permissions/apply_template"
API_PERMISSIONS_ADD_GROUP_TO_TEMPLATE_ENDPOINT = (
    "/api/permissions/add_group_to_template"
)
API_PERMISSIONS_ADD_PROJECT_CREATOR_TO_TEMPLATE_ENDPOINT = (
    "/api/permissions/add_project_creator_to_template"
)
API_PERMISSIONS_ADD_USER_TO_TEMPLATE_ENDPOINT = "/api/permissions/add_user_to_template"
API_PERMISSIONS_BULK_APPLY_TEMPLATE_ENDPOINT = "/api/permissions/bulk_apply_template"
API_PERMISSIONS_CREATE_TEMPLATE_ENDPOINT = "/api/permissions/create_template"
API_PERMISSIONS_DELETE_TEMPLATE_ENDPOINT = "/api/permissions/delete_template"
API_PERMISSIONS_REMOVE_GROUP_FROM_TEMPLATE_ENDPOINT = (
    "/api/permissions/remove_group_from_template"
)
API_PERMISSIONS_REMOVE_PROJECT_CREATOR_FROM_TEMPLATE_ENDPOINT = (
    "/api/permissions/remove_project_creator_from_template"
)
API_PERMISSIONS_REMOVE_USER_FROM_TEMPLATE_ENDPOINT = (
    "/api/permissions/remove_user_from_template"
)
API_PERMISSIONS_SEARCH_TEMPLATES_ENDPOINT = "/api/permissions/search_templates"
API_PERMISSIONS_SET_DEFAULT_TEMPLATE_ENDPOINT = "/api/permissions/set_default_template"
API_PERMISSIONS_UPDATE_TEMPLATE_ENDPOINT = "/api/permissions/update_template"

API_CE_ACTIVITY_ENDPOINT = "/api/ce/activity"
API_CE_ACTIVITY_STATUS_ENDPOINT = "/api/ce/activity_status"
API_CE_ANALYSIS_STATUS_ENDPOINT = "/api/ce/analysis_status"
API_CE_COMPONENT_ENDPOINT = "/api/ce/component"
API_CE_TASK_ENDPOINT = "/api/ce/task"

API_MEASURES_COMPONENT_ENDPOINT = "/api/measures/component"
API_MEASURES_COMPONENT_TREE_ENDPOINT = "/api/measures/component_tree"
API_MEASURES_SEARCH_HISTORY_ENDPOINT = "/api/measures/search_history"

API_PROJECT_BRANCHES_LIST_ENDPOINT = "/api/project_branches/list"
API_PROJECT_BRANCHES_RENAME_ENDPOINT = "/api/project_branches/rename"
API_PROJECT_BRANCHES_DELETE_ENDPOINT = "/api/project_branches/delete"
API_PROJECT_BRANCHES_SET_PROTECTION_ENDPOINT = "/api/project_branches/set_automatic_deletion_protection"

API_NOTIFICATIONS_ADD_ENDPOINT = "/api/notifications/add"
API_NOTIFICATIONS_LIST_ENDPOINT = "/api/notifications/list"
API_NOTIFICATIONS_REMOVE_ENDPOINT = "/api/notifications/remove"

API_ISSUES_SEARCH_ENDPOINT = "/api/issues/search"
API_ISSUES_ASSIGN_ENDPOINT = "/api/issues/assign"
API_ISSUES_DO_TRANSITION_ENDPOINT = "/api/issues/do_transition"
API_ISSUES_ADD_COMMENT_ENDPOINT = "/api/issues/add_comment"
API_ISSUES_EDIT_COMMENT_ENDPOINT = "/api/issues/edit_comment"
API_ISSUES_DELETE_COMMENT_ENDPOINT = "/api/issues/delete_comment"
API_ISSUES_SET_SEVERITY_ENDPOINT = "/api/issues/set_severity"
API_ISSUES_SET_TYPE_ENDPOINT = "/api/issues/set_type"
API_ISSUES_AUTHORS_ENDPOINT = "/api/issues/authors"
API_ISSUES_BULK_CHANGE_ENDPOINT = "/api/issues/bulk_change"
API_ISSUES_CHANGELOG_ENDPOINT = "/api/issues/changelog"
API_ISSUES_SET_TAGS_ENDPOINT = "/api/issues/set_tags"
API_ISSUES_TAGS_ENDPOINT = "/api/issues/tags"

API_PROJECT_LINKS_CREATE_ENDPOINT = "/api/project_links/create"
API_PROJECT_LINKS_DELETE_ENDPOINT = "/api/project_links/delete"
API_PROJECT_LINKS_SEARCH_ENDPOINT = "/api/project_links/search"

API_QUALITYGATES_PROJECT_STATUS_ENDPOINT = "/api/qualitygates/project_status"
API_QUALITYGATES_LIST_ENDPOINT = "/api/qualitygates/list"
API_QUALITYGATES_SELECT_ENDPOINT = "/api/qualitygates/select"
API_QUALITYGATES_DESELECT_ENDPOINT = "/api/qualitygates/deselect"
API_QUALITYGATES_SHOW_ENDPOINT = "/api/qualitygates/show"
API_QUALITYGATES_GET_BY_PROJECT_ENDPOINT = "/api/qualitygates/get_by_project"
API_QUALITYGATES_COPY_ENDPOINT = "/api/qualitygates/copy"
API_QUALITYGATES_CREATE_ENDPOINT = "/api/qualitygates/create"
API_QUALITYGATES_CREATE_CONDITION_ENDPOINT = "/api/qualitygates/create_condition"
API_QUALITYGATES_DELETE_CONDITION_ENDPOINT = "/api/qualitygates/delete_condition"
API_QUALITYGATES_DESTROY_ENDPOINT = "/api/qualitygates/destroy"
API_QUALITYGATES_RENAME_ENDPOINT = "/api/qualitygates/rename"
API_QUALITYGATES_SEARCH_ENDPOINT = "/api/qualitygates/search"
API_QUALITYGATES_SET_AS_DEFAULT_ENDPOINT = "/api/qualitygates/set_as_default"
API_QUALITYGATES_UPDATE_CONDITION_ENDPOINT = "/api/qualitygates/update_condition"

API_COMPONTENTS_SHOW_ENDPOINT = "/api/components/show"
API_COMPONTENTS_SEARCH_ENDPOINT = "/api/components/search"
API_COMPONTENTS_TREE_ENDPOINT = "/api/components/tree"

API_RULES_SEARCH_ENDPOINT = "/api/rules/search"
API_RULES_CREATE_ENDPOINT = "/api/rules/create"
API_RULES_UPDATE_ENDPOINT = "/api/rules/update"
API_RULES_DELETE_ENDPOINT = "/api/rules/delete"
API_RULES_SHOW_ENDPOINT = "/api/rules/show"
API_RULES_TAGS_ENDPOINT = "/api/rules/tags"
API_RULES_REPOSITORIES_ENDPOINT = "/api/rules/repositories"

API_QUALITYPROFILES_ACTIVATE_RULE_ENDPOINT = "/api/qualityprofiles/activate_rule"
API_QUALITYPROFILES_SEARCH_ENDPOINT = "/api/qualityprofiles/search"
API_QUALITYPROFILES_DELETE_ENDPOINT = "/api/qualityprofiles/delete"
API_QUALITYPROFILES_SET_DEFAULT_ENDPOINT = "/api/qualityprofiles/set_default"
API_QUALITYPROFILES_ADD_PROJECT_ENDPOINT = "/api/qualityprofiles/add_project"
API_QUALITYPROFILES_REMOVE_PROJECT_ENDPOINT = "/api/qualityprofiles/remove_project"
API_QUALITYPROFILES_ACTIVATE_RULES_ENDPOINT = "/api/qualityprofiles/activate_rules"
API_QUALITYPROFILES_BACKUP_ENDPOINT = "/api/qualityprofiles/backup"
API_QUALITYPROFILES_CHANGE_PARENT_ENDPOINT = "/api/qualityprofiles/change_parent"
API_QUALITYPROFILES_CHANGELOG_ENDPOINT = "/api/qualityprofiles/changelog"
API_QUALITYPROFILES_COPY_ENDPOINT = "/api/qualityprofiles/copy"
API_QUALITYPROFILES_CREATE_ENDPOINT = "/api/qualityprofiles/create"
API_QUALITYPROFILES_DEACTIVATE_RULE_ENDPOINT = "/api/qualityprofiles/deactivate_rule"
API_QUALITYPROFILES_DEACTIVATE_RULES_ENDPOINT = "/api/qualityprofiles/deactivate_rules"
API_QUALITYPROFILES_EXPORT_ENDPOINT = "/api/qualityprofiles/export"
API_QUALITYPROFILES_EXPORTERS_ENDPOINT = "/api/qualityprofiles/exporters"
API_QUALITYPROFILES_IMPORTERS_ENDPOINT = "/api/qualityprofiles/importers"
API_QUALITYPROFILES_INHERITANCE_ENDPOINT = "/api/qualityprofiles/inheritance"
API_QUALITYPROFILES_PROJECTS_ENDPOINT = "/api/qualityprofiles/projects"
API_QUALITYPROFILES_RENAME_ENDPOINT = "/api/qualityprofiles/rename"
API_QUALITYPROFILES_RESTORE_ENDPOINT = "/api/qualityprofiles/restore"

API_DUPLICATIONS_SHOW_ENDPOINT = "/api/duplications/show"

API_PDFREPORT_GET_ENDPOINT = "/api/pdfreport/get"

API_METRICS_SEARCH_ENDPOINT = "/api/metrics/search"
API_METRICS_TYPES_ENDPOINT = "/api/metrics/types"

API_NEW_CODE_PERIODS_LIST_ENDPOINT = "/api/new_code_periods/list"
API_NEW_CODE_PERIODS_SET_ENDPOINT = "/api/new_code_periods/set"
API_NEW_CODE_PERIODS_SHOW_ENDPOINT = "/api/new_code_periods/show"
API_NEW_CODE_PERIODS_UNSET_ENDPOINT = "/api/new_code_periods/unset"

API_SETTINGS_LIST_DEFINITIONS_ENDPOINT = "/api/settings/list_definitions"
API_SETTINGS_RESET_ENDPOINT = "/api/settings/reset"
API_SETTINGS_SET_ENDPOINT = "/api/settings/set"
API_SETTINGS_VALUES_ENDPOINT = "/api/settings/values"

API_SOURCES_SCM_ENDPOINT = "/api/sources/scm"
API_SOURCES_SHOW_ENDPOINT = "/api/sources/show"
API_SOURCES_RAW_ENDPOINT = "/api/sources/raw"

API_AUTH_LOGIN_ENDPOINT = "/api/authentication/login"
API_AUTH_LOGOUT_ENDPOINT = "/api/authentication/logout"
API_AUTH_VALIDATE_ENDPOINT = "/api/authentication/validate"

API_FAVORITES_ADD_ENDPOINT = "/api/favorites/add"
API_FAVORITES_REMOVE_ENDPOINT = "/api/favorites/remove"
API_FAVORITES_SEARCH_ENDPOINT = "/api/favorites/search"

API_HOTSPOTS_SEARCH_ENDPOINT = "/api/hotspots/search"
API_HOTSPOTS_SHOW_ENDPOINT = "/api/hotspots/show"

API_LANGUAGES_LIST_ENDPOINT = "/api/languages/list"

API_PROJECT_BADGES_MEASURE_ENDPOINT = "/api/project_badges/measure"
API_PROJECT_BADGES_QUALITY_GATE_ENDPOINT = "/api/project_badges/quality_gate"

API_PROJECT_TAGS_SEARCH_ENDPOINT = "/api/project_tags/search"
API_PROJECT_TAGS_SET_ENDPOINT = "/api/project_tags/set"

API_PROJECT_PULL_REQUESTS_DELETE_ENDPOINT = "/api/project_pull_requests/delete"
API_PROJECT_PULL_REQUESTS_LIST_ENDPOINT = "/api/project_pull_requests/list"

API_PROJECT_ANALYSES_CREATE_EVENT_ENDPOINT = "/api/project_analyses/create_event"
API_PROJECT_ANALYSES_DELETE_ENDPOINT = "/api/project_analyses/delete"
API_PROJECT_ANALYSES_DELETE_EVENT_ENDPOINT = "/api/project_analyses/delete_event"
API_PROJECT_ANALYSES_SEARCH_ENDPOINT = "/api/project_analyses/search"
API_PROJECT_ANALYSES_SET_BASELINE_ENDPOINT = "/api/project_analyses/set_baseline"
API_PROJECT_ANALYSES_UNSET_BASELINE_ENDPOINT = "/api/project_analyses/unset_baseline"
API_PROJECT_ANALYSES_UPDATE_EVENT_ENDPOINT = "/api/project_analyses/update_event"

API_SERVER_VERSION_ENDPOINT = "/api/server/version"

API_USER_TOKENS_GENERATE_ENDPOINT = "/api/user_tokens/generate"
API_USER_TOKENS_REVOKE_ENDPOINT = "/api/user_tokens/revoke"
API_USER_TOKENS_SEARCH_ENDPOINT = "/api/user_tokens/search"

API_WEBHOOKS_CREATE_ENDPOINT = "/api/webhooks/create"
API_WEBHOOKS_DELETE_ENDPOINT = "/api/webhooks/delete"
API_WEBHOOKS_DELIVERIES_ENDPOINT = "/api/webhooks/deliveries"
API_WEBHOOKS_DELIVERY_ENDPOINT = "/api/webhooks/delivery"
API_WEBHOOKS_LIST_ENDPOINT = "/api/webhooks/list"
API_WEBHOOKS_UPDATE_ENDPOINT = "/api/webhooks/update"

API_WEBSERVICES_LIST_ENDPOINT = "/api/webservices/list"
API_WEBSERVICES_RESPONSE_EXAMPLE_ENDPOINT = "/api/webservices/response_example"

API_SYSTEM_CHANGE_LOG_LEVEL_ENDPOINT = "/api/system/change_log_level"
API_SYSTEM_DB_MIGRATION_STATUS_ENDPOINT = "/api/system/db_migration_status"
API_SYSTEM_HEALTH_ENDPOINT = "/api/system/health"
API_SYSTEM_LOGS_ENDPOINT = "/api/system/logs"
API_SYSTEM_MIGRATE_DB_ENDPOINT = "/api/system/migrate_db"
API_SYSTEM_PING_ENDPOINT = "/api/system/ping"
API_SYSTEM_RESTART_ENDPOINT = "/api/system/restart"
API_SYSTEM_STATUS_ENDPOINT = "/api/system/status"
API_SYSTEM_UPGRADES_ENDPOINT = "/api/system/upgrades"
API_SYSTEM_INFO_ENDPOINT = "/api/system/info"

API_PLUGINS_AVAILABLE_ENDPOINT = "/api/plugins/available"
API_PLUGINS_CANCEL_ALL_ENDPOINT = "/api/plugins/cancel_all"
API_PLUGINS_INSTALL_ENDPOINT = "/api/plugins/install"
API_PLUGINS_INSTALLED_ENDPOINT = "/api/plugins/installed"
API_PLUGINS_PENDING_ENDPOINT = "/api/plugins/pending"
API_PLUGINS_UNINSTALL_ENDPOINT = "/api/plugins/uninstall"
API_PLUGINS_UPDATE_ENDPOINT = "/api/plugins/update"
API_PLUGINS_UPDATES_ENDPOINT = "/api/plugins/updates"

API_PROJECT_DUMP_EXPORT_ENDPOINT = "/api/project_dump/export"
API_PROJECT_DUMP_IMPORT_ENDPOINT = "/api/project_dump/import"

API_ALM_INTEGRATION_SET_PAT = "/api/alm_integrations/set_pat"
API_ALM_INTEGRATION_SEARCH_GITLAB_REPOS = "/api/alm_integrations/search_gitlab_repos"
API_ALM_INTEGRATION_SEARCH_BITBUCKETSERVER_REPOS = "/api/alm_integrations/search_bitbucketserver_repos"
API_ALM_INTEGRATION_SEARCH_AZURE_REPOS = "/api/alm_integrations/search_azure_repos"
API_ALM_INTEGRATION_SEARCH_BITBUCKETSERVER_PROJECTS = "/api/alm_integrations/list_bitbucketserver_projects"
API_ALM_INTEGRATION_LIST_AZURE_PROJECTS = "/api/alm_integrations/list_azure_projects"
API_ALM_INTEGRATION_IMPORT_GITLAB_PROJECT = "/api/alm_integrations/import_gitlab_project"

API_ALM_SETTINGS_VALIDATE = "/api/alm_settings/validate"
API_ALM_SETTINGS_UPDATE_GITLAB = "/api/alm_settings/update_gitlab"
API_ALM_SETTINGS_UPDATE_GITHUB = "/api/alm_settings/update_github"
API_ALM_SETTINGS_UPDATE_BITBUCKET = "/api/alm_settings/update_bitbucket"
API_ALM_SETTINGS_UPDATE_AZURE = "/api/alm_settings/update_azure"
API_ALM_SETTINGS_SET_GITLAB_BINDING = "/api/alm_settings/set_gitlab_binding"
API_ALM_SETTINGS_SET_GITHUB_BINDING = "/api/alm_settings/set_github_binding"
API_ALM_SETTINGS_SET_BITBUCKET_BINDING = "/api/alm_settings/set_bitbucket_binding"
API_ALM_SETTINGS_SET_AZURE_BINDING = "/api/alm_settings/set_azure_binding"
API_ALM_SETTINGS_LIST_DEFINITIONS = "/api/alm_settings/list_definitions"
API_ALM_SETTINGS_LIST = "/api/alm_settings/list"
API_ALM_SETTINGS_DELETE = "/api/alm_settings/delete"
API_ALM_SETTINGS_GET_BINDING = "/api/alm_settings/get_binding"
API_ALM_SETTINGS_DELETE_BINDING = "/api/alm_settings/delete_binding"
API_ALM_SETTINGS_CREATE_GITLAB = "/api/alm_settings/create_gitlab"
API_ALM_SETTINGS_CREATE_GITHUB = "/api/alm_settings/create_github"
API_ALM_SETTINGS_CREATE_BITBUCKET = "/api/alm_settings/create_bitbucket"
API_ALM_SETTINGS_CREATE_AZURE = "/api/alm_settings/create_azure"
API_ALM_SETTINGS_COUNT_BINDING = "/api/alm_settings/count_binding"

API_EDITIONS_SET_LICENSE = "/api/editions/set_license"

API_VIEWS_UPDATE = "/api/views/update"
API_VIEWS_SHOW = "/api/views/show"
API_VIEWS_SET_TAGS_MODE = "/api/views/set_tags_mode"
API_VIEWS_SET_REMAINING_PROJECTS_MODE = "/api/views/set_remaining_projects_mode"
API_VIEWS_SET_REGEXP_MODE = "/api/views/set_regexp_mode"
API_VIEWS_SET_MANUAL_MODE = "/api/views/set_manual_mode"
API_VIEWS_REMOVE_PROJECT = "/api/views/remove_project"
API_VIEWS_MOVE_OPTIONS = "/api/views/move_options"
API_VIEWS_MOVE = "/api/views/move"
API_VIEWS_LOCAL_VIEWS = "/api/views/local_views"
API_VIEWS_LIST = "/api/views/list"
API_VIEWS_DEFINITION = "/api/views/definition"
API_VIEWS_DEFINE = "/api/views/define"
API_VIEWS_CREATE = "/api/views/create"
API_VIEWS_DELETE = "/api/views/delete"
API_VIEWS_ADD_SUB_VIEW = "/api/views/add_sub_view"
API_VIEWS_ADD_PROJECT = "/api/views/add_project"
API_VIEWS_ADD_LOCAL_VIEW = "/api/views/add_local_view"
