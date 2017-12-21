CREATE TABLE `adwisedb`.`advices` (
  `Id` INT NOT NULL AUTO_INCREMENT,
  `Title` VARCHAR(150) NOT NULL,
  `ShortDescription` VARCHAR(150) NOT NULL,
  `CategoryID` INT NOT NULL,
  `AuthorID` INT NOT NULL,
  `CreateDate` VARCHAR(100) NOT NULL,
  `ViewsQuantity` INT NULL,
  `CommentsQuantity` INT NULL,
  `body` TEXT(1000) NULL
  PRIMARY KEY (`Id`),
  UNIQUE INDEX `Id_UNIQUE` (`Id` ASC));