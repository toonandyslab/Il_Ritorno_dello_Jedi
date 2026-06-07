import random
import textwrap

# ============================================================
# STAR WARS - IL RITORNO DELLO JEDI
# Mini avventura testuale
# ============================================================

MAX_HEARTS = 3


# ------------------------------------------------------------
# UTILITÀ
# ------------------------------------------------------------

def separatore():
    print("\n" + "=" * 70 + "\n")


def pausa():
    input("\n[INVIO per continuare]")


def testo(t):
    print(textwrap.fill(t, width=72))


def mostra_cuori(cuori):
    print(f"\nVite: {'❤️' * cuori}")


def tiro_dado():
    while True:
        try:
            valore = int(input("\nInserisci il risultato del dado (1-6): "))
            if 1 <= valore <= 6:
                return valore
        except ValueError:
            pass

        print("Valore non valido.")


def scelta(opzioni):
    print()

    for i, opzione in enumerate(opzioni, start=1):
        print(f"{i}) {opzione}")

    while True:
        try:
            s = int(input("\nScelta: "))
            if 1 <= s <= len(opzioni):
                return s
        except ValueError:
            pass

        print("Scelta non valida.")


def perdi_cuore(stato, motivo):
    stato["cuori"] -= 1

    print("\n💥 CONSEGUENZA GRAVE")
    testo(motivo)

    if stato["cuori"] > 0:
        print(f"\nTi restano {stato['cuori']} cuori.")
        pausa()
        return True

    separatore()
    print("GAME OVER")
    testo(
        "Le tue ferite sono troppo gravi. "
        "La tua avventura termina qui."
    )
    return False


# ------------------------------------------------------------
# LUKE
# ------------------------------------------------------------

def luke_jabba(stato):
    separatore()

    testo(
        "Il palazzo di Jabba è immerso nel buio. "
        "Musicisti alieni, guardie armate e mercenari "
        "osservano ogni tuo movimento."
    )

    s = scelta([
        "Lascia che sia il silenzio a parlare.",
        "Offri una proposta insolita a Jabba.",
        "Studia la sala prima di prendere posizione."
    ])

    dado = tiro_dado()

    if s == 1:
        if dado <= 2:
            return perdi_cuore(
                stato,
                "Jabba interpreta il tuo silenzio come un insulto. "
                "Le guardie ti travolgono."
            )
        elif dado <= 4:
            testo("Jabba non reagisce. L'incontro resta in stallo.")
        else:
            testo(
                "La tua calma impressiona molti presenti. "
                "Ottieni fiducia nella Forza."
            )
            stato["forza"] += 1

    elif s == 2:
        if dado <= 2:
            testo(
                "La proposta attira l'attenzione di Jabba, "
                "ma ti espone a sospetti."
            )
        elif dado <= 4:
            testo(
                "Alcuni mercenari discutono fra loro. "
                "Scopri dettagli utili."
            )
            stato["forza"] += 1
        else:
            testo(
                "Jabba ride divertito. Le sue guardie "
                "abbassano leggermente la guardia."
            )
            stato["forza"] += 2

    else:
        if dado <= 2:
            testo(
                "Qualcuno nota che stai osservando troppo attentamente."
            )
        elif dado <= 4:
            testo(
                "Individui alcune uscite secondarie."
            )
            stato["forza"] += 1
        else:
            testo(
                "Scopri punti deboli nelle difese del palazzo."
            )
            stato["forza"] += 2

    pausa()
    return True


