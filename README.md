# Espresso Study: landing page (bozza)

Landing page statica, mobile first, per gli studenti arabofoni che vogliono studiare in Italia.
Mercati prioritari: Algeria, Kuwait, studenti arabi in Israele.

## Struttura

- `index.html`: tutta la pagina in un unico file (HTML, CSS e JS inline, nessun build).
- `assets/`: logo, mascotte e illustrazioni estratti dalla presentazione del brand.

Per vederla basta aprire `index.html` nel browser o pubblicarla su un qualsiasi hosting statico (Netlify, Vercel, GitHub Pages).

## Lingue

Arabo (layout da destra a sinistra), inglese, francese. I testi sono nell'oggetto `T` e nei dati in fondo alla pagina (`STAMPS`, `CMP`, `ROAD`, `WHY`, `PLANS`, `FEATS`, `ADDONS`, `FAQ`).
La lingua iniziale segue questo ordine: `?lang=`, poi la scelta salvata dal visitatore, poi il paese, poi la lingua del browser.

## Link per le campagne

Un link diverso per ogni paese cambia la lingua iniziale e la carta d'imbarco nell'hero (aeroporto di partenza e durata del volo):

| Paese | Link |
|---|---|
| Algeria | `?c=dz` (oppure `?c=dz&lang=fr`) |
| Kuwait | `?c=kw` |
| Israele | `?c=il` |

Sulla pagina non compaiono bandiere né il nome "Israele" accanto a quello degli altri paesi: il pubblico algerino e kuwaitiano potrebbe reagire male.

## Contatti

Tutti i pulsanti aprono WhatsApp (+39 327 599 0381) con un messaggio già scritto nella lingua del visitatore. Il modulo non ha un backend: compone il messaggio e apre WhatsApp.

## Da completare prima di pubblicare

- Testimonianze reali: ora ci sono dei segnaposto, marcati in rosso.
- Prezzi degli add-on: ora c'è scritto "prezzo su richiesta".
- Il banner giallo "BOZZA" in cima va tolto prima di andare online.
- Link Instagram e TikTok, privacy policy e cookie policy.
- Ricontrollare i dati su rette universitarie e borse di studio per l'anno accademico in corso.
