# Espresso Study: landing page (v3, pre-pubblicazione)

Landing statica, mobile first, in arabo (da destra a sinistra), inglese e francese. WhatsApp è il canale di conversione principale.

## File

- `index.html`: la pagina (HTML, CSS e JS inline, nessun build).
- `privacy.html`, `cookie-policy.html`: bozze delle informative, con i campi da completare evidenziati in giallo `[TO COMPLETE: …]`.
- `assets/fonts/`: font ospitati sul sito (licenza SIL OFL), nessuna richiesta a Google Fonts.
- `assets/peeps/`, `assets/italy/`: illustrazioni. `tools/`: script per rigenerarle.

## Aggiornare i contenuti (inizio dello `<script>` in `index.html`)

Tutto si modifica nel blocco **EDITABLE CONTENT**, senza toccare la logica:

| Costante | Cosa contiene |
|---|---|
| `DRAFT` | `true`: mostra i segnaposto e la barra gialla. **Mettere `false` prima di pubblicare**: i segnaposto spariscono e le sezioni vuote si nascondono. |
| `TESTIMONIALS` | Foto (`assets/testimonials/…`), nome, paese, corso, università, commento. Solo testimonianze reali e autorizzate. Le voci con `placeholder:true` non vengono mai pubblicate. |
| `VIDEOS` | Fino a 3 video: incollare l'ID di 11 caratteri (`youtube.com/watch?v=ID`) e il titolo. |
| `OUTLETS`, `NEWS` | Testate e articoli. `logo`: percorso di un logo ufficiale autorizzato, altrimenti si vede il nome della testata. |
| `PARTNERS` | UNIVPM, inlingua, eCapital, con tipo di rapporto (`agreement`, `language`, `award`). Si aggiungono altre voci con lo stesso formato. |
| `LOCAL_PARTNERS` | Agenzie locali con accordo attivo. Non sono mostrate in pagina; restano per future pagine dedicate ai singoli paesi. |

Numero WhatsApp: costante `WA` (`393275990381`).

## Privacy

- Nessun cookie di analisi o pubblicità. Nel browser vengono salvate solo la lingua (`es_lang`) e le scelte privacy (`es_consent`).
- I video YouTube si caricano solo dopo un clic e il consenso, da `youtube-nocookie.com`. Le anteprime vengono da Google solo dopo il consenso.
- "Privacy settings" nel footer apre la finestra per dare o revocare il consenso.
- Se in futuro si aggiungono pixel o strumenti di analisi (Meta, TikTok, Google), servono un banner di consenso e l'aggiornamento della cookie policy **prima** di attivarli.

## Link per le campagne

`?c=dz`, `?c=kw`, `?c=il` aprono la pagina in arabo; `?lang=en|ar|fr` forza la lingua.

## Prima di pubblicare

1. Mettere `DRAFT = false`.
2. Inserire testimonianze, ID dei video ed eventuali loghi ufficiali.
3. Completare i campi `[TO COMPLETE]` di privacy e cookie policy e farli verificare da un consulente; servono anche le versioni in arabo e francese.
4. Verificare i KPI (500+, 12+, 20+) con i dati del report istituzionale 2026 (120+ studenti supportati nel 2026).
