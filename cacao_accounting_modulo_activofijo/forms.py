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

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class FamiliaActivoFijo(FlaskForm):
    nombre = StringField("Familia Activo Fijo", validators=[DataRequired(), Length(max=50)])


class UbicacionActivoFijo(FlaskForm):
    nombre = StringField("Ubicación Activo Fijo", validators=[DataRequired(), Length(max=50)])


class ActivoFijo(FlaskForm):
    nombre = StringField("Activo Fijo", validators=[DataRequired(), Length(max=150)])
