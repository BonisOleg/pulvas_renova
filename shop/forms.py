from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "name",
            "phone",
            "comment",
            "ad_group",
            "utm_source",
            "utm_medium",
            "utm_campaign",
            "utm_content",
            "utm_term",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Ваше ім'я", "autocomplete": "name"}
            ),
            "phone": forms.TextInput(
                attrs={"placeholder": "+380", "type": "tel", "autocomplete": "tel"}
            ),
            "comment": forms.Textarea(
                attrs={
                    "placeholder": (
                        "Опиши річ, назву моделі або встав посилання "
                        "з сайту бренду / Instagram / Pinterest"
                    ),
                    "rows": 3,
                }
            ),
            "ad_group": forms.HiddenInput(),
            "utm_source": forms.HiddenInput(),
            "utm_medium": forms.HiddenInput(),
            "utm_campaign": forms.HiddenInput(),
            "utm_content": forms.HiddenInput(),
            "utm_term": forms.HiddenInput(),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get("phone", "").strip()
        digits = "".join(c for c in phone if c.isdigit())
        if len(digits) < 10:
            raise forms.ValidationError("Введіть коректний номер телефону")
        return phone
