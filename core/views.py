from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView, View
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


class CartView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, "account/cart.html", context)
        except ObjectDoesNotExist:
            messages.error(self.request, "Нет заказов")
            return redirect('/')


@login_required
def checkout(request):
    return render(request, "checkout.html")


@login_required
def add_to_cart(request, slug):
    if request.user.is_authenticated:
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
    return redirect("core:shop-detail", slug=slug)


@login_required
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
            return redirect("core:project-detail", slug=slug)
    else:
        # add a message(order does not exist)
        return redirect("core:project-detail", slug=slug)
    return redirect("core:project-detail", slug=slug)


""" class HomeView():
    template_name = "home.html" """
