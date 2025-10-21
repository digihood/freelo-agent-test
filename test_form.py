#!/usr/bin/env python3
"""
Testovací skript pro kontaktní formulář
Demonstrační použití chrome-devtools MCP nástrojů
"""

def test_contact_form():
    """
    Tento skript ukazuje, jak by se formulář testoval pomocí chrome-devtools MCP.

    Kroky testu:
    1. Navigovat na http://localhost:8000/contact-form.html
    2. Vyplnit pole pro jméno (id="name")
    3. Vyplnit pole pro email (id="email")
    4. Vyplnit textarea pro zprávu (id="message")
    5. Kliknout na submit tlačítko (id="submit")
    6. Ověřit zobrazení úspěšné zprávy
    7. Udělat screenshot

    Příklady MCP příkazů (vykonávané v Claude Code):

    # 1. Navigace na formulář
    mcp__chrome-devtools__navigate_page({
        "url": "http://localhost:8000/contact-form.html"
    })

    # 2. Vytvoření snapshotu pro získání UIDs elementů
    mcp__chrome-devtools__take_snapshot()

    # 3. Vyplnění formuláře pomocí fill
    mcp__chrome-devtools__fill({
        "uid": "name",
        "value": "Jan Novák"
    })

    mcp__chrome-devtools__fill({
        "uid": "email",
        "value": "jan.novak@email.cz"
    })

    mcp__chrome-devtools__fill({
        "uid": "message",
        "value": "Dobrý den, chtěl bych se informovat o vašich službách. Děkuji!"
    })

    # 4. Kliknutí na submit tlačítko
    mcp__chrome-devtools__click({
        "uid": "submit"
    })

    # 5. Čekání na zobrazení úspěšné zprávy
    mcp__chrome-devtools__wait_for({
        "text": "Zpráva byla úspěšně odeslána",
        "timeout": 5000
    })

    # 6. Screenshot (s optimalizací dle best practices)
    mcp__chrome-devtools__take_screenshot({
        "filePath": "/tmp/test-screenshot.png",
        "format": "jpeg",
        "quality": 80
    })

    # 7. Kontrola console logů
    mcp__chrome-devtools__list_console_messages()
    """

    print("Testovací scénář pro kontaktní formulář")
    print("=" * 50)
    print("\nFormulář obsahuje:")
    print("✓ Pole pro jméno (id='name')")
    print("✓ Pole pro email (id='email')")
    print("✓ Textarea pro zprávu (id='message')")
    print("✓ Submit tlačítko (id='submit')")
    print("\nValidace:")
    print("✓ Jméno - minimálně 2 znaky")
    print("✓ Email - validní formát")
    print("✓ Zpráva - minimálně 10 znaků, max 500")
    print("\nFunkce:")
    print("✓ Real-time validace při psaní")
    print("✓ Počítadlo znaků u zprávy")
    print("✓ Zobrazení chybových hlášek")
    print("✓ Úspěšná zpráva po odeslání")
    print("✓ Responsive design")
    print("✓ Moderní gradient UI")

if __name__ == "__main__":
    test_contact_form()
