from pandas import pd
from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import Autor

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--arquivo", default="population/livros.csv")
        parser.add_argument("--truncate", default="store_true")
        parser.add_argument("--update", default="store_true")
    
    @transaction.atomic
    def handle(self, *a, **o):
        df = pd.read_csv(o["arquivo"], encoding="utf-8-sig")
        df.columns = [c.strip().lower().lstrip("\ufeff") for c in df.columns]

        if o['truncate']: Autor.objects.all().delete()

        # Dataframes dos campos de Livros do csv
        df["titulo"] = df["titulo"].astype(str).str.strip()
        df["subtitulo"] = df["subtitulo"].astype(str).str.strip()
        df["descricao"] = df["descricao"].astype(str).str.strip()
        df["idioma"] = df["idioma"].astype(str).str.strip()
        df["ano_publicacao"] = df["ano_publicacao"].astype(int)
        df["paginas"] = df["paginas"].astype(int)
        df["preco"] = df["preco"].astype(float)
        df["estoque"] = df["estoque"].astype(int)
        df["desconto"] = df["desconto"].astype(float)
        df["disponivel"] = df["disponivel"].astype(bool)
        df["dimensoes"] = df["dimensoes"].astype(str).str.strip()
        df["peso"] = df["peso"].astype(float)
        df["autor"] = df["autor"].astype(str).str.strip()

        # Dataframes dos campos com chave estrangeira
        
        