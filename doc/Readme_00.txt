Contacto : Zuny 
		  Alejandro Bareiro 3371
---------------------------------

Se solicita un proceso automatizado para importar los datos de los extractos bancarios de manera a verlos reflejados en el sistema de la Municipalidad.
Los extractos bancarios son remitidos a la Municipalidad de Asunción en formato de planilla electrónica EXCEL. Cada banco utiliza su propio formato por
lo que se debe tener eso en cuenta al momento de elaborar un proceso para importar dichos datos. Según relevamiento realizado con la responsable Zuny
los bancos con mayor movimiento son:
1 Banco Continental
2 Bancard
3 BBVA

De no existir la posibilidad de unificar los formatos de los extratos bancarios recibidos se optaría por un proceso separado para cada Banco manteniendo
como prioridad el orden previamente descrito en función del volumen de transacciones.

Se debe determinar el programa o los programas utilizados actualmente para la carga del extracto bancario de manera a identificar cuáles son los datos
relevantes para el sistema actual. 

Se verificó el formato de los archivos de planillas electrónicas de los tres bancos ya citados y los mismos no se corresponden en lo referente a la organización
y estructuración de los datos contenidos, si bien poseen datos en común, los mismos están dispuestos en diferente orden para cada planilla electrónica de cada
banco.







Yendo por la opción PHP EXCEL

	Busqueda
		https://packagist.org/?query=Import Excel

	Documentación de libraría para manejo de EXCEL desde PHP:
		https://github.com/PHPOffice/PhpSpreadsheet

	Symfony Excel a DB
		https://ghaidabouchala.medium.com/import-excel-data-in-the-database-symfony-back-end-e14efea51cd2
		bundle https://portphp.readthedocs.io/en/latest/readers/

	Ejemplo en PHP
		https://parzibyte.me/blog/2019/02/20/importar-datos-excel-mysql-phpspreadsheet-pdo-php/#Demostracion_importar_desde_Excel_a_MySQL

	API REST
		https://www.itdo.com/blog/primeros-pasos-con-symfony-5-como-api-rest/
		Codigo del ejemplo anterior
			https://github.com/itdoh/Symfony5-API-REST.git 

		Otro Ejemplo
			https://github.com/Cap-Coding/symfony_api/