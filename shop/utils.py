"""Ad-group content mapping for PulvasStore landing page.

Each entry maps a ``?g=`` URL parameter value to a dict of template context
variables. Unknown / missing values fall back to ``DEFAULT_GROUP``.
"""

from __future__ import annotations

# ── Shared material card sets ─────────────────────────────────────────────────

_BAG_MATERIALS_LABEL = "Матеріали та якість"
_BAG_MATERIALS_HEADING = "Кожна деталь —\nдо дрібниць"
_BAG_MATERIALS: list[dict] = [
    {
        "num": "01",
        "title": "Зовнішній матеріал",
        "text": "Преміальна шкіра або канва — зберігає форму, стійка до стирання і набуває характеру з часом.",
    },
    {
        "num": "02",
        "title": "Металева фурнітура",
        "text": "Замки, кільця та карабіни з важкого металу — не окислюються, зберігають вигляд роками.",
    },
    {
        "num": "03",
        "title": "Внутрішня підкладка",
        "text": "М'яка суедева або тканинна підкладка захищає вміст і надає сумці витонченого вигляду всередині.",
    },
    {
        "num": "04",
        "title": "Строчка та збірка",
        "text": "Рівні подвійні шви, міцні ручки та ремінь — витримують щоденне навантаження без деформації.",
    },
]

_SHOE_MATERIALS_LABEL = "Матеріали і деталі"
_SHOE_MATERIALS_HEADING = "Кожна деталь —\nнавмисна"
_SHOE_MATERIALS: list[dict] = [
    {
        "num": "01",
        "title": "Зовнішній покрив",
        "text": "Преміальна шкіра — з роками набуває характеру, зберігає форму і дозволяє нозі дихати.",
    },
    {
        "num": "02",
        "title": "Збереження форми",
        "text": "Натуральні волокна всередині конструкції тримають силует взуття і забезпечують щільне прилягання.",
    },
    {
        "num": "03",
        "title": "Внутрішній дотик",
        "text": "М'яка шкіра всередині — ніжна до ноги, не викликає подразнень, відчувається як друга шкіра.",
    },
    {
        "num": "04",
        "title": "Опора та комфорт",
        "text": "Пружна основа поглинає удари, шкіряна устілка з м'яким підшаром — стопа відпочиває навіть після довгого дня.",
    },
]

_ACC_MATERIALS_LABEL = "Матеріали та якість"
_ACC_MATERIALS_HEADING = "Деталь, яка\nговорить сама"
_ACC_MATERIALS: list[dict] = [
    {
        "num": "01",
        "title": "Шкіряний матеріал",
        "text": "Теляча або зерниста шкіра — еластична, довговічна, формує бездоганний силует аксесуару.",
    },
    {
        "num": "02",
        "title": "Металева фурнітура",
        "text": "Пряжки, кільця та логотипи з важкого металу — стійкі до зносу, зберігають блиск роками.",
    },
    {
        "num": "03",
        "title": "Строчка та обробка",
        "text": "Подвійний шов, фарбовані краї шкіри — рівні, акуратні, без задирок. Деталь, яку помічають цінителі.",
    },
    {
        "num": "04",
        "title": "Внутрішнє оздоблення",
        "text": "Відділення, кишені та потайки — функціональні і акуратно прошиті, без зайвих деталей.",
    },
]

_CLOTH_MATERIALS_LABEL = "Тканини і деталі"
_CLOTH_MATERIALS_HEADING = "Якість у\nкожному шві"
_CLOTH_MATERIALS: list[dict] = [
    {
        "num": "01",
        "title": "Основна тканина",
        "text": "Бавовна, кашемір або технічний нейлон — залежно від моделі. Дихає, зберігає форму, не скочується.",
    },
    {
        "num": "02",
        "title": "Підкладка",
        "text": "М'яка внутрішня підкладка зручна на дотик і не набирає форм тіла з часом.",
    },
    {
        "num": "03",
        "title": "Фурнітура і застібки",
        "text": "Блискавки, кнопки і ґудзики з металу — не ламаються, не окислюються, залишаються точними.",
    },
    {
        "num": "04",
        "title": "Строчка і крій",
        "text": "Рівні шви, точний крій — виріб не деформується після прання і носіння.",
    },
]

# ── Shared feature card sets ──────────────────────────────────────────────────

_DEFAULT_FEATURES: list[dict] = [
    {
        "num": "01",
        "title": "Перевірено до дрібниць",
        "text": "Кожен виріб проходить багатоетапний контроль якості перед відправкою — матеріали, строчка, фурнітура.",
    },
    {
        "num": "02",
        "title": "1–3 дні по Україні",
        "text": "Відправляємо впродовж 24 годин. Нова Пошта доставить у будь-яке місто та відділення.",
    },
    {
        "num": "03",
        "title": "Оплата при отриманні",
        "text": "Жодного ризику для вас — оплачуєте лише тоді, коли тримаєте товар у руках на відділенні.",
    },
    {
        "num": "04",
        "title": "Підтримка та повернення",
        "text": "Персональний менеджер 24/7 у Telegram. Якщо товар не підійшов — повернення протягом 14 днів.",
    },
]

