-- MySQL dump 10.13  Distrib 8.0.27, for Linux (x86_64)
--
-- Host: localhost    Database: t27_unidad_z
-- ------------------------------------------------------
-- Server version	8.0.27-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `a_material`
--

DROP TABLE IF EXISTS `a_material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `a_material` (
  `id` int NOT NULL,
  `Collecting_Materials` varchar(40) NOT NULL,
  `Potterry` int DEFAULT NULL,
  `Lytic_Chipped_Stone` int NOT NULL,
  `Lytic_Ground_Stone` int NOT NULL,
  `Bone` int NOT NULL,
  `Malacate` int NOT NULL,
  `Figurilla` int NOT NULL,
  `Other` varchar(40) NOT NULL,
  `Macrobot` varchar(40) NOT NULL,
  `Carbon_14` varchar(40) NOT NULL,
  `Flotation` int NOT NULL,
  `Soil` varchar(40) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `a_material_ibfk_1` FOREIGN KEY (`id`) REFERENCES `stratigraphy` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `a_material`
--

LOCK TABLES `a_material` WRITE;
/*!40000 ALTER TABLE `a_material` DISABLE KEYS */;
INSERT INTO `a_material` VALUES (1,'0',0,0,0,0,0,0,'0','0','0',0,'0'),(2,'100',1,1,0,0,0,0,'0','0','0',0,'0'),(3,'0',0,0,0,0,0,0,'0','0','0',0,'0'),(4,'0',0,0,0,0,0,0,'0','0','0',0,'0'),(5,'100',1,0,0,0,0,0,'0','0','0',0,'0'),(6,'0',0,0,0,0,0,0,'0','0','0',0,'0'),(7,'0',0,0,0,0,0,0,'0','0','0',0,'0'),(8,'100',1,0,0,0,0,0,'0','0','0',0,'0'),(9,'0',0,0,0,0,0,0,'0','0','0',0,'0'),(10,'0',0,0,0,0,0,0,'0','0','0',0,'0'),(11,'100_sin material',0,0,0,0,0,0,'0','0','0',0,'0'),(12,'0',0,0,0,0,0,0,'0','0','0',0,'0'),(13,'100_sin material',0,0,0,0,0,0,'0','0','0',0,'0'),(14,'100_sin material',0,0,0,0,0,0,'0','0','0',0,'0'),(15,'100_sin material',0,0,0,0,0,0,'0','0','0',0,'0'),(16,'0',0,0,0,0,0,0,'0','0','0',0,'0'),(17,'100_sin material',0,0,0,0,0,0,'0','0','0',0,'0');
/*!40000 ALTER TABLE `a_material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elevation_cmbd`
--

DROP TABLE IF EXISTS `elevation_cmbd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `elevation_cmbd` (
  `id` int NOT NULL,
  `Center_top` int NOT NULL,
  `NW_corner_top` int NOT NULL,
  `NE_corner_top` int NOT NULL,
  `SE_corner_top` int NOT NULL,
  `SW_corner_top` int NOT NULL,
  `Center_bottom` int NOT NULL,
  `NW_corner_bottom` int NOT NULL,
  `NE_corner_bottom` int NOT NULL,
  `SE_corner_bottom` int NOT NULL,
  `SW_corner_bottom` int NOT NULL,
  `Center_difference` int NOT NULL,
  `NW_corner_difference` int NOT NULL,
  `NE_corner_difference` int NOT NULL,
  `SE_corner_difference` int NOT NULL,
  `SW_corner_difference` int NOT NULL,
  `Average` varchar(5) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `elevation_cmbd_ibfk_1` FOREIGN KEY (`id`) REFERENCES `excavation_c` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elevation_cmbd`
--

LOCK TABLES `elevation_cmbd` WRITE;
/*!40000 ALTER TABLE `elevation_cmbd` DISABLE KEYS */;
INSERT INTO `elevation_cmbd` VALUES (1,186,189,199,190,195,217,217,223,223,216,31,28,24,33,21,'27.4'),(2,217,217,223,223,216,233,232,232,235,233,16,15,9,12,17,'13.8'),(3,193,172,190,199,187,211,202,209,220,214,18,30,19,21,27,'23'),(4,183,172,181,190,180,206,195,206,214,205,23,23,25,24,25,'24'),(5,206,195,206,214,205,214,209,216,220,217,8,14,10,6,12,'10'),(6,176,161,171,181,172,195,182,194,203,193,19,21,23,22,21,'21.2'),(7,161,147,165,172,160,191,173,191,200,188,30,26,26,28,28,'27.6'),(8,191,173,191,198,188,197,186,197,200,190,6,13,6,2,2,'5.8'),(9,156,145,159,165,149,174,163,179,183,165,18,18,20,18,16,'18'),(10,137,123,134,149,143,152,135,146,166,154,15,12,12,17,11,'13.4'),(11,152,135,146,166,154,163,152,162,174,161,11,17,16,8,7,'11.8'),(12,199,192,203,201,198,214,207,218,221,215,15,15,15,20,17,'16.4'),(13,214,207,218,221,215,222,211,219,225,218,8,4,1,4,3,'4'),(14,222,211,219,225,218,244,236,236,245,243,22,25,17,20,25,'21.8'),(15,244,236,236,245,0,270,258,268,270,270,26,22,32,25,27,'26'),(16,226,220,232,232,226,245,238,254,249,243,19,18,22,17,17,'19'),(17,245,238,254,249,243,261,258,263,261,256,16,20,9,12,13,'14');
/*!40000 ALTER TABLE `elevation_cmbd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `excavation_c`
--

DROP TABLE IF EXISTS `excavation_c`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `excavation_c` (
  `id` int NOT NULL,
  `Area` varchar(10) NOT NULL,
  `Unit` varchar(10) NOT NULL,
  `Quad` varchar(10) NOT NULL,
  `Lot` int NOT NULL,
  `Position_on_the_terrace` varchar(40) NOT NULL,
  `Position_in_the_excavation_of_the_quad` varchar(40) NOT NULL,
  `Excavated_portion_of_the_quad` varchar(40) NOT NULL,
  `Architectur_al_position` varchar(40) DEFAULT NULL,
  `Feature_No` int DEFAULT NULL,
  `Structure_No` int DEFAULT NULL,
  `Burial_No` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `lote` (`Lot`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `excavation_c`
--

LOCK TABLES `excavation_c` WRITE;
/*!40000 ALTER TABLE `excavation_c` DISABLE KEYS */;
INSERT INTO `excavation_c` VALUES (1,'EFT27','Z','X16Y12',1,'sur','cala longitudinal_limite sur','completo','',0,0,0),(2,'EFT27','Z','X16Y12',7,'sur','cala longitudinal_limite sur','completo','',0,0,0),(3,'EFT27','Z','X16Y16',2,'sur','cala longitudinal_tramo sur','completo','',0,0,0),(4,'EFT27','Z','X16Y20',3,'sur','cala longitudinal_tramo sur','completo','',0,0,0),(5,'EFT27','Z','X16Y20',9,'sur','cala longitudinal_tramo sur','completo','',0,0,0),(6,'EFT27','Z','X16Y24',4,'sur','cala longitudinal_tramo central','completo','',0,0,0),(7,'EFT27','Z','X16Y28',5,'sur','cala longitudinal-tramo norte','completo','',0,0,0),(8,'EFT27','Z','X16Y28',11,'sur','cala longitudinal-tramo norte','completo','',0,0,0),(9,'EFT27','Z','X16Y32',6,'sur','cala longitudinal-límite norte','completo','',0,0,0),(10,'EFT27','Z','X10Y24',22,'suroeste','cala transversal_límite oeste','completo','',0,0,0),(11,'EFT27','Z','X10Y24',23,'suroeste','cala transversal_límite oeste','completo','',0,0,0),(12,'EFT27','Z','X22Y24',19,'sureste','cala transversal_tramo este','completo','',0,0,0),(13,'EFT27','Z','X22Y24',20,'sureste','cala transversal_tramo este','completo','',0,0,0),(14,'EFT27','Z','X22Y24',21,'sureste','cala transversal_tramo este','completo','',0,0,0),(15,'EFT27','Z','X22Y24',28,'sureste','cala transversal_tramo este','completo','',0,0,0),(16,'EFT27','Z','X28Y24',25,'sureste','cala transversal_límite este','completo','',0,0,0),(17,'EFT27','Z','X28Y24',26,'sureste','cala transversal_límite este','completo','',0,0,0);
/*!40000 ALTER TABLE `excavation_c` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registry`
--

DROP TABLE IF EXISTS `registry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registry` (
  `id` int NOT NULL,
  `N_Camera` int NOT NULL,
  `Comments` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `registry_ibfk_1` FOREIGN KEY (`id`) REFERENCES `a_material` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registry`
--

LOCK TABLES `registry` WRITE;
/*!40000 ALTER TABLE `registry` DISABLE KEYS */;
INSERT INTO `registry` VALUES (1,4,'Sin Comentario'),(2,4,'Sin comentario'),(3,4,'Sin comentario'),(4,4,'Sin comentario'),(5,4,'Sin comentario'),(6,4,'Sin comentario'),(7,4,'Sin comentario'),(8,4,'Sin comentario'),(9,4,'Sin comentario'),(10,4,'Sin comentario'),(11,4,'Sin comentario'),(12,4,'Sin comentario'),(13,4,'Sin comentario'),(14,4,'Sin comentario'),(15,4,'Sin comentario'),(16,4,'Sin comentario'),(17,4,'Sin comentario');
/*!40000 ALTER TABLE `registry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `soil`
--

DROP TABLE IF EXISTS `soil`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `soil` (
  `id` int NOT NULL,
  `Soil_Texture` varchar(40) NOT NULL,
  `Soil_color_at_the_moment_of_detachment` varchar(10) NOT NULL,
  `Wet_Soil_Color` varchar(10) NOT NULL,
  `Soil_density` varchar(20) NOT NULL,
  `Humidity` varchar(40) NOT NULL,
  `Soil_volume` int NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `soil_ibfk_1` FOREIGN KEY (`id`) REFERENCES `elevation_cmbd` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `soil`
--

LOCK TABLES `soil` WRITE;
/*!40000 ALTER TABLE `soil` DISABLE KEYS */;
INSERT INTO `soil` VALUES (1,'arcillo-arenosa','10YR3/3','10YR3/3','moderada','húmeda',2580),(2,'arcillo-limosa','10YR3/4','10YR3/4','moderada','húmeda',2500),(3,'arcillo-arenosa','10YR3/3','10YR3/3','moderada','húmeda',2240),(4,'arcillo-arenosa','10YR3/3','10YR3/3','moderada','húmeda',2580),(5,'arcillo-limosa','10YR3/4','10YR3/4','moderada','húmeda',2180),(6,'arcillo-arenosa','10YR3/3','10YR3/3','moderada','húmeda',2340),(7,'arcillo-arenosa','10YR3/3','10YR3/3','moderada','húmeda',2400),(8,'arcillo-limosa','10YR3/4','10YR3/4','compacta','húmeda',1500),(9,'arcillo-arenosa','10YR3/3','10YR3/3','moderada','húmeda',2440),(10,'arcillo-arenosa','10YR3/3','10YR3/3','moderada','húmeda',2120),(11,'arcillo-limosa','10YR3/4','10YR3/4','moderada','húmeda',1300),(12,'arcillo-arenosa','10YR3/3','10YR3/3','moderada','húmeda',1900),(13,'arcillo-limosa-arenosa','10YR3/4','10YR3/4','moderada','húmeda',680),(14,'arcillo-limosa','10YR3/6','10YR3/4','compacta','húmeda',4040),(15,'arcillo-limosa','10YR3/6','10YR3/4','compacta','húmeda',3140),(16,'arcillo-arenosa','10YR3/3','10YR3/3','moderada','húmeda',2940),(17,'arcillo-arenosa','10YR3/4','10YR3/4','moderada','húmeda',1980);
/*!40000 ALTER TABLE `soil` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stratigraphy`
--

DROP TABLE IF EXISTS `stratigraphy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stratigraphy` (
  `id` int NOT NULL,
  `Deposit_type` varchar(40) NOT NULL,
  `Soil_type` varchar(40) NOT NULL,
  `Lots_above` varchar(20) NOT NULL,
  `Lots_below` int NOT NULL,
  `Lots_next_to` int NOT NULL,
  `Lots_from_the_same_deposit` varchar(40) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `stratigraphy_ibfk_1` FOREIGN KEY (`id`) REFERENCES `soil` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stratigraphy`
--

LOCK TABLES `stratigraphy` WRITE;
/*!40000 ALTER TABLE `stratigraphy` DISABLE KEYS */;
INSERT INTO `stratigraphy` VALUES (1,'Superficie','suelo marrón -SM-','-SM-',7,0,'2, 3, 4, 5, 6'),(2,'Nivel Transicional','suelo marrón mezclado -SMM-','1',0,0,'9, 11'),(3,'Superficie','suelo marrón -SM-','-SM-',0,0,'1, 3, 4, 5, 6'),(4,'Superficie','suelo marrón -SM-','-SM-',9,0,'1, 2, 4, 5, 6'),(5,'Nivel Transicional','suelo marrón mezclado -SMM-','3',0,0,'7, 11'),(6,'Superficie','suelo marrón -SM-','-SM-',0,0,'1, 2, 3, 5, 6'),(7,'Superficie','suelo marrón -SM-','-SM-',11,0,'1, 2, 2, 4, 6'),(8,'Nivel Transicional','suelo marrón mezclado -SMM-','5',0,0,'7, 9'),(9,'Superficie','suelo marrón -SM-','-SM-',0,0,'1, 2, 3, 4, 5'),(10,'Superficie','suelo marrón -SM-','-SM-',23,0,'19, 25'),(11,'Nivel Transicional','suelo marrón mezclado -SMM-','22',0,0,'20, 26'),(12,'Superficie','suelo marrón -SM-','-SM-',20,0,'22, 25'),(13,'Nivel Transicional','suelo marrón mezclado -SMM-','19',21,0,'23, 26'),(14,'Suelo Amarillo','suelo amarillo -SA-','20',28,0,'0'),(15,'Suelo Amarillo Nivel 2','suelo amarillo nivel 2 -SAN2-','21',0,0,'0'),(16,'Superficie','suelo marrón -SM-','-SM-',26,0,'19, 22'),(17,'Nivel Transicional','suelo marrón mezclado -SMM-','25',0,0,'20, 23');
/*!40000 ALTER TABLE `stratigraphy` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-14 23:34:51
