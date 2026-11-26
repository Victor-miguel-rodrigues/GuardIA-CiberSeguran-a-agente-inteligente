"""
Laboratório de Demonstração AppSec: Vulnerabilidade de Injeção de SQL (CWE-89)
Projeto: DIO Agent - Especialização em Cibersegurança

Este arquivo demonstra a diferença entre código vulnerável (concatenação direta de strings)
e código seguro (consultas parametrizadas / Prepared Statements).
"""

import sqlite3

def init_db():
    """Inicializa banco SQLite em memória para teste de laboratório."""
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'SuperSecretPassword123')")
    cursor.execute("INSERT INTO users (username, password) VALUES ('user1', 'Password@2026')")
    conn.commit()
    return conn

# ==============================================================================
# 🔴 CÓDIGO VULNERÁVEL (Injeção de SQL - CWE-89 / OWASP A03:2021)
# Técnica MITRE ATT&CK: T1190 (Exploit Public-Facing Application)
# ==============================================================================
def login_vulneravel(conn, username, password):
    """
    VULNERABILIDADE:
    A entrada do usuário é concatenada diretamente na string da query SQL.
    Um atacante pode injetar: admin' --
    Isso comenta o restante da query e efetua o login sem validação da senha.
    """
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"\n[!] Executando Query Vulnerável:\n    {query}")
    cursor.execute(query)
    user = cursor.fetchone()
    return user

# ==============================================================================
# 🟢 CÓDIGO SEGURO (Consulta Parametrizada / Prepared Statement)
# Boas Práticas Blue Team & Defensive Coding
# ==============================================================================
def login_seguro(conn, username, password):
    """
    CORREÇÃO (REMEDIAÇÃO):
    Utiliza placeholders (?) para que os dados do usuário sejam tratados
    estritamente como literais de dados pelo interpretador do banco de dados,
    nunca como código executável.
    """
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    print(f"\n[+] Executando Query Parametrizada Segura:\n    {query}")
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    return user

if __name__ == "__main__":
    banco = init_db()

    print("=== TESTE 1: Login Legítimo ===")
    res = login_seguro(banco, "admin", "SuperSecretPassword123")
    print(f"Resultado: {'Sucesso' if res else 'Falha'}")

    print("\n=== TESTE 2: Tentativa de Bypass com SQL Injection (admin' --) ===")
    payload_injection = "admin' --"

    # Tentativa no código vulnerável
    res_vuln = login_vulneravel(banco, payload_injection, "qualquercoisa")
    print(f"Resultado no código vulnerável: {'🔴 BYPASS CONFIRMADO!' if res_vuln else 'Bloqueado'}")

    # Tentativa no código seguro
    res_seguro = login_seguro(banco, payload_injection, "qualquercoisa")
    print(f"Resultado no código seguro: {'🔴 Vulnerável' if res_seguro else '🟢 MITIGADO COM SUCESSO (Login Falhou)'}")
