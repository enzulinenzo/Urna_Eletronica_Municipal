# URNA ELETRONICA A3
# Versão atualizada do código, de 19/11/26

# Criando a classe de candidato
class Candidato:
    def __init__(self,nome,partido,numero):
        self.nome = nome
        self.partido = partido
        self.numero = numero
        self.votos = 0

    def ReceberVoto(self):
        self.votos += 1

# Criando a classe de candidatos a vereador (usando herança)
class CandidatoVereador(Candidato):
    pass

# Registrando candidatos a vereador
CanVe1 = CandidatoVereador("Capivara Macabra", "Partido Democrata Revolucionário (PDR)", 51687)
CanVe2 = CandidatoVereador("Kim Pinheiro", "MISTÃO", 14067)
CanVe3 = CandidatoVereador("Manoel Gomes", "AVALANCHE", 70311)
CanVe4 = CandidatoVereador("Régis Tadeu", "MISTÃO", 14555)
CanVe5 = CandidatoVereador("Didi Magnussen", "Partido Máster Brasiliense (PMB)", 67228)
CanVe6 = CandidatoVereador("Cirilo Almenara", "Partido da Dentadura Torta (PDT)", 12499)
CanVe7 = CandidatoVereador("Dudu Liso", "Movimento Data Base (MDB)", 15888)
CanVe8 = CandidatoVereador("Gilberto Barros", "Partido Social do Kasino (PSK)", 87006)
CanVe9 = CandidatoVereador("Rosane da Padaria", "Partido Dentadura Torta (PDT)", 12224)
CanVe10 = CandidatoVereador("Nando Moura", "MISTÃO", 14777)
CanVe11 = CandidatoVereador("Marquinhos dos Santos", "AVALANCHE", 70651)
CanVe12 = CandidatoVereador("Rocrisvaldo Torres", "Movimento Data Base (MDB)", 15333)
CanVe13 = CandidatoVereador("Luciano Egípcio", "Partido da Tesla (PT)", 13008)
CanVe14 = CandidatoVereador("Vitória Delgado", "Partido Democrata Revolucionário (PDR)", 51348)
CanVe15 = CandidatoVereador("Flavio Alves", "Partido da Tesla (PT)", 13137)
CanVe16 = CandidatoVereador("Reinaldo de Toninho", "Partido Dentadura Torta (PDT)", 12996)
CanVe17 = CandidatoVereador("Catarina Dentinho", "Partido Capitalista Olfato (PCO)", 29789)
CanVe18 = CandidatoVereador("Patricia Campos", "Partido do Liberalismo (PL)", 22581)
CanVe19 = CandidatoVereador("Vadão do Ginásio", "AVALANCHE", 70070)
CanVe20 = CandidatoVereador("Bob Torres", "MISTÃO", 14114)
CanVe21 = CandidatoVereador("Pedro Paulo Silva", "Partido do Liberalismo (PL)", 22331)
CanVe22 = CandidatoVereador("Lucia Caminos", "Partido do Liberalismo (PL)", 22026)
CanVe23 = CandidatoVereador("Jason Duval", "Partido Social do Kasino (PSK)", 87026)
CanVe24 = CandidatoVereador("Dominic Toretto", "MISTÃO", 14001)
CanVe25 = CandidatoVereador("Mickey Mouse", "Partido Máster Brasiliense (PMB)", 67445)

# Criando a classe de candidatos a prefeito (acrescetando o atributo "vice")
class CandidatoPrefeito(Candidato):
    def __init__(self,nome,partido,vice,numero):
        super().__init__(nome,partido,numero)
        self.vice = vice
        self.votos = 0

# Registrando candidatos a prefeito
CanPref1 = CandidatoPrefeito("Daniel Vorcaro","Partido Máster Brasiliense (PMB)","Cão Orelha", 67)
CanPref2 = CandidatoPrefeito("Nico Barreiros", "Partido da Tecnocracia (PTec)", "João Luiz Costa", 80)
CanPref3 = CandidatoPrefeito("Coronel Natalino", "Partido do Liberalismo (PL)", "Sargento Rocha", 22)
CanPref4 = CandidatoPrefeito("Wenceslau Ambrosini", "MISTÃO", "Lucivaldo Diniz", 14)
CanPref5 = CandidatoPrefeito("Silvio Silva", "Movimento Data Base (MDB)", "Winston Fernandez", 15)

lista_Vereadores = [CanVe1, CanVe2, CanVe3, CanVe4, CanVe5, CanVe6, CanVe7, CanVe8, CanVe9, CanVe10, CanVe11, CanVe12, CanVe13, CanVe14, CanVe15, CanVe16, CanVe17, CanVe18, CanVe19, CanVe20, CanVe21, CanVe22, CanVe23, CanVe24, CanVe25]
lista_Prefeitos = [CanPref1, CanPref2, CanPref3, CanPref4, CanPref5]

