import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills_shop', '0004_demande_utilisateur'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Demande',
            new_name='Query',
        ),
        migrations.AlterField(
            model_name='query',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='queries', to='skills_shop.skill'),
        ),
        migrations.AlterField(
            model_name='query',
            name='utilisateur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='queries', to=settings.AUTH_USER_MODEL),
        ),
    ]
