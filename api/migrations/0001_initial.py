# Generated by Django 3.0 on 2019-12-24 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Defensa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=250)),
                ('fecha_hora', models.DateTimeField()),
                ('calificacion', models.DecimalField(decimal_places=2, max_digits=2)),
                ('mencion_publicacion', models.BooleanField()),
                ('mencion_honorifica', models.BooleanField()),
                ('nota', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Propuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('fecha_entrega', models.DateTimeField()),
                ('titulo', models.CharField(max_length=250)),
                ('estatus', models.CharField(choices=[('PE', 'Por Evaluar'), ('DI', 'Diferida'), ('AP', 'Aprobada'), ('RE', 'Rechazada')], default='PE', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_rol', models.CharField(choices=[('AD', 'Administrador'), ('GT', 'Gestor'), ('IN', 'Invitado')], default='IN', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=15)),
                ('tipo', models.CharField(choices=[('PR', 'Profesor'), ('ES', 'Estudiante'), ('EX', 'Externo')], default='ES', max_length=2)),
                ('primer_nombre', models.CharField(max_length=10)),
                ('segundo_nombre', models.CharField(max_length=10, null=True)),
                ('primer_apellido', models.CharField(max_length=10)),
                ('segundo_apellido', models.CharField(max_length=10, null=True)),
                ('correo_ucab', models.CharField(max_length=250, null=True)),
                ('correo_personal', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('telefono_uno', models.CharField(max_length=11, null=True)),
                ('telefono_dos', models.CharField(max_length=11, null=True)),
                ('observaciones', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioPropuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_propuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Propuesta')),
                ('fk_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='TrabajoDeGrado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=250)),
                ('titulo', models.CharField(max_length=250)),
                ('nrc', models.CharField(max_length=50)),
                ('descriptores', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('fecha_entrega', models.DateTimeField()),
                ('nombre_empresa', models.CharField(max_length=100, null=True)),
                ('estatus', models.CharField(choices=[('PE', 'Por Entregar'), ('EP', 'Entregado y Pendiente por Defender'), ('DI', 'Diferido'), ('AP', 'Aprobada'), ('AC', 'Aprobada con Solicitud de Correciones'), ('RE', 'Rechazada')], default='PE', max_length=2)),
                ('fk_propuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Propuesta')),
                ('fk_term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Term')),
            ],
        ),
        migrations.AddField(
            model_name='propuesta',
            name='fk_term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Term'),
        ),
        migrations.CreateModel(
            name='Jurado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suplente', models.BooleanField()),
                ('fk_defensa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Defensa')),
                ('fk_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='defensa',
            name='fk_trabajo_grado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.TrabajoDeGrado'),
        ),
        migrations.CreateModel(
            name='Correcciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('fk_defensa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Defensa')),
            ],
        ),
    ]
