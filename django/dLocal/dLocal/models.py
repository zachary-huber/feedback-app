# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Forms(models.Model):
    form_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    form_json = models.TextField(db_column='form_JSON', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'forms'


class ProjectsForm(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    created_at = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects_form'


class ProjectsProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    demo_link = models.CharField(max_length=2000, blank=True, null=True)
    source_link = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField()
    id = models.CharField(primary_key=True, max_length=32)
    vote_ratio = models.IntegerField(blank=True, null=True)
    vote_total = models.IntegerField(blank=True, null=True)
    featured_image = models.CharField(max_length=100, blank=True, null=True)
    owner = models.ForeignKey('UsersProfile', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects_project'


class ProjectsProjectTags(models.Model):
    id = models.BigAutoField(primary_key=True)
    project = models.ForeignKey(ProjectsProject, models.DO_NOTHING)
    tag = models.ForeignKey('ProjectsTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'projects_project_tags'
        unique_together = (('project', 'tag'),)


class ProjectsResponse(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    created = models.DateTimeField()
    response_text = models.TextField(blank=True, null=True)
    form = models.ForeignKey(ProjectsForm, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'projects_response'


class ProjectsReview(models.Model):
    body = models.TextField(blank=True, null=True)
    value = models.CharField(max_length=200)
    created = models.DateTimeField()
    id = models.CharField(primary_key=True, max_length=32)
    project = models.ForeignKey(ProjectsProject, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'projects_review'


class ProjectsTag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField()
    id = models.CharField(primary_key=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'projects_tag'


class Responses(models.Model):
    response_id = models.AutoField(primary_key=True)
    form = models.ForeignKey(Forms, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    response_json = models.TextField(db_column='response_JSON', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'responses'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    last_login = models.DateTimeField(blank=True, null=True)
    is_admin = models.IntegerField()
    user_avatar = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users'


class UsersProfile(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.CharField(max_length=100, blank=True, null=True)
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField()
    id = models.CharField(primary_key=True, max_length=32)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_profile'


class UsersSkill(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    id = models.CharField(primary_key=True, max_length=32)
    owner = models.ForeignKey(UsersProfile, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_skill'
