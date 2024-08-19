from django import template

register = template.Library()

@register.filter
def add_class(field, css_class):
    """Ajoute une classe CSS à un champ de formulaire."""
    if not field.field.widget.attrs:
        field.field.widget.attrs = {}
    current_classes = field.field.widget.attrs.get('class', '')
    new_classes = f'{current_classes} {css_class}'.strip()
    field.field.widget.attrs['class'] = new_classes
    return field