# ── Ad group mapping ──────────────────────────────────────────────────────────

AD_GROUPS: dict[str, dict] = {
    # ── ACCESSORIES ───────────────────────────────────────────────────────────

    "Аксесуари_Ремені_Гаманці": {
        "title": "Ремені та гаманці Louis Vuitton, Gucci, Hermès — PulvasStore",
        "description": (
            "Купити ремінь або гаманець Louis Vuitton, Gucci, Hermès, Prada "
            "з доставкою по Україні. Преміальна якість, оплата при отриманні."
        ),
        "hero_eyebrow": "Ремені та гаманці · Люксові аксесуари",
        "hero_heading": "Ремені та гаманці\nвищого класу",
        "hero_subtitle": (
            "Louis Vuitton, Gucci, Hermès, Prada — іконічні аксесуари "
            "з бездоганною якістю. Доставка по всій Україні."
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
            "браслет Hermès з доставкою по Україні."
        ),
        "hero_eyebrow": "Шарфи, окуляри, аксесуари · Преміум",
        "hero_heading": "Стильні аксесуари\nтоп брендів",
        "hero_subtitle": (
            "Шарфи Burberry, окуляри Chanel і Dior, кепки Loro Piana, "
            "браслети Hermès. Швидка доставка по Україні."
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
            "Доставка по Україні, оплата при отриманні."
        ),
        "hero_eyebrow": "Взуття Balenciaga · Нова колекція",
        "hero_heading": "Кросівки\nBalenciaga",
        "hero_subtitle": (
            "Triple S, Track, Runner, Speed — культові моделі для жінок і чоловіків. "
            "Доставка по всій Україні."
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
            "Доставка по Україні, оплата при отриманні."
        ),
        "hero_eyebrow": "Взуття Dior · Елегантність у кожному кроці",
        "hero_heading": "Взуття\nChristian Dior",
        "hero_subtitle": (
            "Кеди, кросівки, туфлі та сандалі Dior — вишукана елегантність "
            "для жінок і чоловіків. Доставка по Україні."
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
            "Доставка по Україні, оплата при отриманні."
        ),
        "hero_eyebrow": "Взуття Gucci · Люксовий стиль",
        "hero_heading": "Взуття\nGucci",
        "hero_subtitle": (
            "Кросівки, лофери, кеди та туфлі Gucci — бездоганний стиль "
            "для жінок і чоловіків. Доставка по Україні."
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
            "Доставка по Україні, оплата при отриманні."
        ),
        "hero_eyebrow": "Взуття Louis Vuitton · Iconic",
        "hero_heading": "Взуття\nLouis Vuitton",
        "hero_subtitle": (
            "Кросівки, кеди, туфлі та лофери LV — легендарний стиль "
            "для жінок і чоловіків. Доставка по Україні."
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
            "з доставкою по Україні. Оплата при отриманні."
        ),
        "hero_eyebrow": "Дизайнерське взуття · Преміальні бренди",
        "hero_heading": "Преміальне взуття\nтоп брендів",
        "hero_subtitle": (
            "Valentino, Loro Piana, Prada, Bottega Veneta — лофери, кросівки, туфлі. "
            "Доставка по всій Україні."
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
            "Доставка по Україні, оплата при отриманні."
        ),
        "hero_eyebrow": "Брендове взуття · Великий вибір",
        "hero_heading": "Брендове взуття\nдля вас",
        "hero_subtitle": (
            "Великий вибір дизайнерського взуття для жінок і чоловіків — "
            "кросівки, лофери, туфлі. Доставка по Україні."
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
            "Доставка по Україні, оплата при отриманні."
        ),
        "hero_eyebrow": "Одяг Balenciaga · Нова колекція",
        "hero_heading": "Одяг\nBalenciaga",
        "hero_subtitle": (
            "Футболки, худі, пуховики і костюми Balenciaga — авангардний стиль "
            "для жінок і чоловіків. Доставка по Україні."
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
            "Доставка по Україні, оплата при отриманні."
        ),
        "hero_eyebrow": "Одяг Gucci · Люксовий стиль",
        "hero_heading": "Одяг\nGucci",
        "hero_subtitle": (
            "Футболки, кофти, штани та костюми Gucci — іконічний стиль "
            "для жінок і чоловіків. Доставка по Україні."
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
            "Доставка по Україні."
        ),
        "hero_eyebrow": "Loro Piana · Кашемір і розкіш",
        "hero_heading": "Одяг\nLoro Piana",
        "hero_subtitle": (
            "Куртки, костюми і кашемірові вироби Loro Piana — преміальна якість "
            "для справжніх поціновувачів. Доставка по Україні."
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
            "Доставка по Україні, оплата при отриманні."
        ),
        "hero_eyebrow": "Moncler · Тепло і стиль",
        "hero_heading": "Куртки та пуховики\nMoncler",
        "hero_subtitle": (
            "Жіночі та чоловічі пуховики Moncler — легкі, теплі, "
            "з бездоганним кроєм. Доставка по всій Україні."
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
            "Доставка по Україні, оплата при отриманні."
        ),
        "hero_eyebrow": "Stone Island · Urban Premium",
        "hero_heading": "Одяг\nStone Island",
        "hero_subtitle": (
            "Куртки, худі, свитшоти та жилети Stone Island — культовий стиль "
            "для міського життя. Доставка по Україні."
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
            "Клітчасті сумки, рюкзаки, через плечо. Доставка по Україні."
        ),
        "hero_eyebrow": "Сумки Balenciaga · Авангард моди",
        "hero_heading": "Сумки\nBalenciaga",
        "hero_subtitle": (
            "Клітчасті сумки, рюкзаки, міські та через плечо — "
            "весь асортимент Balenciaga. Доставка по Україні."
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
            "з доставкою по Україні."
        ),
        "hero_eyebrow": "Сумки Chanel · Вічна класика",
        "hero_heading": "Сумки\nChanel",
        "hero_subtitle": (
            "Класичні фліп-сумки, 2.55, Boy Chanel, mini та клатчі — "
            "квінтесенція жіночої елегантності. Доставка по Україні."
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
            "з доставкою по Україні."
        ),
        "hero_eyebrow": "Сумки Dior · Haute Couture",
        "hero_heading": "Сумки\nChristian Dior",
        "hero_subtitle": (
            "Lady Dior, Miss Dior, Saddle, Book Tote — культові моделі "
            "для жінок і чоловіків. Доставка по Україні."
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
            "з доставкою по Україні."
        ),
        "hero_eyebrow": "Сумки Gucci · Іконічний стиль",
        "hero_heading": "Сумки\nGucci",
        "hero_subtitle": (
            "Ophidia, Dionysus, Jackie, Horsebit — весь культовий асортимент Gucci "
            "для жінок і чоловіків. Доставка по Україні."
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
            "Купити сумку Hermès Birkin або Kelly з доставкою по Україні. "
            "Оплата при отриманні."
        ),
        "hero_eyebrow": "Hermès Birkin · Kelly · Evelyne",
        "hero_heading": "Сумки Hermès\nBirkin та Kelly",
        "hero_subtitle": (
            "Birkin, Kelly, Evelyne, Constance — легендарні сумки Hermès, "
            "символ справжньої розкоші. Доставка по Україні."
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
            "з доставкою по Україні."
        ),
        "hero_eyebrow": "Сумки Louis Vuitton · Monogram і Damier",
        "hero_heading": "Сумки\nLouis Vuitton",
        "hero_subtitle": (
            "Speedy, Neverfull, Alma, Pochette Metis, бананки та чемодани LV — "
            "увесь культовий асортимент. Доставка по Україні."
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
            "з доставкою по Україні."
        ),
        "hero_eyebrow": "Сумки Prada · Milano dal 1913",
        "hero_heading": "Сумки\nPrada",
        "hero_subtitle": (
            "Нейлонові та шкіряні сумки Prada Milano — мінімалізм "
            "і бездоганна якість. Доставка по Україні."
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
            "з доставкою по Україні."
        ),
        "hero_eyebrow": "Сумки YSL · Saint Laurent Paris",
        "hero_heading": "Сумки\nYves Saint Laurent",
        "hero_subtitle": (
            "Niki, Solferino, Sac de Jour, Kate — культові моделі YSL для жінок. "
            "Доставка по всій Україні."
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
            "з доставкою по Україні."
        ),
        "hero_eyebrow": "Дизайнерські сумки · Преміальні бренди",
        "hero_heading": "Дизайнерські\nсумки",
        "hero_subtitle": (
            "Valentino, Celine, Fendi, Loewe, Bottega Veneta, Burberry — "
            "широкий вибір від топових будинків моди. Доставка по Україні."
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
        "Купити брендові сумки, взуття, одяг та аксесуари з доставкою по Україні. "
        "Louis Vuitton, Gucci, Hermès, Chanel та інші."
    ),
    "hero_eyebrow": "Люксові речі · 2025",
    "hero_heading": "PulvasStore\nрозкіш доступна",
    "hero_subtitle": (
        "Сумки, взуття, одяг та аксесуари від провідних будинків моди. "
        "Доставка по всій Україні."
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
