from django.contrib.admin.views.decorators import staff_member_required
from recipecart.cart import Cart
from django.shortcuts import get_object_or_404, redirect, render
from .forms import Order, OrderCreateForm
from .models import OrderItem
from .tasks import order_created

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            # clear the cart
            cart.clear()
            # launch asynchronous task
            order_created.delay(order.id)
            # set the order in the session
            request.session['order_id'] = order.id
            # redirect for payment
            return redirect('recipepayment:process')
    else:
        form = OrderCreateForm()
    return render(
        request,
        'recipeorders/order/create.html',
        {'cart': cart, 'form': form}
    )

@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(
        request, 'admin/recipeorders/order/detail.html', {'order': order}
    )
