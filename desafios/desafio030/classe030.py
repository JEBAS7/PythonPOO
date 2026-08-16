import hashlib


class Credencial:
    def __init__(self, senha_inicial: str):
        self.__hash = ""
        # Usamos o setter para já criptografar a senha inicial
        self.senha = senha_inicial

    # --- SETTER ---
    @property
    def senha(self):
        # O enunciado não pede um getter para a senha (até por segurança),
        # mas precisamos do @property para poder criar o .setter abaixo.
        return "Acesso negado: a senha original não fica salva!"

    @senha.setter
    def senha(self, nova_senha: str):
        """Transforma a senha em texto puro em um hash SHA256 e armazena."""
        # O hashlib precisa que o texto seja convertido em bytes (.encode())
        texto_bytes = str(nova_senha).encode('utf-8')

        # Gera o hash e transforma em uma string legível (hexadecimal)
        self.__hash = hashlib.sha256(texto_bytes).hexdigest()

    # --- MÉTODO DE VALIDAÇÃO ---
    def validar(self, chave: str) -> bool:
        """Verifica se a senha digitada gera o mesmo hash guardado."""
        texto_bytes = str(chave).encode('utf-8')
        hash_tentativa = hashlib.sha256(texto_bytes).hexdigest()

        # Se os hashes forem iguais, a senha está certa!
        return hash_tentativa == self.__hash
