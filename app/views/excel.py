import pandas as pd
from app.models import Periode, Theme, Indicateur, Region, Sous_Region, Fiche

def import_data_from_excel(file_path):
    data = pd.read_excel(file_path)

    for _, row in data.iterrows():
        theme, _ = Theme.objects.get_or_create(name=row['THEMES :'])
        indicateur, _ = Indicateur.objects.get_or_create(name=row['SOUS-THEMES/INDICATEURS :'])
        region, _ = Region.objects.get_or_create(name=row['REGION :'])
        sous_region = Sous_Region.objects.filter(name=row['SOUS-REGION (DISTRICT)']).first()  # Utiliser filter() au lieu de get()

        if sous_region is None:
            # Si aucune instance de Sous_Region n'existe, créez-en une nouvelle
            sous_region = Sous_Region.objects.create(name=row['SOUS-REGION (DISTRICT)'])

        periode, _ = Periode.objects.get_or_create(year=row['PERIODE/ANNEE :'])
        
        fiche = Fiche(
            theme=theme,
            indicateur=indicateur,
            region=region,
            sous_region=sous_region,
            periode=periode,
            age=row["TRANCHE DAGE :"],
            sexe=row["SEXE:"],
            nombre=row["DONNEES"],
            source=row["SOURCE :"]
        )
        fiche.save()

   