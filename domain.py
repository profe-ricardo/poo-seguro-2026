"""Entidades POO del dominio; las validaciones se realizan antes de persistir."""
from dataclasses import dataclass
from datetime import date
import re

class ValidacionError(ValueError):
    pass

def texto(valor, campo, maximo=150):
    if not isinstance(valor, str) or not valor.strip() or len(valor.strip()) > maximo:
        raise ValidacionError(f'{campo}: texto obligatorio (máximo {maximo} caracteres)')
    return valor.strip()

def correo_valido(valor):
    valor = texto(valor, 'Correo')
    if not re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+', valor):
        raise ValidacionError('Correo no válido')
    return valor.lower()

def fecha_valida(valor):
    try: return date.fromisoformat(valor)
    except (ValueError, TypeError): raise ValidacionError('Fecha inválida: use AAAA-MM-DD')

def positivo(valor, nombre, admite_cero=False):
    try: n = float(valor)
    except (ValueError, TypeError): raise ValidacionError(f'{nombre} debe ser numérico')
    import math
    if not math.isfinite(n) or n < 0 or (n == 0 and not admite_cero):
        raise ValidacionError(f'{nombre} fuera de rango')
    return n

@dataclass
class Empleado:
    nombre: str
    direccion: str
    telefono: str
    correo: str
    fecha_contrato: date
    salario: float
    id_departamento: int
    def __post_init__(self):
        self.nombre=texto(self.nombre,'Nombre',120)
        self.direccion=texto(self.direccion,'Dirección',200)
        self.telefono=texto(self.telefono,'Teléfono',30)
        self.correo=correo_valido(self.correo)
        self.salario=positivo(self.salario,'Salario',True)
        if self.id_departamento <= 0: raise ValidacionError('Departamento inválido')

@dataclass
class Proyecto:
    nombre: str
    descripcion: str
    fecha_inicio: date
    estado: str
    pais: str
    moneda: str
    def __post_init__(self):
        self.nombre=texto(self.nombre,'Nombre',120)
        self.descripcion=self.descripcion.strip()[:500]
        self.pais=texto(self.pais,'País',80)
        self.moneda=texto(self.moneda,'Moneda',3).upper()
        if not re.fullmatch('[A-Z]{3}',self.moneda): raise ValidacionError('Moneda ISO de tres letras')
        if self.estado not in ('PLANIFICADO','ACTIVO','FINALIZADO'): raise ValidacionError('Estado inválido')

@dataclass
class RegistroTiempo:
    id_empleado: int
    id_proyecto: int
    fecha: date
    horas: float
    descripcion: str
    def __post_init__(self):
        self.horas=positivo(self.horas,'Horas')
        if self.horas > 24: raise ValidacionError('Horas no pueden superar 24')
        self.descripcion=texto(self.descripcion,'Descripción',300)
