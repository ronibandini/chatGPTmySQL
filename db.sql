CREATE TABLE `categories` (
  `idCategory` int(10) UNSIGNED NOT NULL,
  `categoryDesc` longtext DEFAULT NULL,
  `idParentCategory` int(11) DEFAULT NULL,
  `imageCategory` longtext DEFAULT NULL,
  `active` smallint(6) DEFAULT NULL,
  `displayOrder` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;


CREATE TABLE `categories_products` (
  `idProduct` int(11) DEFAULT NULL,
  `idCategory` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE `products` (
  `idProduct` int(10) UNSIGNED NOT NULL,
  `idSupplier` int(11) DEFAULT NULL,
  `description` longtext DEFAULT NULL,
  `details` longtext DEFAULT NULL,
  `price` float DEFAULT NULL,
  `listPrice` float DEFAULT NULL,
  `bToBPrice` float DEFAULT NULL,
  `imageUrl` longtext DEFAULT NULL,
  `smallImageUrl` longtext DEFAULT NULL,
  `sku` longtext DEFAULT NULL,
  `stock` int(11) DEFAULT NULL,
  `listHidden` int(11) DEFAULT NULL,
  `weight` int(11) DEFAULT NULL,
  `deliveringTime` int(11) DEFAULT NULL,
  `active` int(11) DEFAULT NULL,
  `hotDeal` int(11) DEFAULT NULL,
  `cost` float DEFAULT NULL,
  `visits` int(11) DEFAULT NULL,
  `sales` int(11) DEFAULT NULL,
  `emailText` longtext DEFAULT NULL,
  `stockLevelAlert` int(11) DEFAULT NULL,
  `formQuantity` int(11) DEFAULT NULL,
  `showInHome` int(11) DEFAULT NULL,
  `dateAdded` longtext DEFAULT NULL,
  `hasPersonalization` int(11) DEFAULT NULL,
  `chineseDescription` longtext DEFAULT NULL,
  `function` longtext DEFAULT NULL,
  `spec` longtext DEFAULT NULL,
  `unit` longtext DEFAULT NULL,
  `direction` longtext DEFAULT NULL,
  `ingredients` longtext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;
