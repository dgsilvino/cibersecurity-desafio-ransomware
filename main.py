import sys
import os
from src.engine import RansomwareEngine
from src.utils import log_info, log_success, log_error


def main():
    # 1. Configuração básica
    FIXED_KEY = "testeransomwares"  # Deve ter exatamente 16 caracteres

    # 2. Interface Simples via Terminal
    print("-" * 30)
    print(" CRYPTO-CHALLENGE v1.0 ")
    print("-" * 30)

    action = input("O que deseja fazer? (1: Encriptar / 2: Decriptar): ")
    file_path = input("Caminho do arquivo (ex: tests/alvo.txt): ")

    # 3. Validação de segurança
    if not os.path.exists(file_path):
        log_error(f"Arquivo '{file_path}' não encontrado!")
        return

    # 4. Inicialização da Engine
    try:
        engine = RansomwareEngine(FIXED_KEY)

        if action == "1":
            log_info(f"Criptografando {file_path}...")
            new_path = engine.encrypt_file(file_path)
            log_success(f"Arquivo bloqueado: {new_path}")

        elif action == "2":
            log_info(f"Descriptografando {file_path}...")
            # Se o usuário esquecer o .locked, nós tentamos ajudar
            if not file_path.endswith(".locked"):
                file_path += ".locked"

            original_path = engine.decrypt_file(file_path)
            log_success(f"Arquivo restaurado: {original_path}")

        else:
            log_error("Opção inválida!")

    except Exception as e:
        log_error(f"Falha na operação: {e}")


if __name__ == "__main__":
    main()
