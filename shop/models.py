from django.db import models


class ShoeColor(models.Model):
    name = models.CharField("Назва кольору", max_length=100)
    hex_code = models.CharField("HEX колір", max_length=7, default="#000000")
    image = models.ImageField("Фото", upload_to="shoes/")
    is_available = models.BooleanField("Доступний", default=True)
    sort_order = models.PositiveSmallIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Колір взуття"
        verbose_name_plural = "Кольори взуття"
        ordering = ["sort_order", "name"]

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_NEW = "new"
    STATUS_PROCESSING = "processing"
    STATUS_SHIPPED = "shipped"
    STATUS_DELIVERED = "delivered"
    STATUS_CANCELLED = "cancelled"

    STATUS_CHOICES = [
        (STATUS_NEW, "Нове"),
        (STATUS_PROCESSING, "В обробці"),
        (STATUS_SHIPPED, "Відправлено"),
        (STATUS_DELIVERED, "Доставлено"),
        (STATUS_CANCELLED, "Скасовано"),
    ]

    SIZES = ["39", "40", "41", "42", "43", "44", "45"]

    name = models.CharField("Ім'я", max_length=150, blank=True, default="")
    phone = models.CharField("Телефон", max_length=20)
    shoe_color = models.ForeignKey(
        ShoeColor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Колір",
    )
    size = models.CharField("Розмір", max_length=5, blank=True, default="")
    city_name = models.CharField("Місто", max_length=200, blank=True, default="")
    city_ref = models.CharField("Ref міста НП", max_length=100, blank=True, default="")
    warehouse_name = models.CharField("Відділення НП", max_length=300, blank=True, default="")
    warehouse_ref = models.CharField("Ref відділення НП", max_length=100, blank=True, default="")
    comment = models.TextField("Коментар", blank=True)

    ad_group = models.CharField("Група оголошень (?g=)", max_length=100, blank=True, default="")
    utm_source = models.CharField("UTM Source", max_length=200, blank=True, default="")
    utm_medium = models.CharField("UTM Medium", max_length=200, blank=True, default="")
    utm_campaign = models.CharField("UTM Campaign", max_length=200, blank=True, default="")
    utm_content = models.CharField("UTM Content", max_length=200, blank=True, default="")
    utm_term = models.CharField("UTM Term", max_length=200, blank=True, default="")

    status = models.CharField(
        "Статус", max_length=20, choices=STATUS_CHOICES, default=STATUS_NEW
    )
    created_at = models.DateTimeField("Дата замовлення", auto_now_add=True)

    class Meta:
        verbose_name = "Замовлення"
        verbose_name_plural = "Замовлення"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        label = self.name or "—"
        return f"#{self.pk} — {label} ({self.phone})"
