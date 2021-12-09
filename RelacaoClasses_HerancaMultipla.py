class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            print(f'{self._nome} já está ligado')
            return
        print(f'{self._nome} ligou')
        self._ligado = True

    def desligar(self):
        if not self._ligado:
            print(f'{self._nome} já está desligado')
            return
        print(f'{self._nome} desligou')
        self._ligado = False


class LogMixin:
    @staticmethod
    def write(msg):
        with open('E:\\Google Drive\\VSCode\\Studying\\Studying\\Python_Class\\POO\\RelacaoClasses_HerancaMultipla_log.log', 'a+') as f:
            f.write(msg)
            f.write('\n')

    def log_info(self, msg):
        self.write(f'INFO: {msg}')

    def log_error(self, msg):
        self.write(f'ERROR: {msg}')


# Herança Múltipla
class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            error = f"{self._nome} não está ligado"
            print(error)
            self.log_error(error)
            return

        if self._conectado:
            error = f'{self._nome} já está conectado'
            print(error)
            self.log_error(error)
            return
        info = f'{self._nome} conectou'
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} já está desconectado'
            print(error)
            self.log_error(error)
            return
        info = f'{self._nome} desconectou'
        print(info)
        self.log_info(info)
        self._conectado = False


smartphone = Smartphone('Xiaomi')
smartphone.conectar()
smartphone.desligar()
smartphone.ligar()
smartphone.conectar()
smartphone.conectar()
smartphone.conectar()
smartphone.desligar()
smartphone.conectar()
smartphone.desconectar()
