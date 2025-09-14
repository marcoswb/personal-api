from flask import jsonify, request
from flask_restful import Resource
from rapidfuzz import process
class Mateus(Resource):

    categorias = {
        "Exames de sangue": [
            {"nome": "hemograma", "tempo": 10},
            {"nome": "colesterol", "tempo": 10},
            {"nome": "glicemia", "tempo": 5},
            {"nome": "triglicerídeos", "tempo": 10},
            {"nome": "plaquetas", "tempo": 10},
            {"nome": "hemoglobina glicada", "tempo": 15}
        ],
        "Exames de imagem": [
            {"nome": "raio-x", "tempo": 15},
            {"nome": "ressonância magnética", "tempo": 60},
            {"nome": "tomografia", "tempo": 30},
            {"nome": "ultrassonografia", "tempo": 25},
            {"nome": "mamografia", "tempo": 20},
            {"nome": "densitometria óssea", "tempo": 30}
        ],
        "Exames cardiológicos": [
            {"nome": "eletrocardiograma", "tempo": 10},
            {"nome": "ecocardiograma", "tempo": 40},
            {"nome": "holter", "tempo": 1440},
            {"nome": "teste ergométrico", "tempo": 35},
            {"nome": "MAPA", "tempo": 1440}
        ],
        "Exames de urina": [
            {"nome": "urina tipo i", "tempo": 5},
            {"nome": "urocultura", "tempo": 5},
            {"nome": "exame de urina", "tempo": 5}
        ],
        "Exames hormonais": [
            {"nome": "tsh", "tempo": 10},
            {"nome": "t4 livre", "tempo": 10},
            {"nome": "testosterona", "tempo": 10},
            {"nome": "estradiol", "tempo": 10},
            {"nome": "cortisol", "tempo": 10},
            {"nome": "progesterona", "tempo": 10}
        ],
        "Exames infecciosos": [
            {"nome": "hiv", "tempo": 15},
            {"nome": "hepatite b", "tempo": 15},
            {"nome": "hepatite c", "tempo": 15},
            {"nome": "sífilis", "tempo": 15}
        ],
        "Exames respiratórios": [
            {"nome": "espirometria", "tempo": 20},
            {"nome": "gasometria arterial", "tempo": 10},
            {"nome": "teste de função pulmonar", "tempo": 25}
        ]
    }

    LIMITAR_CONFIANCA = 100

    def get(self):
        nome = request.args.get("nome")  # pega ?nome=valor

        nome = nome.lower().strip()
        melhor_cat = "Categoria não encontrada"
        melhor_exame = None
        melhor_score = 0

        for cat, exames in self.categorias.items():
            nomes_exames = [e["nome"] for e in exames]
            match, score, _ = process.extractOne(nome, nomes_exames)
            if score > melhor_score:
                melhor_score = score
                melhor_cat = cat
                melhor_exame = next(e for e in exames if e["nome"] == match)

        if melhor_score < self.LIMITAR_CONFIANCA:
            return jsonify({
                "exame_digitado": nome,
                "categoria_sugerida": "Categoria não encontrada",
                "confianca": f"{melhor_score:.2f}%",
                "tempo_estimado": None
            })

        return jsonify({
            "exame_digitado": nome,
            "categoria_sugerida": melhor_cat,
            "exame_encontrado": melhor_exame["nome"],
            "confianca": f"{melhor_score:.2f}%",
            "tempo_estimado": melhor_exame["tempo"]
        })
