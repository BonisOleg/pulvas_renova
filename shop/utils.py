"""Ad-group content mapping for PulvasStore landing page.

Each entry maps a ``?g=`` URL parameter value to a dict of template context
variables. Unknown / missing values fall back to ``DEFAULT_GROUP``.
"""

from __future__ import annotations

# ── Shared material card sets ─────────────────────────────────────────────────

_BAG_MATERIALS_LABEL = "Матеріали та якість"
_BAG_MATERIALS_HEADING = "Кожна деталь —\nдо дрібниць"

_SHOE_MATERIALS_LABEL = _BAG_MATERIALS_LABEL
_SHOE_MATERIALS_HEADING = _BAG_MATERIALS_HEADING

_ACC_MATERIALS_LABEL = _BAG_MATERIALS_LABEL
_ACC_MATERIALS_HEADING = _BAG_MATERIALS_HEADING

_CLOTH_MATERIALS_LABEL = _BAG_MATERIALS_LABEL
_CLOTH_MATERIALS_HEADING = _BAG_MATERIALS_HEADING

_UNIVERSAL_MATERIALS: list[dict] = [
    {
        "num": "01",
        "title": "Матеріали преміального рівня",
        "text": "Використовуємо добірну шкіру та якісні текстильні матеріали, що зберігають форму і вигляд навіть після тривалого використання. Фактура, щільність та деталі максимально відповідають моделям преміального сегмента.",
    },
    {
        "num": "02",
        "title": "Надійна фурнітура",
        "text": "Замки, кільця та карабіни виконані з міцного металу з якісним покриттям. Вони не тьмяніють, не втрачають вигляду та забезпечують довговічність виробу.",
    },
    {
        "num": "03",
        "title": "Бездоганна збірка",
        "text": "Акуратні подвійні шви, точна геометрія та контроль кожної деталі. Саме це створює бездоганний вигляд і гарантує надійність у щоденному використанні.",
    },
    {
        "num": "04",
        "title": "Комфорт та посадка",
        "text": "Крій, форма та конструкція продумані так, щоб виріб виглядав стильно та зручно сидів. Одяг добре тримає форму, а взуття забезпечує комфорт навіть при тривалому носінні.",
    },
]

_BAG_MATERIALS = _UNIVERSAL_MATERIALS
_SHOE_MATERIALS = _UNIVERSAL_MATERIALS
_ACC_MATERIALS = _UNIVERSAL_MATERIALS
_CLOTH_MATERIALS = _UNIVERSAL_MATERIALS

# ── Shared feature card sets ──────────────────────────────────────────────────

_DEFAULT_FEATURES: list[dict] = [
    {
        "num": "01",
        "title": "Перевірено до дрібниць",
        "text": "Кожен виріб проходить ретельну перевірку перед відправкою. Ми контролюємо матеріали, фурнітуру та якість збірки, щоб ви отримали бездоганний результат.",
    },
    {
        "num": "02",
        "title": "Швидка доставка",
        "text": "Доставка в Україну та по світу займає близько 2-3 тижнів. Вартість доставки вже входить у ціну товару.",
    },
    {
        "num": "03",
        "title": "Мінімальна передплата",
        "text": "Ми берем мінімальну передплату у 30% при доставці в Україну. Доставка по світу відбувається за повною передоплатою. Можлива оплату готівкою в Україні, а також на карту/ USDT, PayPal, Western Union",
    },
    {
        "num": "04",
        "title": "Підтримка та повернення",
        "text": "Персональний менеджер завжди на зв’язку. Якщо товар не підійшов — можливий обмін протягом 7 днів.",
    },
]

# ── Ad group mapping ──────────────────────────────────────────────────────────

