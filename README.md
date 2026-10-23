# Espresso Study: landing page (bozza v2)

Landing page statica, mobile first, per gli studenti arabofoni che vogliono studiare in Italia.
Mercati prioritari: Algeria, Kuwait, studenti arabi in Israele.

## Struttura

- `index.html`: tutta la pagina in un unico file (HTML, CSS e JS inline, nessun build).
- `assets/peeps/`: personaggi illustrati (Open Peeps, licenza CC0), a figura intera e a mezzo busto. I mezzi busti hanno due versioni, preoccupata (`-worry`) e sorridente (`-happy`).
- `assets/italy/`: monumenti italiani disegnati in SVG e `skyline.svg`, il panorama animato dell'hero.
- `tools/`: script per rigenerare personaggi e monumenti (istruzioni in testa a ogni file).

Per vederla basta aprire `index.html` nel browser o pubblicarla su un hosting statico.

## Sezioni, in ordine

1. **Hero animato**: panorama italiano che scorre, studenti che camminano, notifiche ("Visto approvato ✅").
2. **"Ne parlano"**: nastro che scorre con i nomi delle testate.
3. **Quiz "Posso studiare in Italia?"**: 3 domande e un risultato personalizzato che apre WhatsApp con le risposte.
4. **Le paure** di studenti e genitori, con la risposta di Espresso Study. Il personaggio passa da preoccupato a sorridente.
5. **Cosa ti aspetta in Italia**: cartoline illustrate, dati chiave e confronto delle rette.
6. **Confronto** tra fare da soli, solo con l'università e con Espresso Study.
7. **Percorso** in 4 tappe.
8. **Rassegna stampa**: Gaza → Ancona e premio eCapital 2025, con i link agli articoli.
9. **Partner**: UNIVPM, Inlingua, eCapital, partner locali.
10. **Prezzi e add-on**, testimonianze, domande frequenti, modulo di contatto.

## Lingue

Arabo (layout da destra a sinistra), inglese, francese. I testi sono nell'oggetto `T` e negli array di dati dentro lo `<script>`.
Lingua iniziale: `?lang=`, poi la scelta salvata dal visitatore, poi il paese, poi la lingua del browser.

## Link per le campagne

| Paese | Link | Effetto |
|---|---|---|
| Algeria | `?c=dz` | arabo, partner locale algerino |
| Kuwait | `?c=kw` | arabo, assistenza 100% online |
| Israele | `?c=il` | arabo, partner locali in Israele |

Senza parametro compaiono tutti i partner locali, ma senza indicare il paese di ciascuno.

## Loghi

Testate e partner sono resi come scritte stilizzate in un solo colore (classi `.wm-*`), non con i loghi ufficiali.
Per usare quelli ufficiali, mettete i file in `assets/logos/` e sostituite l'HTML negli oggetti `OUTLET` e `PARTNERS`.

## Da completare prima di pubblicare

- Loghi ufficiali di testate, UNIVPM, Inlingua, eCapital.
- Testimonianze reali: ora ci sono dei segnaposto, marcati in rosso.
- Prezzi degli add-on: ora c'è scritto "prezzo su richiesta".
- Il banner giallo "BOZZA" in cima va tolto.
- Verificare che ogni articolo linkato citi Espresso Study.
- Link Instagram e TikTok, privacy policy e cookie policy.
