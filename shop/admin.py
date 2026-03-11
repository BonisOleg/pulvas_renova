from django.contrib import admin
from django.utils.html import format_html
from .models import ShoeColor, Order


@admin.register(ShoeColor)
class ShoeColorAdmin(admin.ModelAdmin):
    list_display = ("name", "color_preview", "is_available", "sort_order")
    list_editable = ("is_available", "sort_order")
    list_display_links = ("name",)

    def color_preview(self, obj):
        return format_html(
            '<span style="display:inline-block;width:24px;height:24px;'
            'border-radius:50%;background:{};border:1px solid #ccc;"></span>',
            obj.hex_code,
        )

    color_preview.short_description = "Колір"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "phone",
        "shoe_color",
        "size",
        "city_name",
        "warehouse_name",
        "status",
        "created_at",
    )
    list_filter = ("status", "shoe_color", "size")
    search_fields = ("name", "phone", "city_name")
    list_editable = ("status",)
    readonly_fields = ("created_at",)
    date_hierarchy = "created_at"

    fieldsets = (
        ("Покупець", {"fields": ("name", "phone", "comment")}),
        ("Замовлення", {"fields": ("shoe_color", "size")}),
        (
            "Доставка",
            {
                "fields": (
                    "city_name",
                    "city_ref",
                    "warehouse_name",
                    "warehouse_ref",
                )
            },
        ),
        ("Статус", {"fields": ("status", "created_at")}),
    )
