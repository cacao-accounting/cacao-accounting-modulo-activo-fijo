# Copyright 2020 William José Moreno Reyes
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Contributors:
# - William José Moreno Reyes


"""
Define las tablas utilizadas por el módulo de Activo Fijo.
"""

from cacao_accounting.database import db


class FamiliaActivoFijo(db.Model):
    __table_args__ = (db.UniqueConstraint("id", "nombre", name="faf_unica"),)
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    activa = db.Column(db.Boolean())
    nombre = db.Column(db.String(50))
    entidad = db.Column(db.String(10), db.ForeignKey("entidad.id"))
    grupo = db.Column(db.Boolean())
    padre = db.Column(db.String(50), db.ForeignKey("familia_activo_fijo.nombre"), nullable=True)
    cta_activo = db.Column(db.String(50), db.ForeignKey("cuentas.codigo"))
    vida_util = db.Column(db.Integer())
    vida_util_fiscal = db.Column(db.Integer())


class UbicacionActivoFijo(db.Model):
    __table_args__ = (db.UniqueConstraint("id", "nombre", name="uaf_unica"),)
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    activa = db.Column(db.Boolean())
    nombre = db.Column(db.String(50))
    entidad = db.Column(db.String(10), db.ForeignKey("entidad.id"))
    grupo = db.Column(db.Boolean())
    padre = db.Column(db.String(50), db.ForeignKey("ubicacion_activo_fijo.nombre"), nullable=True)
    cta_depreciacion = db.Column(db.String(50), db.ForeignKey("cuentas.codigo"))


class ActivoFijo(db.Model):
    __table_args__ = (db.UniqueConstraint("id", "nombre", name="af_unico"),)
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    alta = db.Column(db.Date())
    codigo = db.Column(db.String(150))
    agrupador = db.Column(db.Boolean())
    individual = db.Column(db.Boolean())
    padre = db.Column(db.String(50), db.ForeignKey("activo_fijo.nombre"))
    fisico = db.Column(db.Boolean())
    amortizable = db.Column(db.Boolean())
    nombre = db.Column(db.String(150), unique=True)
    marca = db.Column(db.String(150))
    modelo = db.Column(db.String(150))
    serie = db.Column(db.String(150))
    motor = db.Column(db.String(150))
    chasis = db.Column(db.String(150))
    placa = db.Column(db.String(150))
    registro = db.Column(db.String(150))
    familia = db.Column(db.String(50), db.ForeignKey("familia_activo_fijo.nombre"))
    ubicacion = db.Column(db.String(50), db.ForeignKey("ubicacion_activo_fijo.nombre"))
    moneda_principal = db.Column(db.String(5), db.ForeignKey("moneda.id"))
    costo = db.Column(db.Numeric())
    moneda_secundaria = db.Column(db.String(5), db.ForeignKey("moneda.id"))
