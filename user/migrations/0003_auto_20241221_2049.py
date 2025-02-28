# Generated by Django 4.2.17 on 2024-12-21 20:49

from django.db import migrations

from django.db import migrations, connection
from django.conf import settings


def fix_admin_log_foreign_key(apps, schema_editor):
    with connection.cursor() as cursor:
        # Drop the old foreign key constraint
        cursor.execute("""
            ALTER TABLE django_admin_log
            DROP CONSTRAINT IF EXISTS django_admin_log_user_id_c564eba6_fk_auth_user_id;
        """)

        # Add the new foreign key constraint pointing to the custom user model
        cursor.execute(f"""
            ALTER TABLE django_admin_log
            ADD CONSTRAINT django_admin_log_user_id_fk
            FOREIGN KEY (user_id)
            REFERENCES {settings.AUTH_USER_MODEL.replace('.', '_')}(id)
            ON DELETE SET NULL
            DEFERRABLE INITIALLY DEFERRED;
        """)


def fix_orphaned_log_entries(apps, schema_editor):
    LogEntry = apps.get_model('admin', 'LogEntry')
    User = apps.get_model(settings.AUTH_USER_MODEL)

    # Set any invalid user_id to NULL to avoid integrity errors
    for log_entry in LogEntry.objects.filter(user_id__isnull=False):
        if not User.objects.filter(id=log_entry.user_id).exists():
            log_entry.user_id = None
            log_entry.save()


class Migration(migrations.Migration):
    dependencies = [
        ('admin', '0001_initial'),  # Ensure this is correct
        ('user', '0002_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.RunPython(fix_orphaned_log_entries),
        migrations.RunPython(fix_admin_log_foreign_key),
    ]
