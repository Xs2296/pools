/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50717
Source Host           : localhost:3306
Source Database       : pools

Target Server Type    : MYSQL
Target Server Version : 50717
File Encoding         : 65001

Date: 2018-11-29 08:44:52
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for proxys
-- ----------------------------
DROP TABLE IF EXISTS `proxys`;
CREATE TABLE `proxys` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `host` varchar(100) NOT NULL,
  `port` varchar(10) NOT NULL,
  `http` varchar(10) NOT NULL,
  `anonymity` varchar(100) NOT NULL,
  `speed` varchar(10) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `sources` varchar(100) NOT NULL,
  `status` float NOT NULL,
  `check_time` datetime DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
