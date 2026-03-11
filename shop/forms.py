from django import forms
from .models import Order, ShoeColor


class OrderForm(forms.ModelForm):
    shoe_color = forms.ModelChoiceField(
        queryset=ShoeColor.objects.filter(is_available=True),
        empty_label=None,
        widget=forms.HiddenInput(),
        label="Колір",
    )
    size = forms.ChoiceField(
        choices=[("", "Оберіть розмір")] + [(s, s) for s in Order.SIZES],
        label="Розмір",
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    class Meta:
        model = Order
        fields = [
            "name",
            "phone",
            "shoe_color",
            "size",
            "city_name",
            "city_ref",
            "warehouse_name",
            "warehouse_ref",
            "comment",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Ваше ім'я", "autocomplete": "name"}
            ),
            "phone": forms.TextInput(
                attrs={"placeholder": "+380", "type": "tel", "autocomplete": "tel"}
            ),
            "city_name": forms.TextInput(
                attrs={
                    "placeholder": "Введіть місто",
                    "autocomplete": "off",
                    "id": "city-input",
                }
            ),
            "city_ref": forms.HiddenInput(attrs={"id": "city-ref"}),
            "warehouse_name": forms.TextInput(
                attrs={
                    "placeholder": "Оберіть відділення",
                    "readonly": "readonly",
                    "id": "warehouse-input",
                }
            ),
            "warehouse_ref": forms.HiddenInput(attrs={"id": "warehouse-ref"}),
            "comment": forms.Textarea(
                attrs={"placeholder": "Коментар (необов'язково)", "rows": 2}
            ),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get("phone", "").strip()
        digits = "".join(c for c in phone if c.isdigit())
        if len(digits) < 10:
            raise forms.ValidationError("Введіть коректний номер телефону")
        return phone

    def clean_size(self):
        size = self.cleaned_data.get("size", "")
        if not size:
            raise forms.ValidationError("Оберіть розмір")
        return size
