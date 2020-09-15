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

from flask import Blueprint, render_template
from flask_login import login_required
from cacao_accounting.modulos import registrar_modulo


nombre_modulo = "fixedassets"
blueprint = Blueprint("activofijo", __name__, template_folder="templates")
info = {
    "modulo": nombre_modulo,
    "estandar": False,
    "habilitado": False,
}
url = "activofijo.activo_fijo"
nombre = "Activo Fijo"


@blueprint.cli.command("registrar-modulo")
def registrar_modulo_activofijo():
    """
    Registra el modulo en la aplicacion principal.
    """
    from cacao_accounting_modulo_activofijo.db import db

    registrar_modulo(info)
    db.create_all()


@blueprint.route("/activofijo")
@blueprint.route("/fixedassets")
@login_required
def activo_fijo():
    return render_template("activofijo.html")


@blueprint.route("/fixedassets/families")
@login_required
def lista_familias():
    return render_template("lists/familia.html")


@blueprint.route("/fixedassets/locations")
@login_required
def lista_ubicaciones():
    return render_template("lists/ubicacion.html")


@blueprint.route("/fixedassets/assets")
@login_required
def lista_activos():
    return render_template("lists/registro.html")


@blueprint.route("/fixedassets/newfamily")
@login_required
def nueva_familia():
    from cacao_accounting_modulo_activofijo.forms import FamiliaActivoFijo

    form = FamiliaActivoFijo()
    return render_template("forms/familia.html", form=form)


@blueprint.route("/fixedassets/newlocation")
@login_required
def nueva_ubicacion():
    from cacao_accounting_modulo_activofijo.forms import UbicacionActivoFijo

    form = UbicacionActivoFijo()
    return render_template("forms/ubicacion.html", form=form)


@blueprint.route("/fixedassets/newasset")
@login_required
def nuevo_activo():
    from cacao_accounting_modulo_activofijo.forms import ActivoFijo

    form = ActivoFijo()
    return render_template("forms/registro.html", form=form)
