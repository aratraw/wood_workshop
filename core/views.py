from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from django.utils import timezone
from .models import Project, ShopItem, OrderItem, Order

# Create your views here.


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def contacts(request):
    return render(request, "contacts.html")


class ProjectsView(ListView):
    model = Project
    paginate_by = 10
    template_name = "projects.html"


class ProjectDetailView(DetailView):
    model = Project
    template_name = "project-detail.html"


class Shop(ListView):
    model = ShopItem
    template_name = "shop.html"


class ShopDetail(DetailView):
    model = ShopItem
    template_name = "shop-detail.html"


def checkout(request):
    return render(request, "checkout.html")


def add_to_cart(request, slug):
    item = get_object_or_404(ShopItem, slug=slug)
    order_item = OrderItem.objects.get_or_create(item=item)
    order_querry = Order.objects.filter(user=request.user, ordered=False)
    if order_querry.exists():
        order = order_querry[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        order = Order.objects.create(
            user=request.user, ordered_date=timezone.now())
        order.items.add(order_item)
    return redirect("core:product", slug=slug)


def remove_from_cart(request, slug):
    item = get_object_or_404(ShopItem, slug=slug)
    order_querry = Order.objects.filter(user=request.user, ordered=False)
    if order_querry.exists():
        order = order_querry[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = order.items.filter(item=item)
            order.items.remove(order_item)
        else:
            # add a message(order does not contain item)
            return redirect("core:product", slug=slug)
    else:
        # add a message(order does not exist)
        return redirect("core:product", slug=slug)
    return redirect("core:product", slug=slug)


""" class HomeView():
    template_name = "home.html" """
