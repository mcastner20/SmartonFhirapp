# Generated by Django 3.0.8 on 2020-09-02 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conditions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.TextField()),
                ('immunizations', models.TextField()),
                ('allergies', models.TextField()),
                ('medications', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Demographics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q26', models.CharField(max_length=100, null=True)),
                ('q27', models.CharField(max_length=100, null=True)),
                ('q28a', models.BooleanField(null=True)),
                ('q28b', models.BooleanField(null=True)),
                ('q28c', models.BooleanField(null=True)),
                ('q28d', models.BooleanField(null=True)),
                ('q28e', models.BooleanField(null=True)),
                ('q28f', models.BooleanField(null=True)),
                ('q29a', models.BooleanField(null=True)),
                ('q29b', models.BooleanField(null=True)),
                ('q29c', models.BooleanField(null=True)),
                ('q29d', models.BooleanField(null=True)),
                ('q29e', models.BooleanField(null=True)),
                ('q29f', models.BooleanField(null=True)),
                ('q30', models.CharField(max_length=100, null=True)),
                ('q31', models.CharField(max_length=100, null=True)),
                ('q32', models.CharField(max_length=100, null=True)),
                ('q33a', models.BooleanField(null=True)),
                ('q33b', models.BooleanField(null=True)),
                ('q33c', models.BooleanField(null=True)),
                ('q33d', models.BooleanField(null=True)),
                ('q33e', models.BooleanField(null=True)),
                ('q33f', models.BooleanField(null=True)),
                ('q33g', models.BooleanField(null=True)),
                ('q34', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q0', models.CharField(max_length=100, null=True)),
                ('q1', models.CharField(max_length=100, null=True)),
                ('q2', models.CharField(max_length=100, null=True)),
                ('q3', models.CharField(max_length=100, null=True)),
                ('q4', models.CharField(max_length=100, null=True)),
                ('q5', models.CharField(max_length=100, null=True)),
                ('q6', models.CharField(max_length=100, null=True)),
                ('q7', models.CharField(max_length=100, null=True)),
                ('q8', models.CharField(max_length=100, null=True)),
                ('q9', models.CharField(max_length=100, null=True)),
                ('q10', models.CharField(max_length=100, null=True)),
                ('q11', models.CharField(max_length=100, null=True)),
                ('q12', models.CharField(max_length=100, null=True)),
                ('q13', models.CharField(max_length=100, null=True)),
                ('q14', models.CharField(max_length=100, null=True)),
                ('q15', models.CharField(max_length=100, null=True)),
                ('q16', models.CharField(max_length=100, null=True)),
                ('q17', models.CharField(max_length=100, null=True)),
                ('q18', models.CharField(max_length=100, null=True)),
                ('q19', models.CharField(max_length=100, null=True)),
                ('q20', models.CharField(max_length=100, null=True)),
                ('q21', models.CharField(max_length=100, null=True)),
                ('q22', models.CharField(max_length=100, null=True)),
                ('q23', models.CharField(max_length=100, null=True)),
                ('q24', models.CharField(max_length=100, null=True)),
                ('q25', models.CharField(max_length=100, null=True)),
                ('q26', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hazard_continued',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q0', models.IntegerField(null=True)),
                ('q1', models.IntegerField(null=True)),
                ('q2', models.IntegerField(null=True)),
                ('q3', models.IntegerField(null=True)),
                ('q4', models.IntegerField(null=True)),
                ('q5', models.IntegerField(null=True)),
                ('q6', models.IntegerField(null=True)),
                ('q7', models.IntegerField(null=True)),
                ('q8', models.IntegerField(null=True)),
                ('q9', models.IntegerField(null=True)),
                ('q10', models.IntegerField(null=True)),
                ('q11', models.IntegerField(null=True)),
                ('q12', models.IntegerField(null=True)),
                ('q13', models.IntegerField(null=True)),
                ('q14', models.IntegerField(null=True)),
                ('q15', models.IntegerField(null=True)),
                ('q16', models.IntegerField(null=True)),
                ('q17', models.IntegerField(null=True)),
                ('q18', models.IntegerField(null=True)),
                ('q19', models.IntegerField(null=True)),
                ('q20', models.IntegerField(null=True)),
                ('q21', models.IntegerField(null=True)),
                ('q22', models.IntegerField(null=True)),
                ('q23', models.IntegerField(null=True)),
                ('q24', models.IntegerField(null=True)),
                ('q25', models.IntegerField(null=True)),
                ('q26', models.IntegerField(null=True)),
                ('q27', models.IntegerField(null=True)),
                ('q28', models.IntegerField(null=True)),
                ('q29', models.IntegerField(null=True)),
                ('q30', models.IntegerField(null=True)),
                ('q31', models.IntegerField(null=True)),
                ('q32', models.IntegerField(null=True)),
                ('q33', models.IntegerField(null=True)),
                ('q34', models.IntegerField(null=True)),
                ('q35', models.IntegerField(null=True)),
                ('q36', models.IntegerField(null=True)),
                ('q37', models.IntegerField(null=True)),
                ('q38', models.IntegerField(null=True)),
                ('q39', models.IntegerField(null=True)),
                ('q40', models.IntegerField(null=True)),
                ('q41', models.IntegerField(null=True)),
                ('q42', models.IntegerField(null=True)),
                ('q43', models.IntegerField(null=True)),
                ('q44', models.IntegerField(null=True)),
                ('q45', models.IntegerField(null=True)),
                ('q46', models.IntegerField(null=True)),
                ('q47', models.IntegerField(null=True)),
                ('q48', models.IntegerField(null=True)),
                ('q49', models.IntegerField(null=True)),
                ('q50', models.IntegerField(null=True)),
                ('q51', models.IntegerField(null=True)),
                ('q52', models.IntegerField(null=True)),
                ('q53', models.IntegerField(null=True)),
                ('q54', models.IntegerField(null=True)),
                ('q55', models.IntegerField(null=True)),
                ('q56', models.IntegerField(null=True)),
                ('q57', models.IntegerField(null=True)),
                ('q58', models.IntegerField(null=True)),
                ('q59', models.IntegerField(null=True)),
                ('q0a', models.BooleanField(null=True)),
                ('q1a', models.BooleanField(null=True)),
                ('q2a', models.BooleanField(null=True)),
                ('q3a', models.BooleanField(null=True)),
                ('q4a', models.BooleanField(null=True)),
                ('q5a', models.BooleanField(null=True)),
                ('q6a', models.BooleanField(null=True)),
                ('q7a', models.BooleanField(null=True)),
                ('q8a', models.BooleanField(null=True)),
                ('q9a', models.BooleanField(null=True)),
                ('q10a', models.BooleanField(null=True)),
                ('q11a', models.BooleanField(null=True)),
                ('q12a', models.BooleanField(null=True)),
                ('q13a', models.BooleanField(null=True)),
                ('q14a', models.BooleanField(null=True)),
                ('q15a', models.BooleanField(null=True)),
                ('q16a', models.BooleanField(null=True)),
                ('q17a', models.BooleanField(null=True)),
                ('q18a', models.BooleanField(null=True)),
                ('q19a', models.BooleanField(null=True)),
                ('q20a', models.BooleanField(null=True)),
                ('q21a', models.BooleanField(null=True)),
                ('q22a', models.BooleanField(null=True)),
                ('q23a', models.BooleanField(null=True)),
                ('q24a', models.BooleanField(null=True)),
                ('q25a', models.BooleanField(null=True)),
                ('q26a', models.BooleanField(null=True)),
                ('q27a', models.BooleanField(null=True)),
                ('q28a', models.BooleanField(null=True)),
                ('q29a', models.BooleanField(null=True)),
                ('q30a', models.BooleanField(null=True)),
                ('q31a', models.BooleanField(null=True)),
                ('q32a', models.BooleanField(null=True)),
                ('q33a', models.BooleanField(null=True)),
                ('q34a', models.BooleanField(null=True)),
                ('q35a', models.BooleanField(null=True)),
                ('q36a', models.BooleanField(null=True)),
                ('q37a', models.BooleanField(null=True)),
                ('q38a', models.BooleanField(null=True)),
                ('q39a', models.BooleanField(null=True)),
                ('q40a', models.BooleanField(null=True)),
                ('q41a', models.BooleanField(null=True)),
                ('q42a', models.BooleanField(null=True)),
                ('q43a', models.BooleanField(null=True)),
                ('q44a', models.BooleanField(null=True)),
                ('q45a', models.BooleanField(null=True)),
                ('q46a', models.BooleanField(null=True)),
                ('q47a', models.BooleanField(null=True)),
                ('q48a', models.BooleanField(null=True)),
                ('q49a', models.BooleanField(null=True)),
                ('q50a', models.BooleanField(null=True)),
                ('q51a', models.BooleanField(null=True)),
                ('q52a', models.BooleanField(null=True)),
                ('q53a', models.BooleanField(null=True)),
                ('q54a', models.BooleanField(null=True)),
                ('q55a', models.BooleanField(null=True)),
                ('q56a', models.BooleanField(null=True)),
                ('q57a', models.BooleanField(null=True)),
                ('q58a', models.BooleanField(null=True)),
                ('q59a', models.BooleanField(null=True)),
                ('q0b', models.BooleanField(null=True)),
                ('q1b', models.BooleanField(null=True)),
                ('q2b', models.BooleanField(null=True)),
                ('q3b', models.BooleanField(null=True)),
                ('q4b', models.BooleanField(null=True)),
                ('q5b', models.BooleanField(null=True)),
                ('q6b', models.BooleanField(null=True)),
                ('q7b', models.BooleanField(null=True)),
                ('q8b', models.BooleanField(null=True)),
                ('q9b', models.BooleanField(null=True)),
                ('q10b', models.BooleanField(null=True)),
                ('q11b', models.BooleanField(null=True)),
                ('q12b', models.BooleanField(null=True)),
                ('q13b', models.BooleanField(null=True)),
                ('q14b', models.BooleanField(null=True)),
                ('q15b', models.BooleanField(null=True)),
                ('q16b', models.BooleanField(null=True)),
                ('q17b', models.BooleanField(null=True)),
                ('q18b', models.BooleanField(null=True)),
                ('q19b', models.BooleanField(null=True)),
                ('q20b', models.BooleanField(null=True)),
                ('q21b', models.BooleanField(null=True)),
                ('q22b', models.BooleanField(null=True)),
                ('q23b', models.BooleanField(null=True)),
                ('q24b', models.BooleanField(null=True)),
                ('q25b', models.BooleanField(null=True)),
                ('q26b', models.BooleanField(null=True)),
                ('q27b', models.BooleanField(null=True)),
                ('q28b', models.BooleanField(null=True)),
                ('q29b', models.BooleanField(null=True)),
                ('q30b', models.BooleanField(null=True)),
                ('q31b', models.BooleanField(null=True)),
                ('q32b', models.BooleanField(null=True)),
                ('q33b', models.BooleanField(null=True)),
                ('q34b', models.BooleanField(null=True)),
                ('q35b', models.BooleanField(null=True)),
                ('q36b', models.BooleanField(null=True)),
                ('q37b', models.BooleanField(null=True)),
                ('q38b', models.BooleanField(null=True)),
                ('q39b', models.BooleanField(null=True)),
                ('q40b', models.BooleanField(null=True)),
                ('q41b', models.BooleanField(null=True)),
                ('q42b', models.BooleanField(null=True)),
                ('q43b', models.BooleanField(null=True)),
                ('q44b', models.BooleanField(null=True)),
                ('q45b', models.BooleanField(null=True)),
                ('q46b', models.BooleanField(null=True)),
                ('q47b', models.BooleanField(null=True)),
                ('q48b', models.BooleanField(null=True)),
                ('q49b', models.BooleanField(null=True)),
                ('q50b', models.BooleanField(null=True)),
                ('q51b', models.BooleanField(null=True)),
                ('q52b', models.BooleanField(null=True)),
                ('q53b', models.BooleanField(null=True)),
                ('q54b', models.BooleanField(null=True)),
                ('q55b', models.BooleanField(null=True)),
                ('q56b', models.BooleanField(null=True)),
                ('q57b', models.BooleanField(null=True)),
                ('q58b', models.BooleanField(null=True)),
                ('q59b', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hazard_probability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q0', models.IntegerField(null=True)),
                ('q1', models.IntegerField(null=True)),
                ('q2', models.IntegerField(null=True)),
                ('q3', models.IntegerField(null=True)),
                ('q4', models.IntegerField(null=True)),
                ('q5', models.IntegerField(null=True)),
                ('q6', models.IntegerField(null=True)),
                ('q7', models.IntegerField(null=True)),
                ('q8', models.IntegerField(null=True)),
                ('q9', models.IntegerField(null=True)),
                ('q10', models.IntegerField(null=True)),
                ('q11', models.IntegerField(null=True)),
                ('q12', models.IntegerField(null=True)),
                ('q13', models.IntegerField(null=True)),
                ('q14', models.IntegerField(null=True)),
                ('q15', models.IntegerField(null=True)),
                ('q16', models.IntegerField(null=True)),
                ('q17', models.IntegerField(null=True)),
                ('q18', models.IntegerField(null=True)),
                ('q19', models.IntegerField(null=True)),
                ('q20', models.IntegerField(null=True)),
                ('q21', models.IntegerField(null=True)),
                ('q22', models.IntegerField(null=True)),
                ('q23', models.IntegerField(null=True)),
                ('q24', models.IntegerField(null=True)),
                ('q25', models.IntegerField(null=True)),
                ('q26', models.IntegerField(null=True)),
                ('q27', models.IntegerField(null=True)),
                ('q28', models.IntegerField(null=True)),
                ('q29', models.IntegerField(null=True)),
                ('q30', models.IntegerField(null=True)),
                ('q31', models.IntegerField(null=True)),
                ('q32', models.IntegerField(null=True)),
                ('q33', models.IntegerField(null=True)),
                ('q34', models.IntegerField(null=True)),
                ('q35', models.IntegerField(null=True)),
                ('q36', models.IntegerField(null=True)),
                ('q37', models.IntegerField(null=True)),
                ('q38', models.IntegerField(null=True)),
                ('q39', models.IntegerField(null=True)),
                ('q40', models.IntegerField(null=True)),
                ('q41', models.IntegerField(null=True)),
                ('q42', models.IntegerField(null=True)),
                ('q43', models.IntegerField(null=True)),
                ('q44', models.IntegerField(null=True)),
                ('q45', models.IntegerField(null=True)),
                ('q46', models.IntegerField(null=True)),
                ('q47', models.IntegerField(null=True)),
                ('q48', models.IntegerField(null=True)),
                ('q49', models.IntegerField(null=True)),
                ('q50', models.IntegerField(null=True)),
                ('q51', models.IntegerField(null=True)),
                ('q52', models.IntegerField(null=True)),
                ('q53', models.IntegerField(null=True)),
                ('q54', models.IntegerField(null=True)),
                ('q55', models.IntegerField(null=True)),
                ('q56', models.IntegerField(null=True)),
                ('q57', models.IntegerField(null=True)),
                ('q58', models.IntegerField(null=True)),
                ('q59', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hazards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q0', models.BooleanField(null=True)),
                ('q1', models.BooleanField(null=True)),
                ('q2', models.BooleanField(null=True)),
                ('q3', models.BooleanField(null=True)),
                ('q4', models.BooleanField(null=True)),
                ('q5', models.BooleanField(null=True)),
                ('q6', models.BooleanField(null=True)),
                ('q7', models.BooleanField(null=True)),
                ('q8', models.BooleanField(null=True)),
                ('q9', models.BooleanField(null=True)),
                ('q10', models.BooleanField(null=True)),
                ('q11', models.BooleanField(null=True)),
                ('q12', models.BooleanField(null=True)),
                ('q13', models.BooleanField(null=True)),
                ('q14', models.BooleanField(null=True)),
                ('q15', models.BooleanField(null=True)),
                ('q16', models.BooleanField(null=True)),
                ('q17', models.BooleanField(null=True)),
                ('q18', models.BooleanField(null=True)),
                ('q19', models.BooleanField(null=True)),
                ('q20', models.BooleanField(null=True)),
                ('q21', models.BooleanField(null=True)),
                ('q22', models.BooleanField(null=True)),
                ('q23', models.BooleanField(null=True)),
                ('q24', models.BooleanField(null=True)),
                ('q25', models.BooleanField(null=True)),
                ('q26', models.BooleanField(null=True)),
                ('q27', models.BooleanField(null=True)),
                ('q28', models.BooleanField(null=True)),
                ('q29', models.BooleanField(null=True)),
                ('q30', models.BooleanField(null=True)),
                ('q31', models.BooleanField(null=True)),
                ('q32', models.BooleanField(null=True)),
                ('q33', models.BooleanField(null=True)),
                ('q34', models.BooleanField(null=True)),
                ('q35', models.BooleanField(null=True)),
                ('q36', models.BooleanField(null=True)),
                ('q37', models.BooleanField(null=True)),
                ('q38', models.BooleanField(null=True)),
                ('q39', models.BooleanField(null=True)),
                ('q40', models.BooleanField(null=True)),
                ('q41', models.BooleanField(null=True)),
                ('q42', models.BooleanField(null=True)),
                ('q43', models.BooleanField(null=True)),
                ('q44', models.BooleanField(null=True)),
                ('q45', models.BooleanField(null=True)),
                ('q46', models.BooleanField(null=True)),
                ('q47', models.BooleanField(null=True)),
                ('q48', models.BooleanField(null=True)),
                ('q49', models.BooleanField(null=True)),
                ('q50', models.BooleanField(null=True)),
                ('q51', models.BooleanField(null=True)),
                ('q52', models.BooleanField(null=True)),
                ('q53', models.BooleanField(null=True)),
                ('q54', models.BooleanField(null=True)),
                ('q55', models.BooleanField(null=True)),
                ('q56', models.BooleanField(null=True)),
                ('q57', models.BooleanField(null=True)),
                ('q58', models.BooleanField(null=True)),
                ('q59', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
            ],
        ),
    ]
