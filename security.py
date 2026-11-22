"""Autenticación local con PBKDF2 y SQLite; contraseñas nunca en texto claro."""
import sqlite3, os, hashlib, hmac, secrets
from pathlib import Path
from domain import ValidacionError, texto
DB = Path(os.getenv('ECOTECH_AUTH_DB','usuarios_local.db'))
ITERACIONES=600_000

def _hash(password,salt):
    return hashlib.pbkdf2_hmac('sha256',password.encode(),salt,ITERACIONES)

class Autenticacion:
    def __init__(self, db=DB):
        self.db=str(db)
        with sqlite3.connect(self.db) as c:
            c.execute('CREATE TABLE IF NOT EXISTS usuarios (usuario TEXT PRIMARY KEY, salt BLOB NOT NULL, hash BLOB NOT NULL, rol TEXT NOT NULL CHECK(rol IN (\'ADMIN\',\'OPERADOR\')))')
    def registrar(self,usuario,password):
        usuario=texto(usuario,'Usuario',40)
        if len(password)<12: raise ValidacionError('Contraseña: mínimo 12 caracteres')
        salt=secrets.token_bytes(16)
        with sqlite3.connect(self.db) as c:
            rol='ADMIN' if c.execute('SELECT COUNT(*) FROM usuarios').fetchone()[0]==0 else 'OPERADOR'
            c.execute('INSERT INTO usuarios VALUES (?,?,?,?)',(usuario,salt,_hash(password,salt),rol))
        return rol
    def autenticar(self,usuario,password):
        with sqlite3.connect(self.db) as c:
            row=c.execute('SELECT salt,hash,rol FROM usuarios WHERE usuario=?',(usuario,)).fetchone()
        if row and hmac.compare_digest(_hash(password,row[0]),row[1]): return row[2]
        raise ValidacionError('Credenciales incorrectas')
    def cambiar_clave(self,usuario,actual,nueva):
        self.autenticar(usuario,actual)
        if len(nueva)<12: raise ValidacionError('Contraseña: mínimo 12 caracteres')
        salt=secrets.token_bytes(16)
        with sqlite3.connect(self.db) as c:
            c.execute('UPDATE usuarios SET salt=?,hash=? WHERE usuario=?', (salt,_hash(nueva,salt),usuario))
