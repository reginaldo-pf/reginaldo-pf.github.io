#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Apoio Didático - Aula 05
Disciplina: Banco de Dados | IFCE Campus Tauá
Docente: Prof. Me. Reginaldo Pereira Fernandes

Tópicos Abordados (Modelagem Puramente Conceitual - Sem SQL):
1. Conceito Formal de Relacionamento no MER (Peter Chen, 1976)
2. Graus de Relacionamento:
   - Unário / Auto-relacionamento com Papéis (Supervisor e Supervisionado)
   - Binário (Ex: Departamento e Funcionário)
   - Ternário (Ex: Médico, Paciente e Medicamento)
3. Razões de Cardinalidade:
   - 1:1 (Um para Um: Gerência de Departamento)
   - 1:N (Um para Muitos: Lotação de Funcionários)
   - N:M (Muitos para Muitos: Alocação em Projetos)
4. Restrições de Participação:
   - Total (Existência dependente / Linha dupla)
   - Parcial (Opcional / Linha simples)
5. Atributos de Relacionamentos (Atributos Descritivos: Horas Semanais)
"""

from enum import Enum
from typing import Any, Dict, List, Optional, Set, Tuple


# ==============================================================================
# 1. METAMODELO CONCEITUAL DO MER EM PYTHON
# ==============================================================================

class TipoCardinalidade(Enum):
    UM_PARA_UM = "1:1"
    UM_PARA_MUITOS = "1:N"
    MUITOS_PARA_MUITOS = "N:M"


class TipoParticipacao(Enum):
    TOTAL = "Total (Obrigatória / Linha Dupla)"
    PARCIAL = "Parcial (Opcional / Linha Simples)"


class InstanciaRelacionamento:
    """Representa uma ligação concreta entre duas instâncias de entidades."""
    def __init__(
        self,
        id_a: str,
        id_b: str,
        atributos: Optional[Dict[str, Any]] = None,
        papel_a: Optional[str] = None,
        papel_b: Optional[str] = None
    ):
        self.id_a = id_a
        self.id_b = id_b
        self.atributos = atributos or {}
        self.papel_a = papel_a
        self.papel_b = papel_b

    def __repr__(self) -> str:
        papeis = f" ({self.papel_a} -> {self.papel_b})" if self.papel_a else ""
        attrs = f" | Dados: {self.atributos}" if self.atributos else ""
        return f"Ligação[{self.id_a} <---> {self.id_b}{papeis}{attrs}]"


class DefinicaoRelacionamento:
    """Representa a especificação conceitual de um Tipo de Relacionamento no MER."""
    def __init__(
        self,
        nome: str,
        entidade_a: str,
        entidade_b: str,
        cardinalidade: TipoCardinalidade,
        participacao_a: TipoParticipacao,
        participacao_b: TipoParticipacao,
        papeis: Optional[Tuple[str, str]] = None,
        atributos_descritivos: Optional[List[str]] = None
    ):
        self.nome = nome
        self.entidade_a = entidade_a
        self.entidade_b = entidade_b
        self.cardinalidade = cardinalidade
        self.participacao_a = participacao_a
        self.participacao_b = participacao_b
        self.papeis = papeis
        self.atributos_descritivos = atributos_descritivos or []
        self.instancias: List[InstanciaRelacionamento] = []

    def adicionar_ligacao(
        self,
        id_a: str,
        id_b: str,
        atributos: Optional[Dict[str, Any]] = None
    ):
        """Valida as restrições conceituais de Peter Chen antes de efetivar o vínculo."""
        atributos = atributos or {}

        # 1. Validar preenchimento dos atributos do relacionamento
        for attr in self.atributos_descritivos:
            if attr not in atributos:
                raise ValueError(
                    f"Violação em '{self.nome}': O atributo descritivo '{attr}' é obrigatório."
                )

        # 2. Validar restrição de cardinalidade 1:1
        # Nem A pode repetir com outro B, nem B pode repetir com outro A
        if self.cardinalidade == TipoCardinalidade.UM_PARA_UM:
            for inst in self.instancias:
                if inst.id_a == id_a:
                    raise ValueError(
                        f"Violação de Cardinalidade 1:1 em '{self.nome}': "
                        f"A entidade '{self.entidade_a}' [{id_a}] já está vinculada a [{inst.id_b}]."
                    )
                if inst.id_b == id_b:
                    raise ValueError(
                        f"Violação de Cardinalidade 1:1 em '{self.nome}': "
                        f"A entidade '{self.entidade_b}' [{id_b}] já está vinculada a [{inst.id_a}]."
                    )

        # 3. Validar restrição de cardinalidade 1:N
        # Uma entidade A pode ter múltiplos B, mas cada B só pode pertencer a no máximo um A!
        elif self.cardinalidade == TipoCardinalidade.UM_PARA_MUITOS:
            for inst in self.instancias:
                if inst.id_b == id_b:
                    raise ValueError(
                        f"Violação de Cardinalidade 1:N em '{self.nome}': "
                        f"A entidade '{self.entidade_b}' [{id_b}] já está vinculada a [{inst.id_a}]."
                    )

        # 4. Validar duplicidade exata em N:M
        elif self.cardinalidade == TipoCardinalidade.MUITOS_PARA_MUITOS:
            for inst in self.instancias:
                if inst.id_a == id_a and inst.id_b == id_b:
                    raise ValueError(
                        f"Violação em '{self.nome}': "
                        f"O par [{id_a}] e [{id_b}] já possui esse relacionamento registrado."
                    )

        papel_a = self.papeis[0] if self.papeis else None
        papel_b = self.papeis[1] if self.papeis else None

        nova_ligacao = InstanciaRelacionamento(id_a, id_b, atributos, papel_a, papel_b)
        self.instancias.append(nova_ligacao)

    def auditar_participacao(
        self,
        todos_a: Set[str],
        todos_b: Set[str]
    ) -> Dict[str, Any]:
        """Verifica se as restrições de participação total (linha dupla) foram respeitadas."""
        presentes_a = {inst.id_a for inst in self.instancias}
        presentes_b = {inst.id_b for inst in self.instancias}

        pendencias_a = todos_a - presentes_a if self.participacao_a == TipoParticipacao.TOTAL else set()
        pendencias_b = todos_b - presentes_b if self.participacao_b == TipoParticipacao.TOTAL else set()

        return {
            "valido": (len(pendencias_a) == 0) and (len(pendencias_b) == 0),
            "pendencias_a": pendencias_a,
            "pendencias_b": pendencias_b
        }


# ==============================================================================
# 2. FUNÇÕES AUXILIARES DE FORMATAÇÃO DIDÁTICA
# ==============================================================================

def cabecalho(titulo: str):
    print("\n" + "=" * 80)
    print(f" {titulo.upper()} ".center(80, "="))
    print("=" * 80)


def divisor(subtitulo: str):
    print("\n" + "-" * 80)
    print(f"[*] {subtitulo}")
    print("-" * 80)


# ==============================================================================
# 3. DEMONSTRAÇÕES DIDÁTICAS DE CARDINALIDADES E RESTRIÇÕES
# ==============================================================================

def main():
    cabecalho("Laboratório Conceitual: Relacionamentos no MER (Peter Chen, 1976)")

    print("""
