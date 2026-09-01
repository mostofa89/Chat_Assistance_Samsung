import re


def _format_value(value):
    if isinstance(value, dict):
        lines = []

        for key, item in value.items():
            label = key.replace("_", " ").title()
            lines.append(f"{label}: {_format_value(item)}")

        return "\n".join(lines)

    if value is None or value == "":
        return "Not available"

    return str(value)


def extract_overall_score(review):
    match = re.search(
        r"OVERALL SCORE\s*[\r\n]+([0-9]+(?:\.[0-9]+)?)\s*/\s*10",
        review,
        re.IGNORECASE
    )

    if match:
        return float(match.group(1))

    return None


def calculate_overall_score(review):
    category_scores = re.findall(
        r"Score:\s*([0-9]+(?:\.[0-9]+)?)\s*/\s*10",
        review,
        re.IGNORECASE
    )

    if not category_scores:
        return None

    scores = [
        float(score)
        for score in category_scores
    ]

    return round(sum(scores) / len(scores), 1)


def _as_text(*values):
    return " ".join(
        str(value).lower()
        for value in values
        if value is not None and value != ""
    )


def _first_number(value):
    if value is None:
        return None

    match = re.search(
        r"(\d+(?:\.\d+)?)",
        str(value)
    )

    if not match:
        return None

    return float(match.group(1))


def _clamp_score(score):
    return max(0, min(10, round(score, 1)))


def _score_display(display):
    display = display or {}

    text = _as_text(
        display.get("type"),
        display.get("resolution"),
        display.get("protection"),
        display.get("brightness")
    )
    refresh_rate = _first_number(display.get("refresh_rate"))
    size = _first_number(display.get("size"))

    score = 5.0

    if "ltpo" in text:
        score += 1.4
    elif "dynamic amoled" in text:
        score += 1.2
    elif "amoled" in text:
        score += 0.9

    if refresh_rate and refresh_rate >= 120:
        score += 1.0
    elif refresh_rate and refresh_rate >= 90:
        score += 0.5

    if "1440" in text or "qhd" in text:
        score += 0.8
    elif "1080" in text:
        score += 0.4

    if size and size >= 6.7:
        score += 0.3

    if "gorilla" in text or "victus" in text or "armor" in text:
        score += 0.5

    return _clamp_score(score)


def _score_performance(platform, memory):
    platform = platform or {}
    memory = memory or {}

    text = _as_text(
        platform.get("chipset"),
        platform.get("cpu"),
        platform.get("gpu")
    )
    ram = _first_number(memory.get("ram"))

    score = 5.0

    if "8 elite" in text:
        score += 2.6
    elif "8 gen 3" in text or "exynos 2400" in text:
        score += 2.3
    elif "8 gen 2" in text:
        score += 2.0
    elif "8 gen 1" in text or "exynos 2200" in text:
        score += 1.5
    elif "888" in text or "exynos 2100" in text:
        score += 1.2
    elif "exynos 1380" in text:
        score += 0.7

    if ram and ram >= 12:
        score += 0.8
    elif ram and ram >= 8:
        score += 0.5
    elif ram and ram >= 6:
        score += 0.2

    return _clamp_score(score)


def _score_camera(camera, selfie_camera):
    camera = camera or {}
    selfie_camera = selfie_camera or {}

    text = _as_text(
        camera.get("main"),
        camera.get("ultrawide"),
        camera.get("telephoto"),
        camera.get("depth"),
        camera.get("features"),
        camera.get("video"),
        selfie_camera.get("camera"),
        selfie_camera.get("video")
    )
    main_mp = _first_number(camera.get("main"))

    score = 5.0

    if main_mp and main_mp >= 200:
        score += 1.6
    elif main_mp and main_mp >= 108:
        score += 1.3
    elif main_mp and main_mp >= 50:
        score += 1.0
    elif main_mp and main_mp >= 12:
        score += 0.5

    if camera.get("ultrawide"):
        score += 0.5

    if camera.get("telephoto"):
        score += 0.8

    if "ois" in text:
        score += 0.5

    if "8k" in text:
        score += 0.5
    elif "4k" in text:
        score += 0.3

    return _clamp_score(score)


