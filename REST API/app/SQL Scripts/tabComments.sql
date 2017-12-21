CREATE TABLE `adwisedb`.`comments` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `AdviceID` INT NOT NULL,
  `AuthorID` INT NOT NULL,
  `CreateDate` VARCHAR(50) NULL,
  `Content` VARCHAR(100) NULL,
  `LikesQuantity` INT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE INDEX `ID_UNIQUE` (`ID` ASC));