Minimundo Didático: Gestão de Pessoas, Departamentos e Projetos de uma Empresa
Entidades Cadastradas:
  - DEPARTAMENTO : Engenharia, Recursos Humanos, Marketing
  - FUNCIONARIO  : Ana Silva, Carlos Souza, Beatriz Lima, Daniel Rocha
  - PROJETO      : Sistema Web, App Mobile, Portal Corporativo
""")

    # --------------------------------------------------------------------------
    # Cenário 1: Relacionamento 1:1 (DEPARTAMENTO <--> FUNCIONARIO: GERENCIA)
    # Regra: Cada departamento tem no máximo 1 gerente; cada funcionário gerencia no máximo 1 depto.
    # --------------------------------------------------------------------------
    divisor("1. Relacionamento 1:1 - [DEPARTAMENTO] <--- GERENCIA ---> [FUNCIONARIO]")
    rel_gerencia = DefinicaoRelacionamento(
        nome="GERENCIA",
        entidade_a="DEPARTAMENTO",
        entidade_b="FUNCIONARIO",
        cardinalidade=TipoCardinalidade.UM_PARA_UM,
        participacao_a=TipoParticipacao.TOTAL,    # Todo depto deve ter 1 gerente
        participacao_b=TipoParticipacao.PARCIAL,  # Nem todo funcionário é gerente
        atributos_descritivos=["data_posse"]
    )

    print("-> Registrando: 'Engenharia' é gerenciado por 'Ana Silva' (Data: 2026-01-15)")
    rel_gerencia.adicionar_ligacao("Engenharia", "Ana Silva", {"data_posse": "2026-01-15"})
    print("   Vínculo 1:1 criado com sucesso!")

    print("\n-> Tentativa de Violação 1:1 (tentar alocar 'Carlos Souza' como segundo gerente de 'Engenharia'):")
    try:
        rel_gerencia.adicionar_ligacao("Engenharia", "Carlos Souza", {"data_posse": "2026-05-10"})
    except ValueError as e:
        print(f"   [BLOQUEIO CONCEITUAL CORRETO]: {e}")

    # --------------------------------------------------------------------------
    # Cenário 2: Relacionamento 1:N (DEPARTAMENTO <--- LOTADO_EM ---> FUNCIONARIO)
    # Regra: 1 Departamento possui muitos funcionários; cada funcionário está em apenas 1 depto.
    # --------------------------------------------------------------------------
    divisor("2. Relacionamento 1:N - [DEPARTAMENTO] <--- LOTADO_EM ---> [FUNCIONARIO]")
    rel_lotacao = DefinicaoRelacionamento(
        nome="LOTADO_EM",
        entidade_a="DEPARTAMENTO",
        entidade_b="FUNCIONARIO",
        cardinalidade=TipoCardinalidade.UM_PARA_MUITOS,
        participacao_a=TipoParticipacao.PARCIAL,  # Depto novo pode estar sem funcionários
        participacao_b=TipoParticipacao.TOTAL     # Todo funcionário deve estar lotado em 1 depto
    )

    print("-> Alocando 'Ana Silva' no departamento de 'Engenharia'")
    rel_lotacao.adicionar_ligacao("Engenharia", "Ana Silva")

    print("-> Alocando 'Carlos Souza' também no departamento de 'Engenharia'")
    rel_lotacao.adicionar_ligacao("Engenharia", "Carlos Souza")
    print("   Ambos alocados no mesmo departamento com sucesso (regra 1:N respeitada)!")

    print("\n-> Tentativa de Violação 1:N (tentar lotar 'Carlos Souza' também no 'Marketing'):")
    try:
        rel_lotacao.adicionar_ligacao("Marketing", "Carlos Souza")
    except ValueError as e:
        print(f"   [BLOQUEIO CONCEITUAL CORRETO]: {e}")

    # --------------------------------------------------------------------------
    # Cenário 3: Relacionamento N:M (FUNCIONARIO <--- TRABALHA_EM ---> PROJETO)
    # Regra: Funcionários atuam em vários projetos; projetos possuem vários funcionários.
    # Atributo do Relacionamento: 'horas_semanais'
    # --------------------------------------------------------------------------
    divisor("3. Relacionamento N:M com Atributo Descritivo - [FUNCIONARIO] <--- TRABALHA_EM ---> [PROJETO]")
    rel_projetos = DefinicaoRelacionamento(
        nome="TRABALHA_EM",
        entidade_a="FUNCIONARIO",
        entidade_b="PROJETO",
        cardinalidade=TipoCardinalidade.MUITOS_PARA_MUITOS,
        participacao_a=TipoParticipacao.PARCIAL,
        participacao_b=TipoParticipacao.PARCIAL,
        atributos_descritivos=["horas_semanais"]
    )

    print("-> 'Ana Silva' atua no 'Sistema Web' por 20 horas/semana")
    rel_projetos.adicionar_ligacao("Ana Silva", "Sistema Web", {"horas_semanais": 20})

    print("-> 'Ana Silva' atua também no 'App Mobile' por 15 horas/semana")
    rel_projetos.adicionar_ligacao("Ana Silva", "App Mobile", {"horas_semanais": 15})

    print("-> 'Carlos Souza' atua no 'Sistema Web' por 30 horas/semana")
    rel_projetos.adicionar_ligacao("Carlos Souza", "Sistema Web", {"horas_semanais": 30})
    print("   Relações N:M com atributo descritivo 'horas_semanais' registradas com sucesso!")

    # --------------------------------------------------------------------------
    # Cenário 4: Auto-relacionamento Unário com Papéis (SUPERVISAO)
    # Regra: Funcionários supervisionam outros funcionários dentro da empresa.
    # --------------------------------------------------------------------------
    divisor("4. Auto-relacionamento Unário com Papéis - [FUNCIONARIO] <--- SUPERVISIONA ---> [FUNCIONARIO]")
    rel_supervisao = DefinicaoRelacionamento(
        nome="SUPERVISAO",
        entidade_a="FUNCIONARIO",
        entidade_b="FUNCIONARIO",
        cardinalidade=TipoCardinalidade.UM_PARA_MUITOS,
        participacao_a=TipoParticipacao.PARCIAL,
        participacao_b=TipoParticipacao.PARCIAL,
        papeis=("Supervisor", "Supervisionado")
    )

    print("-> 'Ana Silva' (Supervisora) supervisiona 'Carlos Souza' (Supervisionado)")
    rel_supervisao.adicionar_ligacao("Ana Silva", "Carlos Souza")

    print("-> 'Ana Silva' (Supervisora) supervisiona 'Beatriz Lima' (Supervisionada)")
    rel_supervisao.adicionar_ligacao("Ana Silva", "Beatriz Lima")
    print("   Auto-relacionamento com papéis explícitos estabelecido com sucesso!")

    # --------------------------------------------------------------------------
    # Cenário 5: Auditoria de Participação Total (Linha Dupla)
    # --------------------------------------------------------------------------
    divisor("5. Auditoria de Restrição de Participação Total")
    todos_funcionarios = {"Ana Silva", "Carlos Souza", "Beatriz Lima", "Daniel Rocha"}
    todos_departamentos = {"Engenharia", "Recursos Humanos", "Marketing"}

    auditoria = rel_lotacao.auditar_participacao(todos_departamentos, todos_funcionarios)
    print("-> Verificando se todo FUNCIONÁRIO está lotado em algum departamento (Participação TOTAL):")
    if not auditoria["valido"]:
        print("   [AVISO DE REGRA DE NEGÓCIO]: Há funcionários cadastrados sem departamento:")
        for func in auditoria["pendencias_b"]:
            print(f"   - {func} (Pendente de lotação departamental!)")

    cabecalho("Fim do Laboratório - Modelagem Conceitual Validada com Sucesso")


if __name__ == "__main__":
    main()
