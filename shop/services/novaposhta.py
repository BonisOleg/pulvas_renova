import requests
from django.conf import settings

NP_URL = "https://api.novaposhta.ua/v2.0/json/"
TIMEOUT = 5


def _post(model_name: str, method: str, properties: dict) -> dict:
    payload = {
        "apiKey": settings.NP_API_KEY,
        "modelName": model_name,
        "calledMethod": method,
        "methodProperties": properties,
    }
    try:
        response = requests.post(NP_URL, json=payload, timeout=TIMEOUT)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return {"success": False, "data": []}


def search_cities(query: str) -> list[dict]:
    if not query or len(query) < 2:
        return []

    result = _post(
        "Address",
        "searchSettlements",
        {"CityName": query, "Limit": "10"},
    )

    cities = []
    if result.get("success") and result.get("data"):
        for item in result["data"]:
            for address in item.get("Addresses", []):
                cities.append(
                    {
                        "ref": address.get("Ref", ""),
                        "name": address.get("Present", ""),
                        "area": address.get("SettlementTypeCode", ""),
                    }
                )
    return cities


def get_warehouses(city_ref: str) -> list[dict]:
    if not city_ref:
        return []

    result = _post(
        "AddressGeneral",
        "getWarehouses",
        {
            "SettlementRef": city_ref,
            "TypeOfWarehouseRef": "",
            "Limit": "100",
        },
    )

    warehouses = []
    if result.get("success") and result.get("data"):
        for item in result["data"]:
            warehouses.append(
                {
                    "ref": item.get("Ref", ""),
                    "name": item.get("Description", ""),
                    "short": item.get("ShortAddress", ""),
                }
            )
    return warehouses