def _score_battery(battery):
    battery = battery or {}

    capacity = _first_number(battery.get("capacity"))
    charging = _first_number(battery.get("charging"))
    wireless = _as_text(battery.get("wireless_charging"))

    score = 5.0

    if capacity and capacity >= 5000:
        score += 1.5
    elif capacity and capacity >= 4700:
        score += 1.2
    elif capacity and capacity >= 4300:
        score += 0.8
    elif capacity and capacity >= 3900:
        score += 0.4

    if charging and charging >= 45:
        score += 0.8
    elif charging and charging >= 25:
        score += 0.5

    if wireless and wireless != "no":
        score += 0.4

    return _clamp_score(score)


def _score_storage(memory):
    memory = memory or {}

    text = _as_text(
        memory.get("storage"),
        memory.get("card_slot")
    )

    score = 5.0

    if "1 tb" in text:
        score += 1.4
    elif "512" in text:
        score += 1.0
    elif "256" in text:
        score += 0.7
    elif "128" in text:
        score += 0.4

    if "microsd" in text:
        score += 0.5

    return _clamp_score(score)


def _score_design(body):
    body = body or {}

    text = _as_text(
        body.get("build"),
        body.get("ip_rating"),
        body.get("dimensions"),
        body.get("weight")
    )
    weight = _first_number(body.get("weight"))

    score = 5.0

    if "titanium" in text:
        score += 1.2
    elif "aluminum" in text and "glass" in text:
        score += 0.8
    elif "plastic" in text:
        score += 0.3

    if "ip68" in text:
        score += 0.8
    elif "ip67" in text or "ipx8" in text:
        score += 0.6

    if weight and weight <= 170:
        score += 0.5
    elif weight and weight <= 200:
        score += 0.3

    return _clamp_score(score)


def _score_connectivity(network, connectivity):
    network = network or {}
    connectivity = connectivity or {}

    text = _as_text(
        network.get("technology"),
        network.get("speed"),
        connectivity.get("wlan"),
        connectivity.get("bluetooth"),
        connectivity.get("gps"),
        connectivity.get("nfc"),
        connectivity.get("usb")
    )

    score = 5.0

    if "5g" in text:
        score += 1.0

    if "wi-fi 7" in text or "/7" in text:
        score += 0.8
    elif "6e" in text:
        score += 0.6
    elif "wi-fi 6" in text or "/6" in text:
        score += 0.4

    if "5.4" in text:
        score += 0.5
    elif "5.3" in text:
        score += 0.4
    elif "5.2" in text:
        score += 0.3

    if "nfc" in text or connectivity.get("nfc"):
        score += 0.3

    if "type-c 3.2" in text:
        score += 0.4

    return _clamp_score(score)


def calculate_gsmarena_overall_score(specifications):
    scores = {
        "display": _score_display(specifications.get("display", {})),
        "performance": _score_performance(
            specifications.get("platform", {}),
            specifications.get("memory", {})
        ),
        "camera": _score_camera(
            specifications.get("camera", {}),
            specifications.get("selfie_camera", {})
        ),
        "battery": _score_battery(specifications.get("battery", {})),
        "storage": _score_storage(specifications.get("memory", {})),
        "design": _score_design(specifications.get("body", {})),
        "connectivity": _score_connectivity(
            specifications.get("network", {}),
            specifications.get("connectivity", {})
        ),
    }

    weights = {
        "display": 1.2,
        "performance": 1.4,
        "camera": 1.3,
        "battery": 1.2,
        "storage": 0.8,
        "design": 0.9,
        "connectivity": 0.7,
    }

    total_weight = sum(weights.values())
    weighted_score = sum(
        scores[key] * weights[key]
        for key in scores
    )

    return _clamp_score(weighted_score / total_weight), scores


