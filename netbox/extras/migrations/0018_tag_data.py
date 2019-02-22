# Generated by Django 2.1.4 on 2019-02-20 06:56

from django.db import migrations, models
import django.db.models.deletion
import utilities.fields


def copy_tags(apps, schema_editor):
    """
    Copy data from taggit_tag to extras_tag
    """
    TaggitTag = apps.get_model('taggit', 'Tag')
    ExtrasTag = apps.get_model('extras', 'Tag')

    tags_values = TaggitTag.objects.all().values('id', 'name', 'slug')
    tags = [ExtrasTag(**tag) for tag in tags_values]
    ExtrasTag.objects.bulk_create(tags)


def copy_taggeditems(apps, schema_editor):
    """
    Copy data from taggit_taggeditem to extras_taggeditem
    """
    TaggitTaggedItem = apps.get_model('taggit', 'TaggedItem')
    ExtrasTaggedItem = apps.get_model('extras', 'TaggedItem')

    tagged_items_values = TaggitTaggedItem.objects.all().values('id', 'object_id', 'content_type_id', 'tag_id')
    tagged_items = [ExtrasTaggedItem(**tagged_item) for tagged_item in tagged_items_values]
    ExtrasTaggedItem.objects.bulk_create(tagged_items)


def delete_taggit_taggeditems(apps, schema_editor):
    """
    Delete all TaggedItem instances from taggit_taggeditem
    """
    TaggitTaggedItem = apps.get_model('taggit', 'TaggedItem')
    TaggitTaggedItem.objects.all().delete()


def delete_taggit_tags(apps, schema_editor):
    """
    Delete all Tag instances from taggit_tag
    """
    TaggitTag = apps.get_model('taggit', 'Tag')
    TaggitTag.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0017_tag_taggeditem'),
        ('circuits', '0015_custom_tag_models'),
        ('dcim', '0070_custom_tag_models'),
        ('ipam', '0025_custom_tag_models'),
        ('secrets', '0006_custom_tag_models'),
        ('tenancy', '0006_custom_tag_models'),
        ('virtualization', '0009_custom_tag_models'),
    ]

    operations = [
        migrations.RunPython(copy_tags),
        migrations.RunPython(copy_taggeditems),
        migrations.RunPython(delete_taggit_taggeditems),
        migrations.RunPython(delete_taggit_tags),
    ]
