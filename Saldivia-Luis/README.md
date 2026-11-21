# Sistema de Órdenes de Servicio - POO Seguro 2026

## Estructura

```
saldivia-luis/
├── config/
│   └── app_config.py
├── model/
│   ├── cliente.py
│   ├── equipo.py
│   └── orden_servicio.py
├── main.py
├── .gitignore
└── README.md
```

## Requisitos

- Python 3.8+
- oracledb
- python-dotenv

```bash
pip install oracledb python-dotenv
```

## Configuración

Crear archivo `.env` en la raíz del proyecto:

```
DB_USER=tu_usuario
DB_PASS=tu_password
DB_DSN=localhost:1521/XEPDB1
```

## Ejecución

```bash
python main.py
```

## Funcionalidades

- **Cliente**: valida tabla, inserta, actualiza teléfono
- **Equipo**: valida tabla, inserta (serie única)
- **OrdenServicio**: valida tabla, inserta, cambia estado, registra diagnóstico
