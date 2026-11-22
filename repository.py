"""Acceso Oracle """
import os
from contextlib import contextmanager
import oracledb

class OracleRepo:
    def __init__(self, connect=None): self._connect=connect or self._default
    @staticmethod
    def _default():
        return oracledb.connect(user=os.environ['ORACLE_USER'],password=os.environ['ORACLE_PASSWORD'],dsn=os.environ['ORACLE_DSN'])
    @contextmanager
    def conexion(self):
        c=self._connect()
        try:
            yield c
            c.commit()
        except Exception:
            c.rollback()
            raise
        finally: c.close()
    def consultar(self,sql,params=None):
        with self.conexion() as c:
            cur=c.cursor();cur.execute(sql,params or {});return cur.fetchall()
    def ejecutar(self,sql,params=None):
        with self.conexion() as c:
            cur=c.cursor();cur.execute(sql,params or {});return cur.rowcount
    def insertar(self,sql,params=None,id_col="id"):
        with self.conexion() as c:
            cur=c.cursor();out=cur.var(int)
            cur.execute(sql+f' RETURNING {id_col} INTO :nuevo_id',dict(params or {},nuevo_id=out))
            return int(out.getvalue()[0])

class EcoTechRepo(OracleRepo):
    def departamentos(self): return self.consultar('SELECT id_departamento,nombre,gerente_id FROM departamentos ORDER BY id_departamento')
    def crear_departamento(self,nombre): return self.insertar('INSERT INTO departamentos(nombre) VALUES(:nombre)',{'nombre':nombre},'id_departamento')
    def empleados(self): return self.consultar('SELECT id_empleado,nombre,correo,salario,id_departamento FROM empleados ORDER BY id_empleado')
    def crear_empleado(self,e):
        return self.insertar('INSERT INTO empleados(nombre,direccion,telefono,correo,fecha_contrato,salario,id_departamento) VALUES(:nombre,:direccion,:telefono,:correo,:fecha_contrato,:salario,:id_departamento)',vars(e),'id_empleado')
    def actualizar_empleado(self,id_empleado,e):
        return self.ejecutar('UPDATE empleados SET nombre=:nombre,direccion=:direccion,telefono=:telefono,correo=:correo,fecha_contrato=:fecha_contrato,salario=:salario,id_departamento=:id_departamento WHERE id_empleado=:id_empleado',dict(vars(e),id_empleado=id_empleado))
    def borrar_empleado(self,id_empleado): return self.ejecutar('DELETE FROM empleados WHERE id_empleado=:id',{'id':id_empleado})
    def proyectos(self): return self.consultar('SELECT id_proyecto,nombre,estado,pais,moneda FROM proyectos ORDER BY id_proyecto')
    def crear_proyecto(self,p):
        return self.insertar('INSERT INTO proyectos(nombre,descripcion,fecha_inicio,estado,pais,moneda) VALUES(:nombre,:descripcion,:fecha_inicio,:estado,:pais,:moneda)',vars(p),'id_proyecto')
    def actualizar_proyecto(self,id_proyecto,p):
        return self.ejecutar('UPDATE proyectos SET nombre=:nombre,descripcion=:descripcion,fecha_inicio=:fecha_inicio,estado=:estado,pais=:pais,moneda=:moneda WHERE id_proyecto=:id_proyecto',dict(vars(p),id_proyecto=id_proyecto))
    def borrar_proyecto(self,id_proyecto): return self.ejecutar('DELETE FROM proyectos WHERE id_proyecto=:id',{'id':id_proyecto})
    def asignar(self,empleado,proyecto): return self.ejecutar('INSERT INTO asignaciones(id_empleado,id_proyecto) VALUES(:e,:p)',{'e':empleado,'p':proyecto})
    def desasignar(self,empleado,proyecto): return self.ejecutar('DELETE FROM asignaciones WHERE id_empleado=:e AND id_proyecto=:p',{'e':empleado,'p':proyecto})
    def asignaciones(self): return self.consultar('SELECT id_empleado,id_proyecto FROM asignaciones ORDER BY id_proyecto,id_empleado')
    def registrar_horas(self,r): return self.insertar('INSERT INTO registros_tiempo(id_empleado,id_proyecto,fecha,horas,descripcion) VALUES(:id_empleado,:id_proyecto,:fecha,:horas,:descripcion)',vars(r),'id_registro')
    def reporte_horas(self): return self.consultar('SELECT e.nombre,p.nombre,SUM(r.horas) FROM registros_tiempo r JOIN empleados e ON e.id_empleado=r.id_empleado JOIN proyectos p ON p.id_proyecto=r.id_proyecto GROUP BY e.nombre,p.nombre ORDER BY p.nombre,e.nombre')
