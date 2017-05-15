from __future__ import absolute_import

from .base import BulkModelDeletionTask, ModelDeletionTask, ModelRelation  # NOQA
from .manager import DeletionTaskManager

default_manager = DeletionTaskManager(default_task=ModelDeletionTask)


def load_defaults():
    from sentry import models
    from . import defaults

    default_manager.register(models.Activity, BulkModelDeletionTask)
    default_manager.register(models.ApiApplication, defaults.ApiApplicationDeletionTask)
    default_manager.register(models.ApiKey, BulkModelDeletionTask)
    default_manager.register(models.ApiGrant, BulkModelDeletionTask)
    default_manager.register(models.ApiToken, BulkModelDeletionTask)
    default_manager.register(models.CommitAuthor, BulkModelDeletionTask)
    default_manager.register(models.CommitFileChange, BulkModelDeletionTask)
    default_manager.register(models.EnvironmentProject, BulkModelDeletionTask)
    default_manager.register(models.Event, defaults.EventDeletionTask)
    default_manager.register(models.EventMapping, BulkModelDeletionTask)
    default_manager.register(models.EventTag, BulkModelDeletionTask)
    default_manager.register(models.EventUser, BulkModelDeletionTask)
    default_manager.register(models.Group, defaults.GroupDeletionTask)
    default_manager.register(models.GroupAssignee, BulkModelDeletionTask)
    default_manager.register(models.GroupBookmark, BulkModelDeletionTask)
    default_manager.register(models.GroupCommitResolution, BulkModelDeletionTask)
    default_manager.register(models.GroupEmailThread, BulkModelDeletionTask)
    default_manager.register(models.GroupHash, BulkModelDeletionTask)
    default_manager.register(models.GroupMeta, BulkModelDeletionTask)
    default_manager.register(models.GroupRedirect, BulkModelDeletionTask)
    default_manager.register(models.GroupRelease, BulkModelDeletionTask)
    default_manager.register(models.GroupResolution, BulkModelDeletionTask)
    default_manager.register(models.GroupRuleStatus, BulkModelDeletionTask)
    default_manager.register(models.GroupSeen, BulkModelDeletionTask)
    default_manager.register(models.GroupSnooze, BulkModelDeletionTask)
    default_manager.register(models.GroupSubscription, BulkModelDeletionTask)
    default_manager.register(models.GroupTagKey, BulkModelDeletionTask)
    default_manager.register(models.GroupTagValue, BulkModelDeletionTask)
    default_manager.register(models.Organization, defaults.OrganizationDeletionTask)
    default_manager.register(models.OrganizationMemberTeam, BulkModelDeletionTask)
    default_manager.register(models.Project, defaults.ProjectDeletionTask)
    default_manager.register(models.ProjectBookmark, BulkModelDeletionTask)
    default_manager.register(models.ProjectKey, BulkModelDeletionTask)
    default_manager.register(models.Repository, defaults.RepositoryDeletionTask)
    default_manager.register(models.SavedSearch, BulkModelDeletionTask)
    default_manager.register(models.SavedSearchUserDefault, BulkModelDeletionTask)
    default_manager.register(models.TagKey, defaults.TagKeyDeletionTask)
    default_manager.register(models.TagValue, BulkModelDeletionTask)
    default_manager.register(models.Team, defaults.TeamDeletionTask)
    default_manager.register(models.UserReport, BulkModelDeletionTask)


load_defaults()

get = default_manager.get
register = default_manager.register
