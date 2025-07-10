.. w0sa documentation master file, created by
   sphinx-quickstart on Thu Jul  3 21:58:32 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Bienvenido/a a la documentación de w0sa!
========================================

¿Qué es **w0sa**?
-----------------

**w0sa** es un simulador (en desarrollo) *low-cost* que emula el comportamiento de un **Analizador de Espectro Óptico (OSA)** frente a configuraciones en un **Switch Selectivo de Longitud de Onda (WSS)**. Su propósito es permitir la visualización y análisis de espectros ópticos generados por un WSS sin necesidad de disponer físicamente de un OSA.

Un **Wavelength Selective Switch (WSS)** es un dispositivo que filtra y redirecciona señales ópticas en diferentes longitudes de onda, cumpliendo un rol esencial en sistemas de comunicaciones ópticas y cuánticas para multiplexar, enrutar o configurar canales de forma flexible. Por su parte, un **Optical Spectrum Analyzer (OSA)** permite visualizar la distribución de potencia de estas longitudes de onda, midiendo el espectro óptico de la señal. El WSS simulado es un *Finisar Flexgrid*, mientras que el OSA corresponde al funcionamiento general de OSAs comerciales.

Contexto y relevancia
---------------------

Este proyecto nace en la **Universidad del Bío-Bío (Concepción, Chile)** en el contexto del montaje de un laboratorio de comunicaciones ópticas y cuánticas. Allí, el WSS es un componente esencial para experimentos de coherencia, multiplexación y enrutamiento de señales. Sin embargo, adquirir un OSA real implica un costo económico muy elevado, con precios que pueden rondar los 40.000 USD `Thorlabs <https://www.thorlabs.com/newgrouppage9.cfm?objectgroup_id=5276>`_.

Ante este escenario, **w0sa** surge como solución práctica y *low-cost* que permite evitar trabajar a ciegas. Además, incluso si se dispone de un OSA real, **w0sa** permite realizar simulaciones y pruebas preliminares en entornos sin acceso directo al equipo físico, reduciendo tiempos de laboratorio y facilitando el aprendizaje.

Con **w0sa**, se eliminan barreras de acceso a equipamiento de alto costo, potenciando la formación práctica y la investigación aplicada en tecnologías ópticas y cuánticas.


.. toctree::
   :maxdepth: 2


Contenidos
----------

.. toctree::
   :maxdepth: 2
   
   installation
   getting_started
   technical_ref

