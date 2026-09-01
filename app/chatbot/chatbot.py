from app.rag.retriever import search


def _clean(value):
    if value is None or value == "":
        return "Not available"

    return str(value)


def _number_from_text(value):
    import re

    if value is None:
        return 0

    match = re.search(
        r"(\d+(?:\.\d+)?)",
        str(value)
    )

    if not match:
        return 0

    return float(match.group(1))


def _normalize(text):
    return " ".join(
        text.lower().replace("+", " plus").split()
    )


def _phone_aliases(phone):
    normalized_name = _normalize(phone.name)
    aliases = {
        normalized_name,
        normalized_name.replace("samsung ", ""),
        normalized_name.replace("samsung galaxy ", ""),
        normalized_name.replace(" 5g", ""),
        normalized_name.replace("samsung ", "").replace(" 5g", ""),
        normalized_name.replace("samsung galaxy ", "").replace(" 5g", ""),
    }

    return {
        alias.strip()
        for alias in aliases
        if alias.strip()
    }


def _find_mentioned_phones(question, phones):
    normalized_question = _normalize(question)
    matches = []

    for phone in phones or []:
        if any(alias in normalized_question for alias in _phone_aliases(phone)):
            matches.append(phone)

    return sorted(
        matches,
        key=lambda phone: len(phone.name),
        reverse=True
    )


def _display_answer(phone):
    return (
        f"{phone.name} has a {_clean(phone.display_size)} "
        f"{_clean(phone.display_type)} display with "
        f"{_clean(phone.display_resolution)} resolution"
        f" and {_clean(phone.display_refresh_rate)} refresh rate."
    )


def _camera_answer(phone):
    parts = [
        f"main camera: {_clean(phone.main_camera)}",
        f"ultrawide: {_clean(phone.ultrawide_camera)}",
        f"telephoto: {_clean(phone.telephoto_camera)}",
        f"selfie camera: {_clean(phone.selfie_camera)}",
        f"video: {_clean(phone.main_camera_video)}",
    ]

    return f"{phone.name} camera specs are " + ", ".join(parts) + "."


def _battery_answer(phone):
    return (
        f"{phone.name} has a {_clean(phone.battery)} battery, "
        f"{_clean(phone.charging)} charging, and "
        f"{_clean(phone.wireless_charging)} wireless charging."
    )


def _performance_answer(phone):
    return (
        f"{phone.name} uses {_clean(phone.chipset)}, "
        f"with {_clean(phone.cpu)} CPU and {_clean(phone.gpu)} GPU."
    )


def _memory_answer(phone):
    return (
        f"{phone.name} has {_clean(phone.ram)} RAM and "
        f"{_clean(phone.storage)} storage. Card slot: {_clean(phone.card_slot)}."
    )


def _summary_answer(phone):
    return (
        f"{phone.name}: {_clean(phone.display_size)} "
        f"{_clean(phone.display_type)} display, {_clean(phone.chipset)} chipset, "
        f"{_clean(phone.ram)} RAM, {_clean(phone.storage)} storage, "
        f"{_clean(phone.main_camera)} main camera, and {_clean(phone.battery)} battery."
    )


def _list_phones_answer(question, phones):
    q = question.lower()

    if not phones:
        return None

    if not any(word in q for word in ["list", "available", "models", "phones"]):
        return None

    if any(word in q for word in ["best", "camera", "battery", "processor", "compare"]):
        return None

    names = [
        phone.name
        for phone in phones
    ]

    return "Available phones in the database: " + ", ".join(names) + "."


