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


from cacao_accounting.database import db


class ActivoFijo(db.Model):
    """
    Define un activo fijo en la base de datos.
    """

    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    # Datos basicos
    descripcion = db.Column(db.String(250))
    codigo = db.Column(db.String(250))
    marca = db.Column(db.String(250))
    modelo = db.Column(db.String(250))
    serie = db.Column(db.String(250))
    # Vehiculos
    motor = db.Column(db.String(250))
    chasis = db.Column(db.String(250))
    placa = db.Column(db.String(50))
    # Costo Historico
    costo = db.Column(db.Float(precision=4, asdecimal=True))
    tasacambio = db.Column(db.Float(precision=4, asdecimal=True))
    costousd = db.Column(db.Float(precision=4, asdecimal=True))
    # Vida Util
    contable = db.Column(db.Integer(), nullable=True)
    fiscal = db.Column(db.Integer(), nullable=True)
    # Revaluos
    avaluo = db.Column(db.Float(precision=4, asdecimal=True))
    tasacambioavaluo = db.Column(db.Float(precision=4, asdecimal=True))
    avaluousd = db.Column(db.Float(precision=4, asdecimal=True))
    plazoavaluo = db.Column(db.Integer(), nullable=True)
