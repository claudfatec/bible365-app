import pytest
from core.engine import expandir_trecho

def test_expansao_intervalo_simples():
    # Teste para Gn 1-3 -> Deve retornar 3 capítulos
    resultado = expandir_trecho("Gn 1-3")
    assert resultado == ["Gn 1", "Gn 2", "Gn 3"]

def test_expansao_capitulo_unico():
    # Teste para livro de um capítulo só ou entrada única
    resultado = expandir_trecho("Ob 1")
    assert resultado == ["Ob 1"]

def test_expansao_livro_com_numero():
    # Teste para livros que começam com número
    resultado = expandir_trecho("1Sm 1-2")
    assert resultado == ["1Sm 1", "1Sm 2"]

def test_item_vazio_ou_invalido():
    # Garante que o sistema não quebra com strings inesperadas
    resultado = expandir_trecho("")
    assert resultado == [""]
