from equipment.models import Equipment
from django import template


register = template.Library()


@register.inclusion_tag('cart.html')
def get_cart(request):
    cart = request.session.get('cart', [])
    equipment = Equipment.objects.filter(id__in=cart)
    return {'cart': equipment}


@register.assignment_tag()
def cart_length(request):
    cart = request.session.get('cart', [])
    return len(cart)


@register.filter
def to_class_name(value):
    return value.__class__.__name__


@register.filter
def checkconflict(obj, index):
    return obj.checkconflict(index)
