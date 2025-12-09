# Integrantes:
# - BELTRAN ARREAGA MARIALISA
# - ESPINOZA VILLAO GEOVANNY FABRICIO
# - GOMEZ GOMEZ MELANY NAYEL
# - MANZABA ZAMBRANO JOSUE FABIAN

"""
Módulo: servicio_bancario.py
Descripción: SuperClase, base abstracta para servicios bancarios
"""

from abc import ABC, abstractmethod
from datetime import datetime


class ServicioBancario(ABC):
    """
    Clase abstracta base para todos los servicios bancarios.
    Define la estructura común y métodos que heredarán las clases hijas.
    """

    # Constante para comisión base
    COMISION_BASE = 0.50

    def __init__(self, numero_transaccion, cliente, monto, fecha=None):
        """
        Constructor de la clase ServicioBancario.

        Args:
            numero_transaccion (str): Identificador único de la transacción
            cliente (str): Nombre del cliente
            monto (float): Monto de la transacción
            fecha (datetime, optional): Fecha de la transacción
        """
        self._numero_transaccion = numero_transaccion
        self._cliente = cliente
        self._monto = monto
        self._fecha = fecha if fecha else datetime.now()
        self._estado = "Pendiente"

    # Properties para encapsulamiento
    @property
    def numero_transaccion(self):
        """Obtiene el número de transacción."""
        return self._numero_transaccion

    @numero_transaccion.setter
    def numero_transaccion(self, valor):
        """
        Establece el número de transacción con validación.

        Args:
            valor (str): Nuevo número de transacción

        Raises:
            ValueError: Si el valor es vacío o no es string
        """
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El número de transacción debe ser un texto no vacío")
        self._numero_transaccion = valor.strip()

    @property
    def cliente(self):
        """Obtiene el nombre del cliente."""
        return self._cliente

    @cliente.setter
    def cliente(self, valor):
        """
        Establece el cliente con validación.

        Args:
            valor (str): Nombre del cliente

        Raises:
            ValueError: Si el valor es vacío
        """
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre del cliente debe ser un texto no vacío")
        self._cliente = valor.strip()

    @property
    def monto(self):
        """Obtiene el monto de la transacción."""
        return self._monto

    @monto.setter
    def monto(self, valor):
        """
        Establece el monto con validación.

        Args:
            valor (float): Monto de la transacción

        Raises:
            ValueError: Si el monto es negativo o cero
        """
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("El monto debe ser un número positivo mayor a cero")
        self._monto = float(valor)

    @property
    def fecha(self):
        """Obtiene la fecha de la transacción."""
        return self._fecha

    @fecha.setter
    def fecha(self, valor):
        """
        Establece la fecha de la transacción.

        Args:
            valor (datetime): Fecha de la transacción
        """
        if not isinstance(valor, datetime):
            raise ValueError("La fecha debe ser un objeto datetime")
        self._fecha = valor

    @property
    def estado(self):
        """Obtiene el estado de la transacción."""
        return self._estado

    @estado.setter
    def estado(self, valor):
        """
        Establece el estado con validación.

        Args:
            valor (str): Estado de la transacción
        """
        estados_validos = ["Pendiente", "Procesado", "Cancelado", "Completado"]
        if valor not in estados_validos:
            raise ValueError(f"Estado debe ser uno de: {estados_validos}")
        self._estado = valor

    @abstractmethod
    def calcular_costo(self):
        """
        Método abstracto para calcular el costo total del servicio.
        Debe ser implementado por las clases hijas.

        Returns:
            float: Costo total del servicio
        """
        pass

    @abstractmethod
    def procesar_transaccion(self):
        """
        Método abstracto para procesar la transacción.
        Debe ser implementado por las clases hijas.

        Returns:
            bool: True si la transacción fue exitosa
        """
        pass

    def obtener_tipo_servicio(self):
        """
        Obtiene el tipo de servicio bancario.

        Returns:
            str: Nombre de la clase (tipo de servicio)
        """
        return self.__class__.__name__

    def marcar_como_completado(self):
        """Marca la transacción como completada."""
        self._estado = "Completado"

    def __str__(self):
        """
        Representación en string del objeto.

        Returns:
            str: Información formateada del servicio
        """
        return (f"Transacción: {self._numero_transaccion}\n"
                f"Tipo: {self.obtener_tipo_servicio()}\n"
                f"Cliente: {self._cliente}\n"
                f"Monto: ${self._monto:.2f}\n"
                f"Fecha: {self._fecha.strftime('%d/%m/%Y %H:%M:%S')}\n"
                f"Estado: {self._estado}\n"
                f"Costo Total: ${self.calcular_costo():.2f}")

    def __repr__(self):
        """
        Representación técnica del objeto.

        Returns:
            str: Representación para debugging
        """
        return (f"{self.__class__.__name__}(numero_transaccion='{self._numero_transaccion}', "
                f"cliente='{self._cliente}', monto={self._monto})")
