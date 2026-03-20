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
                attrs={
                    "placeholder": "+380 (XX) XXX-XX-XX",
                    "type": "tel",
                    "autocomplete": "tel",
                    "data-phone-mask": "",
                    "inputmode": "tel",
                }
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

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["name"].required = False

    def clean_phone(self) -> str:
        raw: str = self.cleaned_data.get("phone", "").strip()
        digits = "".join(c for c in raw if c.isdigit())

        # Normalize: leading 0 → 380..., leading 380... stays as-is
        if digits.startswith("0") and len(digits) == 10:
            digits = "38" + digits
        elif digits.startswith("80") and len(digits) == 11:
            digits = "3" + digits

        if len(digits) != 12 or not digits.startswith("380"):
            raise forms.ValidationError(
                "Введіть коректний номер телефону (+380 XX XXX-XX-XX)"
            )

        return f"+{digits}"