def luke_sarlacc(stato):
    separatore()

    testo(
        "La situazione precipita. Sei vicino alla fossa del "
        "Sarlacc mentre gli uomini di Jabba si preparano "
        "a eliminarti."
    )

    s = scelta([
        "Attendi il momento meno prevedibile.",
        "Concentrati sui nemici più pericolosi.",
        "Affidati agli alleati senza dare ordini."
    ])

    dado = tiro_dado() + stato["forza"]

    if s == 1:
        if dado <= 3:
            return perdi_cuore(
                stato,
                "Esiti troppo a lungo e vieni colpito."
            )
        elif dado <= 5:
            testo("Riesci a reagire appena in tempo.")
        else:
            testo(
                "La tua azione sorprende tutti. "
                "Sfuggi al caos con eleganza."
            )
            stato["forza"] += 1

    elif s == 2:
        if dado <= 3:
            testo(
                "Un avversario secondario ti coglie di sorpresa."
            )
        elif dado <= 5:
            testo("La situazione si riequilibra.")
        else:
            testo(
                "Elimini rapidamente la minaccia principale."
            )
            stato["forza"] += 1

    else:
        if dado <= 3:
            return perdi_cuore(
                stato,
                "La coordinazione fallisce e vieni ferito gravemente."
            )
        elif dado <= 5:
            testo("Gli alleati riescono a sostenerti.")
        else:
            testo(
                "La fiducia reciproca porta a una fuga perfetta."
            )
            stato["forza"] += 2

    pausa()
    return True


def luke_yoda(stato):
    separatore()

    testo(
        "Su Dagobah ritrovi il vecchio Maestro Yoda."
    )

    s = scelta([
        "Chiedi del futuro.",
        "Chiedi dell'Imperatore.",
        "Chiedi di tuo padre."
    ])

    dado = tiro_dado()

    if s == 1:
        testo(
            "Yoda ricorda che il futuro è sempre in movimento."
        )
        stato["forza"] += 1

    elif s == 2:
        if dado >= 4:
            testo(
                "Comprendi meglio il pericolo rappresentato "
                "da Palpatine."
            )
            stato["forza"] += 2
        else:
            testo(
                "Le risposte restano enigmatiche."
            )

    else:
        if dado >= 5:
            testo(
                "Le parole di Yoda rafforzano la tua determinazione."
            )
            stato["forza"] += 2
        else:
            testo(
                "Molti dubbi restano irrisolti."
            )

    if stato["cuori"] < MAX_HEARTS and dado == 6:
        stato["cuori"] += 1
        print("\n❤️ Recuperi un cuore.")

    pausa()
    return True


def luke_vader(stato):
    separatore()

    testo(
        "A bordo della Morte Nera affronti Darth Vader."
    )

    successi = 0

    for turno in range(2):
        print(f"\nConfronto {turno + 1}/2")

        s = scelta([
            "Osserva prima di colpire.",
            "Metti pressione all'avversario.",
            "Cerca una reazione emotiva."
        ])

        dado = tiro_dado() + stato["forza"]

        if s == 1:
            if dado >= 5:
                successi += 1
                testo("Trovi una breccia nella difesa di Vader.")
            else:
                testo("Vader mantiene il controllo.")

        elif s == 2:
            if dado >= 6:
                successi += 1
                testo("L'iniziativa è tua.")
            elif dado <= 2:
                if not perdi_cuore(
                    stato,
                    "Vader contrattacca con violenza."
                ):
                    return False

        else:
            if dado >= 5:
                successi += 1
                testo(
                    "Per un attimo percepisci il conflitto "
                    "interiore di Vader."
                )
            else:
                testo("Le sue emozioni restano nascoste.")

    stato["vader_successi"] = successi
    pausa()
    return True


def finale_luke(stato):
    separatore()

    testo(
        "Davanti all'Imperatore si decide il destino "
        "della galassia."
    )

    s = scelta([
        "Lascia che siano le azioni a parlare.",
        "Sfida direttamente Palpatine.",
        "Rivolgiti a ciò che resta di Anakin."
    ])

    dado = tiro_dado() + stato["forza"]

    separatore()

    if s == 3 and stato["vader_successi"] >= 1:
        print("⭐ FINALE CANONICO")

        testo(
            "Le tue parole raggiungono Vader. "
            "Anakin Skywalker riemerge e sacrifica la propria "
            "vita per distruggere Palpatine."
        )

        print("\nL'Impero subisce un colpo devastante.")
        print("La Ribellione trionfa.")

    elif dado >= 8:
        print("⭐ FINALE LUMINOSO")

        testo(
            "La tua fede nella Forza ispira chi ti circonda. "
            "Le ultime difese dell'Impero crollano più rapidamente "
            "del previsto."
        )

    elif dado >= 5:
        print("⭐ FINALE INCERTO")

        testo(
            "Sopravvivi allo scontro. La guerra continua, "
            "ma la speranza resta viva."
        )

    else:
        print("⭐ FINALE OSCURO")

        testo(
            "I tuoi dubbi prevalgono. L'Imperatore ottiene "
            "un vantaggio decisivo."
        )