# Criando a classe Urna Eletronica
class UrnaEletronica:
    def __init__(self, lista_Vereadores, lista_Prefeitos, senhaUrna):
        self.lista_Vereadores = lista_Vereadores
        self.lista_Prefeitos = lista_Prefeitos
        self.senhaUrna = senhaUrna
        self.votos_Descartados = {
            "brancoVer": 0,
            "nuloVer": 0,
            "brancoPref": 0,
            "nuloPref": 0
            }

    # Função para votar em vereador:
    def VotacaoVereador(self):
        while True:
            digitarNumVer = input("\n       VEREADOR       \n").strip().upper()
            encontrou = False
            voto_Confirmado = False

            if digitarNumVer == "BRANCO":
                print("VOTO EM BRANCO")
                confirmar = input("\nCONFIRMAR? (Digite sim ou não): \n").strip().upper()
                if confirmar == "SIM":
                    self.votos_Descartados["brancoVer"] += 1
                    voto_Confirmado = True
                    break
            else:
                for voto_verador in self.lista_Vereadores:
                    if str(voto_verador.numero) == digitarNumVer:
                        print(voto_verador.nome)
                        confirmar = input("\nCONFIRMAR? (Digite sim ou não): \n").strip().upper()
                        if confirmar == "SIM":
                            voto_verador.ReceberVoto()
                            voto_Confirmado = True
                        encontrou = True
                        break
                
                if not encontrou:
                    print("VOTO ANULADO")
                    confirmar = input("\nCONFIRMAR? (Digite sim ou não): \n").strip().upper()
                    if confirmar == "SIM":
                        self.votos_Descartados["nuloVer"] += 1
                        voto_Confirmado = True
                        break

            if voto_Confirmado:
                break

    # Função para votar em prefeito:
    def VotacaoPrefeito(self):
        while True:
            digitarNumPref = input("\n       PREFEITO       \n").strip().upper()
            encontrou = False
            voto_Confirmado = False

            if digitarNumPref == "BRANCO":
                print("VOTO EM BRANCO")
                confirmar = input("\nCONFIRMAR? (Digite sim ou não): \n").strip().upper()
                if confirmar == "SIM":
                    self.votos_Descartados["brancoPref"] += 1
                    voto_Confirmado = True
                    break
            else:
                for voto_prefeito in self.lista_Prefeitos:
                    if str(voto_prefeito.numero) == digitarNumPref:
                        print(voto_prefeito.nome)
                        print(f"Vice: {voto_prefeito.vice}")
                        confirmar = confirmar = input("\nCONFIRMAR? (Digite sim ou não): \n").strip().upper()
                        if confirmar == "SIM":
                            voto_prefeito.ReceberVoto()
                            voto_Confirmado = True
                        encontrou = True
                        break

                if not encontrou:
                    print("VOTO ANULADO")
                    confirmar = input("\nCONFIRMAR? (Digite sim ou não): \n").strip().upper()
                    if confirmar == "SIM":
                        self.votos_Descartados["nuloPref"] += 1
                        voto_Confirmado = True
                        break

            if voto_Confirmado:
                break
    # Função para apurar os votos:
    def ApuracaoVotos(self):
        print("\n     APURAÇÃO DOS VOTOS      \n")
        print("--     VEREADOR      --")
        for apurarVer in self.lista_Vereadores:
            print(f"Candidato: {apurarVer.nome} ({apurarVer.partido}): {apurarVer.votos} votos")
        print("\n")
        print(f"Brancos: {self.votos_Descartados['brancoVer']} votos")
        print(f"Nulos: {self.votos_Descartados['nuloVer']} votos")
        print("#"*40)

        print("\n")
        print("--     PREFEITO      --")
        for apurarPref in self.lista_Prefeitos:
            print(f"Candidato: {apurarPref.nome} ({apurarPref.partido}): {apurarPref.votos} votos")
        print("\n")
        print(f"Brancos: {self.votos_Descartados['brancoPref']} votos")
        print(f"Nulos: {self.votos_Descartados['nuloPref']}")
        print("#"*40)

    # Função para inicializar o processo de votação:
    def iniciarVotacao(self):
      while True:
        print("\n" + "-"*40)
        print("         JUSTIÇA ELEITORAL           ")
        print("-"*40)
        print("1 - Iniciar Nova Votação")
        print("2 - Encerrar Votação (Área do Mesário)")

        PerguntaVotacao = input("Você deseja iniciar/continuar a votação ou encerrar? ").strip()

        if PerguntaVotacao == "1":
            print("\n")
            self.VotacaoVereador()
            self.VotacaoPrefeito()
            print("\nFIM")

        elif PerguntaVotacao == "2":
            digiSenha = input("Digite a senha da urna: ").strip()
            if digiSenha == self.senhaUrna:
                self.ApuracaoVotos()
                break
            else:
                print("Senha incorreta! Tente novamente\n")

        else:
            print("\nOpção Inválida! Digite 1 ou 2\n")

# Iniciando a urna:
urna = UrnaEletronica(lista_Vereadores, lista_Prefeitos, "40028922")
urna.iniciarVotacao()