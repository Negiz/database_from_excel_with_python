CREATE DATABASE  IF NOT EXISTS `workers_and_departments` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `workers_and_departments`;
-- MySQL dump 10.13  Distrib 5.7.18, for Win32 (AMD64)
--
-- Host: 127.0.0.1    Database: workers_and_departments
-- ------------------------------------------------------
-- Server version	5.5.5-10.1.28-MariaDB

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
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `department` (
  `department_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(15) NOT NULL,
  `floor_number` int(2) NOT NULL,
  `location` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES (1,'Evil laboratory',66,'Tampere'),(2,'Dragon stone',2,'Joensuu'),(3,'Secret place',2,'Helsinki'),(4,'Alchemy lab',3,'Turku'),(5,'Magic Tower',45,'Korso'),(6,'Bullet of Doom',1,'Oulu'),(7,'Area 23',1,'Jyväskylä'),(8,'Candy land',1,'Kemi'),(9,'Työmaa',45,'Tornio'),(10,'Asd',33,'Utsjoki');
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee` (
  `employee_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(20) NOT NULL,
  `last_name` varchar(25) NOT NULL,
  `telephone` varchar(10) NOT NULL,
  `address` varchar(30) NOT NULL,
  `city` varchar(20) NOT NULL,
  `zip` int(5) NOT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,'Seppo','Taalasmaa','441303563','Pihlajakatu 4','Helsinki',40222),(2,'Ismo','Laitela','2048920','Pihlajakatu 3','Helsinki',40222),(3,'Aku','Ankka','24040204','Paratiisitie 13','Ankkalinna',23444),(4,'Mikki','Hiiri','412412444','Paratiisitie 2','Ankkalinna',23444),(5,'Möhkö','Fantti','412412412','Puolenhehtaarinmetsä','Hehtaari',24567),(6,'Seppo','Hovi','241242124','Tampereenkatu 6','Tampere',15678),(7,'Teppo','Tulppu','2414166','Parasiittitie 12','Ankkalinna',23444),(8,'Magic','Mike','353535','Universe 4','Blue Galaxy',55555),(9,'Dead','Man','646454','Kirkonhauta 2','Joensuu',63356),(10,'Osteri','Ossi','35325','Pihlajakatu 3','Helsinki',14553),(11,'Pallo','Masi','5236526','Monsterila 8','Kap Mörkö',45454),(12,'Ned','Flanders','35623525','Homerin naapuri 1','Oulu',36783),(13,'Bill','Cosby','346346346','Siperian katu 2','Utsjoki',99999);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `who_works_where`
--

DROP TABLE IF EXISTS `who_works_where`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `who_works_where` (
  `department_departmentid` int(11) NOT NULL,
  `employee_employeeid` int(11) NOT NULL,
  `worked_hours` int(4) DEFAULT NULL,
  PRIMARY KEY (`department_departmentid`,`employee_employeeid`),
  KEY `fk_who_works_where_department1_idx` (`department_departmentid`),
  KEY `fk_who_works_where_employee1_idx` (`employee_employeeid`),
  CONSTRAINT `fk_who_works_where_department1` FOREIGN KEY (`department_departmentid`) REFERENCES `department` (`department_id`),
  CONSTRAINT `fk_who_works_where_employee1` FOREIGN KEY (`employee_employeeid`) REFERENCES `employee` (`employee_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `who_works_where`
--

LOCK TABLES `who_works_where` WRITE;
/*!40000 ALTER TABLE `who_works_where` DISABLE KEYS */;
INSERT INTO `who_works_where` VALUES (1,2,10),(1,11,56),(2,3,20),(2,12,75),(3,3,45),(3,8,54),(4,2,22),(4,9,777),(5,4,566),(6,5,245),(7,6,277),(7,7,346),(8,13,33),(9,1,225),(9,10,24);
/*!40000 ALTER TABLE `who_works_where` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-06-03 19:55:56
