# NOTICE — mualliflik huquqi va atributsiya

## Bu repozitoriydagi materiallar

Dars rejalari, ish varaqlari, testlar, kalitlar, o'yinlar, lug'at ro'yxatlari va matnlar **original** yozilgan va faqat 3-sinf ta'lim maqsadida tayyorlangan. Ular quyidagi darsliklarning matnini, mashqlarini, rasmlarini, audio va videolarini **ko'chirmaydi**:

| Darslik | Nashriyot | Qanday foydalanilgan |
|---|---|---|
| *Guess What!* Level 3 — British English (Susannah Reed, Lesley Koustaff, Kay Bentley; ISBN 978-1-107-52801-7) va American English nashri | Cambridge University Press | Faqat unit nomlari, mavzu va grammatika maqsadlari (rasmiy mundarija) asosida mavzulashtirilgan |
| *Round-Up 3* (Virginia Evans) | Pearson / Longman | Faqat bo'limlar tartibi va mavzulari (rasmiy mundarija) asosida |
| *Destination A1* (*Destination A1 Plus*, 2017, ISBN 9781380015464) | Macmillan Education | Faqat bo'limlar tartibi va mavzulari (rasmiy mundarija) asosida |

*Guess What!*, *Round-Up* va *Destination* — o'z egalarining nomlari / savdo belgilari. Bu repozitoriy ular bilan **bog'liq emas** va ular tomonidan tasdiqlanmagan; nomlar faqat materiallar qaysi darslik mavzulariga mos kelishini ko'rsatish uchun ishlatilgan.

Darslik fayllari (PDF, audio, video, Test Generator) sizning shaxsiy Google Drive papkangizda qoladi va **bu repozitoriyga qo'yilmagan** — bu fayllar nashriyotlarning mualliflik huquqi ostida (qarang: [docs/drive-inventory.md](docs/drive-inventory.md)).

## Uchinchi tomon komponentlari

### Rasmlar — Twemoji

`tools/assets/emoji/` papkasidagi rasmlar — **Twemoji** (© Twitter, Inc. va boshqa hissa qo'shuvchilar; hozirgi qo'llab-quvvatlovchi: jdecked/twemoji). Grafikalar **CC-BY 4.0** ostida: <https://creativecommons.org/licenses/by/4.0/>. Rasmlar `@twemoji/svg` 15.0.0 to'plamidan PNG formatiga o'tkazilgan (`tools/build_assets.py`); hajmi va rangi o'zgartirilgan. Har bir chop etiladigan sahifaning pastida atributsiya ko'rsatilgan: *emoji: Twemoji (CC-BY 4.0)*.

Soat va old qo'shimchali rasmlar (`[[clock-…]]`, `[[prep-…]]`) shu loyihada dastur orqali chizilgan original sodda grafikalar.

### Shrift — Andika

PDF'lardagi shrift — **Andika** (© 2004–2022 SIL International), **SIL Open Font License 1.1** ostida. Litsenziya matni: [tools/assets/fonts/OFL.txt](tools/assets/fonts/OFL.txt). Shrift o'zgartirilmagan. Andika o'qishni endi o'rganayotgan bolalar uchun mo'ljallangan (aniq farqlanadigan *a, g, I, l* harflari).

### Qurish uchun kutubxonalar

ReportLab, python-docx, CairoSVG, Pillow, lxml, pytest — har biri o'z ochiq litsenziyasi ostida; ular repozitoriyga ko'chirilmagan, [tools/requirements.txt](tools/requirements.txt) orqali o'rnatiladi.

## Litsenziya

Bu repozitoriyga hozircha **`LICENSE` fayli qo'shilmagan**. Fayl bo'lmaganda, ochiq repozitoriyda ham materiallar bo'yicha barcha huquqlar muallifda (repozitoriy egasida) qoladi; boshqalar ularni ko'rishi mumkin, lekin qayta tarqatish huquqi berilmagan. Tanlov — egasining qaroriga bog'liq. Odatiy tanlovlar:

- **CC BY-NC-SA 4.0** — materiallarni noshirlik bo'lmagan maqsadda erkin ulashish va moslashtirish, muallif ko'rsatilgan holda;
- **CC BY 4.0** — eng erkin; tijoriy foydalanishga ham ruxsat;
- kod (`tools/`, `tests/`, `content/` Python fayllari) uchun **MIT**.

Qaysi litsenziya tanlansa ham, yuqoridagi Twemoji (CC-BY 4.0) va Andika (OFL) shartlari saqlanib qoladi.
