import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt

from .models import ShoeColor, Order
from .forms import OrderForm
from .services.novaposhta import search_cities, get_warehouses
from .services.telegram import send_order_notification


def landing(request):
    colors = ShoeColor.objects.filter(is_available=True)
    form = OrderForm()
    return render(request, "shop/landing.html", {"colors": colors, "form": form})


@require_POST
def create_order(request):
    form = OrderForm(request.POST)
    if form.is_valid():
        order = form.save()
        send_order_notification(order)
        return render(request, "shop/partials/order_success.html", {"order": order})
    return render(
        request,
        "shop/partials/order_form.html",
        {"form": form},
        status=422,
    )


@require_POST
def np_cities(request):
    try:
        body = json.loads(request.body)
        query = body.get("query", "").strip()
    except (json.JSONDecodeError, AttributeError):
        query = request.POST.get("query", "").strip()

    cities = search_cities(query)
    return render(request, "shop/partials/city_results.html", {"cities": cities})


@require_POST
def np_warehouses(request):
    try:
        body = json.loads(request.body)
        city_ref = body.get("city_ref", "").strip()
    except (json.JSONDecodeError, AttributeError):
        city_ref = request.POST.get("city_ref", "").strip()

    warehouses = get_warehouses(city_ref)
    return render(
        request, "shop/partials/warehouse_results.html", {"warehouses": warehouses}
    )


@require_GET
def colors_json(request):
    colors = ShoeColor.objects.filter(is_available=True).values(
        "id", "name", "hex_code", "image"
    )
    data = []
    for c in colors:
        data.append(
            {
                "id": c["id"],
                "name": c["name"],
                "hex_code": c["hex_code"],
                "image": request.build_absolute_uri(f"/media/{c['image']}"),
            }
        )
    return JsonResponse({"colors": data})
