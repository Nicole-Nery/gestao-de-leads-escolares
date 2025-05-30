import re

def formatar_telefone(numero: str) -> str:
        """Formata um número de telefone brasileiro"""
        numero_limpo = re.sub(r'\D', '', numero)  # Remove tudo que não for dígito

        if len(numero_limpo) == 11:
            # Com DDD + celular (ex: 34991234567)
            return f"({numero_limpo[:2]}) {numero_limpo[2:7]}-{numero_limpo[7:]}"
        elif len(numero_limpo) == 10:
            # Com DDD + fixo (ex: 3421234567)
            return f"({numero_limpo[:2]}) {numero_limpo[2:6]}-{numero_limpo[6:]}"
        elif len(numero_limpo) == 9:
            # Celular sem DDD (ex: 991234567)
            return f"{numero_limpo[:5]}-{numero_limpo[5:]}"
        elif len(numero_limpo) == 8:
            # Fixo sem DDD (ex: 21234567)
            return f"{numero_limpo[:4]}-{numero_limpo[4:]}"
        else:
            return numero  # Retorna como veio se não bater com formatos esperados