AD_GROUPS: dict[str, dict] = {
    # ── ACCESSORIES ───────────────────────────────────────────────────────────

    "Аксесуари_Ремені_Гаманці": {
        "title": "Ремені та гаманці Louis Vuitton, Gucci, Hermès — PulvasStore",
        "description": (
            "Купити ремінь або гаманець Louis Vuitton, Gucci, Hermès, Prada "
            "з доставкою по всьому світу. Преміальна якість."
        ),
        "hero_eyebrow": "Ремені та гаманці · Люксові аксесуари",
        "hero_heading": "Ремені та гаманці\nвищого класу",
        "hero_subtitle": (
            "Louis Vuitton, Gucci, Hermès, Prada — іконічні аксесуари "
            "з бездоганною якістю. Доставка по всьому світу."
        ),
        "hero_price": "149$",
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "show_size_chart": False,
        "materials_label": _ACC_MATERIALS_LABEL,
        "materials_heading": _ACC_MATERIALS_HEADING,
        "materials": _ACC_MATERIALS,
    },

    "Аксесуари_Шарфи_Очки_Інше": {
        "title": "Шарфи Burberry, окуляри Chanel і Dior, кепки Loro Piana — PulvasStore",
        "description": (
            "Купити шарф Burberry, окуляри Chanel або Dior, кепку Loro Piana, "
            "браслет Hermès з доставкою по всьому світу."
        ),
        "hero_eyebrow": "Шарфи, окуляри, аксесуари · Преміум",
        "hero_heading": "Стильні аксесуари\nтоп брендів",
        "hero_subtitle": (
            "Шарфи Burberry, окуляри Chanel і Dior, кепки Loro Piana, "
            "браслети Hermès. Доставка по всьому світу."
        ),
        "hero_price": "99$",
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "show_size_chart": False,
        "materials_label": _ACC_MATERIALS_LABEL,
        "materials_heading": _ACC_MATERIALS_HEADING,
        "materials": _ACC_MATERIALS,
    },

    # ── FOOTWEAR ──────────────────────────────────────────────────────────────

    "Взуття_Balenciaga": {
        "title": "Кросівки Balenciaga — Triple S, Track, Runner — PulvasStore",
        "description": (
            "Купити кросівки Balenciaga Triple S, Track, Runner для жінок і чоловіків. "
            "Доставка по всьому світу."
        ),
        "hero_eyebrow": "Взуття Balenciaga · Нова колекція",
        "hero_heading": "Кросівки\nBalenciaga",
        "hero_subtitle": (
            "Triple S, Track, Runner, Speed — культові моделі для жінок і чоловіків. "
            "Доставка по всьому світу."
        ),
        "hero_price": "249$",
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "show_size_chart": True,
        "materials_label": _SHOE_MATERIALS_LABEL,
        "materials_heading": _SHOE_MATERIALS_HEADING,
        "materials": _SHOE_MATERIALS,
    },

    "Взуття_Dior": {
        "title": "Взуття Dior — кеди, кросівки, туфлі Christian Dior — PulvasStore",
        "description": (
            "Купити кеди або кросівки Dior, Christian Dior для жінок і чоловіків. "
            "Доставка по всьому світу."
        ),
        "hero_eyebrow": "Взуття Dior · Елегантність у кожному кроці",
        "hero_heading": "Взуття\nChristian Dior",
        "hero_subtitle": (
            "Кеди, кросівки, туфлі та сандалі Dior — вишукана елегантність "
            "для жінок і чоловіків. Доставка по всьому світу."
        ),
        "hero_price": "249$",
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "show_size_chart": True,
        "materials_label": _SHOE_MATERIALS_LABEL,
        "materials_heading": _SHOE_MATERIALS_HEADING,
        "materials": _SHOE_MATERIALS,
    },

    "Взуття_Gucci": {
        "title": "Взуття Gucci — кросівки, лофери, кеди — PulvasStore",
        "description": (
            "Купити кросівки або лофери Gucci для жінок і чоловіків. "
            "Доставка по всьому світу."
        ),
        "hero_eyebrow": "Взуття Gucci · Люксовий стиль",
        "hero_heading": "Взуття\nGucci",
        "hero_subtitle": (
            "Кросівки, лофери, кеди та туфлі Gucci — бездоганний стиль "
            "для жінок і чоловіків. Доставка по всьому світу."
        ),
        "hero_price": "219$",
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "show_size_chart": True,
        "materials_label": _SHOE_MATERIALS_LABEL,
        "materials_heading": _SHOE_MATERIALS_HEADING,
        "materials": _SHOE_MATERIALS,
    },

    "Взуття_LV": {
        "title": "Взуття Louis Vuitton — кросівки, кеди, туфлі LV — PulvasStore",
        "description": (
            "Купити кросівки або кеди Louis Vuitton для жінок і чоловіків. "
            "Доставка по всьому світу."
        ),
        "hero_eyebrow": "Взуття Louis Vuitton · Iconic",
        "hero_heading": "Взуття\nLouis Vuitton",
        "hero_subtitle": (
            "Кросівки, кеди, туфлі та лофери LV — легендарний стиль "
            "для жінок і чоловіків. Доставка по всьому світу."
        ),
        "hero_price": "259$",
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "show_size_chart": True,
        "materials_label": _SHOE_MATERIALS_LABEL,
        "materials_heading": _SHOE_MATERIALS_HEADING,
        "materials": _SHOE_MATERIALS,
    },

    "Взуття_Інші": {
        "title": "Взуття Valentino, Loro Piana, Prada, Bottega Veneta — PulvasStore",
        "description": (
            "Купити взуття Valentino, Loro Piana, Prada, Bottega Veneta "
            "з доставкою по всьому світу. Преміальна якість."
        ),
        "hero_eyebrow": "Дизайнерське взуття · Преміальні бренди",
        "hero_heading": "Преміальне взуття\nтоп брендів",
        "hero_subtitle": (
            "Valentino, Loro Piana, Prada, Bottega Veneta — лофери, кросівки, туфлі. "
            "Доставка по всьому світу."
        ),
        "hero_price": "219$",
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "show_size_chart": True,
        "materials_label": _SHOE_MATERIALS_LABEL,
        "materials_heading": _SHOE_MATERIALS_HEADING,
        "materials": _SHOE_MATERIALS,
    },

    "Взуття_Бренд_загальне": {
        "title": "Брендове взуття — кросівки, лофери, туфлі — PulvasStore",
        "description": (
            "Купити брендові кросівки, лофери або туфлі для жінок і чоловіків. "
            "Доставка по всьому світу."
        ),
        "hero_eyebrow": "Брендове взуття · Великий вибір",
        "hero_heading": "Брендове взуття\nдля вас",
        "hero_subtitle": (
            "Великий вибір дизайнерського взуття для жінок і чоловіків — "
            "кросівки, лофери, туфлі. Доставка по всьому світу."
        ),
        "hero_price": "199$",
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "show_size_chart": True,
        "materials_label": _SHOE_MATERIALS_LABEL,
        "materials_heading": _SHOE_MATERIALS_HEADING,
        "materials": _SHOE_MATERIALS,
    },

    # ── CLOTHING ──────────────────────────────────────────────────────────────

    "Одяг_Balenciaga_одяг": {
        "title": "Одяг Balenciaga — футболки, худі, куртки — PulvasStore",
        "description": (
            "Купити футболку, худі або куртку Balenciaga. "
            "Доставка по всьому світу."
        ),
        "hero_eyebrow": "Одяг Balenciaga · Нова колекція",
        "hero_heading": "Одяг\nBalenciaga",
        "hero_subtitle": (
            "Футболки, худі, пуховики і костюми Balenciaga — авангардний стиль "
            "для жінок і чоловіків. Доставка по всьому світу."
        ),
        "hero_price": "179$",
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "show_size_chart": False,
        "materials_label": _CLOTH_MATERIALS_LABEL,
        "materials_heading": _CLOTH_MATERIALS_HEADING,
        "materials": _CLOTH_MATERIALS,
    },

    "Одяг_Gucci_одяг": {
        "title": "Одяг Gucci — футболки, кофти, костюми — PulvasStore",
        "description": (
            "Купити футболку, кофту або костюм Gucci. "
            "Доставка по всьому світу."
        ),
        "hero_eyebrow": "Одяг Gucci · Люксовий стиль",
        "hero_heading": "Одяг\nGucci",
        "hero_subtitle": (
            "Футболки, кофти, штани та костюми Gucci — іконічний стиль "
            "для жінок і чоловіків. Доставка по всьому світу."
        ),
        "hero_price": "169$",
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "show_size_chart": False,
        "materials_label": _CLOTH_MATERIALS_LABEL,
        "materials_heading": _CLOTH_MATERIALS_HEADING,
        "materials": _CLOTH_MATERIALS,
    },

    "Одяг_LoroPiana": {
        "title": "Одяг Loro Piana — куртки, костюми, кашемір — PulvasStore",
        "description": (
            "Купити куртку або костюм Loro Piana. Кашемір і преміальні тканини. "
            "Доставка по всьому світу."
        ),
        "hero_eyebrow": "Loro Piana · Кашемір і розкіш",
        "hero_heading": "Одяг\nLoro Piana",
        "hero_subtitle": (
            "Куртки, костюми і кашемірові вироби Loro Piana — преміальна якість "
            "для справжніх поціновувачів. Доставка по всьому світу."
        ),
        "hero_price": "299$",
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "show_size_chart": False,
        "materials_label": _CLOTH_MATERIALS_LABEL,
        "materials_heading": _CLOTH_MATERIALS_HEADING,
        "materials": _CLOTH_MATERIALS,
    },

    "Одяг_Moncler": {
        "title": "Куртки та пуховики Moncler — PulvasStore",
        "description": (
            "Купити куртку або пуховик Moncler для жінок і чоловіків. "
            "Доставка по всьому світу."
        ),
        "hero_eyebrow": "Moncler · Тепло і стиль",
        "hero_heading": "Куртки та пуховики\nMoncler",
        "hero_subtitle": (
            "Жіночі та чоловічі пуховики Moncler — легкі, теплі, "
            "з бездоганним кроєм. Доставка по всьому світу."
        ),
        "hero_price": "349$",
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "show_size_chart": False,
        "materials_label": _CLOTH_MATERIALS_LABEL,
        "materials_heading": _CLOTH_MATERIALS_HEADING,
        "materials": _CLOTH_MATERIALS,
    },

    "Одяг_StoneIsland": {
        "title": "Одяг Stone Island — куртки, худі, свитшоти — PulvasStore",
        "description": (
            "Купити куртку, худі або свитшот Stone Island. "
            "Доставка по всьому світу."
        ),
        "hero_eyebrow": "Stone Island · Urban Premium",
        "hero_heading": "Одяг\nStone Island",
        "hero_subtitle": (
            "Куртки, худі, свитшоти та жилети Stone Island — культовий стиль "
            "для міського життя. Доставка по всьому світу."
        ),
        "hero_price": "219$",
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "show_size_chart": False,
        "materials_label": _CLOTH_MATERIALS_LABEL,
        "materials_heading": _CLOTH_MATERIALS_HEADING,
        "materials": _CLOTH_MATERIALS,
    },

    # ── BAGS ──────────────────────────────────────────────────────────────────

    "Сумки_Balenciaga": {
        "title": "Сумки Balenciaga — клітчасті, рюкзаки, через плечо — PulvasStore",
        "description": (
            "Купити сумку Balenciaga для жінок і чоловіків. "
            "Клітчасті сумки, рюкзаки, через плечо. Доставка по всьому світу."
        ),
        "hero_eyebrow": "Сумки Balenciaga · Авангард моди",
        "hero_heading": "Сумки\nBalenciaga",
        "hero_subtitle": (
            "Клітчасті сумки, рюкзаки, міські та через плечо — "
            "весь асортимент Balenciaga. Доставка по всьому світу."
        ),
        "hero_price": "219$",
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "show_size_chart": False,
        "materials_label": _BAG_MATERIALS_LABEL,
        "materials_heading": _BAG_MATERIALS_HEADING,
        "materials": _BAG_MATERIALS,
    },

    "Сумки_Chanel": {
        "title": "Сумки Chanel — класика 2.55, Boy, mini — PulvasStore",
        "description": (
            "Купити сумку Chanel, Chanel 2.55, mini Chanel, клатч Chanel "
            "з доставкою по всьому світу."
        ),
        "hero_eyebrow": "Сумки Chanel · Вічна класика",
        "hero_heading": "Сумки\nChanel",
        "hero_subtitle": (
            "Класичні фліп-сумки, 2.55, Boy Chanel, mini та клатчі — "
            "квінтесенція жіночої елегантності. Доставка по всьому світу."
        ),
        "hero_price": "279$",
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "show_size_chart": False,
        "materials_label": _BAG_MATERIALS_LABEL,
        "materials_heading": _BAG_MATERIALS_HEADING,
        "materials": _BAG_MATERIALS,
    },

    "Сумки_Dior": {
        "title": "Сумки Dior — Lady Dior, Miss Dior, Saddle — PulvasStore",
        "description": (
            "Купити сумку Dior, Lady Dior, Miss Dior або Saddle Dior "
            "з доставкою по всьому світу."
        ),
        "hero_eyebrow": "Сумки Dior · Haute Couture",
        "hero_heading": "Сумки\nChristian Dior",
        "hero_subtitle": (
            "Lady Dior, Miss Dior, Saddle, Book Tote — культові моделі "
            "для жінок і чоловіків. Доставка по всьому світу."
        ),
        "hero_price": "249$",
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "show_size_chart": False,
        "materials_label": _BAG_MATERIALS_LABEL,
        "materials_heading": _BAG_MATERIALS_HEADING,
        "materials": _BAG_MATERIALS,
    },

    "Сумки_Gucci": {
        "title": "Сумки Gucci — Ophidia, Dionysus, Jackie — PulvasStore",
        "description": (
            "Купити сумку Gucci, рюкзак Gucci або сумку через плечо Gucci "
            "з доставкою по всьому світу."
        ),
        "hero_eyebrow": "Сумки Gucci · Іконічний стиль",
        "hero_heading": "Сумки\nGucci",
        "hero_subtitle": (
            "Ophidia, Dionysus, Jackie, Horsebit — весь культовий асортимент Gucci "
            "для жінок і чоловіків. Доставка по всьому світу."
        ),
        "hero_price": "219$",
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "show_size_chart": False,
        "materials_label": _BAG_MATERIALS_LABEL,
        "materials_heading": _BAG_MATERIALS_HEADING,
        "materials": _BAG_MATERIALS,
    },

    "Сумки_Hermes_Birkin": {
        "title": "Сумки Hermès Birkin та Kelly — PulvasStore",
        "description": (
            "Купити сумку Hermès Birkin або Kelly з доставкою по всьому світу. "
            "Преміальна якість."
        ),
        "hero_eyebrow": "Hermès Birkin · Kelly · Evelyne",
        "hero_heading": "Сумки Hermès\nBirkin та Kelly",
        "hero_subtitle": (
            "Birkin, Kelly, Evelyne, Constance — легендарні сумки Hermès, "
            "символ справжньої розкоші. Доставка по всьому світу."
        ),
        "hero_price": "399$",
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "show_size_chart": False,
        "materials_label": _BAG_MATERIALS_LABEL,
        "materials_heading": _BAG_MATERIALS_HEADING,
        "materials": _BAG_MATERIALS,
    },

    "Сумки_LV": {
        "title": "Сумки Louis Vuitton — Speedy, Neverfull, Alma — PulvasStore",
        "description": (
            "Купити сумку Louis Vuitton, бананку LV, рюкзак LV або клатч LV "
            "з доставкою по всьому світу."
        ),
        "hero_eyebrow": "Сумки Louis Vuitton · Monogram і Damier",
        "hero_heading": "Сумки\nLouis Vuitton",
        "hero_subtitle": (
            "Speedy, Neverfull, Alma, Pochette Metis, бананки та чемодани LV — "
            "увесь культовий асортимент. Доставка по всьому світу."
        ),
        "hero_price": "249$",
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "show_size_chart": False,
        "materials_label": _BAG_MATERIALS_LABEL,
        "materials_heading": _BAG_MATERIALS_HEADING,
        "materials": _BAG_MATERIALS,
    },

    "Сумки_Prada": {
        "title": "Сумки Prada — нейлон, шкіра, Milano dal 1913 — PulvasStore",
        "description": (
            "Купити сумку Prada Milano, нейлонову сумку Prada або шкіряну Prada "
            "з доставкою по всьому світу."
        ),
        "hero_eyebrow": "Сумки Prada · Milano dal 1913",
        "hero_heading": "Сумки\nPrada",
        "hero_subtitle": (
            "Нейлонові та шкіряні сумки Prada Milano — мінімалізм "
            "і бездоганна якість. Доставка по всьому світу."
        ),
        "hero_price": "219$",
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "show_size_chart": False,
        "materials_label": _BAG_MATERIALS_LABEL,
        "materials_heading": _BAG_MATERIALS_HEADING,
        "materials": _BAG_MATERIALS,
    },

    "Сумки_YSL": {
        "title": "Сумки YSL — Niki, Solferino, Sac de Jour — PulvasStore",
        "description": (
            "Купити сумку Yves Saint Laurent, YSL Niki, YSL Solferino або клатч YSL "
            "з доставкою по всьому світу."
        ),
        "hero_eyebrow": "Сумки YSL · Saint Laurent Paris",
        "hero_heading": "Сумки\nYves Saint Laurent",
        "hero_subtitle": (
            "Niki, Solferino, Sac de Jour, Kate — культові моделі YSL для жінок. "
            "Доставка по всьому світу."
        ),
        "hero_price": "229$",
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "show_size_chart": False,
        "materials_label": _BAG_MATERIALS_LABEL,
        "materials_heading": _BAG_MATERIALS_HEADING,
        "materials": _BAG_MATERIALS,
    },

    "Сумки_Інші": {
        "title": "Дизайнерські сумки — Valentino, Celine, Fendi, Loewe — PulvasStore",
        "description": (
            "Купити сумку Valentino, Celine, Burberry, Fendi, Loewe або Bottega Veneta "
            "з доставкою по всьому світу."
        ),
        "hero_eyebrow": "Дизайнерські сумки · Преміальні бренди",
        "hero_heading": "Дизайнерські\nсумки",
        "hero_subtitle": (
            "Valentino, Celine, Fendi, Loewe, Bottega Veneta, Burberry — "
            "широкий вибір від топових будинків моди. Доставка по всьому світу."
        ),
        "hero_price": "199$",
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "show_size_chart": False,
        "materials_label": _BAG_MATERIALS_LABEL,
        "materials_heading": _BAG_MATERIALS_HEADING,
        "materials": _BAG_MATERIALS,
    },
}

# ── Default (no ?g= parameter or unknown value) ───────────────────────────────

DEFAULT_GROUP: dict = {
    "title": "PulvasStore — Люксові аксесуари, взуття та одяг",
    "description": (
        "Купити брендові сумки, взуття, одяг та аксесуари з доставкою по всьому світу. "
        "Louis Vuitton, Gucci, Hermès, Chanel та інші."
    ),
    "hero_eyebrow": "Люксові речі · 2025",
    "hero_heading": "PulvasStore\nрозкіш доступна",
    "hero_subtitle": (
        "Сумки, взуття, одяг та аксесуари від провідних будинків моди. "
        "Доставка по всьому світу."
    ),
    "hero_price": "99$",
    "features_label": "Чому PulvasStore",
    "features": _DEFAULT_FEATURES,
    "show_size_chart": False,
    "materials_label": _BAG_MATERIALS_LABEL,
    "materials_heading": _BAG_MATERIALS_HEADING,
    "materials": _BAG_MATERIALS,
}


def get_group(key: str) -> dict:
    """Return the content dict for the given ad-group key, or the default."""
    return AD_GROUPS.get(key, DEFAULT_GROUP)
