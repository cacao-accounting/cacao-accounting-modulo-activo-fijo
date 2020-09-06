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

from setuptools import setup
from os import path

aqui = path.abspath(path.dirname(__file__))
with open(path.join(aqui, "README.md"), encoding="utf-8") as f:
    descripcion = f.read()

setup(
    name="cacao_accounting_modulo_activofijo",
    version="0.0.1dev",
    author="William José Moreno Reyes",
    author_email="williamjmorenor@gmail.com",
    description="Modulo Activo Fijo",
    long_description=descripcion,
    long_description_content_type="text/markdown",
    packages=["cacao_accounting_activofijo"],
    include_package_data=True,
    install_requires=[
        "cacao-accounting",
    ],
)