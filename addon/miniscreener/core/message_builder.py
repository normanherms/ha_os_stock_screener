def build_message(filtered: dict, max_length: int = 254) -> str:
    if not filtered:
        return "📭 Keine auffälligen Aktienbewegungen heute."

    lines = []
    hint = "📈 Weitere Ergebnisse anzeigen..."

    for name, data in filtered.items():
        sign = "📉" if data["change_pct"] < 0 else "📈"
        change = f"{data['change_pct']}%"
        price = f"{data['price']} €"
        volume_mio = round(data["volume"] / 1_000_000, 1)
        volume_str = f"{volume_mio} Mio."

        line = f"{sign} {name}: {change} | Kurs: {price} | Volumen: {volume_str}"

        # Wenn nächste Zeile + Hinweis zu lang wäre → abbrechen mit Hinweis
        preview = "\n".join(lines + [line, hint])
        if len(preview) > max_length:
            lines.append(hint)
            break

        lines.append(line)

    if not lines:
        return "📭 Keine auffälligen Aktienbewegungen heute."

    return "\n".join(lines)
