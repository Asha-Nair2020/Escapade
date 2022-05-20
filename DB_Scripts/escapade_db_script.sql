
CREATE DATABASE IF NOT EXISTS escapade;
USE escapade;

-- Table structure for table `escapade_users`
--

DROP TABLE IF EXISTS `escapade_users`;

CREATE TABLE `escapade_users` (
  `USER_ID` int NOT NULL AUTO_INCREMENT,
  `USER_NAME` varchar(100) NOT NULL,
  `EMAIL_ADDRESS` varchar(100) NOT NULL,
  `USER_PASSWORD` varchar(100) NOT NULL,
  PRIMARY KEY (`USER_ID`),
  UNIQUE KEY `USER_NAME_UNIQUE` (`USER_NAME`),
  UNIQUE KEY `EMAIL_ADDRESS_UNIQUE` (`EMAIL_ADDRESS`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `escapade_users` WRITE;

INSERT INTO `escapade_users` VALUES (1,'Asha','asha@email.com','abcdef'),(2,'Hodan','hodan@email.com','abcd'),(3,'Seynab','seynab@email.com','Seynab@1'),(4,'Zahra@3','zahra@email.com','Zahra@123'),(6,'John','john@email.com','ohn@345J'),(9,'Suad Ali','suad@hotmail.com','Suad@1234'),(10,'Diana','dia@email.com','dI@234'),(11,'Jason','jason@email.com','Jason@123'),(12,'John_001','john01@email.com','John@123'),(13,'Johan','johan@email.com','Johan@123'),(14,'Sheldon','sheldon@email.com','Sheldon@12'),(15,'Shaima23','shaima@email.com','Shaima34!'),(16,'Shaima123','shaima1@email.com','Shaima@123'),(17,'Jonas','jon@email.com','Jon@1234'),(18,'jon@123','jon1@email.com','John@123');

UNLOCK TABLES;





--
-- Table structure for table `application_rating`
--

DROP TABLE IF EXISTS `application_rating`;
CREATE TABLE `application_rating` (
  `APP_RATING_ID` int NOT NULL AUTO_INCREMENT,
  `USER_ID` int DEFAULT NULL,
  `APPLICATION_RATING` int DEFAULT NULL,
  PRIMARY KEY (`APP_RATING_ID`),
  KEY `USER_ID_idx` (`USER_ID`),
  CONSTRAINT `FK_USER_ID` FOREIGN KEY (`USER_ID`) REFERENCES `escapade_users` (`USER_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



LOCK TABLES `application_rating` WRITE;

INSERT INTO `application_rating` VALUES (1,1,5),(2,1,4),(3,1,5),(4,11,5),(5,14,3),(6,17,5);

UNLOCK TABLES;



--
-- Table structure for table `saved_recommendations`
--

DROP TABLE IF EXISTS `saved_recommendations`;

CREATE TABLE `saved_recommendations` (
  `RECOMMENDATION_ID` int NOT NULL AUTO_INCREMENT,
  `USER_ID` int DEFAULT NULL,
  `NAME` varchar(100) DEFAULT NULL,
  `ADDRESS` varchar(200) DEFAULT NULL,
  `CATEGORY` varchar(100) DEFAULT NULL,
  `PHONE` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`RECOMMENDATION_ID`),
  KEY `USER_ID_idx` (`USER_ID`),
  CONSTRAINT `FK_SR_USER_ID` FOREIGN KEY (`USER_ID`) REFERENCES `escapade_users` (`USER_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `saved_recommendations` WRITE;

INSERT INTO `saved_recommendations` VALUES (1,1,'Trafalgar','75 York Road, Waterloo, London, SE1 7NZ','Important Tourist Attraction','+44 20 7620 8900'),(2,1,'Stave Hill Ecological Park','Timber Pond Road, Rotherhithe, London, SE16 6AX','Important Tourist Attraction','+44 20 7237 9175'),(3,1,'Texas Joe\'s','8-9 Snowsfields,London SE1 3SU,United Kingdom','Restaurants','+44 20 3759 7355'),(4,3,'Woolwich Foot Tunnel','Woolwich Foot Tunnel, Woolwich, London, SE18 6','Important Tourist Attraction','+44 20 8921 4661'),(5,1,'Millennium Bridge','Millennium Bridge, South Bank, London, EC4V 3','Important Tourist Attraction',''),(6,11,'Astronomy Centre','Blackheath Avenue, Greenwich, London, SE10 8','Important Tourist Attraction',''),(7,11,'Marks and Spencer','70 Finsbury Pavement,London EC2A 1SA,United Kingdom','Shopping','+44 20 7786 9494'),(8,11,'New Destination Education Corporation','9 Charlton Road, Blackheath, London, SE3 7HB','Hotel',''),(9,11,'Gaucho - Tower Bridge','2 More London Riverside,London SE1 2AP,United Kingdom','Restaurants','+44 20 7407 5222'),(10,11,'The Coal Shed London','4 Crown Square,One Tower Bridge,London SE1 2SE,United Kingdom','Restaurants','+44 20 3384 7272'),(11,11,'Hall Place And Gardens','Bourne Road, Bexley, DA5 1','Important Tourist Attraction','+44 1322 526574'),(12,13,'Hilly Fields Stone Circle','Hilly Fields, Honor Oak Park, London, SE4 1','Important Tourist Attraction',''),(13,11,'The Upper Crust Sandwich Bar','139 Southwood Road,New Eltham,London SE9 3QL,United Kingdom','Restaurants','+44 20 8333 0848'),(14,14,'Hampton Court Palace Hotel','35 Hampton Street, Elephant & Castle, London, SE17 3AN','Hotel','+44 20 7703 0011'),(15,1,'Maryon Park','122 Maryon Road, Charlton, London, SE7 8DH','Important Tourist Attraction','+44 20 8854 0446'),(16,17,'London Bridge Pedestrian Tunnel','Tooley Street, Bermondsey, London, SE1 2QF','Important Tourist Attraction',''),(17,17,'Gaucho - Tower Bridge','2 More London Riverside,London SE1 2AP,United Kingdom','Restaurants','+44 20 7407 5222'),(18,18,'City Gardens','Mount Pleasant, Grays Inn, London, WC1X 0AR','Important Tourist Attraction','+44 20 7374 4127');

UNLOCK TABLES;



--
-- Table structure for table `reviews_recommendations`
--

DROP TABLE IF EXISTS `reviews_recommendations`;

CREATE TABLE `reviews_recommendations` (
  `USER_ID` int DEFAULT NULL,
  `RECOMMENDATION_ID` int NOT NULL,
  `REVIEWS_ID` int NOT NULL AUTO_INCREMENT,
  `NAME` varchar(100) DEFAULT NULL,
  `REVIEW` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`REVIEWS_ID`),
  KEY `USER_ID_idx` (`USER_ID`),
  KEY `RECOMMENDATIONS_ID_idx` (`RECOMMENDATION_ID`),
  CONSTRAINT `RECOMMENDATIONS_ID` FOREIGN KEY (`RECOMMENDATION_ID`) REFERENCES `saved_recommendations` (`RECOMMENDATION_ID`),
  CONSTRAINT `USER_ID` FOREIGN KEY (`USER_ID`) REFERENCES `escapade_users` (`USER_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


LOCK TABLES `reviews_recommendations` WRITE;

INSERT INTO `reviews_recommendations` VALUES 
(1,3,2,'Texas Joe\'s','Great Customer Service. Really Enjoyed it!'),(1,2,3,'Stave Hill Ecological Park','Beautiful park.'),(1,1,4,'Trafalgar','Didnt like it'),(1,5,5,'Millennium Bridge','Excellent place!'),(11,7,6,'Marks and Spencer','Wonderful shop!!'),(11,13,7,'The Upper Crust Sandwich Bar','Tasty sandwiches'),(1,15,8,'Maryon Park','It was a peaceful place!'),(17,16,9,'London Bridge Pedestrian Tunnel','It was incredible!');

UNLOCK TABLES;

