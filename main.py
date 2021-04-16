############################
##### Importa Librerie #####
############################

import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image
import time
import random

##########################
######## Funzioni ########
##########################

Nucleotidi = ['A', 'C', 'G', 'T']


def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotidi:
            return False
    return tmpseq


#########################
## Composizione Pagina ##
#########################

image = Image.open('dna-logo.jpg')

st.image(image, use_column_width=True)

#####################

st.write('''
# Alla Ricerca dei Nucleotidi (By *II O*)

Questa applicazione conta la composizione nucleotidica di una composizione di DNA!

**Curiosità**: Questa applicazione web, è stata sviluppata in Python, utilizzando le seguenti librerie:
- Pandas
- Streamlit (Libreria principale per la composizione web)
- Altair

***
''')

##########################
##### Input Text Box #####
##########################

st.sidebar.header('Inserisci la sequenza del DNA')
st.sidebar.write(
    'Attenzione: Per inserire più sequenze contemporaneamente, andare al rigo di sotto!')

sequence_input = "> DNA Query\n" + ''.join([random.choice(Nucleotidi)
                                            for nuc in range(50)]) + "\n" + ''.join([random.choice(Nucleotidi)
                                                                                     for nuc in range(50)])

sequence = st.sidebar.text_area(
    "Input di sequenza:", sequence_input, height=250)
st.sidebar.write(
    '***Suggerimento:*** *Rimani le stringhe di DNA di default per eseguire l\'esempio senza avere problemi!*')
sequence = sequence.splitlines()
sequence = sequence[1:]
sequence = ', '.join(sequence)

if st.sidebar.button('Esegui Analisi!'):
    if not sequence:
        st.sidebar.warning('Per piacere inserisci una o più sequenze di DNA!')
        st.sidebar.stop()
    else:
        my_bar = st.progress(0)
        barset = 0

        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1)
            barset = 100

    if barset == 100:
        st.write('***')
        # Stampa la sequenza di DNA di input
        st.header('INPUT (DNA Query)')
        st.write(sequence)

        # Contatore dei nucleotidi del DNA
        st.header('OUTPUT (DNA Nucleotide Count)')

        # 1. Calcolo Valori
        st.subheader('1. Valori')


        def DNA_nucleotide_count(seq):
            d = dict([
                ('A', seq.count('A')),
                ('T', seq.count('T')),
                ('G', seq.count('G')),
                ('C', seq.count('C'))
            ])

            return d


        X = DNA_nucleotide_count(sequence)

        st.write(X)

        test = X['A'] + X['T'] + X['G'] + X['C']
        calc1 = X['A'] * 100 / test
        calc2 = X['T'] * 100 / test
        calc3 = X['G'] * 100 / test
        calc4 = X['C'] * 100 / test

        st.write('---')
        st.write('Ci sono ' + str(X['A']) + ' (' + str(calc1) + '%)  nucleotidi di adenina (A)')
        st.write('Ci sono ' + str(X['T']) + ' (' + str(calc2) + '%) nucleotidi di timina (T)')
        st.write('Ci sono ' + str(X['G']) + ' (' + str(calc3) + '%) nucleotidi di guanina (G)')
        st.write('Ci sono ' + str(X['C']) + ' (' + str(calc4) + '%) nucleotidi di citosina (C)')

        calcolo = X['A'] + X['T']
        if calcolo == calcolo:
            frase1 = "Il risultato è vero, quindi il paziente non riscontra alterazioni"
        else:
            frase1 = "Il risultato è falso, quindi il paziente riscontra alterazioni"

        calcolo2 = X['G'] + X['C']
        if calcolo2 == calcolo2:
            frase1 = "Il risultato è vero, quindi il paziente non riscontra alterazioni"
        else:
            frase1 = "Il risultato è falso, quindi il paziente riscontra alterazioni"

        calcolo3 = X['A']
        calcolo4 = X['T']
        if calcolo3 == calcolo4:
            frase1 = "Il risultato è vero, quindi il paziente non riscontra mutazioni"
        else:
            frase1 = "Il risultato è falso, quindi il paziente riscontra mutazioni"

        calcolo5 = X['G']
        calcolo6 = X['C']
        if calcolo5 == calcolo6:
            frase1 = "Il risultato è vero, quindi il paziente non riscontra mutazioni"
        else:
            frase1 = "Il risultato è falso, quindi il paziente riscontra mutazioni"

        st.write('**Verifica dei dati**')
        st.write('**A + T = A + T** || **' + str(X['A']) + ' + ' + str(X['T']) + ' = ' + str(X['A']) + ' + ' + str(X['T']) + '** (*' + frase1 + '*)')
        st.write('**G + C = G + C** || **' + str(X['G']) + ' + ' + str(X['C']) + ' = ' + str(X['G']) + ' + ' + str(X['C']) + '** (*' + frase1 + '*)')
        st.write('***')
        st.write('**A = T** || **' + str(X['A']) + ' = ' + str(X['T']) + '** (*' + frase1 + '*)')
        st.write('**G = C** || **' + str(X['G']) + ' = ' + str(X['C']) + '** (*' + frase1 + '*)')
        st.write('***')

        # 3. Tabella
        st.subheader('2. Tabella')
        df = pd.DataFrame.from_dict(X, orient='index')
        df = df.rename({0: 'count'}, axis='columns')
        df.reset_index(inplace=True)
        df = df.rename(columns={'index': 'nucleotidi'})
        st.write(df)

        # 4. Grafici
        st.subheader('3. Grafici')
        p = alt.Chart(df).mark_bar().encode(
            x='nucleotidi',
            y='count'
        )
        p = p.properties(
            width=alt.Step(80)
        )
        st.write(p)

        st.write('***')

