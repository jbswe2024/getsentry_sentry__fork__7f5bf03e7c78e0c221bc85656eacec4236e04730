# Generated by Django 5.1.1 on 2024-12-04 17:57

from django.apps.registry import Apps
from django.db import migrations
from django.db.backends.base.schema import BaseDatabaseSchemaEditor

from sentry.new_migrations.migrations import CheckedMigration


def remove_grouping_auto_update_option(
    apps: Apps, _schema_editor: BaseDatabaseSchemaEditor
) -> None:
    ProjectOption = apps.get_model("sentry", "ProjectOption")

    for option in ProjectOption.objects.filter(key="sentry:grouping_auto_update"):
        option.delete()


class Migration(CheckedMigration):
    # This flag is used to mark that a migration shouldn't be automatically run in production.
    # This should only be used for operations where it's safe to run the migration after your
    # code has deployed. So this should not be used for most operations that alter the schema
    # of a table.
    # Here are some things that make sense to mark as post deployment:
    # - Large data migrations. Typically we want these to be run manually so that they can be
    #   monitored and not block the deploy for a long period of time while they run.
    # - Adding indexes to large tables. Since this can take a long time, we'd generally prefer to
    #   run this outside deployments so that we don't block them. Note that while adding an index
    #   is a schema change, it's completely safe to run the operation after the code has deployed.
    # Once deployed, run these manually via: https://develop.sentry.dev/database-migrations/#migration-deployment

    is_post_deployment = False

    dependencies = [
        ("sentry", "0801_drop_incidentseen_incidentsubscription"),
    ]

    operations = [
        migrations.RunPython(
            remove_grouping_auto_update_option,
            migrations.RunPython.noop,
            hints={"tables": ["sentry_projectoptions"]},
        ),
    ]
