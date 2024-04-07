query_creacion_bbdd = "CREATE SCHEMA IF NOT EXISTS `Empresa_f`;"

query_tabla_producto = """CREATE TABLE IF NOT EXISTS `Empresa_f`.`productos` (
  `Id_producto` VARCHAR(45) NOT NULL,
  `Nombre_producto` VARCHAR(100) NOT NULL,
  `Categoría` VARCHAR(100) NOT NULL,
  `Precio` FLOAT NOT NULL,
  `Origen` VARCHAR(45) NOT NULL,
  `Descripcion` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`Id_producto`));"""

query_tabla_clientes = """CREATE TABLE IF NOT EXISTS `Empresa_f`.`clientes` (
  `Id_cliente` INT NOT NULL,
  `First_name` VARCHAR(100) NULL,
  `Last_name` VARCHAR(100) NULL,
  `Email` VARCHAR(100) NOT NULL,
  `Gender` VARCHAR(45) NOT NULL,
  `City` VARCHAR(100) NOT NULL,
  `Country` VARCHAR(45) NOT NULL,
  `Address` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`Id_cliente`));"""

query_insertar_producto = "INSERT INTO producto (Id_producto, Nombre_producto, Categoría, Precio, Origen, Descripcion) VALUES (%s, %s, %s, %s, %s, %s)"

query_insertar_clientes = "INSERT INTO clientes (Id_cliente, First_name, Last_name, Email, Gender, City, Country, Address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

