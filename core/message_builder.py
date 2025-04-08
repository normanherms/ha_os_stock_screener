def build_message(filtered: dict) -> str:
    if not filtered:
        return "📭 Keine auffälligen Aktienbewegungen heute."

    lines = []
    for name, data in filtered.items():
        sign = "📉" if data["change_pct"] < 0 else "📈"
        change = f"{data['change_pct']}%"
        price = f"{data['price']} €"
        volume_mio = round(data["volume"] / 1_000_000, 1)
        volume_str = f"{volume_mio} Mio."
        lines.append(f"{sign} {name}: {change} | Kurs: {price} | Volumen: {volume_str}")

    return "\n".join(lines)
