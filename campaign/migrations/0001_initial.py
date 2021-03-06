
import campaign.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [

        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),

    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('details', models.TextField(max_length=2000)),
                ('target', models.PositiveIntegerField()),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(default=campaign.models.in_fourteen_days)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_featured', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donations', to='campaign.campaign')),
                ('donator', models.ForeignKey(default=None, on_delete=models.SET(campaign.models.get_anonymous_user), related_name='donations', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CampaignReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField(max_length=2000)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign.campaign')),
                ('reporter', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CampaignImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.ImageField(upload_to='campaign', verbose_name='Image')),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='campaign.campaign')),
            ],
        ),
        migrations.AddField(
            model_name='campaign',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='campaign.category'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='creator',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='campaigns', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='campaign',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='campaign.campaign')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('campaign', 'user')},
            },
        ),
    ]
