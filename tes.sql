-- 1. Buat Tabel Kategori
CREATE TABLE IF NOT EXISTS `kategori` (
  `id_kategori` int(11) NOT NULL AUTO_INCREMENT,
  `nama_kategori` varchar(100) NOT NULL,
  PRIMARY KEY (`id_kategori`),
  UNIQUE KEY `nama_kategori` (`nama_kategori`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2. Buat Tabel Status
CREATE TABLE IF NOT EXISTS `status` (
  `id_status` int(11) NOT NULL AUTO_INCREMENT,
  `nama_status` varchar(50) NOT NULL,
  PRIMARY KEY (`id_status`),
  UNIQUE KEY `nama_status` (`nama_status`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 3. Buat Tabel Produk
CREATE TABLE IF NOT EXISTS `produk` (
  `id_produk` int(11) NOT NULL AUTO_INCREMENT,
  `id_produk_api` int(11) NOT NULL,
  `nama_produk` varchar(255) NOT NULL,
  `harga` decimal(12,0) NOT NULL,
  `kategori_id` int(11) NOT NULL,
  `status_id` int(11) NOT NULL,
  PRIMARY KEY (`id_produk`),
  UNIQUE KEY `id_produk_api` (`id_produk_api`),
  CONSTRAINT `fk_kategori` FOREIGN KEY (`kategori_id`) REFERENCES `kategori` (`id_kategori`) ON DELETE CASCADE,
  CONSTRAINT `fk_status` FOREIGN KEY (`status_id`) REFERENCES `status` (`id_status`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

-- 4. Insert Data Kategori 
INSERT IGNORE INTO `kategori` (`nama_kategori`) VALUES 
('L QUEENLY'),
('L MTH AKSESORIS (IM)'),
('L MTH TABUNG (LK)'),
('SP MTH SPAREPART (LK)'),
('CI MTH TINTA LAIN (IM)'),
('L MTH AKSESORIS (LK)'),
('S MTH STEMPEL (IM)');

-- 5. Insert Data Status
INSERT IGNORE INTO `status` (`nama_status`) VALUES 
('bisa dijual'),
('tidak bisa dijual');

-- 6. Insert Data Produk
-- id_kategori: 1=QUEENLY, 2=AKSESORIS(IM), 3=TABUNG(LK), 4=SPAREPART, 5=TINTA, 6=AKSESORIS(LK), 7=STEMPEL
-- id_status: 1=bisa dijual, 2=tidak bisa dijual

INSERT IGNORE INTO `produk` (`id_produk_api`, `nama_produk`, `harga`, `kategori_id`, `status_id`) VALUES 
(6, 'ALCOHOL GEL POLISH CLEANSER GP-CLN01', 12500, 1, 1),
(9, 'ALUMUNIUM FOIL ALL IN ONE BULAT 23mm IM', 1000, 2, 1),
(11, 'ALUMUNIUM FOIL ALL IN ONE BULAT 30mm IM', 1000, 2, 1),
(12, 'ALUMUNIUM FOIL ALL IN ONE SHEET 250mm IM', 12500, 2, 2),
(15, 'ALUMUNIUM FOIL HDPE/PE BULAT 23mm IM', 12500, 2, 1),
(17, 'ALUMUNIUM FOIL HDPE/PE BULAT 30mm IM', 1000, 2, 1),
(18, 'ALUMUNIUM FOIL HDPE/PE SHEET 250mm IM', 13000, 2, 2),
(19, 'ALUMUNIUM FOIL PET SHEET 250mm IM', 1000, 2, 2),
(22, 'ARM PENDEK MODEL U', 13000, 2, 1),
(23, 'ARM SUPPORT KECIL', 13000, 3, 2),
(24, 'ARM SUPPORT KOTAK PUTIH', 13000, 2, 2),
(26, 'ARM SUPPORT PENDEK POLOS', 13000, 3, 1),
(27, 'ARM SUPPORT S IM', 1000, 2, 2),
(28, 'ARM SUPPORT T (IMPORT)', 13000, 2, 1),
(29, 'ARM SUPPORT T - MODEL 1 ( LOKAL )', 10000, 3, 1),
(50, 'BLACK LASER TONER FP-T3 (100gr)', 13000, 2, 2),
(56, 'BODY PRINTER CANON IP2770', 500, 4, 1),
(58, 'BODY PRINTER T13X', 15000, 4, 1),
(59, 'BOTOL 1000ML BLUE KHUSUS UNTUK EPSON R1800/R800 - 4180 IM (T054920)', 10000, 5, 1),
(70, 'BOTOL KOTAK 100ML LK', 1000, 6, 1),
(72, 'BOTOL 10ML IM', 1000, 7, 2);