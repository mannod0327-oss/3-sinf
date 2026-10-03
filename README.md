# 3-sinf — ingliz tili (Grade 3) o'qituvchi materiallari

3-sinf o'quvchilari (8–9 yosh, CEFR Pre-A1 → A1) uchun **tayyor, chop etishga mo'ljallangan** dars materiallari. Uchta manba bo'yicha **alohida-alohida paket** tuzilgan: dars rejalari, ish varaqlari, kalitlar, o'yinlar va nazorat ishlari.

> Hamma narsa **original** yozilgan: darsliklarning matnlari, rasmlari, audio va videolari bu repozitoriyda **yo'q**. Paketlar darsliklarning rasmiy mundarijasiga mos mavzularda tuzilgan (qarang: [NOTICE.md](NOTICE.md)).

## Uchta paket

| Paket | Nima uchun | Hajmi | Boshlash |
|---|---|---|---|
| [**guess-what/**](guess-what/README.md) | Asosiy dastur — Cambridge *Guess What! Level 3* | Welcome + 8 unit, **68 soatlik yillik reja**, 4 ta chorak nazorati (40 ball) + og'zaki nazorat, lug'at | [README](guess-what/README.md) · [yillik reja](guess-what/annual-plan.md) |
| [**round-up-3/**](round-up-3/README.md) | Grammatika qo'shimchasi — *Round-Up 3* (Virginia Evans) | 8 ta grammatika mini-uniti (26 dars), 2 ta progress test (30 ball) | [README](round-up-3/README.md) · [reja](round-up-3/plan.md) |
| [**destination-a1/**](destination-a1/README.md) | Lug'at + grammatika qo'shimchasi — *Destination A1* (Macmillan) | 9 ta mini-unit (29 dars), 2 ta progress test (30 ball) | [README](destination-a1/README.md) · [reja](destination-a1/plan.md) |

Har bir unit/mini-unit papkasida bir xil to'plam bor:

- **dars rejalari** (45 daqiqa, 6 bosqich, o'zbek tilidagi metodik maslahatlar — o'zbekcha ta'sirdan keladigan odatiy xatolar bilan) — Markdown va Word;
- **2 ta ish varag'i** + **15 daqiqalik quick quiz** — PDF (chop etish uchun) va Word (tahrirlash uchun);
- **kalitlar** (`answer-keys.pdf`, faqat o'qituvchi uchun; tinglash matnlari bilan);
- **o'yinlar**: flashcards (A5), bingo (8 karta + caller sheet), juftlik (memory) kartalari;
- Round-Up va Destination'da qo'shimcha: 1 sahifalik **grammatika / so'z kartasi**.

Jami: **~223 PDF, ~117 Word, ~63 Markdown** fayl, hammasi bitta manba (`content/`) dan avtomatik qurilgan — shuning uchun kalitlar varaqlar bilan hech qachon mos kelmay qolmaydi.

## Qaysi paketdan qachon foydalanish

1. **Asos — Guess What!** Darslikka ergashasiz: yillik rejadagi dars raqami → unit papkasidagi `lesson-plans.md`.
2. **Grammatika yetishmasa — Round-Up 3 mini-unitlari** (masalan, *a / an / some*, *Present simple*, *Present continuous*). Har biri mustaqil: kerakli mavzuni tanlang.
3. **Lug'at va og'zaki nutq — Destination A1 mini-unitlari** (uy, kasblar, maktab, ovqat, ob-havo, kiyim).

Mavzular qanday bog'langani: [docs/curriculum-bridge.md](docs/curriculum-bridge.md). To'liq qo'llanma: [docs/teacher-handbook.md](docs/teacher-handbook.md).

## Hujjatlar

| Hujjat | Mazmuni |
|---|---|
| [docs/teacher-handbook.md](docs/teacher-handbook.md) | 45 daqiqalik dars tuzilishi, baholash (5-4-3-2), chop etish, o'yinlarni o'tkazish, o'zbek o'quvchilari uchun odatiy xatolar |
| [docs/curriculum-bridge.md](docs/curriculum-bridge.md) | Guess What! ↔ Round-Up 3 ↔ Destination A1 mavzu xaritasi |
| [docs/drive-inventory.md](docs/drive-inventory.md) | Google Drive papkangizdagi 12 ta fayl: nima 3-sinfga tegishli, nima emas, nima uchun repozitoriyga qo'yilmagan |
| [docs/sources.md](docs/sources.md) | Internetdan topilgan va tekshirilgan bepul resurslar (British Council, Cambridge, TeachingEnglish) |
| [NOTICE.md](NOTICE.md) | Mualliflik huquqi, Twemoji (CC-BY 4.0) va Andika (SIL OFL) atributsiyasi |

## Repozitoriy tuzilishi

```
guess-what/        round-up-3/        destination-a1/    <- tayyor materiallar (PDF / Word / Markdown)
content/                                                  <- manba: har bir unit bitta Python fayl
tools/                                                    <- quruvchi (PDF, Word, Markdown renderlar), shrift va rasmlar
tests/                                                    <- avtomatik tekshiruvlar (kalitlar, ballar, dars vaqtlari, Word tuzilishi)
docs/                                                     <- qo'llanmalar
```

## O'zgartirish va qayta qurish (ixtiyoriy)

Materialni o'zgartirish uchun `content/<paket>/<unit>.py` faylini tahrirlang va qaytadan quring — PDF, Word, kalit va Markdown birga yangilanadi.

```bash
python -m venv .venv && . .venv/bin/activate
pip install -r tools/requirements.txt
python tools/build.py                   # hammasi
python tools/build.py destination-a1 7  # bitta paketning bitta uniti
python -m pytest tests -q               # kalit, ball va dars vaqti tekshiruvlari
```

Testlar har bir mashq kaliti, ball yig'indisi (quiz = 20, chorak testi = 40, progress test = 30), lug'atdagi tarjima va rasm, har bir dars = 45 daqiqa ekanini va Word fayllarining OOXML tuzilishini tekshiradi.

## Cheklovlar (ochiq aytamiz)

- **Round-Up 3 va Destination A1 fayllari Drive papkangizda yo'q edi.** Bu ikki paket kitoblarning rasmiy mundarijasi asosida, 3-sinfga (A1) mos bo'limlardan tuzilgan. Kitob nusxangiz bo'lsa — har bir paketdagi `book-map.md` orqali mos bo'limni toping; nashrlar orasida unit raqamlari farq qilishi mumkin.
- **Guess What! darslik PDF'lari (SB / TB / WB) skaner rasm** ko'rinishida va juda katta (180–430 MB), shuning uchun ularning ichki matnini bu yerda o'qib bo'lmadi. Unit mavzulari Cambridge'ning rasmiy mundarijasi va Flashcards PDF'dan olingan; dars rejalarida **sahifa raqamlari ko'rsatilmagan** (nashrlarda farq qiladi).
- **Audio yo'q:** tinglash mashqlarida matnni o'qituvchi o'zi o'qiydi (kalit ichida *Teacher reads* qutisi bor). Darslikning audio / videosi Drive'dagi nusxangizdan olinadi.
- **Word fayllari** bu muhitda (Word / LibreOffice yo'q) ko'z bilan tekshirilmadi; ularning tuzilishi avtomatik testdan o'tgan. Birinchi ochganingizda biror joy ko'chib ketsa — PDF asosiy nusxa.
- Materiallarni **sinfda ishlatishdan oldin tajribali o'qituvchi ko'zdan kechirsin**: matnlar va o'zbekcha izohlar sinchiklab tekshirilgan, ammo AI yordamida tayyorlangan.
- **Litsenziya hali tanlanmagan** — repozitoriy ochiq (public), lekin `LICENSE` fayli yo'q, ya'ni standart bo'yicha barcha huquqlar sizda. Boshqa o'qituvchilar erkin foydalansin desangiz, litsenziya tanlang (masalan, materiallar uchun CC BY-NC-SA 4.0, kod uchun MIT) — bu sizning qaroringiz.
