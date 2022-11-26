'''
Escreva um programa para simular a operação de um terminal bancário, com as seguintes operações:
 Saque
 Depósito (reabastecimento do terminal)
 Histórico de saques e depósitos
 Informar o saldo disponível
Cada operação será implementada por meio de uma função e todas as funções serão chamadas na função
principal (main). Inicialmente o terminal terá 100 (cem) cédulas (notas) de cada valor: R$100, R$50,
R$20, R$10, R$5, R$2, R$1.
Detalhamento das operações:
Saque: solicitar um valor em reais (R$) e verificar se há disponibilidade de saldo. Em caso afirmativo,
determinar e informar o número de notas para se obter esse valor. Caso contrário, emitir uma mensagem
informando que não há saldo suficiente.
Depósito: solicitar a quantidade de cada uma das cédulas e acrescentá-la à quantidade já existente de
cada uma delas, atualizando o saldo disponível.
Histórico de saques e depósitos: informar os valores sacados, como valores negativos, e os valores
depositados, como valores positivos.
Informar o saldo disponível: informar o total disponível considerando a quantidade existente de cada
uma das cédulas.
A função principal (main) deverá exibir um menu com as opções representando as operações e uma
opção para encerramento do programa.
Importante: na avaliação das soluções apresentadas, serão consideradas as estruturas usadas para
construir o programa e as funções, apenas o abordado no curso.
A solução da prova deverá ser feita em um único arquivo .py ou .ipynb
'''

class BankNote:

    def __init__(self, value: int) -> None:
        self.value = value
    
    def __repr__(self) -> str:
        return f'R${self.value}'

class Terminal:

    def __init__(self) -> None:
        self.bank_notes = {'100': [], '50': [], '20': [], '10': [], '5': [], '2': [], '1': []}
        self.logs = '\n------LOGS------\n'
        for key in self.bank_notes.keys():
            self.bank_notes[key] = [BankNote(int(key)) for i in range(100)]
    
    def withdraw(self, notes_amount) -> None:
        for note in notes_amount.keys():
            if notes_amount[note] != 0:
                self.bank_notes[note] = self.bank_notes[note][:(-notes_amount[note])]

    def deposit(self, notes_amount) -> None:
        for key in notes_amount.keys():
            self.bank_notes[key].extend([BankNote(100) for _ in range(notes_amount[key])])

    def total_money_value(self) -> int:
        value = 0
        for note in self.bank_notes.keys():
            value += len(self.bank_notes[note]) * int(note)
        return value    

    def tnotes_and_tvalues(self) -> None:
        for note in self.bank_notes.keys():
            print(f'{len(self.bank_notes[note])} notas de {note} totalizando R${len(self.bank_notes[note]) * int(note)}')
    
    def __repr__(self) -> str:
        print()
        self.tnotes_and_tvalues()
        return f'Totalizando R${self.total_money_value()}\n'

    def process_deposit(self) -> None:
        print('\n\nPROCESSO DE DEPOSITO\n\n')
        print('Valores invalidos serão considerados 0 ex: "a" = 0.\nparte decimal é desconsiderada ex: 4.8 = 4')
        notes = {'100': 0, '50': 0, '20': 0, '10': 0, '5': 0, '2': 0, '1': 0}
        amount = 0
        for note in notes.keys():
            try:
                notes[note] = int(float(input(f'Quantas notas de R${note} quer depositar?..: ')))
                amount += notes[note] * int(note)
            except:
                notes[note] = 0

        self.deposit(notes)
        self.logs += f'DEPOSITO: R${amount}\n'
        for note in notes.keys():
            self.logs += f'R${note} x {notes[note]}\n'
        self.logs += '\n'
    
    def process_withdraw(self) -> None:
        print('\n\nPROCESSO DE SAQUE\n\n')
        print('Valores invalidos serão considerados 0 ex: "a" = 0.\nparte decimal é desconsiderada ex: 4.8 = 4')
        notes = {'100': 0, '50': 0, '20': 0, '10': 0, '5': 0, '2': 0, '1': 0}
        try:
            amount = int(float(input('Quantos reais quer sacar?..: ')))
        except:
            amount = 0
        if amount == 0:
            print('Valor invalido, nenhum saque realizado\n\n')
            return
        amount1 = amount
        for note in self.bank_notes.keys():
            qntt = amount // int(note)
            amount = amount % int(note)
            notes[note] = qntt
        
        self.withdraw(notes)
        print(f'Voce sacou R${amount1}')
        self.logs += f'SAQUE: R${amount1}\n'
        for note in notes.keys():
            self.logs += f'R${note} x {notes[note]}\n'
        self.logs += '\n'    


def menu_text() -> None:
    print('\n1: SAQUE')
    print('2: DEPOSITO')
    print('3: SALDO DISPONIVEL')
    print('4: HISTORICO SAQUES & DEPOSITOS\n')


def main():
    user_input = -1
    terminal = Terminal()
    while user_input != 0:
        menu_text()
        user_input = input('Escolha uma opção..: ')
        if user_input == '1':
            terminal.process_withdraw()
        elif user_input == '2':
            terminal.process_deposit()
        elif user_input == '3':
            print(terminal)
        elif user_input == '4':
            print(terminal.logs)
        else:
            pass

if __name__ == '__main__':
    main()
