from enum import Enum, EnumMeta


class ChoiceEnumMeta(EnumMeta):
    def __iter__(self):
        return ((tag, tag.value) for tag in super().__iter__())

class ChoiceEnum(Enum, metaclass=ChoiceEnumMeta):
    """
    Enum for Django ChoiceField use.

    Usage::

        class Colors(ChoiceEnum):
            red = "Red"
            green = "Green"
            blue = "Blue"

        class MyModel(models.Model):
            color = models.CharField(max_length=20, choices=Colors)
    """
