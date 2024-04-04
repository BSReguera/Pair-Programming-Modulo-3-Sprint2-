-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Empresa_f
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Empresa_f
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Empresa_f` DEFAULT CHARACTER SET utf8 ;
USE `Empresa_f` ;

-- -----------------------------------------------------
-- Table `Empresa_f`.`clientes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Empresa_f`.`clientes` (
  `Id_cliente` INT NOT NULL,
  `First_name` VARCHAR(100) NULL,
  `Last_name` VARCHAR(100) NULL,
  `Email` VARCHAR(100) NOT NULL,
  `Gender` VARCHAR(45) NOT NULL,
  `City` VARCHAR(100) NOT NULL,
  `Country` VARCHAR(45) NOT NULL,
  `Address` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`Id_cliente`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Empresa_f`.`productos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Empresa_f`.`productos` (
  `Id_producto` VARCHAR(45) NOT NULL,
  `Nombre_producto` VARCHAR(100) NOT NULL,
  `Categoría` VARCHAR(100) NOT NULL,
  `Precio` FLOAT NOT NULL,
  `Origen` VARCHAR(45) NOT NULL,
  `Descripcion` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`Id_producto`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
