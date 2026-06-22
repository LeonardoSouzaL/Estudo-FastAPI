from typing import Optional

from pydantic import BaseModel, field_validator


class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @field_validator('titulo')
    @classmethod
    def validar_titulo(csl, value):
        # Validação 1
        palavra = value.split(' ')
        if len(palavra) < 3:
            raise ValueError('O título deve ter pelo menos 3 palavaras.')
        
        # Validação 2
        if  value.islower():
            raise ValueError('O título deve ser capitalizado.')
        return value

cursos = [
    Curso(id=1, titulo='Programação para Leigos', aulas=42, horas=56),
    Curso(id=2, titulo='Algoritmos e Lógica de Programação', aulas=52, horas=66),
]