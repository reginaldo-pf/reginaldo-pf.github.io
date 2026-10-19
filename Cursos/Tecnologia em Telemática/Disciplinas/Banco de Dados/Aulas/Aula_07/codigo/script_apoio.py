#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IFCE Campus Taua - Curso de Tecnologia em Telematica
Disciplina: Banco de Dados (Semestre 2026.2)
Docente: Prof. Me. Reginaldo Pereira Fernandes
Aula 07 (Sabado Letivo): Estudo Dirigido do Projeto Pratico (AVP1)

Objetivo do Script:
Implementar um Metamodelo Conceitual e um Validador Automatico de Escopo (Checklist AVP1)
em Python, demonstrando a especificacao completa do Caso Modelo (Clinica Medica "VidaPlena").
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


@dataclass
class AtributoChen:
    """Representa um atributo na taxonomia canonica de Peter Chen (1976)."""
    nome: str
    tipo: str  # 'PK', 'simples', 'composto', 'multivalorado', 'derivado', 'discriminador'
    subatributos: List[str] = field(default_factory=list)
    regra_derivacao: Optional[str] = None


@dataclass
class EntidadeConceitual:
    """Representa uma Entidade Forte, Subclasse EER ou Entidade Fraca."""
    nome: str
    categoria: str  # 'forte', 'fraca', 'subclasse_eer'
    atributos: List[AtributoChen] = field(default_factory=list)
    entidade_proprietaria: Optional[str] = None
    relacionamento_identificador: Optional[str] = None


@dataclass
class RelacionamentoConceitual:
    """Representa um relacionamento entre conjuntos de entidades no MER."""
    nome: str
    entidades_papeis: List[Tuple[str, str, str]]  # [(Entidade, Papel, Participacao_min_max)]
    cardinalidade: str  # '1:1', '1:N', 'N:M'
    eh_recursivo: bool = False
    eh_identificador: bool = False
    atributos_descritivos: List[str] = field(default_factory=list)


@dataclass
class HierarquiaEER:
    """Representa uma Especializacao/Generalizacao no Modelo EER."""
    superclasse: str
    subclasses: List[str]
    disjuncao: str       # 'd' (Disjunta) ou 'o' (Sobreposta)
    integralidade: str   # 'Total' ou 'Parcial'


