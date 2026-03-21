"""Ad-group content mapping for PulvasStore landing page.

Each entry maps a ``?g=`` URL parameter value to a dict of template context
variables. Unknown / missing values fall back to ``DEFAULT_GROUP``.
"""

from __future__ import annotations

# ── Shared generic card sets (cards 03–04 reused across groups) ───────────────

_MATERIAL_03 = {
    "num": "03",
    "title": "Бездоганна збірка",
    "text": (
        "Акуратні подвійні шви, точна геометрія — кожен виріб "
        "виконаний з абсолютною точністю та увагою до деталей."
    ),
}

_MATERIAL_04 = {
    "num": "04",
    "title": "Комфорт та посадка",
    "text": (
        "Бездоганний крій і форма — речі ідеально сідають по фігурі."
    ),
}

_DEFAULT_FEATURES: list[dict] = [
    {
        "num": "01",
        "title": "Безкомпромісна якість",
        "text": (
            "Преміальні матеріали, надійна фурнітура та фірмове пакування. "
            "Ми перевіряємо кожен виріб перед відправкою."
        ),
    },
    {
        "num": "02",
        "title": "Каталог і замовлення під запит",
        "text": (
            "Переглянь наш щоденно оновлюваний каталог у Telegram — "
            "або надішли фото будь-якої речі, і ми її доставимо. "
            "Якщо чогось немає в наявності — знайдемо спеціально для тебе."
        ),
    },
    {
        "num": "03",
        "title": "Доставка в Україну та світ",
        "text": (
            "2–3 тижні. Вартість доставки вже включена в ціну. "
            "Мінімальна передплата 30\u00a0% для України, "
            "повна — для міжнародних замовлень."
        ),
    },
    {
        "num": "04",
        "title": "Менеджер завжди на зв'язку",
        "text": (
            "Відповідаємо в Telegram впродовж дня. "
            "Не підійшло — обмін протягом 7 днів."
        ),
    },
]

_BAG_MATERIALS_LABEL = "Матеріали та якість"
_BAG_MATERIALS_HEADING = "Кожна деталь —\nдо дрібниць"

_SHOE_MATERIALS_LABEL = _BAG_MATERIALS_LABEL
_SHOE_MATERIALS_HEADING = _BAG_MATERIALS_HEADING

_ACC_MATERIALS_LABEL = _BAG_MATERIALS_LABEL
_ACC_MATERIALS_HEADING = _BAG_MATERIALS_HEADING

_CLOTH_MATERIALS_LABEL = _BAG_MATERIALS_LABEL
_CLOTH_MATERIALS_HEADING = _BAG_MATERIALS_HEADING

# ── Ad group mapping ──────────────────────────────────────────────────────────