# ------------------------------------------------------------
# HAN
# ------------------------------------------------------------

def han_risveglio(stato):
    separatore()

    testo(
        "La tua vista è ancora annebbiata dopo essere stato "
        "liberato dalla carbonite."
    )

    s = scelta([
        "Fidati dell'istinto.",
        "Lascia decidere agli altri.",
        "Concentrati su piccoli dettagli."
    ])

    dado = tiro_dado()

    if s == 1:
        if dado <= 2:
            return perdi_cuore(
                stato,
                "Ti muovi nella direzione sbagliata "
                "e vieni ferito."
            )
        else:
            testo("Ritrovi rapidamente lucidità.")

    elif s == 2:
        testo("I tuoi amici ti guidano fuori dal pericolo.")

    else:
        if dado >= 5:
            testo(
                "Noti un'opportunità che altri ignorano."
            )
            stato["leadership"] += 1
        else:
            testo("Non trovi nulla di utile.")

    pausa()
    return True


def han_spazio(stato):
    separatore()

    testo(
        "La flotta ribelle si prepara all'operazione "
        "contro la seconda Morte Nera."
    )

    s = scelta([
        "Osserva i movimenti nemici.",
        "Prendi una decisione immediata.",
        "Coordina gli altri piloti."
    ])

    dado = tiro_dado()

    if s == 1:
        if dado >= 5:
            stato["leadership"] += 2
            testo("Individui un'importante anomalia.")
        else:
            testo("Non emerge nulla di significativo.")

    elif s == 2:
        if dado <= 2:
            return perdi_cuore(
                stato,
                "La situazione degenera rapidamente."
            )
        else:
            testo("La scelta si rivela adeguata.")

    else:
        if dado >= 4:
            stato["leadership"] += 1
            testo(
                "Le comunicazioni migliorano "
                "l'efficienza della flotta."
            )
        else:
            testo("Le informazioni sono confuse.")

    pausa()
    return True


def han_endor(stato):
    separatore()

    testo(
        "La squadra sbarca sulla luna boscosa di Endor."
    )

    s = scelta([
        "Seguire il percorso più evidente.",
        "Muoversi senza una meta precisa.",
        "Procedere con frequenti soste."
    ])

    dado = tiro_dado()

    if s == 1:
        if dado <= 2:
            return perdi_cuore(
                stato,
                "Una pattuglia imperiale ti intercetta."
            )
        else:
            testo("Attraversi la foresta senza problemi.")

    elif s == 2:
        if dado >= 5:
            testo(
                "Incontri gli Ewok in circostanze favorevoli."
            )
            stato["ewok"] = True
        else:
            testo("Ti perdi per un po' nella foresta.")

    else:
        if dado >= 4:
            stato["leadership"] += 1
            testo("La prudenza evita problemi.")
        else:
            testo("Il tempo scorre inutilmente.")

    pausa()
    return True


