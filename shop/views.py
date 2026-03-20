import json

from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET, require_POST

from .forms import OrderForm
from .models import Order, ShoeColor
from .services.novaposhta import search_cities, get_warehouses
from .services.telegram import send_order_notification
from .utils import get_group


def landing(request):
    group_key = request.GET.get("g", "")
    group = get_group(group_key)
    colors = ShoeColor.objects.filter(is_available=True)
    utm: dict[str, str] = {
        "ad_group": group_key,
        "utm_source": request.GET.get("utm_source", ""),
        "utm_medium": request.GET.get("utm_medium", ""),
        "utm_campaign": request.GET.get("utm_campaign", ""),
        "utm_content": request.GET.get("utm_content", ""),
        "utm_term": request.GET.get("utm_term", ""),
    }
    form = OrderForm(initial=utm)
    return render(request, "shop/landing.html", {
        "group": group,
        "page_title": group["title"],
        "page_description": group["description"],
        "tg_men_url": settings.TG_MEN_URL,
        "tg_women_url": settings.TG_WOMEN_URL,
        "tg_contact_url": settings.TG_CONTACT_URL,
        "colors": colors,
        "form": form,
    })


@require_POST
def create_order(request):
    form = OrderForm(request.POST)
    if form.is_valid():
        order = form.save()
        send_order_notification(order)
        request.session["last_order_id"] = order.id
        response = HttpResponse(status=204)
        response["HX-Redirect"] = "/success/"
        return response
    return render(
        request,
        "shop/partials/order_form.html",
        {"form": form, "tg_contact_url": settings.TG_CONTACT_URL},
        status=422,
    )


@require_GET
def order_success_page(request):
    order_id = request.session.pop("last_order_id", None)
    order: Order | None = None
    if order_id is not None:
        order = Order.objects.filter(pk=order_id).first()
    return render(request, "shop/success.html", {"order": order})


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
