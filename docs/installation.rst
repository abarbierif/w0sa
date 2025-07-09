Instalación
===========

.. important::

   Es necesario contar con ``python`` `<https://www.python.org/downloads/>`_ y ``git`` `<https://git-scm.com/downloads>`_ instalados.

Para usar **w0sa** primero clona el repositorio usando ``git`` e ingresa al directorio:

.. code-block:: console

   $ git clone https://github.com/abarbierif/w0sa.git
   $ cd w0sa

Crea y activa un entorno virtual con ``venv``:

En **Linux**:

.. code-block:: console

   $ python3 -m venv .venv
   $ source .venv/bin/activate

En **Windows** (PowerShell):

.. code-block:: console

   $ py -m venv .venv
   $ .\.venv\Scripts\Activate.ps1

Instala el paquete (modo editable) e inicia **w0sa**:

.. code-block:: console

   $ pip install -e .
   $ w0sa
