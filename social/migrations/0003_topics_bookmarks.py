from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies=[('social','0002_post_image'),migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations=[
        migrations.AddField(model_name='post',name='topic',field=models.CharField(choices=[('BUILD','Build'),('LEARN','Learn'),('EVENTS','Events'),('ASK','Ask'),('OPPORTUNITIES','Opportunities')],default='BUILD',max_length=20)),
        migrations.CreateModel(name='Bookmark',fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('created_at',models.DateTimeField(auto_now_add=True)),('post',models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name='bookmarks',to='social.post')),('user',models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name='bookmarks',to=settings.AUTH_USER_MODEL))]),
        migrations.AddConstraint(model_name='bookmark',constraint=models.UniqueConstraint(fields=('user','post'),name='unique_bookmark')),
    ]
