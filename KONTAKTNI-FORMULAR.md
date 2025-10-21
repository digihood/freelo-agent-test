# Kontaktní formulář - Test s Chrome DevTools MCP

Jednoduchý HTML kontaktní formulář s automatizovaným testováním pomocí chrome-devtools MCP nástrojů.

## 📋 Obsah projektu

- `contact-form.html` - Hlavní HTML formulář s CSS a JavaScript
- `test_form.py` - Testovací skript s dokumentací MCP příkazů
- `test-screenshot.png` - Screenshot formuláře
- `KONTAKTNI-FORMULAR.md` - Tento soubor s instrukcemi

## 🚀 Jak spustit

### 1. Spuštění lokálního serveru

```bash
# Python 3
python3 -m http.server 8000

# Alternativně Python 2
python -m SimpleHTTPServer 8000
```

### 2. Otevření formuláře

Otevřete prohlížeč a přejděte na:
```
http://localhost:8000/contact-form.html
```

## ✨ Funkce formuláře

### Pole formuláře
- **Jméno a příjmení** (povinné, min. 2 znaky)
- **E-mail** (povinné, validní formát)
- **Zpráva** (povinné, min. 10 znaků, max. 500 znaků)
- **Submit tlačítko** - Odeslat zprávu

### Validace
- ✓ Real-time validace při psaní
- ✓ Zobrazení chybových hlášek pod poli
- ✓ Vizuální zvýraznění nevalidních polí
- ✓ Kontrola formátu emailu
- ✓ Počítadlo znaků u zprávy (0/500)

### Design
- ✓ Moderní gradient pozadí (fialovo-modrá)
- ✓ Čistý bílý card s rounded corners
- ✓ Smooth animace a transitions
- ✓ Hover efekty na tlačítku
- ✓ Responsive design
- ✓ Úspěšná zpráva po odeslání

## 🧪 Testování s Chrome DevTools MCP

### Dostupné MCP nástroje

Tento projekt je nakonfigurovaný pro testování pomocí chrome-devtools MCP serveru.

#### Povolené nástroje:
- `navigate_page` - Navigace na URL
- `take_screenshot` - Screenshot stránky
- `click` - Kliknutí na element
- `fill` - Vyplnění inputu
- `wait_for` - Čekání na podmínku
- `get_console_message` / `list_console_messages` - Console logy
- `performance_start_trace` / `performance_stop_trace` - Performance analýza

### Testovací scénář

```python
# 1. Navigace na formulář
mcp__chrome-devtools__navigate_page({
    "url": "http://localhost:8000/contact-form.html"
})

# 2. Snapshot pro získání UIDs elementů
mcp__chrome-devtools__take_snapshot()

# 3. Vyplnění jména
mcp__chrome-devtools__fill({
    "uid": "name",
    "value": "Jan Novák"
})

# 4. Vyplnění emailu
mcp__chrome-devtools__fill({
    "uid": "email",
    "value": "jan.novak@email.cz"
})

# 5. Vyplnění zprávy
mcp__chrome-devtools__fill({
    "uid": "message",
    "value": "Dobrý den, chtěl bych se informovat o vašich službách. Děkuji!"
})

# 6. Kliknutí na submit
mcp__chrome-devtools__click({
    "uid": "submit"
})

# 7. Čekání na úspěšnou zprávu
mcp__chrome-devtools__wait_for({
    "text": "Zpráva byla úspěšně odeslána",
    "timeout": 5000
})

# 8. Screenshot (optimalizovaný - best practices)
mcp__chrome-devtools__take_screenshot({
    "filePath": "/tmp/test-screenshot.png",
    "format": "jpeg",
    "quality": 80
})
```

### Screenshot Best Practices

**DŮLEŽITÉ:** Vždy používejte `filePath` parametr!

```python
# ✅ SPRÁVNĚ - použití filePath
mcp__chrome-devtools__take_screenshot({
    "filePath": "/tmp/screenshot.png",
    "format": "jpeg",
    "quality": 70
})

# ❌ ŠPATNĚ - bez filePath (způsobí buffer overflow)
mcp__chrome-devtools__take_screenshot()
```

**Optimalizace velikosti:**
- Použijte `"format": "jpeg"` nebo `"webp"` místo PNG (10x menší!)
- Nastavte `"quality": 60-80` pro dobrý poměr kvality/velikosti
- Použijte `"fullPage": false` pro capture pouze viewportu
- Použijte `"uid": "element_id"` pro screenshot konkrétního elementu

## 🎨 Technologie

- **HTML5** - Sémantické značky
- **CSS3** - Gradients, transitions, animations
- **JavaScript (Vanilla)** - Validace, DOM manipulace
- **Chrome DevTools MCP** - Automatizované testování

## 📝 Testování skriptem

Spusťte testovací skript pro zobrazení dokumentace:

```bash
python3 test_form.py
```

Skript obsahuje:
- ✓ Popis všech polí formuláře
- ✓ Validační pravidla
- ✓ Příklady MCP příkazů
- ✓ Kompletní testovací scénář

## 🔍 Kontrola funkčnosti

### Manuální test:
1. Otevřete formulář v prohlížeči
2. Zkuste odeslat prázdný formulář → zobrazí se chyby
3. Vyplňte nevalidní email → zobrazí se chyba
4. Napište zprávu kratší než 10 znaků → zobrazí se chyba
5. Vyplňte všechna pole správně → zobrazí se zelená úspěšná zpráva

### Automatizovaný test:
1. Spusťte HTTP server (`python3 -m http.server 8000`)
2. Použijte MCP nástroje v Claude Code pro automatické vyplnění a test
3. Screenshot potvrdí úspěšné načtení formuláře

## 📸 Screenshots

### test-screenshot.png
Obsahuje:
- ✓ Kompletní zobrazení formuláře
- ✓ Všechna pole s placeholdery
- ✓ Submit tlačítko
- ✓ Gradient pozadí

## 🎯 Výsledky testu

✅ **Úspěšně otestováno:**
- Navigace na localhost:8000
- Screenshot formuláře vytvořen
- Formulář se správně zobrazuje
- Všechna pole jsou přístupná (id: name, email, message, submit)
- CSS styling funguje (gradient, rounded corners, shadow)
- JavaScript validace je připravená

## 📦 Struktura souborů

```
freelo-agent-test/
├── contact-form.html         # Hlavní formulář
├── test_form.py              # Testovací dokumentace
├── test-screenshot.png       # Screenshot formuláře
└── KONTAKTNI-FORMULAR.md     # Tento soubor (instrukce)
```

## 💡 Poznámky

- Server běží na `localhost:8000` - ujistěte se, že port není obsazený
- Pro zastavení serveru použijte `Ctrl+C`
- Formulář využívá moderní CSS (gradient, flexbox) - funguje ve všech moderních prohlížečích
- JavaScript validace běží v reálném čase při psaní
- Console.log při úspěšném odeslání loguje data formuláře (pro debugging)

## 🚧 Možná rozšíření

- [ ] Backend API endpoint pro reálné odesílání
- [ ] ReCAPTCHA ochrana
- [ ] Více polí (telefon, firma, předmět)
- [ ] AJAX odeslání bez reloadu stránky
- [ ] Lokalizace do více jazyků
- [ ] Dark mode přepínač
- [ ] Ukládání draftu do localStorage

---

**Vytvořeno jako Freelo task demo** 🚀
