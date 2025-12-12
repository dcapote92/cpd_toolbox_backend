from django.db import models


SECTION_CHOICES = (
    ('FRL', 'Frente de Loja'),
    ('ACO', 'Açougue'),
    ('PEI', 'Peixaria'),
    ('FRI', 'Frios e Laticinios'),
    ('PAD', 'Padaria'),
    ('HOR', 'Hortifrúti'),
    ('DOC', 'Docas Secas'),
    ('DOCF', 'Docas Frias')
)


class Section(models.Model):
    name = models.CharField(
        max_length=100,
        choices=SECTION_CHOICES,
    )

    def __str__(self):
        return self.name
