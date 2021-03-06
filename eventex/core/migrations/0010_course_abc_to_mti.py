# Generated by Django 3.1.2 on 2020-11-11 17:21

from django.db import migrations


def copy_src_to_dest(Source, Destination):
    for src in Source.objects.all():
        dest = Destination(
            title=src.title,
            start=src.start,
            description=src.description,
            slots=src.slots,
        )
        dest.save()
        dest.speakers.set(src.speakers.all())
        src.delete()


def forward_course_abc_to_mti(apps, schema_editor):
    """
    para cada ABC, instanciar um MTI com todos os atributos
    salvar o MTI
    associar os speakers do ABC no MTI
    deletar o abc
    """
    copy_src_to_dest(
        apps.get_model('core', 'CourseOld'),
        apps.get_model('core', 'Course'),
    )


def backwards_course_abc_to_mti(apps, schema_editor):
    """
    é o movimento contrário da função 
    forward_course_abc_to_mti
    """
    copy_src_to_dest(
        apps.get_model('core', 'CourseOld'),
        apps.get_model('core', 'Course'),
    )


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_course'),
    ]

    operations = [
        migrations.RunPython(forward_course_abc_to_mti,
                             backwards_course_abc_to_mti,)
    ]