def han_ewok(stato):
    separatore()

    testo(
        "Gli Ewok osservano il gruppo con curiosità."
    )

    s = scelta([
        "Parla della missione.",
        "Mostra rispetto per le loro usanze.",
        "Lascia parlare C-3PO."
    ])

    dado = tiro_dado()

    if s == 1:
        if dado >= 5:
            stato["ewok"] = True
            testo("Gli Ewok sembrano convinti.")
        else:
            testo("Non comprendono bene le tue intenzioni.")

    elif s == 2:
        if dado >= 4:
            stato["ewok"] = True
            testo("Si crea fiducia reciproca.")
        else:
            testo("La situazione resta incerta.")

    else:
        if dado >= 3:
            stato["ewok"] = True
            stato["leadership"] += 1
            testo(
                "C-3PO impressiona profondamente gli Ewok."
            )
        else:
            testo("Il risultato è meno spettacolare del previsto.")

    pausa()
    return True


def han_bunker(stato):
    separatore()

    testo(
        "Il generatore dello scudo è protetto da truppe "
        "imperiali."
    )

    s = scelta([
        "Creare una distrazione.",
        "Attendere un'occasione favorevole.",
        "Tentare un ingresso rapido."
    ])

    dado = tiro_dado() + stato["leadership"]

    if s == 1:
        if dado >= 5:
            testo("Le guardie abboccano.")
            stato["bunker"] = True
        else:
            testo("La distrazione ha effetti limitati.")

    elif s == 2:
        if dado >= 4:
            testo("Si apre una finestra di opportunità.")
            stato["bunker"] = True
        else:
            testo("L'attesa non produce risultati.")

    else:
        if dado <= 2:
            return perdi_cuore(
                stato,
                "L'assalto viene respinto."
            )
        elif dado >= 5:
            stato["bunker"] = True
            testo("L'ingresso riesce perfettamente.")
        else:
            testo("Entrate con difficoltà.")

    pausa()
    return True


def finale_han(stato):
    separatore()

    testo(
        "Tutto dipende dagli ultimi istanti "
        "della missione."
    )

    s = scelta([
        "Proteggi la squadra.",
        "Concentrati sull'obiettivo.",
        "Affidati all'improvvisazione."
    ])

    dado = tiro_dado() + stato["leadership"]

    separatore()

    if stato["ewok"] and dado >= 6:
        print("⭐ EROE DI ENDOR")

        testo(
            "Gli Ewok e i ribelli combattono insieme. "
            "Lo scudo cade e la vittoria è completa."
        )

    elif dado >= 5:
        print("⭐ VITTORIA")

        testo(
            "Il generatore viene distrutto. "
            "La Morte Nera resta vulnerabile."
        )

    elif dado >= 3:
        print("⭐ VITTORIA COSTOSA")

        testo(
            "La missione riesce, ma il prezzo pagato "
            "è elevato."
        )

    else:
        print("⭐ MISSIONE FALLITA")

        testo(
            "Lo scudo resta attivo. "
            "La battaglia prende una piega drammatica."
        )


# ------------------------------------------------------------
# CAMPAGNE
# ------------------------------------------------------------

def avventura_luke():
    stato = {
        "cuori": 3,
        "forza": 0,
        "vader_successi": 0
    }

    if not luke_jabba(stato):
        return

    if not luke_sarlacc(stato):
        return

    if not luke_yoda(stato):
        return

    if not luke_vader(stato):
        return

    finale_luke(stato)


def avventura_han():
    stato = {
        "cuori": 3,
        "leadership": 0,
        "ewok": False,
        "bunker": False
    }

    if not han_risveglio(stato):
        return

    if not han_spazio(stato):
        return

    if not han_endor(stato):
        return

    if not han_ewok(stato):
        return

    if not han_bunker(stato):
        return

    finale_han(stato)


# ------------------------------------------------------------
# MAIN
# ------------------------------------------------------------

def main():
    separatore()

    print("STAR WARS")
    print("EPISODIO VI")
    print("IL RITORNO DELLO JEDI")

    separatore()

    testo(
        "Scegli il tuo eroe e affronta una versione "
        "interattiva degli eventi del film."
    )

    eroe = scelta([
        "Luke Skywalker",
        "Han Solo"
    ])

    if eroe == 1:
        avventura_luke()
    else:
        avventura_han()

    separatore()
    print("Grazie per aver giocato.")


if __name__ == "__main__":
    main()