AD_GROUPS: dict[str, dict] = {
    # ── ACCESSORIES ───────────────────────────────────────────────────────────

    "Аксесуари_Ремені_Гаманці": {
        "title": "Аксесуари Louis Vuitton, Gucci, Hermès — ремені, гаманці та більше — PulvasStore",
        "description": (
            "Купити ремені, гаманці та аксесуари Louis Vuitton, Gucci, Hermès, Prada "
            "з доставкою по всьому світу. Преміальна якість."
        ),
        "hero_eyebrow": "Люксові аксесуари · LV, Gucci, Hermès",
        "hero_heading": "Ремені, гаманці та аксесуари LV, Gucci, Hermès — бездоганна якість",
        "hero_subtitle": (
            "Луї Віттон, Gucci, Hermès — весь асортимент шкіряних аксесуарів бездоганної якості."
        ),
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "materials_label": _ACC_MATERIALS_LABEL,
        "materials_heading": _ACC_MATERIALS_HEADING,
        "materials": [
            {
                "num": "01",
                "title": "Шкіра преміального рівня",
                "text": (
                    "Ремінь луї вітон, ремінь Hermès і гаманець Louis Vuitton — "
                    "добірна теляча шкіра і полотно Monogram зберігають форму "
                    "та вигляд роками навіть при щоденному носінні."
                ),
            },
            {
                "num": "02",
                "title": "Надійна металева фурнітура",
                "text": (
                    "Замки та пряжки ременів LV, Gucci та Hermès — "
                    "гаманець луї вітон і пояс гуччі оздоблені міцними "
                    "металевими деталями, що не тьмяніють і не іржавіють."
                ),
            },
            _MATERIAL_03,
            _MATERIAL_04,
        ],
        "keywords": [
            "ремінь луї вітон", "гаманець gucci", "ремінь hermes",
            "гаманець louis vuitton", "ремінь lv", "пояс гуччі",
            "кошелек луи витон", "ремінь gucci", "гаманець луі вітон",
            "ремінь гуччи", "гаманець prada", "пояс louis vuitton",
        ],
    },

    "Аксесуари_Шарфи_Очки_Інше": {
        "title": "Шарфи Burberry, окуляри Chanel і Dior, кепки Loro Piana — PulvasStore",
        "description": (
            "Купити шарф Burberry, окуляри Chanel або Dior, кепку Loro Piana, "
            "браслет Hermès з доставкою по всьому світу."
        ),
        "hero_eyebrow": "Аксесуари · Шарфи, окуляри та інше",
        "hero_heading": "Аксесуари Burberry, Chanel, Dior — преміальний вибір",
        "hero_subtitle": (
            "Шарфи Burberry, окуляри Chanel і Dior — якість, що вражає з першого дотику."
        ),
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "materials_label": _ACC_MATERIALS_LABEL,
        "materials_heading": _ACC_MATERIALS_HEADING,
        "materials": [
            {
                "num": "01",
                "title": "Матеріали преміального рівня",
                "text": (
                    "Шарф барбері і шарф Burberry виготовлені з добірної вовни та кашеміру, "
                    "а окуляри шанель і сонцезахисні окуляри Chanel — "
                    "з ацетату та полірованих металевих рамок найвищої якості."
                ),
            },
            {
                "num": "02",
                "title": "Надійна фурнітура",
                "text": (
                    "Кепка Loro Piana та кепка Gucci оздоблені міцною фурнітурою. "
                    "Браслет Hermès і браслет Louis Vuitton виготовлені з металу "
                    "та шкіри, що зберігають блиск і форму роками."
                ),
            },
            _MATERIAL_03,
            _MATERIAL_04,
        ],
        "keywords": [
            "шарф burberry", "окуляри шанель", "шарф барбери",
            "очки dior", "браслет hermes", "кепка loro piana",
            "шарф gucci", "окуляри chanel", "тапочки hermes",
            "шарф гуччи", "браслет луї вітон", "кепка gucci",
        ],
    },

    # ── FOOTWEAR ──────────────────────────────────────────────────────────────

    "Взуття_Balenciaga": {
        "title": "Кросівки Balenciaga — Triple S, Track, Runner — PulvasStore",
        "description": (
            "Купити кросівки Balenciaga Triple S, Track, Runner для жінок і чоловіків. "
            "Доставка по всьому світу."
        ),
        "hero_eyebrow": "Взуття Balenciaga · Бездоганна якість",
        "hero_heading": "Кросівки Balenciaga — преміальна якість та культовий дизайн",
        "hero_subtitle": (
            "Triple S, Track, Runner, Speed — для жінок і чоловіків."
        ),
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "materials_label": _SHOE_MATERIALS_LABEL,
        "materials_heading": _SHOE_MATERIALS_HEADING,
        "materials": [
            {
                "num": "01",
                "title": "Шкіра і текстиль Balenciaga",
                "text": (
                    "Кросівки баленсіага Triple S, Track та Runner — "
                    "добірна шкіра й технічний текстиль, що зберігають форму "
                    "та вигляд навіть після тривалого носіння. "
                    "Взуття баленсіага витримує щоденні навантаження."
                ),
            },
            {
                "num": "02",
                "title": "Підошва та амортизація",
                "text": (
                    "Кроси баленсіага мають масивну багатошарову підошву "
                    "з чудовою амортизацією. "
                    "Кросівки Balenciaga жіночі та чоловічі забезпечують "
                    "максимальний комфорт при щоденному носінні."
                ),
            },
            _MATERIAL_03,
            _MATERIAL_04,
        ],
        "keywords": [
            "кросівки баленсіага", "кроссовки balenciaga",
            "баленсіага кросівки", "triple s balenciaga",
            "кроси баленсіага", "balenciaga track",
            "кросівки баленсіага жіночі", "кросівки баленсіага чоловічі",
            "шлепки balenciaga", "кроссовки баленсиага купить",
        ],
    },

    "Взуття_Dior": {
        "title": "Взуття Dior — кеди, кросівки, туфлі Christian Dior — PulvasStore",
        "description": (
            "Купити кеди або кросівки Dior, Christian Dior для жінок і чоловіків. "
            "Доставка по всьому світу."
        ),
        "hero_eyebrow": "Взуття Dior · Бездоганна якість",
        "hero_heading": "Кеди та кросівки Dior — бездоганна якість та преміальний стиль",
        "hero_subtitle": (
            "B27, B22, Walk'n'Dior — весь культовий асортимент Dior."
        ),
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "materials_label": _SHOE_MATERIALS_LABEL,
        "materials_heading": _SHOE_MATERIALS_HEADING,
        "materials": [
            {
                "num": "01",
                "title": "Шкіра і текстиль Dior",
                "text": (
                    "Кеди Dior та кросівки Christian Dior виготовлені "
                    "з добірної шкіри і технічного текстилю. "
                    "Взуття діор зберігає форму і вигляд роками завдяки "
                    "матеріалам преміального рівня."
                ),
            },
            {
                "num": "02",
                "title": "Підошва та деталі Dior",
                "text": (
                    "Кросівки Dior жіночі та чоловічі мають підошву "
                    "з чудовою амортизацією та підтримкою стопи. "
                    "Кожна деталь взуття діор виготовлена з найвищоякісних матеріалів."
                ),
            },
            _MATERIAL_03,
            _MATERIAL_04,
        ],
        "keywords": [
            "кеди діор", "кросівки dior", "кеды dior",
            "взуття dior", "кеди christian dior", "dior b27",
            "кросівки кристиан диор", "шльопки dior",
            "туфлі dior", "сандалі dior",
        ],
    },

    "Взуття_Gucci": {
        "title": "Взуття Gucci — кросівки, лофери, кеди — PulvasStore",
        "description": (
            "Купити кросівки або лофери Gucci для жінок і чоловіків. "
            "Доставка по всьому світу."
        ),
        "hero_eyebrow": "Взуття Gucci · Бездоганна якість",
        "hero_heading": "Кросівки та лофери Gucci — преміальна якість та розкішний стиль",
        "hero_subtitle": (
            "Rhyton, Ace, лофери Horsebit — для жінок і чоловіків."
        ),
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "materials_label": _SHOE_MATERIALS_LABEL,
        "materials_heading": _SHOE_MATERIALS_HEADING,
        "materials": [
            {
                "num": "01",
                "title": "Шкіра і замша Gucci",
                "text": (
                    "Кросівки гуччі та лофери Gucci виготовлені "
                    "з добірної телячої шкіри і замші преміального рівня. "
                    "Кроси гуччі зберігають форму і вигляд роками "
                    "при щоденному носінні."
                ),
            },
            {
                "num": "02",
                "title": "Підошва та оздоблення Gucci",
                "text": (
                    "Кросівки gucci жіночі та чоловічі мають підошву "
                    "з чудовою амортизацією. "
                    "Лофери гуччі оздоблені знаковою пряжкою Horsebit "
                    "та деталями найвищої якості."
                ),
            },
            _MATERIAL_03,
            _MATERIAL_04,
        ],
        "keywords": [
            "кросівки гуччі", "лофери gucci", "кеди gucci",
            "взуття gucci", "кроси гуччі", "лофери гуччи",
            "босоніжки gucci", "тапочки gucci",
            "кросівки гуччі жіночі", "кросівки gucci чоловічі",
        ],
    },

    "Взуття_LV": {
        "title": "Взуття Louis Vuitton — кросівки, кеди, туфлі LV — PulvasStore",
        "description": (
            "Купити кросівки або кеди Louis Vuitton для жінок і чоловіків. "
            "Доставка по всьому світу."
        ),
        "hero_eyebrow": "Взуття Louis Vuitton · Бездоганна якість",
        "hero_heading": "Кросівки Louis Vuitton — бездоганна якість та культова монограма",
        "hero_subtitle": (
            "Trainer, Archlight, Run Away — весь асортимент LV."
        ),
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "materials_label": _SHOE_MATERIALS_LABEL,
        "materials_heading": _SHOE_MATERIALS_HEADING,
        "materials": [
            {
                "num": "01",
                "title": "Шкіра і монограма LV",
                "text": (
                    "Кросівки луї вітон та кеди LV виготовлені з добірної шкіри "
                    "і знакового полотна Monogram. "
                    "Взуття Louis Vuitton зберігає форму і вигляд роками "
                    "завдяки матеріалам преміального рівня."
                ),
            },
            {
                "num": "02",
                "title": "Підошва та фурнітура LV",
                "text": (
                    "Кросівки Louis Vuitton жіночі та чоловічі мають "
                    "підошву з відмінною амортизацією. "
                    "Кеди LV оздоблені знаковою монограмою і фурнітурою "
                    "найвищої якості."
                ),
            },
            _MATERIAL_03,
            _MATERIAL_04,
        ],
        "keywords": [
            "кросівки луї вітон", "кроссовки louis vuitton",
            "взуття lv", "кеди луі вітон", "кроси луї вітон",
            "louis vuitton trainer", "шльопки луі вітон",
            "тапочки луи витон", "кросівки lv жіночі",
        ],
    },

    "Взуття_Інші": {
        "title": "Взуття Valentino, Loro Piana, Prada, Bottega Veneta — PulvasStore",
        "description": (
            "Купити взуття Valentino, Loro Piana, Prada, Bottega Veneta "
            "з доставкою по всьому світу. Преміальна якість."
        ),
        "hero_eyebrow": "Брендове взуття · Бездоганна якість",
        "hero_heading": "Лофери Loro Piana, кросівки Valentino, Prada — преміальна якість",
        "hero_subtitle": (
            "Bottega Veneta, Valentino, Prada — добірне взуття від провідних брендів."
        ),
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "materials_label": _SHOE_MATERIALS_LABEL,
        "materials_heading": _SHOE_MATERIALS_HEADING,
        "materials": [
            {
                "num": "01",
                "title": "Шкіра та текстиль преміум брендів",
                "text": (
                    "Кросівки Valentino та туфлі Prada виготовлені "
                    "з добірної шкіри і замші преміального рівня. "
                    "Лофери Loro Piana та взуття Bottega Veneta "
                    "зберігають форму і вигляд роками."
                ),
            },
            {
                "num": "02",
                "title": "Підошва та фурнітура",
                "text": (
                    "Лофери Loro Piana мають підошву з натуральної шкіри, "
                    "а кросівки Valentino Garavani — гумову підошву "
                    "з чудовою амортизацією. "
                    "Кожна деталь преміального взуття бездоганна."
                ),
            },
            _MATERIAL_03,
            _MATERIAL_04,
        ],
        "keywords": [
            "лофери loro piana", "кросівки valentino",
            "туфлі prada", "лофери prada", "кеди valentino",
            "взуття bottega veneta", "лофери лоро пиано",
            "кросівки валентино", "valentino garavani",
        ],
    },

    "Взуття_Бренд_загальне": {
        "title": "Брендове взуття — кросівки, лофери, туфлі — PulvasStore",
        "description": (
            "Купити брендові кросівки, лофери або туфлі для жінок і чоловіків. "
            "Доставка по всьому світу."
        ),
        "hero_eyebrow": "Брендове взуття · Преміальний стиль",
        "hero_heading": "Брендові кросівки та туфлі — преміальна якість та вишуканість",
        "hero_subtitle": (
            "Louis Vuitton, Gucci, Balenciaga, Dior — весь асортимент взуття."
        ),
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "materials_label": _SHOE_MATERIALS_LABEL,
        "materials_heading": _SHOE_MATERIALS_HEADING,
        "materials": [
            {
                "num": "01",
                "title": "Шкіра преміального рівня",
                "text": (
                    "Брендове взуття жіноче і чоловіче виготовлене "
                    "з добірної шкіри та якісного текстилю. "
                    "Купити брендове взуття — означає отримати матеріали, "
                    "що зберігають форму роками."
                ),
            },
            {
                "num": "02",
                "title": "Надійна підошва і фурнітура",
                "text": (
                    "Брендові кросівки жіночі та чоловічі мають "
                    "підошву з чудовою амортизацією. "
                    "Брендове взуття чоловіче та жіноче оздоблене "
                    "міцною фурнітурою для довговічного носіння."
                ),
            },
            _MATERIAL_03,
            _MATERIAL_04,
        ],
        "keywords": [
            "брендове взуття жіноче", "брендові кросівки",
            "брендова взуття чоловіча", "брендові лофери",
            "брендові кеди", "брендове зимове взуття",
            "брендові туфлі", "фірмові кросівки",
        ],
    },

    # ── CLOTHING ──────────────────────────────────────────────────────────────

    "Одяг_Balenciaga_одяг": {
        "title": "Одяг Balenciaga — футболки, худі, куртки — PulvasStore",
        "description": (
            "Купити футболку, худі або куртку Balenciaga. "
            "Доставка по всьому світу."
        ),
        "hero_eyebrow": "Одяг Balenciaga · Бездоганна якість",
        "hero_heading": "Футболки, худі, пуховики Balenciaga — преміальна якість",
        "hero_subtitle": (
            "Paris, Speed, Gap — весь культовий одяг Balenciaga."
        ),
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "materials_label": _CLOTH_MATERIALS_LABEL,
        "materials_heading": _CLOTH_MATERIALS_HEADING,
        "materials": [
            {
                "num": "01",
                "title": "Бавовна і трикотаж Balenciaga",
                "text": (
                    "Футболки та худі Balenciaga виготовлені з щільної "
                    "преміальної бавовни. "
                    "Одяг баленсіага зберігає форму і насиченість кольорів "
                    "навіть після багаторазового прання."
                ),
            },
            {
                "num": "02",
                "title": "Фурнітура і деталі Balenciaga",
                "text": (
                    "Замки та фурнітура курток і пуховиків Balenciaga "
                    "виготовлені з міцних матеріалів. "
                    "Костюм баленсіага і худі Balenciaga мають бездоганний "
                    "крій і акуратні шви."
                ),
            },
            _MATERIAL_03,
            _MATERIAL_04,
        ],
        "keywords": [
            "футболка balenciaga", "худі баленсіага",
            "пуховик balenciaga", "костюм баленсіага",
            "свитшот balenciaga", "носки balenciaga",
            "купити худі баленсіага", "футболка баленсіага paris",
        ],
    },

    "Одяг_Gucci_одяг": {
        "title": "Одяг Gucci — футболки, кофти, костюми — PulvasStore",
        "description": (
            "Купити футболку, кофту або костюм Gucci. "
            "Доставка по всьому світу."
        ),
        "hero_eyebrow": "Одяг Gucci · Бездоганна якість",
        "hero_heading": "Футболки, худі, костюми Gucci — преміальна якість",
        "hero_subtitle": (
            "Логотипний принт, тигр, полотно GG — весь асортимент одягу Gucci."
        ),
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "materials_label": _CLOTH_MATERIALS_LABEL,
        "materials_heading": _CLOTH_MATERIALS_HEADING,
        "materials": [
            {
                "num": "01",
                "title": "Бавовна і трикотаж Gucci",
                "text": (
                    "Футболки та кофти Gucci виготовлені з преміальної бавовни. "
                    "Купити футболку гуччі — це отримати одяг, "
                    "що зберігає форму і яскравість кольорів і вишивки "
                    "після тривалого носіння."
                ),
            },
            {
                "num": "02",
                "title": "Фурнітура та вишивка Gucci",
                "text": (
                    "Костюм Gucci і штани Gucci мають бездоганний крій "
                    "та акуратні шви. "
                    "Кофта гуччі оздоблена знаковою вишивкою GG та деталями "
                    "найвищої якості."
                ),
            },
            _MATERIAL_03,
            _MATERIAL_04,
        ],
        "keywords": [
            "футболка gucci", "кофта гуччі", "худі gucci",
            "костюм gucci", "спортивний костюм гуччи",
            "штани gucci", "купити футболку gucci",
            "футболка gucci paris",
        ],
    },

    "Одяг_LoroPiana": {
        "title": "Одяг Loro Piana — куртки, костюми, кашемір — PulvasStore",
        "description": (
            "Купити куртку або костюм Loro Piana. Кашемір і преміальні тканини. "
            "Доставка по всьому світу."
        ),
        "hero_eyebrow": "Одяг Loro Piana · Преміальний стиль",
        "hero_heading": "Куртки та костюми Loro Piana — преміальна якість та тиха розкіш",
        "hero_subtitle": (
            "Кашемірові костюми та пуховики Loro Piana — "
            "для тих, хто цінує тишу розкоші."
        ),
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "materials_label": _CLOTH_MATERIALS_LABEL,
        "materials_heading": _CLOTH_MATERIALS_HEADING,
        "materials": [
            {
                "num": "01",
                "title": "Кашемір і преміальна шерсть",
                "text": (
                    "Куртки і костюми Loro Piana виготовлені з "
                    "найрідкіснішого кашеміру Vicuña та мериносової вовни. "
                    "Кашемір Loro Piana зберігає тепло і форму роками."
                ),
            },
            {
                "num": "02",
                "title": "Замки та фурнітура Loro Piana",
                "text": (
                    "Спортивний костюм Loro Piana і куртка Loro Piana "
                    "оздоблені преміальними замками YKK та фурнітурою, "
                    "що забезпечують довговічність і незмінний вигляд."
                ),
            },
            _MATERIAL_03,
            _MATERIAL_04,
        ],
        "keywords": [
            "куртка loro piana", "костюм лоро пиано",
            "пуховик loro piana", "кашемір loro piana",
            "спортивний костюм loro piana",
            "куртка loro piana чоловіча", "куртка loro piana жіноча",
        ],
    },

    "Одяг_Moncler": {
        "title": "Куртки та пуховики Moncler — PulvasStore",
        "description": (
            "Купити куртку або пуховик Moncler для жінок і чоловіків. "
            "Доставка по всьому світу."
        ),
        "hero_eyebrow": "Одяг Moncler · Тепло і стиль",
        "hero_heading": "Пуховики та куртки Moncler — преміальна якість та бездоганне тепло",
        "hero_subtitle": (
            "Легкі, теплі, з бездоганним кроєм — "
            "куртки Moncler для жінок і чоловіків."
        ),
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "materials_label": _CLOTH_MATERIALS_LABEL,
        "materials_heading": _CLOTH_MATERIALS_HEADING,
        "materials": [
            {
                "num": "01",
                "title": "Пух і нейлон Moncler",
                "text": (
                    "Куртка монклер і пуховик Moncler виготовлені "
                    "з преміального нейлону та добірного гусячого пуху. "
                    "Мoncler куртка жіноча і чоловіча зберігає тепло навіть "
                    "при екстремальних морозах."
                ),
            },
            {
                "num": "02",
                "title": "Замки та фурнітура Moncler",
                "text": (
                    "Куртка монклер жіноча та пуховик Moncler мають "
                    "замки YKK і преміальну фурнітуру. "
                    "Купити куртку монклер — означає отримати виріб "
                    "з бездоганною збіркою і деталями найвищої якості."
                ),
            },
            _MATERIAL_03,
            _MATERIAL_04,
        ],
        "keywords": [
            "куртка монклер", "пуховик moncler",
            "куртка moncler жіноча", "пуховик монклер чоловічий",
            "купити куртку moncler", "пухан монклер",
            "куртка moncler palm angels",
        ],
    },

    "Одяг_StoneIsland": {
        "title": "Одяг Stone Island — куртки, худі, свитшоти — PulvasStore",
        "description": (
            "Купити куртку, худі або свитшот Stone Island. "
            "Доставка по всьому світу."
        ),
        "hero_eyebrow": "Одяг Stone Island · Бездоганна якість",
        "hero_heading": "Куртки та худі Stone Island — преміальна якість",
        "hero_subtitle": (
            "Shadow Project, Ghost — весь асортимент Stone Island."
        ),
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "materials_label": _CLOTH_MATERIALS_LABEL,
        "materials_heading": _CLOTH_MATERIALS_HEADING,
        "materials": [
            {
                "num": "01",
                "title": "Інноваційні тканини Stone Island",
                "text": (
                    "Зимова куртка Stone Island і куртка стон айленд "
                    "виготовлені з інноваційного нейлону та гортексу. "
                    "Одяг Stone Island витримує будь-яку погоду і зберігає "
                    "тепло та форму протягом багатьох сезонів."
                ),
            },
            {
                "num": "02",
                "title": "Знакова нашивка і фурнітура",
                "text": (
                    "Куртка стон айленд має знакову знімну нашивку-компас "
                    "на рукаві. Свитшот Stone Island і худі стон айленд "
                    "оздоблені преміальними замками і фурнітурою для "
                    "довговічного носіння."
                ),
            },
            _MATERIAL_03,
            _MATERIAL_04,
        ],
        "keywords": [
            "куртка stone island", "худі стон айленд",
            "свитшот stone island", "куртка стонік",
            "стон айленд одяг", "зимова куртка stone island",
            "stone island shadow project",
        ],
    },

    # ── BAGS ──────────────────────────────────────────────────────────────────

    "Сумки_Balenciaga": {
        "title": "Сумки Balenciaga — клітчасті, рюкзаки, через плечо — PulvasStore",
        "description": (
            "Купити сумку Balenciaga для жінок і чоловіків. "
            "Клітчасті сумки, рюкзаки, через плечо. Доставка по всьому світу."
        ),
        "hero_eyebrow": "Сумки Balenciaga · Іконічний стиль",
        "hero_heading": "Сумки Balenciaga — преміальна якість та іконічний стиль",
        "hero_subtitle": (
            "City, Le Cagole, клітчата шопінг-бег — весь асортимент Balenciaga."
        ),
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "materials_label": _BAG_MATERIALS_LABEL,
        "materials_heading": _BAG_MATERIALS_HEADING,
        "materials": [
            {
                "num": "01",
                "title": "Шкіра і текстиль Balenciaga",
                "text": (
                    "Клітчаста сумка Balenciaga та рюкзак Balenciaga "
                    "виготовлені з добірної шкіри і міцного нейлону. "
                    "Сумка Balenciaga зберігає форму і вигляд "
                    "при щоденному використанні."
                ),
            },
            {
                "num": "02",
                "title": "Замки та фурнітура Balenciaga",
                "text": (
                    "Бананка Balenciaga і сумка Balenciaga через плечо "
                    "оздоблені міцними металевими замками і фурнітурою, "
                    "що не тьмяніє. Сумка Balenciaga жіноча і чоловіча — "
                    "бездоганна збірка кожного виробу."
                ),
            },
            _MATERIAL_03,
            _MATERIAL_04,
        ],
        "keywords": [
            "сумка баленсіага", "сумки balenciaga",
            "рюкзак balenciaga", "клітчата сумка balensiaga",
            "сумка баленсіага жіноча", "бананка balenciaga",
            "сумка balenciaga city",
        ],
    },

    "Сумки_Chanel": {
        "title": "Сумки Chanel — класика 2.55, Boy, mini — PulvasStore",
        "description": (
            "Купити сумку Chanel, Chanel 2.55, mini Chanel, клатч Chanel "
            "з доставкою по всьому світу."
        ),
        "hero_eyebrow": "Сумки Chanel · Вічна класика",
        "hero_heading": "Сумки Chanel — бездоганна якість та вічна класика",
        "hero_subtitle": (
            "2.55, Classic Flap, 22 — весь культовий асортимент Chanel."
        ),
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "materials_label": _BAG_MATERIALS_LABEL,
        "materials_heading": _BAG_MATERIALS_HEADING,
        "materials": [
            {
                "num": "01",
                "title": "Шкіра та твід Chanel",
                "text": (
                    "Сумка шанель 2.55 та Boy Chanel виготовлені "
                    "з добірної ягнячої шкіри та твіду Maison Lesage. "
                    "Сумка коко шанель зберігає форму і вигляд "
                    "десятиліттями — це справжня класика."
                ),
            },
            {
                "num": "02",
                "title": "Фурнітура та ланцюжок Chanel",
                "text": (
                    "Золота та срібна фурнітура сумки шанель маленька і mini — "
                    "ланцюжки, застібки і логотип CC виготовлені "
                    "з металу найвищої якості, що зберігає блиск роками."
                ),
            },
            _MATERIAL_03,
            _MATERIAL_04,
        ],
        "keywords": [
            "сумка шанель", "сумка chanel", "сумка chanel mini",
            "сумка шанель 2.55", "сумка коко шанель",
            "клатч chanel", "купити сумку шанель",
            "сумка шанель на ланцюжку",
        ],
    },

    "Сумки_Dior": {
        "title": "Сумки Dior — Lady Dior, Miss Dior, Saddle — PulvasStore",
        "description": (
            "Купити сумку Dior, Lady Dior, Miss Dior або Saddle Dior "
            "з доставкою по всьому світу."
        ),
        "hero_eyebrow": "Сумки Dior · Жіночність та стиль",
        "hero_heading": "Сумки Dior — преміальна якість та витончений стиль",
        "hero_subtitle": (
            "Lady Dior, Saddle, Miss Dior — весь асортимент Dior."
        ),
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "materials_label": _BAG_MATERIALS_LABEL,
        "materials_heading": _BAG_MATERIALS_HEADING,
        "materials": [
            {
                "num": "01",
                "title": "Шкіра Cannage та Dior Oblique",
                "text": (
                    "Сумка діор Lady Dior і сумка крістіан діор "
                    "виготовлені з добірної телячої шкіри Cannage — "
                    "характерного стьобаного принту. "
                    "Кожна сумка Dior зберігає форму і вигляд роками."
                ),
            },
            {
                "num": "02",
                "title": "Фурнітура DIOR та Cannage-оздоблення",
                "text": (
                    "Сумка діор сідло (Saddle) і Miss Dior оздоблені "
                    "золотою фурнітурою з написом DIOR. "
                    "Замки, D-образні кільця і застібки сумки діор — "
                    "бездоганна якість кожної деталі."
                ),
            },
            _MATERIAL_03,
            _MATERIAL_04,
        ],
        "keywords": [
            "сумка діор", "сумка lady dior", "сумка dior saddle",
            "сумка christian dior", "рюкзак dior",
            "косметичка dior", "сумка miss dior", "сумка dior mini",
        ],
    },

    "Сумки_Gucci": {
        "title": "Сумки Gucci — Ophidia, Dionysus, Jackie — PulvasStore",
        "description": (
            "Купити сумку Gucci, рюкзак Gucci або сумку через плечо Gucci "
            "з доставкою по всьому світу."
        ),
        "hero_eyebrow": "Сумки Gucci · Іконічний стиль",
        "hero_heading": "Сумки Gucci — преміальна якість та іконічний стиль",
        "hero_subtitle": (
            "Ophidia, Dionysus, Jackie, Horsebit — весь асортимент Gucci."
        ),
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "materials_label": _BAG_MATERIALS_LABEL,
        "materials_heading": _BAG_MATERIALS_HEADING,
        "materials": [
            {
                "num": "01",
                "title": "Шкіра і полотно GG Gucci",
                "text": (
                    "Сумка гуччі Ophidia та Dionysus виготовлені "
                    "з добірної шкіри і фірмового полотна GG Supreme. "
                    "Купити сумку Gucci — отримати виріб, що зберігає "
                    "форму і вигляд роками."
                ),
            },
            {
                "num": "02",
                "title": "Фурнітура та зелено-червона смужка",
                "text": (
                    "Сумка гуччі Jackie та Horsebit оздоблені знаковою "
                    "пряжкою та зелено-червоною смужкою Web. "
                    "Рюкзак гуччі і сумка через плечо Gucci — "
                    "бездоганна якість металевих деталей."
                ),
            },
            _MATERIAL_03,
            _MATERIAL_04,
        ],
        "keywords": [
            "сумка гуччі", "сумка gucci ophidia",
            "сумка gucci dionysus", "сумка gucci jackie",
            "рюкзак gucci", "сумка gucci horsebit",
            "купити сумку гуччі", "сумка gucci supreme",
        ],
    },

    "Сумки_Hermes_Birkin": {
        "title": "Сумки Hermès Birkin та Kelly — PulvasStore",
        "description": (
            "Купити сумку Hermès Birkin або Kelly з доставкою по всьому світу. "
            "Преміальна якість."
        ),
        "hero_eyebrow": "Сумки Hermès · Легендарна якість",
        "hero_heading": "Birkin, Kelly, Constance Hermès — легендарна якість",
        "hero_subtitle": (
            "Добірна шкіра, ручна збірка, іконічні замки — "
            "бездоганність у кожному шві та легендарний дизайн."
        ),
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "materials_label": _BAG_MATERIALS_LABEL,
        "materials_heading": _BAG_MATERIALS_HEADING,
        "materials": [
            {
                "num": "01",
                "title": "Теляча шкіра Togo та Box Calf",
                "text": (
                    "Сумка Birkin і Kelly Hermès виготовлені вручну "
                    "паризькими майстрами з найрідкіснішої шкіри Togo, "
                    "Clemence та Epsom. "
                    "Сумка гермес зберігає форму і фактуру десятиліттями."
                ),
            },
            {
                "num": "02",
                "title": "Фурнітура palladium та золото",
                "text": (
                    "Замки та застібки Birkin і Kelly виготовлені "
                    "з паладію або позолочених металів найвищого ґатунку. "
                    "Сумка біркін і сумка Kelly — фурнітура, "
                    "що не тьмяніє роками."
                ),
            },
            _MATERIAL_03,
            _MATERIAL_04,
        ],
        "keywords": [
            "сумка біркін", "сумка hermes birkin",
            "сумка kelly", "сумка гермес",
            "сумка hermes kelly", "hermes evelyne",
            "сумка hermes constance", "купити сумку birkin",
        ],
    },

    "Сумки_LV": {
        "title": "Сумки Louis Vuitton — Speedy, Neverfull, Alma — PulvasStore",
        "description": (
            "Купити сумку Louis Vuitton, бананку LV, рюкзак LV або клатч LV "
            "з доставкою по всьому світу."
        ),
        "hero_eyebrow": "Сумки Louis Vuitton · Класика",
        "hero_heading": "Сумки Louis Vuitton — бездоганна якість та вічна класика",
        "hero_subtitle": (
            "Speedy, Neverfull, Alma, Pochette — весь асортимент LV."
        ),
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "materials_label": _BAG_MATERIALS_LABEL,
        "materials_heading": _BAG_MATERIALS_HEADING,
        "materials": [
            {
                "num": "01",
                "title": "Monogram Canvas та шкіра LV",
                "text": (
                    "Сумка луї вітон Speedy, Neverfull та Alma "
                    "виготовлені зі знакового Monogram Canvas "
                    "і добірної телячої шкіри. "
                    "Жіноча сумка луї вітон і чоловіча зберігають "
                    "форму і вигляд роками."
                ),
            },
            {
                "num": "02",
                "title": "Золота фурнітура та замки LV",
                "text": (
                    "Бананка луї вітон і косметичка Louis Vuitton "
                    "оздоблені золотою фурнітурою LV. "
                    "Замки S-lock, кнопки та кільця сумок Louis Vuitton "
                    "виготовлені з металу найвищої якості."
                ),
            },
            _MATERIAL_03,
            _MATERIAL_04,
        ],
        "keywords": [
            "сумка луї вітон", "сумка louis vuitton speedy",
            "сумка lv neverfull", "сумка louis vuitton alma",
            "косметичка louis vuitton", "бананка луі вітон",
            "чемодан louis vuitton", "сумка lv pochette",
        ],
    },

    "Сумки_Prada": {
        "title": "Сумки Prada — нейлон, шкіра, Milano dal 1913 — PulvasStore",
        "description": (
            "Купити сумку Prada Milano, нейлонову сумку Prada або шкіряну Prada "
            "з доставкою по всьому світу."
        ),
        "hero_eyebrow": "Сумки Prada · Бездоганна якість",
        "hero_heading": "Сумки Prada — преміальна якість та бездоганний стиль",
        "hero_subtitle": (
            "Re-Edition, Galleria, нейлон Milano — весь асортимент Prada."
        ),
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "materials_label": _BAG_MATERIALS_LABEL,
        "materials_heading": _BAG_MATERIALS_HEADING,
        "materials": [
            {
                "num": "01",
                "title": "Re-Nylon та шкіра Saffiano",
                "text": (
                    "Сумка прада нейлон виготовлена з переробленого нейлону Re-Nylon — "
                    "екологічний і надзвичайно міцний матеріал. "
                    "Шкіряна сумка Prada Milano зі шкірою Saffiano "
                    "зберігає форму і витримує подряпини роками."
                ),
            },
            {
                "num": "02",
                "title": "Трикутна пластина та фурнітура Prada",
                "text": (
                    "Знаковий трикутний логотип Prada і фурнітура сумок "
                    "Prada Milano dal 1913 виготовлені з металу найвищої якості. "
                    "Замки і застібки сумки Prada — бездоганна точність збірки."
                ),
            },
            _MATERIAL_03,
            _MATERIAL_04,
        ],
        "keywords": [
            "сумка prada", "сумка прада", "сумка prada milano",
            "сумка прада нейлон", "сумка prada мужська",
            "сумки prada жіночі", "купити сумку prada",
            "сумка прада через плечо",
        ],
    },

    "Сумки_YSL": {
        "title": "Сумки YSL — Niki, Solferino, Sac de Jour — PulvasStore",
        "description": (
            "Купити сумку Yves Saint Laurent, YSL Niki, YSL Solferino або клатч YSL "
            "з доставкою по всьому світу."
        ),
        "hero_eyebrow": "Сумки Saint Laurent · Стиль і харизма",
        "hero_heading": "Сумки YSL Saint Laurent — преміальна якість та харизматичний стиль",
        "hero_subtitle": (
            "Sac de Jour, Niki, Solferino — весь асортимент Saint Laurent."
        ),
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "materials_label": _BAG_MATERIALS_LABEL,
        "materials_heading": _BAG_MATERIALS_HEADING,
        "materials": [
            {
                "num": "01",
                "title": "Шкіра та замша YSL",
                "text": (
                    "Сумка ів сен лоран Niki та Solferino виготовлені "
                    "з добірної м'якої шкіри і замші. "
                    "Сумка YSL Sac de Jour і Kate зберігають форму "
                    "і м'якість шкіри після тривалого використання."
                ),
            },
            {
                "num": "02",
                "title": "Фурнітура Saint Laurent",
                "text": (
                    "Замки, кільця і застібки сумок Saint Laurent "
                    "виготовлені з золотистого металу. "
                    "Сумка YSL Niki і сумка ів сен лоран — "
                    "кожна деталь бездоганної якості."
                ),
            },
            _MATERIAL_03,
            _MATERIAL_04,
        ],
        "keywords": [
            "сумка ysl", "сумка saint laurent",
            "сумка ів сен лоран", "сумка ysl niki",
            "сумка ysl solferino", "сумка sac de jour",
            "купити сумку ysl", "шоппер ів сен лоран",
        ],
    },

    "Сумки_Інші": {
        "title": "Дизайнерські сумки — Valentino, Celine, Fendi, Loewe — PulvasStore",
        "description": (
            "Купити сумку Valentino, Celine, Burberry, Fendi, Loewe або Bottega Veneta "
            "з доставкою по всьому світу."
        ),
        "hero_eyebrow": "Брендові сумки · Преміальний стиль",
        "hero_heading": "Сумки Valentino, Celine, Fendi, Bottega — преміальна якість",
        "hero_subtitle": (
            "Burberry, Loewe, Givenchy, Loro Piana — увесь світ преміальних сумок."
        ),
        "features_label": "Чому PulvasStore",
        "features": _DEFAULT_FEATURES,
        "materials_label": _BAG_MATERIALS_LABEL,
        "materials_heading": _BAG_MATERIALS_HEADING,
        "materials": [
            {
                "num": "01",
                "title": "Шкіра та текстиль преміум брендів",
                "text": (
                    "Сумка Valentino та сумка Fendi Roma виготовлені "
                    "з добірної телячої шкіри і нейлону. "
                    "Плетена сумка Bottega Veneta і сумка Loewe Puzzle — "
                    "вироби, що зберігають форму роками."
                ),
            },
            {
                "num": "02",
                "title": "Фурнітура та деталі",
                "text": (
                    "Замки і застібки сумок Celine та Burberry "
                    "виготовлені з металу найвищої якості. "
                    "Сумка Givenchy і сумка Loro Piana оздоблені "
                    "фурнітурою, що не тьмяніє роками."
                ),
            },
            _MATERIAL_03,
            _MATERIAL_04,
        ],
        "keywords": [
            "сумка valentino", "сумка celine", "сумка fendi",
            "сумка bottega veneta", "сумка burberry", "сумка loewe",
            "сумка givenchy", "сумка loro piana",
            "сумки барбери", "клатч bottega veneta",
        ],
    },
}

