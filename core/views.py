from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

class IndexView(TemplateView):
    template_name = 'index.html'
    
class DataJSONView(BaseLineChartView):
    
    def get_labels(self):
        """ Os labels ficam no eixo x do gráfico, e na nossa aplicação teremos 12 labels . São as colunas."""
        labels = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ]
        return labels
    
    def get_providers(self):
        """Retorna os nomes dos datasets. São as linhas"""
        datasets = [
            "Software Engineering",
            "Big Data & Analytics",
            "Programming with Python",
            "Full Stack with Django",
            "Database SQL & NoSQL",
            "Machine Learning with Python"
        ]
        return datasets
    
    def get_data(self):
        """"
        Retorna os datasets (temos 6 nesse caso) para plotar o gráfico.
        Cada linha representa um dataset.
        Cada coluna representa um label.
        
        A quantidade de dados precisa ser igual aos datasets/labels
        """
        
        dados = []
        for linha in range(6):
            for coluna in range(12):
                dado = [
                    randint(1,200), #January
                    randint(1,200), #February
                    randint(1,200), #March
                    randint(1,200), #April
                    randint(1,200), #May
                    randint(1,200), #June
                    randint(1,200), #July
                    randint(1,200), #August
                    randint(1,200), #September
                    randint(1,200), #October
                    randint(1,200), #November
                    randint(1,200)  #December
                ]
            dados.append(dado)
        return dados