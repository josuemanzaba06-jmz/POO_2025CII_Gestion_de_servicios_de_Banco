# Integrantes:
# - BELTRAN ARREAGA MARIALISA
# - ESPINOZA VILLAO GEOVANNY FABRICIO
# - GOMEZ GOMEZ MELANY NAYEL
# - MANZABA ZAMBRANO JOSUE FABIAN

"""
Módulo: transferencia_bancaria.py
Descripción: Representa una transferencia bancaria entre cuentas.
Implementa los métodos de ServicioBancario.
"""

from servicio_bancario import ServicioBancario


class TransferenciaBancaria(ServicioBancario):
    """
    Representa una transferencia bancaria entre cuentas.
    """

    # Constante para calcular el costo
    COMISION_TRANSFERENCIA = 2.00

    def __init__(self, numero_transaccion, cliente, monto, cuenta_destino, fecha=None):
        """
        Constructor de TransferenciaBancaria.

        Args:
            numero_transaccion (str): ID de la transacción
            cliente (str): Nombre del cliente
            monto (float): Monto a transferir
            cuenta_destino (str): Número de cuenta destino
            fecha (datetime, optional): Fecha de la transferencia
        """
        super().__init__(numero_transaccion, cliente, monto, fecha)
        self.cuenta_destino = cuenta_destino

    @property
    def cuenta_destino(self):
        """Obtiene la cuenta destino."""
        return self._cuenta_destino

    @cuenta_destino.setter
    def cuenta_destino(self, valor):
        """
        Establece la cuenta destino con validación.

        Args:
            valor (str): Número de cuenta destino
        """
        if not isinstance(valor, str):
            raise ValueError("La cuenta debe ser un texto.")
        if len(valor) < 10:
            raise ValueError("La cuenta destino debe tener al menos 10 caracteres")
        if not valor.isdigit():
            raise ValueError("La cuenta destino solo puede contener dígitos numéricos")
        self._cuenta_destino = valor

    def calcular_costo(self):
        """
        Calcula el costo total de la transferencia.

        Returns:
            float: Costo total
        """
        return self.COMISION_BASE + self.COMISION_TRANSFERENCIA

    def procesar_transaccion(self):
        """
        Procesa la transferencia bancaria.

        Returns:
            bool: True si fue exitosa
        """
        LIMITE_MAXIMO = 10000.00

        if self._monto > LIMITE_MAXIMO:
            self._estado = "Cancelado"
            return False

        self.marcar_como_completado()
        return True

    def __str__(self):
        """Información de la transferencia."""
        return (f"Transacción: {self._numero_transaccion}\n"
                f"Tipo: {self.obtener_tipo_servicio()}\n"
                f"Cliente: {self._cliente}\n"
                f"Monto: ${self._monto:.2f}\n"
                f"Cuenta Destino: {self._cuenta_destino}\n"
                f"Fecha: {self._fecha.strftime('%d/%m/%Y %H:%M:%S')}\n"
                f"Estado: {self._estado}\n"
                f"Costo Total: ${self.calcular_costo():.2f}")