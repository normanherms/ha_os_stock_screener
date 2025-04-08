from .screener import run_screener
from .message_builder import build_message

def main():
    filtered = run_screener(limit=50)  # Optional: Limit für Tests
    message = build_message(filtered)

    with open("output/message.txt", "w", encoding="utf-8") as f:
        f.write(message)

    print("📨 Nachricht vorbereitet:")
    print(message)

if __name__ == "__main__":
    main()