@dataclass
class EscopoProjetoAVP1:
    """Agrega todo o escopo conceitual de um Projeto Pratico AVP1 e audita sua conformidade."""
    titulo: str
    dominio_didatico: str
    narrativa_resumida: str
    entidades: Dict[str, EntidadeConceitual] = field(default_factory=dict)
    relacionamentos: List[RelacionamentoConceitual] = field(default_factory=list)
    hierarquias_eer: List[HierarquiaEER] = field(default_factory=list)

    def adicionar_entidade(self, ent: EntidadeConceitual) -> None:
        self.entidades[ent.nome] = ent

    def adicionar_relacionamento(self, rel: RelacionamentoConceitual) -> None:
        self.relacionamentos.append(rel)

    def adicionar_hierarquia_eer(self, eer: HierarquiaEER) -> None:
        self.hierarquias_eer.append(eer)

    def auditar_conformidade(self) -> Tuple[bool, List[str], List[str]]:
        """
        Verifica se o escopo atende aos 6 criterios obrigatorios da AVP1:
        1. Minimo de 5 entidades fortes/subclasses;
        2. Presenca dos 5 tipos de atributos de Chen (PK, simples, composto, multivalorado, derivado);
        3. Relacionamentos 1:1, 1:N e N:M (com atributo descritivo);
        4. Ao menos 1 auto-relacionamento (recursivo) com papeis;
        5. Ao menos 1 Entidade Fraca com discriminador e entidade proprietaria;
        6. Ao menos 1 Hierarquia EER com restricoes (d/o, Total/Parcial).
        """
        aprovados: List[str] = []
        pendencias: List[str] = []

        # 1. Contagem de entidades fortes (incluindo superclasse/subclasses regulares)
        fortes = [e.nome for e in self.entidades.values() if e.categoria in ("forte", "subclasse_eer")]
        if len(fortes) >= 5:
            aprovados.append(f"[OK] Entidades Regulares/Subclasses ({len(fortes)}): {', '.join(fortes)}")
        else:
            pendencias.append(f"[FALHA] Possui apenas {len(fortes)} entidades fortes (minimo exigido: 5).")

        # 2. Taxonomia de atributos de Peter Chen
        tipos_encontrados = {
            atr.tipo
            for ent in self.entidades.values()
            for atr in ent.atributos
        }
        tipos_exigidos = ["PK", "simples", "composto", "multivalorado", "derivado"]
        faltantes = [t for t in tipos_exigidos if t not in tipos_encontrados]
        if not faltantes:
            aprovados.append("[OK] Taxonomia de Atributos Chen completa (PK, simples, composto, multivalorado, derivado).")
        else:
            pendencias.append(f"[FALHA] Faltam atributos do(s) tipo(s): {', '.join(faltantes)}.")

        # 3. Cardinalidades 1:1, 1:N e N:M com atributo descritivo
        cards = {r.cardinalidade for r in self.relacionamentos}
        for c in ["1:1", "1:N", "N:M"]:
            if c not in cards:
                pendencias.append(f"[FALHA] Nao possui relacionamento de cardinalidade {c}.")
        rels_nm_com_atr = [r.nome for r in self.relacionamentos if r.cardinalidade == "N:M" and r.atributos_descritivos]
        if {"1:1", "1:N", "N:M"}.issubset(cards) and rels_nm_com_atr:
            aprovados.append(f"[OK] Cardinalidades 1:1, 1:N e N:M (com atributo em {', '.join(rels_nm_com_atr)}) presentes.")
        elif "N:M" in cards and not rels_nm_com_atr:
            pendencias.append("[FALHA] Relacionamento N:M nao possui atributo descritivo proprio.")

        # 4. Auto-relacionamento (Recursivo)
        recursivos = [r.nome for r in self.relacionamentos if r.eh_recursivo]
        if recursivos:
            aprovados.append(f"[OK] Auto-relacionamento (Unario/Recursivo) especificado: {', '.join(recursivos)}.")
        else:
            pendencias.append("[FALHA] Falta especificar ao menos 1 Auto-relacionamento (recursivo) com papeis.")

        # 5. Entidade Fraca e Discriminador
        fracas = [e for e in self.entidades.values() if e.categoria == "fraca"]
        if fracas:
            ef = fracas[0]
            disc = [a.nome for a in ef.atributos if a.tipo == "discriminador"]
            if disc and ef.entidade_proprietaria:
                aprovados.append(
                    f"[OK] Entidade Fraca '{ef.nome}' vinculada a '{ef.entidade_proprietaria}' "
                    f"com discriminador '{disc[0]}'."
                )
            else:
                pendencias.append(f"[FALHA] Entidade Fraca '{ef.nome}' sem discriminador ou proprietario definido.")
        else:
            pendencias.append("[FALHA] Nao possui Entidade Fraca no escopo.")

        # 6. Hierarquia EER
        if self.hierarquias_eer:
            h = self.hierarquias_eer[0]
            aprovados.append(
                f"[OK] Hierarquia EER: {h.superclasse} -> ({', '.join(h.subclasses)}) "
                f"[Restricoes: ({h.disjuncao}, {h.integralidade})]."
            )
        else:
            pendencias.append("[FALHA] Nao possui Hierarquia de Especializacao/Generalizacao (EER).")

        return (len(pendencias) == 0, aprovados, pendencias)


