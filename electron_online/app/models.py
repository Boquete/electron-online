from django.db import models
# from django.template.defaultfilters import slugify

'''
def app_source_path(instance, filename):
    return '{0}/app_{1}/{2}/{3}'.format(slugify(instance.app.author), slugify(instance.app.name), instance.version, filename)


def app_destiny_path(instance, filename):
    return '{0}/app_{1}/{2}/{3}/{4}'.format(slugify(instance.app.author), slugify(instance.app.name),instance.version, "build", filename)
'''

class App(models.Model):
    name = models.CharField(max_length=120, unique=True, blank=False)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=120)

    def save(self, *args, **kwargs):
        print('save() is called.')
        super(App, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Version(models.Model):
    app = models.ForeignKey(App)
    version = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        print('save() is called.')
        super(Version, self).save(*args, **kwargs)

    git_url = models.URLField(default="https://github.com/Boquete/electron-online-example.git")
    # source_local = models.FileField(upload_to=app_source_path, blank=True)
    destiny_git_url = models.URLField(default="https://github.com/Boquete/electron-online-example.git")
    # destiny_local = models.FilePathField(path=app_destiny_path, editable=False)
    config_editor = models.TextField(blank=True)
    config_file = models.URLField(default="https://github.com/Boquete/electron-online-example/blob/master/electron_config.js", blank=True)

    def __unicode__(self):
        return self.version

    def __str__(self):
        return self.version



