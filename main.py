#########################
# Importa Librerie
#########################

import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

#########################
# Titolo Pagina
#########################

image = Image.open('dna-logo.jpg')

st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

Questa applicazione conta la composizione nucleotidica della query DNA!

***
""")

#########################
# Input Text Box
#########################

st.header('Inserisci la sequenza del DNA')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Input di sequenza", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]  # Salta il nome della sequenza (prima riga)
sequence = ''.join(sequence)

## Stampa la sequenza di DNA di input
st.header('INPUT (DNA Query)')
sequence

## Contatore dei nucleotidi del DNA
st.header('OUTPUT (DNA Nucleotide Count)')

### 1. Dizionario di stampa
st.subheader('1. Dizionario di stampa')


def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])

    return d


X = DNA_nucleotide_count(sequence)

X

### 2. Testo di stampa
st.subheader('2. Testo di stampa')
st.write('Ci sono ' + str(X['A']) + ' di adenina (A)')
st.write('Ci sono ' + str(X['T']) + ' di timina (T)')
st.write('Ci sono ' + str(X['G']) + ' di guanina (G)')
st.write('Ci sono ' + str(X['C']) + ' di citosina (C)')

### 3. Mostra DataFrame
st.subheader('3. Mostra DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'nucleotide'})
st.write(df)

### 4. Visualizza grafico a barre utilizzando Altair
st.subheader('4. Mostra un grafico a barre')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)
)
st.write(p)