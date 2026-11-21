# poo-seguro-2026

## CONFIGURAR GIT
1. Descargar git desde su web [git-scm.com](https://git-scm.com/install/)
2. En la carpeta donde tendrás tu código ejecuta el git bash
3. Ejecuta los siguientes comandos:
   - `git config user.name "tu_nombre_en_github"`
   - `git config user.email "tu_correo"`
4. Clona el repositorio:
   - `git clone https://github.com/profe-ricardo/poo-seguro-2026.git`
5. Asegúrate de estar en tu rama:
   - `git checkout "nombre_de_tu_rama"`
6. Generar git ignore desde este [enlace](https://gitignore.io)
7. Genera el env y comienza a usarlo:
   - `python -m venv env` -> `env` es el nombre de tu enviroment
   - ejecuta `env\Scripts\Activate.ps1` para habilitar tu enviroment
8. Instala todo lo necesario con el siguiente comando:
   - `pip install -r requirements.txt`
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