def construir_caso_modelo_clinica() -> EscopoProjetoAVP1:
    """Constroi o escopo completo do Caso Modelo: Clinica Medica VidaPlena."""
    projeto = EscopoProjetoAVP1(
        titulo="Clinica Medica VidaPlena",
        dominio_didatico="Saude / Gestao Clinica e Ambulatorial",
        narrativa_resumida=(
            "Controle de Colaboradores (especializados em Medicos e Atendentes), "
            "Departamentos Clinicos, Pacientes, Dependentes (Entidade Fraca) e Exames Laboratoriais."
        ),
    )

    # Entidades Fortes e Subclasses
    projeto.adicionar_entidade(EntidadeConceitual(
        nome="COLABORADOR",
        categoria="forte",
        atributos=[
            AtributoChen("matricula", "PK"),
            AtributoChen("cpf", "simples"),
            AtributoChen("nome_completo", "simples"),
            AtributoChen("endereco", "composto", subatributos=["rua", "numero", "bairro", "cidade"]),
            AtributoChen("telefones", "multivalorado"),
            AtributoChen("tempo_servico", "derivado", regra_derivacao="Data_Atual - Data_Admissao"),
        ]
    ))
    projeto.adicionar_entidade(EntidadeConceitual(
        nome="MEDICO",
        categoria="subclasse_eer",
        atributos=[
            AtributoChen("crm", "simples"),
            AtributoChen("especialidades", "multivalorado"),
        ]
    ))
    projeto.adicionar_entidade(EntidadeConceitual(
        nome="ATENDENTE",
        categoria="subclasse_eer",
        atributos=[
            AtributoChen("ramal", "simples"),
            AtributoChen("turno", "simples"),
        ]
    ))
    projeto.adicionar_entidade(EntidadeConceitual(
        nome="DEPTO_CLINICO",
        categoria="forte",
        atributos=[
            AtributoChen("cod_depto", "PK"),
            AtributoChen("nome_depto", "simples"),
            AtributoChen("bloco", "simples"),
        ]
    ))
    projeto.adicionar_entidade(EntidadeConceitual(
        nome="PACIENTE",
        categoria="forte",
        atributos=[
            AtributoChen("id_prontuario", "PK"),
            AtributoChen("cpf", "simples"),
            AtributoChen("nome_paciente", "simples"),
            AtributoChen("idade", "derivado", regra_derivacao="Data_Atual - Data_Nascimento"),
        ]
    ))
    projeto.adicionar_entidade(EntidadeConceitual(
        nome="EXAME",
        categoria="forte",
        atributos=[
            AtributoChen("cod_exame", "PK"),
            AtributoChen("nome_exame", "simples"),
            AtributoChen("preparo_exigido", "simples"),
        ]
    ))

    # Entidade Fraca
    projeto.adicionar_entidade(EntidadeConceitual(
        nome="DEPENDENTE",
        categoria="fraca",
        entidade_proprietaria="PACIENTE",
        relacionamento_identificador="POSSUI_DEP",
        atributos=[
            AtributoChen("nome_dep", "discriminador"),
            AtributoChen("data_nascimento", "simples"),
            AtributoChen("parentesco", "simples"),
        ]
    ))

    # Hierarquia EER
    projeto.adicionar_hierarquia_eer(HierarquiaEER(
        superclasse="COLABORADOR",
        subclasses=["MEDICO", "ATENDENTE"],
        disjuncao="d",
        integralidade="Total"
    ))

    # Relacionamentos
    projeto.adicionar_relacionamento(RelacionamentoConceitual(
        nome="DIRIGE",
        entidades_papeis=[("MEDICO", "diretor", "(0,1)"), ("DEPTO_CLINICO", "dirigido", "(1,1)")],
        cardinalidade="1:1"
    ))
    projeto.adicionar_relacionamento(RelacionamentoConceitual(
        nome="ALOCA",
        entidades_papeis=[("DEPTO_CLINICO", "lotacao", "(1,N)"), ("MEDICO", "alocado", "(1,1)")],
        cardinalidade="1:N"
    ))
    projeto.adicionar_relacionamento(RelacionamentoConceitual(
        nome="SUPERVISIONA",
        entidades_papeis=[("MEDICO", "preceptor", "(0,N)"), ("MEDICO", "residente", "(0,1)")],
        cardinalidade="1:N",
        eh_recursivo=True
    ))
    projeto.adicionar_relacionamento(RelacionamentoConceitual(
        nome="REALIZA_EXAME",
        entidades_papeis=[("PACIENTE", "submetido", "(0,N)"), ("EXAME", "prescrito", "(0,M)")],
        cardinalidade="N:M",
        atributos_descritivos=["data_solicitacao", "resultado_laudo"]
    ))
    projeto.adicionar_relacionamento(RelacionamentoConceitual(
        nome="POSSUI_DEP",
        entidades_papeis=[("PACIENTE", "titular", "(0,N)"), ("DEPENDENTE", "dependente", "(1,1)")],
        cardinalidade="1:N",
        eh_identificador=True
    ))

    return projeto


if __name__ == "__main__":
    print("=" * 78)
    print(" AUDITORIA AUTOMATICA DE ESCOPO DO PROJETO PRATICO (AVP1 - AULA 07)")
    print("=" * 78)

    caso_modelo = construir_caso_modelo_clinica()
    conforme, itens_ok, itens_erro = caso_modelo.auditar_conformidade()

    print(f"\nProjeto Auditado : {caso_modelo.titulo}")
    print(f"Dominio Didatico : {caso_modelo.dominio_didatico}")
    print("-" * 78)
    for msg in itens_ok:
        print(f"  {msg}")
    for err in itens_erro:
        print(f"  {err}")
    print("-" * 78)
    print(f"RESULTADO FINAL  : {'APROVADO (100% CONFORME COM A RUBRICA AVP1)' if conforme else 'PENDENTE DE AJUSTES'}")
    print("=" * 78)
