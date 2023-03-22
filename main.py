import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("FactoryFlow Productie Dashboard")
st.write("""
Welkom bij het FactoryFlow Productie Dashboard. Ons eenvoudige maar professionele ontwerp helpt u om inzicht te krijgen in de belangrijkste KPI's van uw productieproces. 
Met deze tool kunt u gemakkelijk de efficiëntie van uw fabriek analyseren, bottlenecks identificeren en uw processen optimaliseren. FactoryFlow richt zich op het creëren 
van dashboards voor productiebedrijven. De markt voor deze dashboards is de afgelopen jaren sterk gegroeid, omdat bedrijven zoeken naar oplossingen om hun productieprocessen efficiënter 
en effectiever te maken. Concurrenten in deze markt bieden doorgaans vergelijkbare oplossingen aan, zoals realtime monitoring, voorspellende analyses en geïntegreerde communicatietools. 
Enkele bekende spelers in deze markt zijn Siemens, GE Digital en ABB. \t

FactoryFlow onderscheidt zich van de concurrentie door zich te concentreren op het bieden van gebruiksvriendelijke, op maat gemaakte dashboards die eenvoudig te implementeren zijn.
Dit maakt het gemakkelijker voor productiebedrijven om hun processen snel te optimaliseren en direct resultaten te zien. \t

Laten we samen de productiviteit verhogen!
""")

bg_color = st.get_option("theme.backgroundColor")
grid_color = "#ABB8C3"

# Eerste grafiek
st.header("Quick Stats")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Productie volume")
    st.write("1234")
    
with col2:
    st.subheader("Aantal actieve machines")
    st.write("18")

col3, col4 = st.columns(2)

with col3:
    st.subheader("Openstaande bestellingen")
    st.write("150")

with col4:
    st.subheader("Totale omzet")
    st.write("€200,000")

# Grafieken onder elkaar
st.header("Grafieken")

# Tweede grafiek: Oorzaak uitvaltijd (Piechart)
st.header("Oorzaak uitvaltijd")
oorzaken = ["Kapotte machine", "Missende onderdelen", "Onderhoud", "Onbekende storing"]
percentages = [30, 20, 40, 10]

plt.figure(figsize=(7, 4))
sns.set_palette("pastel")
plt.pie(percentages, autopct="%1.1f%%", startangle=90)
plt.legend(oorzaken, title="Oorzaken", loc="best")
plt.axis("equal")

plt.gca().set_facecolor(bg_color)
plt.gca().set_axis_off()

st.pyplot(plt.gcf())

# Derde grafiek: Top 5 verkochte producten
st.subheader("Top 5 verkochte producten")
product_data = pd.DataFrame({
    "Product": ["Product A", "Product B", "Product C", "Product D", "Product E"],
    "Prijs": [100, 200, 150, 250, 300],
    "Aantal verkocht": [50, 30, 20, 10, 5],
    "Omzet": [5000, 6000, 3000, 2500, 1500]
 })

# Verberg indexkolom bij het weergeven van het DataFrame
st.write(product_data.to_html(index=False, border=0, classes=["table", "table-striped"]), unsafe_allow_html=True)


# Vierde grafiek: Teruggestuurde producten (Stacked bar graph)
st.header("Teruggestuurde producten")
terugstuur_oorzaken = ["Kapot", "Anders dan verwacht", "Geen reden"]
terugstuur_data = pd.DataFrame({
    "Product": ["Product A", "Product B", "Product C", "Product D", "Product E"],
    "Kapot": [10, 15, 20, 12, 8],
    "Anders dan verwacht": [5, 8, 10, 4, 2],
    "Geen reden": [7, 10, 15, 8, 5]
 })

fig, ax = plt.subplots(figsize=(7, 4))
sns.set_palette("deep")
terugstuur_data.set_index("Product")[terugstuur_oorzaken].plot(kind="bar", stacked=True, ax=ax)
ax.set_ylabel("Aantal teruggestuurde producten")
ax.set_title("Teruggestuurde producten per oorzaak")

bg_color = "white"
ax.set_facecolor(bg_color)
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["bottom"].set_color(grid_color)
plt.gca().spines["left"].set_color(grid_color)

st.pyplot(fig)

st.subheader("Vraag een demo aan!")
st.write("""
Waarom FactoryFlow kiezen? FactoryFlow is dé keuze voor productiebedrijven die hun processen willen verbeteren. Onze intuïtieve en op maat gemaakte dashboards stellen u 
in staat om snel inzicht te krijgen in uw productiegegevens en weloverwogen beslissingen te nemen. In tegenstelling tot de concurrentie biedt FactoryFlow een gepersonaliseerde 
aanpak, waardoor u precies krijgt wat u nodig heeft zonder overbodige extra's. Bovendien is ons team van deskundige ingenieurs altijd beschikbaar om u te ondersteunen bij het 
implementeren en optimaliseren van uw dashboard, zodat u zich kunt concentreren op het runnen van uw bedrijf. \t

Met een eenvoudig maar professioneel ontwerp helpt FactoryFlow u om tijd en middelen te besparen en uw klanten sneller en efficiënter van dienst te zijn. We nodigen u uit om een demo te proberen en zelf te ervaren hoe ons dashboard uw bedrijf kan transformeren.

Klik hieronder om een demo aan te vragen en ontdek hoe FactoryFlow uw bedrijf naar een hoger niveau kan tillen!
""")

if st.button("Probeer Demo"):
    st.success("Bedankt voor uw interesse! Ons team neemt spoedig contact met u op.")
