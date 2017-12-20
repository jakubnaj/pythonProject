CREATE TABLE `adwisedb`.`comments` (
  `ID` INT NOT NULL,
  `AdviceID` INT NOT NULL,
  `AuthorID` INT NOT NULL,
  `CreateDate` DATETIME NULL,
  `Content` VARCHAR(100) NULL,
  PRIMARY KEY (`ID`),
  UNIQUE INDEX `ID_UNIQUE` (`ID` ASC));