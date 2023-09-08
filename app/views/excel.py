import pandas as pd
from app.models import Periode, Theme, Indicateur, Region, Sous_Region, Fiche

def import_data_from_excel(file_path):
    data = pd.read_excel(file_path)

    for _, row in data.iterrows():
        theme, _ = Theme.objects.get_or_create(name=row['THEMES :'])
        indicateur, _ = Indicateur.objects.get_or_create(name=row['SOUS-THEMES/INDICATEURS :'])
        region, _ = Region.objects.get_or_create(name=row['REGION :'])
        sous_region, _ = Sous_Region.objects.get_or_create(name=row['SOUS-REGION (DISTRICT)'])
        periode, _ = Periode.objects.get_or_create(year=row['PERIODE/ANNEE :'])
        
        fiche = Fiche(
            theme=theme,
            indicateur=indicateur,
            region=region,
            sous_region=sous_region,
            periode=periode,
            age=row["TRANCHE DAGE :"],
            sexe=row["Sexe"],
            nombre=row["DONNEES"],
            source=row["SOURCE :"]
        )
        fiche.save()

   