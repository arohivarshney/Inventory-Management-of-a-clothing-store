-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: myclothingdatabase
-- ------------------------------------------------------
-- Server version	8.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory` (
  `ProductCode` int NOT NULL,
  `SubProductCode` int NOT NULL,
  `ProductCategory` varchar(45) NOT NULL,
  `Brand` varchar(45) NOT NULL,
  `Color` varchar(255) DEFAULT NULL,
  `Size` varchar(255) DEFAULT NULL,
  `Quantity` int NOT NULL,
  `cart` int DEFAULT '0',
  PRIMARY KEY (`ProductCode`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES (0,0,'','',NULL,NULL,0,NULL),(1001,1,'Oversized Shirt','Levis','Pink','Small',1,1),(1002,1,'Oversized Shirt','Levis','Pink','Medium',12,0),(1003,2,'Fine Knit Cardigan','Zara','Grey','Small',8,0),(1004,2,'Fine Knit Cardigan','Zara','Black','Medium',10,0),(1005,2,'Fine Knit Cardigan','Zara','Grey','Medium',15,0),(1006,2,'Fine Knit Cardigan','Zara','Grey','Large',1,0),(1007,3,'Sweatshirt','H&M','Blue','Small',5,1),(1008,3,'Sweatshirt','H&M','Blue','Medium',0,0),(1009,3,'Sweatshirt','H&M','Blue','Large',10,0),(1010,4,'Sweatshirt','H&M','Beige','Small',7,0),(1011,4,'Sweatshirt','H&M','Beige','Medium',3,1),(1012,4,'Sweatshirt','H&M','Beige','Large',3,0),(1013,5,'Denim shorts','Mango','Blue','Small',5,0),(1014,5,'Denim shorts','Mango','Blue','Medium',3,0),(1015,5,'Denim shorts','Mango','Blue','Large',2,0),(1016,6,'Blazer','Uniqlo','Grey','Small',1,0),(1017,6,'Blazer','Uniqlo','Grey','Large',3,0),(1018,7,'Trousers','Mango','Red','Small',2,0),(1019,8,'Trousers','Mango','Green','Large',1,0),(1020,9,'Flared Leggings','Zara','Black','Small',7,0),(1021,9,'Flared Leggings','Zara','Black','Medium',10,0),(1022,9,'Flared Leggings ','Zara','Black','Large',8,0),(1023,10,'White Shirt','H&M','White','Small',6,0),(1024,10,'White Shirt','H&M','White','Medium',3,0),(1025,10,'White Shirt','H&M','White','Large',1,0);
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'myclothingdatabase'
--

--
-- Dumping routines for database 'myclothingdatabase'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-08-30 21:28:53