def ensure_overall_score(review, overall_score=None):
    if overall_score is None:
        overall_score = extract_overall_score(review)

    if overall_score is not None:
        review = re.sub(
            r"\n*OVERALL SCORE\s*[\r\n]+[0-9]+(?:\.[0-9]+)?\s*/\s*10",
            "",
            review,
            flags=re.IGNORECASE
        ).rstrip()

        review = (
            f"{review}\n\n"
            f"OVERALL SCORE\n"
            f"{overall_score}/10"
        )

        return review, overall_score

    overall_score = calculate_overall_score(review)

    if overall_score is None:
        return review, None

    review = (
        f"{review.rstrip()}\n\n"
        f"OVERALL SCORE\n"
        f"{overall_score}/10"
    )

    return review, overall_score


class ReviewAgent:

    def generate_review(self, specifications):

        phone = specifications.get("name", "Unknown Phone")

        context = f"""
Phone: {phone}

Display:
{_format_value(specifications.get("display"))}

Processor:
{_format_value(specifications.get("platform"))}

RAM:
{_format_value(specifications.get("memory", {}).get("ram"))}

Storage:
{_format_value(specifications.get("memory", {}).get("storage"))}

Camera:
{_format_value(specifications.get("camera"))}

Battery:
{_format_value(specifications.get("battery"))}

Design:
{_format_value(specifications.get("body"))}

Connectivity:
{_format_value(specifications.get("connectivity"))}

Software:
{_format_value(specifications.get("platform", {}).get("os"))}

Audio:
{_format_value(specifications.get("sound"))}

Sensors:
{_format_value(specifications.get("sensors"))}

Price:
{_format_value(specifications.get("other", {}).get("price"))}
"""

        question = """

You are a professional Samsung smartphone reviewer.

Analyze the phone using ONLY the specifications provided in
the context.

Do NOT invent specifications or features.

Review the phone using these categories:

1. Display
2. Performance
3. Camera
4. Battery
5. Storage
6. Design & Build
7. Connectivity
8. Software
9. Audio
10. Value for Money

For every category:

* Give a short explanation.
* Give a score from 0 to 10.

Then calculate the OVERALL SCORE from all available category
scores.

Use this exact response structure:

PHONE
[Phone name]

DISPLAY
[Short evaluation]
Score: X/10

PERFORMANCE
[Short evaluation]
Score: X/10

CAMERA
[Short evaluation]
Score: X/10

BATTERY
[Short evaluation]
Score: X/10

STORAGE
[Short evaluation]
Score: X/10

DESIGN & BUILD
[Short evaluation]
Score: X/10

CONNECTIVITY
[Short evaluation]
Score: X/10

SOFTWARE
[Short evaluation]
Score: X/10

AUDIO
[Short evaluation]
Score: X/10

VALUE FOR MONEY
[Short evaluation]
Score: X/10

PROS

* [Pro 1]
* [Pro 2]
* [Pro 3]
* [Pro 4]

CONS

* [Con 1]
* [Con 2]
* [Con 3]
* [Con 4]

OVERALL SCORE
X/10

VERDICT
[Write a balanced final recommendation.]

SCORING:

0-2   = Very Poor
3-4   = Poor
5-6   = Average
7     = Good
8     = Very Good
9     = Excellent
10    = Outstanding

IMPORTANT RULES:

* Use ONLY information from the context.
* Never invent missing specifications.
* If information is missing, say "Not available".
* Do not assume specifications from the phone model name.
* Do not give a score based on information that is not available.
* The overall score must be based on the category scores.
* Keep the review factual and balanced.
"""

        try:
            from app.chatbot.llm import ask_llm

            review = ask_llm(
                context,
                question
            ).strip()

            overall_score, _ = calculate_gsmarena_overall_score(
                specifications
            )

            review, _ = ensure_overall_score(
                review,
                overall_score
            )

            return review

        except Exception as e:
            return (
                f"Unable to generate review for {phone}. "
                f"Error: {str(e)}"
            )
