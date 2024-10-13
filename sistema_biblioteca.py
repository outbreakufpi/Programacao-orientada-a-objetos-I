
class Livro:
    """Classe que representa um livro na biblioteca."""
    
    def __init__(self, titulo, autor):
        """Inicializa o livro com título e autor."""
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        """Representa o livro como uma string."""
        return f"{self.titulo} por {self.autor} - {'Disponível' if self.disponivel else 'Indisponível'}"


class Usuario:
    """Classe que representa um usuário da biblioteca."""
    
    def __init__(self, nome):
        """Inicializa o usuário com um nome."""
        self.nome = nome
        self.livros_emprestados = []

    def __str__(self):
        """Representa o usuário como uma string."""
        return self.nome

    def emprestar(self, livro):
        """Adiciona um livro à lista de livros emprestados do usuário."""
        self.livros_emprestados.append(livro)

    def retornar(self, livro):
        """Remove um livro da lista de livros emprestados do usuário."""
        self.livros_emprestados.remove(livro)


class Biblioteca:
    """Classe que representa a biblioteca, controlando livros e usuários."""
    
    def __init__(self):
        """Inicializa a biblioteca com listas vazias de livros e usuários."""
        self.livros = []
        self.usuarios = {}

    def adicionar_livro(self, livro):
        """Adiciona um livro à biblioteca."""
        self.livros.append(livro)

    def registrar_usuario(self, usuario):
        """Registra um usuário na biblioteca."""
        self.usuarios[usuario.nome] = usuario

    def emprestar_livro(self, titulo, usuario_nome):
        """Empresta um livro para um usuário, se disponível."""
        for livro in self.livros:
            if livro.titulo == titulo and livro.disponivel:
                livro.disponivel = False
                usuario = self.usuarios.get(usuario_nome)
                if usuario:
                    usuario.emprestar(livro)
                    print(f"Livro '{titulo}' emprestado para {usuario_nome}.")
                return
        print(f"Desculpe, o livro '{titulo}' não está disponível ou não existe.")

    def retornar_livro(self, titulo, usuario_nome):
        """Retorna um livro para a biblioteca."""
        usuario = self.usuarios.get(usuario_nome)
        if usuario:
            for livro in usuario.livros_emprestados:
                if livro.titulo == titulo:
                    livro.disponivel = True
                    usuario.retornar(livro)
                    print(f"Livro '{titulo}' retornado por {usuario_nome}.")
                    return
        print(f"Desculpe, o livro '{titulo}' não foi emprestado por {usuario_nome}.")

    def listar_livros(self):
        """Lista todos os livros na biblioteca."""
        for livro in self.livros:
            print(livro)


def main():
    """Função principal que executa o programa."""
    biblioteca = Biblioteca()

    # Adicionando alguns livros
    biblioteca.adicionar_livro(Livro("Dom Casmurro", "Machado de Assis"))
    biblioteca.adicionar_livro(Livro("O Alquimista", "Paulo Coelho"))
    biblioteca.adicionar_livro(Livro("1984", "George Orwell"))

    # Registrando usuários
    usuario1 = Usuario("Alice")
    usuario2 = Usuario("Bob")
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Interação com o usuário
    while True:
        print("\nMenu:")
        print("1. Listar livros")
        print("2. Emprestar livro")
        print("3. Retornar livro")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            biblioteca.listar_livros()
        elif opcao == "2":
            titulo = input("Digite o título do livro: ")
            usuario_nome = input("Digite seu nome: ")
            biblioteca.emprestar_livro(titulo, usuario_nome)
        elif opcao == "3":
            titulo = input("Digite o título do livro: ")
            usuario_nome = input("Digite seu nome: ")
            biblioteca.retornar_livro(titulo, usuario_nome)
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
