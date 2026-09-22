from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skills_shop', '0005_rename_demande_to_query'),
    ]

    operations = [
        migrations.RenameField(
            model_name='query',
            old_name='utilisateur',
            new_name='user',
        ),
    ]
