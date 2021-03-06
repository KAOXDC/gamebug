# Generated by Django 3.1.7 on 2021-10-20 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('code', models.CharField(max_length=20)),
                ('dev_card', models.PositiveIntegerField()),
                ('mod_card', models.PositiveIntegerField()),
                ('err_card', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Registred',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_number', models.CharField(choices=[('player 1', 'player 1'), ('player 2', 'player 2'), ('player 3', 'player 3'), ('player 4', 'player 4')], max_length=20)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='game.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='game.player')),
            ],
        ),
        migrations.CreateModel(
            name='Turn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_card', models.CharField(max_length=20)),
                ('mod_card', models.CharField(max_length=20)),
                ('err_card', models.CharField(max_length=20)),
                ('cards', models.CharField(blank=True, max_length=20, null=True)),
                ('correct_card', models.PositiveIntegerField(blank=True, max_length=20, null=True)),
                ('player_request', models.PositiveIntegerField()),
                ('player_reply', models.PositiveIntegerField(blank=True, null=True)),
                ('current_player', models.PositiveIntegerField()),
                ('type', models.CharField(choices=[('blame!', 'blame!'), ('ask!', 'ask!')], max_length=20)),
                ('registred', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.registred')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='cards')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='game.card_type')),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_d1', models.CharField(max_length=50, null=True)),
                ('card_d2', models.CharField(max_length=50, null=True)),
                ('card_d3', models.CharField(max_length=50, null=True)),
                ('card_d4', models.CharField(max_length=50, null=True)),
                ('card_d5', models.CharField(max_length=50, null=True)),
                ('card_d6', models.CharField(max_length=50, null=True)),
                ('card_d7', models.CharField(max_length=50, null=True)),
                ('card_m1', models.CharField(max_length=50, null=True)),
                ('card_m2', models.CharField(max_length=50, null=True)),
                ('card_m3', models.CharField(max_length=50, null=True)),
                ('card_m4', models.CharField(max_length=50, null=True)),
                ('card_m5', models.CharField(max_length=50, null=True)),
                ('card_m6', models.CharField(max_length=50, null=True)),
                ('card_e1', models.CharField(max_length=50, null=True)),
                ('card_e2', models.CharField(max_length=50, null=True)),
                ('card_e3', models.CharField(max_length=50, null=True)),
                ('card_e4', models.CharField(max_length=50, null=True)),
                ('card_e5', models.CharField(max_length=50, null=True)),
                ('card_e6', models.CharField(max_length=50, null=True)),
                ('registred', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='game.registred')),
            ],
        ),
    ]