# ── Default (no ?g= parameter or unknown value) ───────────────────────────────

DEFAULT_GROUP: dict = {
    "title": "PulvasStore — Люксові аксесуари, взуття та одяг",
    "description": (
        "Купити брендові сумки, взуття, одяг та аксесуари з доставкою по всьому світу. "
        "Louis Vuitton, Gucci, Hermès, Chanel та інші."
    ),
    "hero_eyebrow": "Люксові речі · 2026",
    "hero_heading": "PulvasStore\nбезкомпромісна якість",
    "hero_subtitle": (
        "Louis Vuitton, Gucci, Hermès, Chanel, Balenciaga, Dior, Prada — "
        "весь асортимент від провідних будинків моди."
    ),
    "features_label": "Чому PulvasStore",
    "features": _DEFAULT_FEATURES,
    "materials_label": _BAG_MATERIALS_LABEL,
    "materials_heading": _BAG_MATERIALS_HEADING,
    "materials": [
        {
            "num": "01",
            "title": "Матеріали преміального рівня",
            "text": (
                "Добірна шкіра та якісний текстиль, що зберігають форму "
                "і вигляд навіть після тривалого використання."
            ),
        },
        {
            "num": "02",
            "title": "Надійна фурнітура",
            "text": (
                "Міцні замки та металеві деталі, що не тьмяніють "
                "і забезпечують довговічність."
            ),
        },
        _MATERIAL_03,
        _MATERIAL_04,
    ],
    "keywords": [
        "брендові сумки", "брендове взуття", "брендовий одяг",
        "люксові аксесуари", "купити луї вітон", "купити gucci",
        "купити chanel", "купити dior", "купити balenciaga",
        "сумка louis vuitton", "взуття gucci", "одяг balenciaga",
        "сумки hermès", "аксесуари prada",
    ],
}


def get_group(key: str) -> dict:
    """Return the content dict for the given ad-group key, or the default."""
    return AD_GROUPS.get(key, DEFAULT_GROUP)