def _single_phone_answer(question, phone):
    q = question.lower()

    if any(word in q for word in ["battery", "mah", "charging"]):
        return _battery_answer(phone)

    if any(word in q for word in ["camera", "photo", "video", "selfie"]):
        return _camera_answer(phone)

    if any(word in q for word in ["display", "screen", "resolution", "refresh"]):
        return _display_answer(phone)

    if any(word in q for word in ["processor", "chipset", "performance", "cpu", "gpu"]):
        return _performance_answer(phone)

    if any(word in q for word in ["ram", "storage", "memory"]):
        return _memory_answer(phone)

    if any(word in q for word in ["price", "cost"]):
        return f"{phone.name} price: {_clean(phone.price)}."

    if any(word in q for word in ["os", "android", "software"]):
        return f"{phone.name} runs {_clean(phone.os)}."

    if any(word in q for word in ["weight", "build", "design", "ip rating", "water"]):
        return (
            f"{phone.name} has {_clean(phone.dimensions)} dimensions, "
            f"{_clean(phone.weight)} weight, {_clean(phone.build)} build, "
            f"and {_clean(phone.ip_rating)} rating."
        )

    return _summary_answer(phone)


def _comparison_answer(question, phones):
    q = question.lower()

    if len(phones) < 2:
        return None

    if not any(word in q for word in ["compare", "difference", "better", "vs"]):
        return None

    phone1 = phones[0]
    phone2 = phones[1]

    return (
        f"{phone1.name} vs {phone2.name}: "
        f"display: {_clean(phone1.display_size)} {_clean(phone1.display_resolution)} "
        f"vs {_clean(phone2.display_size)} {_clean(phone2.display_resolution)}; "
        f"processor: {_clean(phone1.chipset)} vs {_clean(phone2.chipset)}; "
        f"RAM/storage: {_clean(phone1.ram)}, {_clean(phone1.storage)} vs "
        f"{_clean(phone2.ram)}, {_clean(phone2.storage)}; "
        f"main camera: {_clean(phone1.main_camera)} vs {_clean(phone2.main_camera)}; "
        f"battery: {_clean(phone1.battery)} vs {_clean(phone2.battery)}."
    )


def _best_phone_answer(question, phones):
    q = question.lower()

    if not phones:
        return None

    if not any(word in q for word in ["best", "strongest", "top", "highest", "largest", "most"]):
        return None

    if "battery" in q:
        phone = max(
            phones,
            key=lambda item: _number_from_text(item.battery)
        )

        return (
            f"Based on the database, {phone.name} has the strongest battery "
            f"capacity at {_clean(phone.battery)}."
        )

    if "camera" in q:
        phone = max(
            phones,
            key=lambda item: (
                _number_from_text(item.main_camera),
                1 if item.telephoto_camera else 0,
                1 if item.ultrawide_camera else 0
            )
        )

        return (
            f"Based on the database, {phone.name} has the strongest camera "
            f"setup: main {_clean(phone.main_camera)}, ultrawide "
            f"{_clean(phone.ultrawide_camera)}, telephoto "
            f"{_clean(phone.telephoto_camera)}, and video "
            f"{_clean(phone.main_camera_video)}."
        )

    if any(word in q for word in ["performance", "processor", "chipset"]):
        chipset_order = [
            "8 elite",
            "8 gen 3",
            "exynos 2400",
            "8 gen 2",
            "8 gen 1",
            "exynos 2200",
            "888",
            "exynos 2100",
        ]

        def score(phone):
            chipset = _normalize(_clean(phone.chipset))

            for index, name in enumerate(chipset_order):
                if name in chipset:
                    return len(chipset_order) - index

            return 0

        phone = max(phones, key=score)

        return (
            f"Based on the database, {phone.name} has the strongest listed "
            f"processor: {_clean(phone.chipset)}."
        )

    return None


def answer_question(index, question, phones=None):
    list_answer = _list_phones_answer(question, phones)

    if list_answer:
        return list_answer

    direct_answer = _best_phone_answer(question, phones)

    if direct_answer:
        return direct_answer

    mentioned_phones = _find_mentioned_phones(question, phones)

    if mentioned_phones:
        comparison_answer = _comparison_answer(
            question,
            mentioned_phones
        )

        if comparison_answer:
            return comparison_answer

        direct_answer = _single_phone_answer(
            question,
            mentioned_phones[0]
        )

        if direct_answer:
            return direct_answer

    if index is None:
        return "The information is not available in the database."

    documents = search(index, question, k=3)

    if not documents:
        return "The information is not available in the database."

    context = "\n\n".join(documents)

    from app.chatbot.llm import ask_llm

    answer = ask_llm(
        context,
        question
    )

    return answer
