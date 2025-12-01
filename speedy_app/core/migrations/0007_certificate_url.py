from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_certificate_image_alter_certificate_icon_svg"),
    ]

    operations = [
        migrations.AddField(
            model_name="certificate",
            name="url",
            field=models.URLField(blank=True, null=True, help_text="Optional: Link to open when certificate is clicked."),
        ),
    ]
