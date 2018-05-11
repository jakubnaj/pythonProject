-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: adwisedb
-- ------------------------------------------------------
-- Server version	5.7.20-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `advices`
--

DROP TABLE IF EXISTS `advices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `advices` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(150) NOT NULL,
  `shortDescription` varchar(150) NOT NULL,
  `categoryName` varchar(50) NOT NULL,
  `authorName` varchar(50) NOT NULL,
  `createDate` varchar(100) NOT NULL,
  `viewsQuantity` int(11) DEFAULT NULL,
  `commentsQuantity` int(11) DEFAULT NULL,
  `body` text,
  `tags` mediumtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `advices`
--

LOCK TABLES `advices` WRITE;
/*!40000 ALTER TABLE `advices` DISABLE KEYS */;
INSERT INTO `advices` VALUES (29,'Telewizor LG czy SAMSUNG','LG vs SAMSUNG ktory polecacie','Turystyka','janek','2018-04-27 15:52:44.612743',74,3,'Witam stoje przed decyzja kupna telewizora prosze o rade ',NULL),(30,'Wakacje Egipt czy Turcja','Hej gdzie na wakacje w 2018 roku polecacie','Turystyka','janek','2018-04-27 16:01:11.021934',19,2,'jak w opisie',NULL),(31,'Angular czy react','Witam zaczynam nowy duzy projekt ktore polecacie','informatyka','bartek','2018-04-27 16:02:54.023232',7,1,'Witam zaczynam nowy duzy projekt ktore polecacie',NULL),(32,'Podejrzewam meza o zdrade','od kilku dni sie dziwnie zachowuje.....','inne','beata','2018-04-27 16:04:14.844616',3,1,'Od kilku dni sie dziwnie zachowuje, biega rozwcieczony po domu i ciagle karze sobie gotowac bigos. Co poradzicie?',NULL),(33,'testk','krotki opisd','Turystyka','piekarz007','2018-05-06 12:37:50.153309',0,0,'Zdam czy nie zddam',NULL),(34,'testk','krotki opisd','Turystyka','piekarz007','2018-05-06 12:40:40.483385',163,10,'Zdam czy nie zddam','turystyka,sport,turcja,wczasy\r\n'),(35,'Turcja wakacje','Czy kierunek Turcja 2018 to dobry wybor?','Turystyka','beata','2018-05-07 19:17:22.549412',79,11,'Wybieram sie na wakacje do Turcji prosze o opinie ','jedzenie,atmosfera,bezpieczenstwo,pogoda,plaza');
/*!40000 ALTER TABLE `advices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categories` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Id`),
  UNIQUE KEY `Id_UNIQUE` (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (1,'podroze'),(12,'sport'),(15,'Turystyka'),(16,'eletronika'),(17,'informatyka'),(18,'inne');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `iD` int(11) NOT NULL AUTO_INCREMENT,
  `adviceID` int(11) NOT NULL,
  `authorName` varchar(50) NOT NULL,
  `createDate` varchar(50) DEFAULT NULL,
  `content` varchar(100) DEFAULT NULL,
  `likesQuantity` int(11) DEFAULT NULL,
  PRIMARY KEY (`iD`),
  UNIQUE KEY `ID_UNIQUE` (`iD`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (30,29,'janek','2018-04-27 16:00:16.283355','mam od 3 lat samusnga X5 i sprawdza sie super polecam',11),(31,29,'beata','2018-04-27 16:04:41.898831','ja mam jeszcze ten stary taki z tylem duzym i chodzi ale chyba marka inna',-2),(32,31,'beata','2018-04-27 16:07:33.031329','tylko angular !',0),(33,30,'bartek','2018-04-27 16:08:37.035986','bylam w zeszlym roku w turcji jedzenie pyszne hotel super tanio!!!',0),(34,32,'bartek','2018-04-27 16:09:07.678422','o moj boze....',0),(35,30,'beata','2018-04-27 16:09:42.494512','mozna umrzec',0),(36,29,'beata','2018-05-06 12:10:25.623373','bardzo polecam super kontrast',-1),(37,34,'beata','2018-05-06 14:45:58.476319','zdam',1),(38,34,'beata','2018-05-06 14:46:11.148602','nie',-1),(39,34,'beata','2018-05-06 15:03:06.739643','turystyka ',1),(40,34,'beata','2018-05-06 15:03:13.426973','turystyka ',1),(41,34,'beata','2018-05-06 15:03:21.411851','wczasy',-2),(42,34,'beata','2018-05-06 15:16:05.792833','turcja',1),(43,34,'beata','2018-05-06 15:37:24.559409','wczasy',-1),(44,34,'beata','2018-05-06 15:39:19.729219','sport',-1),(45,34,'beata','2018-05-06 15:39:53.240337','sport',1),(46,34,'beata','2018-05-06 15:56:48.694929','uwazam ze sport jest zly',-1),(47,35,'beata','2018-05-07 19:18:26.712285','Bylam w tamtym roku i jedzenie , atmosfera na duzy plus!',8),(48,35,'beata','2018-05-07 19:18:53.156364','Niestety ludzie z karabinami chodza na ulicy takze bezpieczenstwo na minus',-2),(49,35,'beata','2018-05-07 19:36:01.059743','Ja akurat jedzenie na Minus',-5),(50,35,'beata','2018-05-07 19:41:20.385523','Jedzenie jak najbardziej na plus!',1),(51,35,'beata','2018-05-07 19:41:48.178161','jedzenie jak najbardziej na plus',1),(52,35,'beata','2018-05-07 19:45:15.089637','jedzenie , atmosfera , pogada ',1),(53,35,'beata','2018-05-07 19:45:42.716080','pogoda plaza',1),(54,35,'beata','2018-05-07 19:46:58.628927','pogoda plaza',-1),(55,35,'beata','2018-05-07 19:47:32.691415','jedzenie',-1),(56,35,'beata','2018-05-07 19:47:50.280643','jedzenie jedzenie jedzenie',-1),(57,35,'beata','2018-05-07 19:48:02.901780','jedzenie',-1);
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tags`
--

DROP TABLE IF EXISTS `tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tags` (
  `name` varchar(45) NOT NULL,
  `adviceID` int(11) NOT NULL,
  `like` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tags`
--

LOCK TABLES `tags` WRITE;
/*!40000 ALTER TABLE `tags` DISABLE KEYS */;
/*!40000 ALTER TABLE `tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `UserId` int(11) NOT NULL AUTO_INCREMENT,
  `UserName` varchar(100) NOT NULL,
  `UserEmail` varchar(100) NOT NULL,
  `UserPassword` varchar(100) NOT NULL,
  PRIMARY KEY (`UserId`),
  UNIQUE KEY `id_users_UNIQUE` (`UserId`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'piekarz007','jakubnaj@gmail.com','najgebauer2'),(7,'tokassssssassrzS','wwwSssw@wp.pl','dupassS'),(10,'toksasssssssassrzS','tomaszek@wp.pl','dupssassS'),(11,'admin','admin@wp.pl','admin'),(12,'asdasd','admssssin@wp.pl','adminasdasd'),(13,'asdasddd','admdssssin@wp.pl','adminasdaddsd'),(15,'asdadsdfdd','addmdssdssin@wp.pl','adminadsdaddsd'),(16,'asdadssddd','admdsssdssin@wp.pl','adminsadsdaddsd'),(17,'piekarz0007','kkkkk@wp.pl','najgebauer'),(18,'adasdasdas','piekarz007','najgebauer'),(19,'Jakub Najgebauer','asdasdadsdas@wp.pl','najgebauer'),(20,'asdadsa ads das','piekarz007s','asdasd'),(21,'sdfsdfdsf','sdfsdffd','asdasd'),(22,'','',''),(23,'asdasdasd','asdasdas','asdasd'),(24,'piekarz007s','asdasda@wp.pl','asdasd'),(25,'jareczek','wp@wp.pl','jareczek'),(26,'martynka','martynka@wp.pl','martynka'),(27,'janek','krowa@wp.pl','janek'),(28,'bartek','wwww@wp.pl','bartek'),(29,'beata','beata@wp.pl','beata');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'adwisedb'
--
/*!50003 DROP PROCEDURE IF EXISTS `spChangePassword` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `spChangePassword`(
IN p_UserId INT(50),
IN p_OldPassword varchar(100),
IN p_NewPassword varchar(100)
)
BEGIN
IF ( select NOT exists (select 1 from users where UserId = p_UserId) ) THEN

    select 'User not exists.';

ELSEIF ( select NOT exists (select 1 from users where UserId = p_UserId AND UserPassword = p_OldPassword) ) THEN

    select 'Incorrect old password.';

ELSE 
BEGIN
UPDATE users SET UserPassword = p_NewPassword
WHERE UserId = p_UserId;
END;
END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `spCreateAdvice` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `spCreateAdvice`(
IN p_adviceTitle varchar(150),
IN p_adviceShortDescription varchar(150),
IN p_adviceCategoryName varchar(50),
IN p_adviceAuthorName varchar(50),
IN p_adviceCreateDate varchar(100),
IN p_adviceBody TEXT,
IN p_adviceTags TEXT
)
BEGIN
IF ( select NOT exists (select 1 from users where UserName = p_adviceAuthorName) ) THEN

    select 'Author not exists.';

ELSE 
BEGIN
insert into advices
(
    Title,
    ShortDescription,
    CategoryName,
    AuthorName,
    CreateDate,
    ViewsQuantity,
    CommentsQuantity,
    Body,
    Tags
    
)
values
(
    p_adviceTitle,
    p_adviceShortDescription,
    p_adviceCategoryName,
    p_adviceAuthorName,
    p_adviceCreateDate,
    0,
    0,
    p_adviceBody,
    p_adviceTags
);
END;
END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `spCreateComment` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `spCreateComment`(
IN p_adviceID INT,
IN p_authorName VARCHAR(50),
IN p_createDate VARCHAR(50),
IN p_content VARCHAR(100),
IN p_likesQuantity INT
)
BEGIN
IF ( select NOT exists (select 1 from users where UserName = p_authorName) ) THEN

    select 'Author not exists.';

ELSEIF ( select NOT exists (select 1 from advices where Id = p_adviceID) ) THEN

    select 'Advice not exists.';
ELSE
BEGIN
insert into comments
(
    AdviceID,
    AuthorName,
    CreateDate,
    Content,
    LikesQuantity
)
values
(
    p_adviceID,
    p_authorName,
    p_createDate,
    p_content,
    p_likesQuantity
);

END;
END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `spCreateUser` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `spCreateUser`(
IN p_Username varchar(100),
IN p_Email varchar(100),
IN p_Password varchar(100)
)
BEGIN
IF ( select exists (select 1 from users where UserName = p_Username) ) THEN

    select 'Username Exists !!';

ELSEIF ( select exists (select 1 from users where UserEmail = p_Email) ) THEN

    select 'Email Exists !!';

ELSE 
BEGIN
insert into users
(
    UserName,
    UserEmail,
    UserPassword
)
values
(
    p_Username,
    p_Email,
    p_Password
);
END;
END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `spDeleteUser` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'NO_BACKSLASH_ESCAPES' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `spDeleteUser`(
IN p_UserId int(20))
BEGIN
IF ( select exists (select 1 from users where UserId = p_UserId) ) THEN
    DELETE FROM users WHERE UserId = p_UserId;
ELSE 
	SELECT 'User not exist';
END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-05-11 20:31:18