#########################
######## NOZIONI STORICHE #######
#########################

st.sidebar.write('***')

st.sidebar.subheader('DNA Nella Storia...')

st.sidebar.markdown('''
Nonostante la sua scoperta risalga a ormai 65 anni, la celebre doppia elica del **DNA** custodisce ancora molti misteri. Sappiamo, per esempio, che ci sono particolari **simmetrie** all’interno dei singoli filamenti di DNA, ma molto resta da scoprire sulla loro **origine**.
Un po’ di storia… nel 1944 **[Avery](http://www.dnaftb.org/17/bio.html)** e colleghi avevano dimostrato che il portatore dei caratteri genetici era l'acido desossiribonucleico, ovvero il **[DNA](https://www.scienceforpassion.com/2010/06/il-dna-una-molecola-semplicemente.html)**. Qualche anno più tardi, nel 1952, questi risultati verranno confermati dall'esperimento di **[Alfred Day Hershey e Martha Chase](https://www.nobelprize.org/prizes/medicine/1969/hershey/biographical/)** che convinse definitivamente anche gli scienziati più scettici. Alla fine degli anni '40 un gruppo di ricercatori, guidati dal biochimico austriaco **[Erwin Chargaff](https://www.famousscientists.org/erwin-chargaff/)**, cercò di comprendere meglio le peculiarità del DNA. Quali caratteristiche chimiche permettevano a questa molecola di contenere le informazioni genetiche? 
Attraverso la cromatografia su carta (una tecnica di separazione delle sostanze) riuscì a comprendere che:
- La composizione in basi del DNA varia da una specie all'altra. 
- Molecole di DNA isolate da tessuti diversi della stessa specie hanno la stessa composizione in basi. 
- La composizione in basi del DNA di una certa specie non si modifica in base all'età, allo stato nutritivo o alle variazioni ambientali. 
- Inoltre, in tutte le molecole di DNA, indipendentemente dalla specie: Il numero di residui di A è uguale al numero di residui di T Il numero di residui di G è uguale al numero di residui di C 
- La somma dei residui purinici è uguale alla somma dei residui pirimidinici
''')

st.sidebar.write('***')

st.sidebar.subheader('Un passo avanti...')

st.sidebar.write('''
Un passo avanti è stato fatto  da  un gruppo di ricerca italo-australiano che coinvolge l’Università di Milano-Bicocca, l’Università di Sydney e l’Università di Bologna. Pubblicato su *Nature Scientific Reports*, lo [studio](https://www.nature.com/articles/s41598-018-34136-w) presenta per la prima volta un modello matematico in grado di spiegare la particolare ripartizione delle basi all’interno del DNA.
Un risultato che potrebbe aiutarci a far luce sui processi evolutivi della doppia elica e a spiegare le funzioni ad oggi ancora ignote di molte sue parti.
''')

st.sidebar.write('***')

st.sidebar.subheader('La nostra idea...')

st.sidebar.write('''
I bioinformatici stanno riscoprendo oggi le "wheels" letteralmente le “ruote” di Chargaff, Wyatt e altri biochimici. Ne consegue dalla seconda regola di parità di Chargaff (%A = %T, %G = %C per DNA a filamento singolo) che le simmetrie osservate per le due coppie di basi mononucleotidiche complementari, dovrebbero applicarsi anche alle otto coppie di basi dinucleotidiche complementari, in 32 paia di basi trinucleotidiche complementari, ecc... Di qui la nostra idea di realizzare un counting di nucleotidi in grado di dare velocemente il rapporto, la percentuale di basi puriniche o pirimidiniche. In campo diagnostico questo strumento potrebbe consentire l’identificazione di eventuali alterazioni o anomalie quantitative legate al numero di nucleotidi. In un momento cosi complesso, come quello che stiamo vivendo, l’immediata identificazione di variazioni nel numero di nucletidi potrebbe facilitare il lavoro diagnostico.
''')

st.sidebar.write('***')

#########################
######## Feedback #######
#########################

st.sidebar.subheader('Feedback')

valore = st.sidebar.select_slider(
    'Valuta il nostro servizio',
    options=['Pessimo', 'Mediocre', 'Buono', 'Ottimo'],
    value=('Ottimo'))

feedback = st.sidebar.text_input(
    'Inviaci un commento', 'Ottimo lavoro I.T.I. E. Barsanti!')

st.sidebar.write(
    '**Attenzione**: Il sistema di feedback/commenti non collega a nessun Servizio di terze parti, essendo che è solo un progetto di scuola.')

if st.sidebar.button('Invia Feedback!'):
    if not feedback:
        st.sidebar.warning(
            'Per piacere inserisci un commento prima di inviare un feedback!')
        s.sidebar.stop()
    else:
        st.sidebar.success(
            '**Feedback Inviato!** Grazie per la valutazione e per l\'attenzione al nostro servizio.')
        st.sidebar.write('**Voto:** ' + valore + '')
        st.sidebar.write('**Commento:** ' + feedback + '')
        st.sidebar.write('***')
else:
    st.sidebar.write('***')

st.write('''## I.T.I. E. Barsanti Project

**Coder**/**Ideatore**: Maritato Vincenzo
''')
