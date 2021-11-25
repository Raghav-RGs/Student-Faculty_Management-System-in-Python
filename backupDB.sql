-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.1.37-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win32
-- HeidiSQL Version:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for studentdb
CREATE DATABASE IF NOT EXISTS `studentdb` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `studentdb`;

-- Dumping structure for table studentdb.admin
CREATE TABLE IF NOT EXISTS `admin` (
  `Username` varchar(20) NOT NULL DEFAULT '',
  `Password` varchar(20) NOT NULL,
  PRIMARY KEY (`Username`),
  UNIQUE KEY `Password_UNIQUE` (`Password`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table studentdb.admin: ~6 rows (approximately)
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` (`Username`, `Password`) VALUES
	('', ''),
	('sanskar', '123456789'),
	('raju', '55555'),
	('Huzefa', 'Huzefa@1999'),
	('Raghav', 'Raghav@123'),
	('Rajesh', 'Rajesh123');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;

-- Dumping structure for table studentdb.faculty
CREATE TABLE IF NOT EXISTS `faculty` (
  `ID` varchar(12) NOT NULL,
  `F_name` varchar(12) NOT NULL,
  `L_name` varchar(12) NOT NULL,
  `Branch` varchar(5) NOT NULL,
  `Section` varchar(1) NOT NULL,
  `Subject` varchar(12) NOT NULL,
  `password` varchar(10) NOT NULL,
  `Semester` varchar(1) NOT NULL,
  `City` varchar(10) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `password_UNIQUE` (`password`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table studentdb.faculty: ~2 rows (approximately)
/*!40000 ALTER TABLE `faculty` DISABLE KEYS */;
INSERT INTO `faculty` (`ID`, `F_name`, `L_name`, `Branch`, `Section`, `Subject`, `password`, `Semester`, `City`) VALUES
	('0157F001', 'Deepak', 'Sonidhya', 'CSE', 'B', 'Physics', 'Deepak576', '6', 'Bhopal'),
	('0157F005', 'Safdar', 'Khan', 'CSE', 'B', 'DS', 'Safdar123', '5', 'Bhopal');
/*!40000 ALTER TABLE `faculty` ENABLE KEYS */;

-- Dumping structure for table studentdb.student
CREATE TABLE IF NOT EXISTS `student` (
  `ID` varchar(14) NOT NULL,
  `password` varchar(10) NOT NULL,
  `F_name` varchar(12) NOT NULL,
  `L_name` varchar(12) NOT NULL,
  `Branch` varchar(5) NOT NULL,
  `semester` varchar(3) NOT NULL,
  `Section` varchar(1) NOT NULL,
  `address` varchar(20) NOT NULL,
  `city` varchar(20) NOT NULL,
  `fees` varchar(6) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Attendance` int(3) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table studentdb.student: ~2 rows (approximately)
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` (`ID`, `password`, `F_name`, `L_name`, `Branch`, `semester`, `Section`, `address`, `city`, `fees`, `Email`, `Attendance`) VALUES
	('0157CS171124', 'Raghav123', 'Raghav', 'Patidar', 'CSE', '6', 'B', 'Anjad', 'Bhopal', 'paid', 'Raghav@gmail.com', 95),
	('0157CS171130', 'Raju123', 'Raju', 'Pandit', 'CSE', '6', 'B', 'Ayodhya Bypass', 'Bhopal', 'Paid', 'Rajupandit@gmail.com', 90);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
