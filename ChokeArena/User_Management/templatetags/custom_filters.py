from django import template
from django.forms.utils import flatatt

register = template.Library()

@register.filter
def add_class(field, css_class):
    """Ajoute une classe CSS à un champ de formulaire."""
    if not hasattr(field, 'field') or not field.field.widget.attrs:
        return field

    # Assurez-vous que le champ est bien un champ de formulaire
    widget = field.field.widget
    attrs = widget.attrs.copy()
    current_classes = attrs.get('class', '')
    new_classes = f'{current_classes} {css_class}'.strip()
    attrs['class'] = new_classes

    # Modifiez les attributs du widget et renvoyez le champ
    widget.attrs = attrs
    return field
