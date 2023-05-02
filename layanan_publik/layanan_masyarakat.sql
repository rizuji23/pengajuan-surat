-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Apr 20, 2023 at 02:17 PM
-- Server version: 8.0.27
-- PHP Version: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `layanan_masyarakat`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add user', 7, 'add_user'),
(26, 'Can change user', 7, 'change_user'),
(27, 'Can delete user', 7, 'delete_user'),
(28, 'Can view user', 7, 'view_user'),
(29, 'Can add domisili', 8, 'add_domisili'),
(30, 'Can change domisili', 8, 'change_domisili'),
(31, 'Can delete domisili', 8, 'delete_domisili'),
(32, 'Can view domisili', 8, 'view_domisili'),
(33, 'Can add laporan', 9, 'add_laporan'),
(34, 'Can change laporan', 9, 'change_laporan'),
(35, 'Can delete laporan', 9, 'delete_laporan'),
(36, 'Can view laporan', 9, 'view_laporan'),
(37, 'Can add surat_ pindah', 10, 'add_surat_pindah'),
(38, 'Can change surat_ pindah', 10, 'change_surat_pindah'),
(39, 'Can delete surat_ pindah', 10, 'delete_surat_pindah'),
(40, 'Can view surat_ pindah', 10, 'view_surat_pindah'),
(41, 'Can add surat_ kematian', 11, 'add_surat_kematian'),
(42, 'Can change surat_ kematian', 11, 'change_surat_kematian'),
(43, 'Can delete surat_ kematian', 11, 'delete_surat_kematian'),
(44, 'Can view surat_ kematian', 11, 'view_surat_kematian'),
(45, 'Can add surat_ kelahiran', 12, 'add_surat_kelahiran'),
(46, 'Can change surat_ kelahiran', 12, 'change_surat_kelahiran'),
(47, 'Can delete surat_ kelahiran', 12, 'delete_surat_kelahiran'),
(48, 'Can view surat_ kelahiran', 12, 'view_surat_kelahiran'),
(49, 'Can add sku', 13, 'add_sku'),
(50, 'Can change sku', 13, 'change_sku'),
(51, 'Can delete sku', 13, 'delete_sku'),
(52, 'Can view sku', 13, 'view_sku'),
(53, 'Can add sktm_ pend', 14, 'add_sktm_pend'),
(54, 'Can change sktm_ pend', 14, 'change_sktm_pend'),
(55, 'Can delete sktm_ pend', 14, 'delete_sktm_pend'),
(56, 'Can view sktm_ pend', 14, 'view_sktm_pend'),
(57, 'Can add sktm_ kes', 15, 'add_sktm_kes'),
(58, 'Can change sktm_ kes', 15, 'change_sktm_kes'),
(59, 'Can delete sktm_ kes', 15, 'delete_sktm_kes'),
(60, 'Can view sktm_ kes', 15, 'view_sktm_kes'),
(61, 'Can add skck', 16, 'add_skck'),
(62, 'Can change skck', 16, 'change_skck'),
(63, 'Can delete skck', 16, 'delete_skck'),
(64, 'Can view skck', 16, 'view_skck'),
(65, 'Can add nikah', 17, 'add_nikah'),
(66, 'Can change nikah', 17, 'change_nikah'),
(67, 'Can delete nikah', 17, 'delete_nikah'),
(68, 'Can view nikah', 17, 'view_nikah'),
(69, 'Can add beda_ nama', 18, 'add_beda_nama'),
(70, 'Can change beda_ nama', 18, 'change_beda_nama'),
(71, 'Can delete beda_ nama', 18, 'delete_beda_nama'),
(72, 'Can view beda_ nama', 18, 'view_beda_nama');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_bin NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_bin NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_bin NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_bin NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_bin NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_bin,
  `object_repr` varchar(200) COLLATE utf8mb4_bin NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext COLLATE utf8mb4_bin NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-04-13 22:33:21.829525', '1', 'aye', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\", \"Role\"]}}]', 7, 1),
(2, '2023-04-14 10:51:37.444679', '1', 'aye', 2, '[{\"changed\": {\"fields\": [\"Nik\", \"No hp\", \"Jenis kelamin\", \"Alamat\"]}}]', 7, 1),
(3, '2023-04-14 13:25:21.159394', '14', 'nikah (Aye Shabira)', 2, '[{\"changed\": {\"fields\": [\"Is active\"]}}]', 9, 1),
(4, '2023-04-14 13:25:36.719232', '14', 'nikah (Aye Shabira)', 2, '[{\"changed\": {\"fields\": [\"Is active\"]}}]', 9, 1),
(5, '2023-04-16 09:29:11.847866', '2', 'petugas', 1, '[{\"added\": {}}]', 7, 1),
(6, '2023-04-18 12:02:26.620451', '3', 'kepala', 1, '[{\"added\": {}}]', 7, 1),
(7, '2023-04-20 10:26:51.563902', '5', 'surat_kelahiran (Aye Shabira)', 2, '[{\"changed\": {\"fields\": [\"Kode surat\", \"Is active\"]}}]', 9, 1),
(8, '2023-04-20 10:52:17.783749', '6', 'surat_pindah (Aye Shabira)', 2, '[{\"changed\": {\"fields\": [\"Kode surat\", \"Is active\"]}}]', 9, 1),
(9, '2023-04-20 11:14:29.885766', '7', 'skck (Aye Shabira)', 2, '[{\"changed\": {\"fields\": [\"Kode surat\", \"Is active\"]}}]', 9, 1),
(10, '2023-04-20 11:23:33.879652', '8', 'sku (Aye Shabira)', 2, '[{\"changed\": {\"fields\": [\"Kode surat\", \"Is active\"]}}]', 9, 1),
(11, '2023-04-20 11:26:58.768301', '9', 'sktm_kes (Aye Shabira)', 2, '[{\"changed\": {\"fields\": [\"Kode surat\", \"Is active\"]}}]', 9, 1),
(12, '2023-04-20 11:29:33.834412', '10', 'sktm_pend (Aye Shabira)', 2, '[{\"changed\": {\"fields\": [\"Kode surat\", \"Is active\"]}}]', 9, 1),
(13, '2023-04-20 11:31:47.514795', '11', 'domisili (Aye Shabira)', 2, '[{\"changed\": {\"fields\": [\"Kode surat\", \"Is active\"]}}]', 9, 1),
(14, '2023-04-20 11:34:59.632650', '12', 'beda_nama (Aye Shabira)', 2, '[{\"changed\": {\"fields\": [\"Kode surat\", \"Is active\"]}}]', 9, 1),
(15, '2023-04-20 11:37:21.032460', '13', 'surat_kematian (Aye Shabira)', 2, '[{\"changed\": {\"fields\": [\"Kode surat\", \"Is active\"]}}]', 9, 1),
(16, '2023-04-20 11:51:47.116374', '16', 'nikah (Aye Shabira)', 2, '[{\"changed\": {\"fields\": [\"Is active\"]}}]', 9, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'layanan_app', 'user'),
(8, 'layanan_app', 'domisili'),
(9, 'layanan_app', 'laporan'),
(10, 'layanan_app', 'surat_pindah'),
(11, 'layanan_app', 'surat_kematian'),
(12, 'layanan_app', 'surat_kelahiran'),
(13, 'layanan_app', 'sku'),
(14, 'layanan_app', 'sktm_pend'),
(15, 'layanan_app', 'sktm_kes'),
(16, 'layanan_app', 'skck'),
(17, 'layanan_app', 'nikah'),
(18, 'layanan_app', 'beda_nama');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_bin NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-04-11 14:50:00.567998'),
(2, 'auth', '0001_initial', '2023-04-11 14:50:00.842814'),
(3, 'admin', '0001_initial', '2023-04-11 14:50:00.939001'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-04-11 14:50:00.944559'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-04-11 14:50:00.949441'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-04-11 14:50:00.992922'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-04-11 14:50:01.013343'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-04-11 14:50:01.034417'),
(9, 'auth', '0004_alter_user_username_opts', '2023-04-11 14:50:01.039410'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-04-11 14:50:01.059205'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-04-11 14:50:01.061206'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-04-11 14:50:01.068526'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-04-11 14:50:01.089487'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-04-11 14:50:01.111194'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-04-11 14:50:01.133672'),
(16, 'auth', '0011_update_proxy_permissions', '2023-04-11 14:50:01.138679'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-04-11 14:50:01.161066'),
(18, 'sessions', '0001_initial', '2023-04-11 14:50:01.182133'),
(19, 'layanan_app', '0001_initial', '2023-04-11 15:06:00.211362'),
(20, 'layanan_app', '0002_user_alamat_user_jenis_kelamin_user_nik', '2023-04-14 09:39:43.516635'),
(21, 'layanan_app', '0003_domisili_laporan_user_no_hp_surat_pindah_and_more', '2023-04-14 10:31:53.945606'),
(22, 'layanan_app', '0004_domisili_id_laporan', '2023-04-14 12:51:36.810626'),
(23, 'layanan_app', '0005_alter_beda_nama_dokumen_benar_and_more', '2023-04-14 12:55:49.038193'),
(24, 'layanan_app', '0006_beda_nama_dokumen_pembeda_beda_nama_kk_beda_nama_ktp_and_more', '2023-04-14 14:31:44.513917'),
(25, 'layanan_app', '0007_alter_user_role', '2023-04-16 09:32:11.738260'),
(26, 'layanan_app', '0008_alter_laporan_is_active', '2023-04-16 09:58:31.740714'),
(27, 'layanan_app', '0009_laporan_kode_surat', '2023-04-16 13:20:59.282593'),
(28, 'layanan_app', '0010_alter_laporan_is_active', '2023-04-16 13:50:38.407748'),
(29, 'layanan_app', '0011_user_agama_user_kewarganegaraan_user_pekerjaan_and_more', '2023-04-20 10:17:52.501999');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_bin NOT NULL,
  `session_data` longtext COLLATE utf8mb4_bin NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- --------------------------------------------------------

--
-- Table structure for table `layanan_app_beda_nama`
--

DROP TABLE IF EXISTS `layanan_app_beda_nama`;
CREATE TABLE IF NOT EXISTS `layanan_app_beda_nama` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_beda_nama` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `nik` bigint NOT NULL,
  `dokumen_keliru` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `dokumen_benar` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `keterangan` longtext COLLATE utf8mb4_bin NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `id_laporan_id` int NOT NULL,
  `dokumen_pembeda` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `kk` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `ktp` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `surat_pengantar` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `surat_pernyataan` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `layanan_app_beda_nama_id_laporan_id_6ea96c77` (`id_laporan_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Dumping data for table `layanan_app_beda_nama`
--

INSERT INTO `layanan_app_beda_nama` (`id`, `id_beda_nama`, `nik`, `dokumen_keliru`, `dokumen_benar`, `keterangan`, `created_at`, `updated_at`, `id_laporan_id`, `dokumen_pembeda`, `kk`, `ktp`, `surat_pengantar`, `surat_pernyataan`) VALUES
(1, '5c6d897f', 1231231231231, 'dokumen_keliru/dawdawd.pdf', 'dokumen_benar/dawdawd.pdf', 'dawdawdawd', '2023-04-14 13:02:52.341533', '2023-04-14 13:02:52.341533', 12, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `layanan_app_domisili`
--

DROP TABLE IF EXISTS `layanan_app_domisili`;
CREATE TABLE IF NOT EXISTS `layanan_app_domisili` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_domisili` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `nik` bigint NOT NULL,
  `keterangan` longtext COLLATE utf8mb4_bin NOT NULL,
  `masa_berlaku` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `id_laporan_id` int DEFAULT NULL,
  `kk` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `ktp` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `pas_foto` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `layanan_app_domisili_id_laporan_id_85ef0dff` (`id_laporan_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Dumping data for table `layanan_app_domisili`
--

INSERT INTO `layanan_app_domisili` (`id`, `id_domisili`, `nik`, `keterangan`, `masa_berlaku`, `created_at`, `updated_at`, `id_laporan_id`, `kk`, `ktp`, `pas_foto`) VALUES
(1, 'd4ff66c9', 1231231231231, 'dawdawd', '2023-04-14', '2023-04-14 12:53:05.319497', '2023-04-14 12:53:05.319497', 11, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `layanan_app_laporan`
--

DROP TABLE IF EXISTS `layanan_app_laporan`;
CREATE TABLE IF NOT EXISTS `layanan_app_laporan` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_laporan` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `jenis_surat` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `is_active` smallint UNSIGNED DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `id_user_id` bigint NOT NULL,
  `kode_surat` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `layanan_app_laporan_id_user_id_360eee0a` (`id_user_id`)
) ;

--
-- Dumping data for table `layanan_app_laporan`
--

INSERT INTO `layanan_app_laporan` (`id`, `id_laporan`, `jenis_surat`, `is_active`, `created_at`, `updated_at`, `id_user_id`, `kode_surat`) VALUES
(1, '393b3792', 'nikah', 0, '2023-04-14 12:18:09.204252', '2023-04-14 12:18:09.204252', 1, NULL),
(2, '4078f519', 'nikah', 0, '2023-04-14 12:21:00.789768', '2023-04-14 12:21:00.789768', 1, NULL),
(3, '4c583a54', 'nikah', 0, '2023-04-14 12:21:19.560814', '2023-04-14 12:21:19.560814', 1, NULL),
(4, '1f402d87', 'surat_kelahiran', 0, '2023-04-14 12:32:25.903994', '2023-04-14 12:32:25.903994', 1, NULL),
(5, 'a087052f', 'surat_kelahiran', 1, '2023-04-14 12:33:47.398225', '2023-04-20 10:26:51.562902', 1, '-'),
(6, '58a0031d', 'surat_pindah', 1, '2023-04-14 12:37:04.138800', '2023-04-20 10:52:17.782749', 1, '-'),
(7, '6a197ea1', 'skck', 1, '2023-04-14 12:40:57.258263', '2023-04-20 11:14:29.884760', 1, '-'),
(8, '8f9f3128', 'sku', 1, '2023-04-14 12:43:49.447907', '2023-04-20 11:23:33.878649', 1, '-'),
(9, '16cd4b8b', 'sktm_kes', 1, '2023-04-14 12:46:42.892742', '2023-04-20 11:26:58.768301', 1, '-'),
(10, '01b17279', 'sktm_pend', 1, '2023-04-14 12:49:49.964737', '2023-04-20 11:29:33.833392', 1, '-'),
(11, '83c93afc', 'domisili', 1, '2023-04-14 12:53:05.315762', '2023-04-20 11:31:47.513795', 1, '-'),
(12, 'b52731eb', 'beda_nama', 1, '2023-04-14 13:02:52.327331', '2023-04-20 11:34:59.631651', 1, '-'),
(13, 'db83568e', 'surat_kematian', 1, '2023-04-14 13:07:03.215746', '2023-04-20 11:37:21.031459', 1, '-'),
(14, '859d30c4', 'nikah', 3, '2023-04-14 13:15:36.522630', '2023-04-16 13:58:05.994952', 1, NULL),
(15, 'a8b78ea6', 'nikah', 1, '2023-04-14 14:41:38.510290', '2023-04-19 06:45:07.560098', 1, NULL),
(16, 'ea226054', 'nikah', 1, '2023-04-20 11:51:06.974889', '2023-04-20 11:51:47.115376', 1, '511.1/016/Ekbang');

-- --------------------------------------------------------

--
-- Table structure for table `layanan_app_nikah`
--

DROP TABLE IF EXISTS `layanan_app_nikah`;
CREATE TABLE IF NOT EXISTS `layanan_app_nikah` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_nikah` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `nik` bigint NOT NULL,
  `mempelai_pria` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `mempelai_wanita` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `nama_wali` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `id_laporan_id` int NOT NULL,
  `akta_lahir` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `foto_pas_1` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `foto_pas_2` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `ijazah` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `kk` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `ktp` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `surat_belum_nikah` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `surat_persetujuan` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `surat_rt_rw` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `layanan_app_nikah_id_laporan_id_c4a8dd44` (`id_laporan_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Dumping data for table `layanan_app_nikah`
--

INSERT INTO `layanan_app_nikah` (`id`, `id_nikah`, `nik`, `mempelai_pria`, `mempelai_wanita`, `nama_wali`, `created_at`, `updated_at`, `id_laporan_id`, `akta_lahir`, `foto_pas_1`, `foto_pas_2`, `ijazah`, `kk`, `ktp`, `surat_belum_nikah`, `surat_persetujuan`, `surat_rt_rw`) VALUES
(1, 'faa89544', 1231231231231, 'dawdawd', 'dawdaw', 'dawd', '2023-04-14 12:18:09.213474', '2023-04-14 12:18:09.213474', 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(2, '7eb6b4a9', 1231231231231, 'dawdawd', 'dawdawd', 'dawdaw', '2023-04-14 12:21:00.791769', '2023-04-14 12:21:00.791769', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(3, '62e897a1', 1231231231231, 'dawdaw', 'dawdaw', 'daw', '2023-04-14 12:21:19.561810', '2023-04-14 12:21:19.561810', 3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(4, '640a7a92', 1231231231231, 'dawd', 'dawd', 'dawd', '2023-04-14 13:15:36.525184', '2023-04-14 13:15:36.525184', 14, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(5, '46c9cf63', 1231231231231, 'dawdawd', 'dawd123123', 'dawdawd', '2023-04-14 14:41:38.532369', '2023-04-14 14:41:38.532369', 15, 'all/dawdawd_SexK7ZS.pdf', 'all/dawdawd_Ktf0qE8.pdf', 'all/dawdawd_XkEOg7s.pdf', 'all/dawdawd_VGvBF3q.pdf', 'all/dawdawd_EhtoBGp.pdf', 'all/dawdawd_GZ5Ww88.pdf', 'all/dawdawd_7XEIpxw.pdf', 'all/dawdawd_dCpQ94w.pdf', 'all/dawdawd.pdf'),
(6, '5d600f05', 1231231231231, 'dawd', 'ddd', 'ddd', '2023-04-20 11:51:06.991850', '2023-04-20 11:51:06.991850', 16, 'all/exportstok_XkN6010.pdf', 'all/exportstok_kqhxrLC.pdf', 'all/exportstok_1BvPgoc.pdf', 'all/exportstok_R3KVdHB.pdf', 'all/exportstok_0HrPiSP.pdf', 'all/exportstok_RRdxXeN.pdf', 'all/exportstok_llQ28x0.pdf', 'all/exportstok_TWyJoAj.pdf', 'all/exportstok.pdf');

-- --------------------------------------------------------

--
-- Table structure for table `layanan_app_skck`
--

DROP TABLE IF EXISTS `layanan_app_skck`;
CREATE TABLE IF NOT EXISTS `layanan_app_skck` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_skck` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `nik` bigint NOT NULL,
  `keterangan` longtext COLLATE utf8mb4_bin NOT NULL,
  `keperluan` longtext COLLATE utf8mb4_bin NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `id_laporan_id` int NOT NULL,
  `akta` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `kk` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `pas_foto` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `sim` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `layanan_app_skck_id_laporan_id_b51c7ac1` (`id_laporan_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Dumping data for table `layanan_app_skck`
--

INSERT INTO `layanan_app_skck` (`id`, `id_skck`, `nik`, `keterangan`, `keperluan`, `created_at`, `updated_at`, `id_laporan_id`, `akta`, `kk`, `pas_foto`, `sim`) VALUES
(1, '05fe3899', 1231231231231, 'dawdawd', 'dawdawd', '2023-04-14 12:40:57.260263', '2023-04-14 12:40:57.260263', 7, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `layanan_app_sktm_kes`
--

DROP TABLE IF EXISTS `layanan_app_sktm_kes`;
CREATE TABLE IF NOT EXISTS `layanan_app_sktm_kes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_sktm_kes` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `nik` bigint NOT NULL,
  `nama_anggota_keluarga` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `hubungan` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `keterangan` longtext COLLATE utf8mb4_bin NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `id_laporan_id` int NOT NULL,
  `kk` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `ktp` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `surat_pengantar` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `layanan_app_sktm_kes_id_laporan_id_d2479f0f` (`id_laporan_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Dumping data for table `layanan_app_sktm_kes`
--

INSERT INTO `layanan_app_sktm_kes` (`id`, `id_sktm_kes`, `nik`, `nama_anggota_keluarga`, `hubungan`, `keterangan`, `created_at`, `updated_at`, `id_laporan_id`, `kk`, `ktp`, `surat_pengantar`) VALUES
(1, '2c5896c6', 1231231231231, 'dawd', 'dawd', 'dawd', '2023-04-14 12:46:42.893786', '2023-04-14 12:46:42.893786', 9, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `layanan_app_sktm_pend`
--

DROP TABLE IF EXISTS `layanan_app_sktm_pend`;
CREATE TABLE IF NOT EXISTS `layanan_app_sktm_pend` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_sktm_pend` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `nik` bigint NOT NULL,
  `nama_tanggungan` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `jml_tanggungan` int NOT NULL,
  `hubungan_tanggungan` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `keterangan` longtext COLLATE utf8mb4_bin NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `id_laporan_id` int NOT NULL,
  `kk` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `ktp` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `surat_pengantar` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `layanan_app_sktm_pend_id_laporan_id_6198d1f8` (`id_laporan_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Dumping data for table `layanan_app_sktm_pend`
--

INSERT INTO `layanan_app_sktm_pend` (`id`, `id_sktm_pend`, `nik`, `nama_tanggungan`, `jml_tanggungan`, `hubungan_tanggungan`, `keterangan`, `created_at`, `updated_at`, `id_laporan_id`, `kk`, `ktp`, `surat_pengantar`) VALUES
(1, '17bec791', 1231231231231, 'dawdawd', 2, 'dawdaw', 'ddawd', '2023-04-14 12:49:49.966695', '2023-04-14 12:49:49.966695', 10, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `layanan_app_sku`
--

DROP TABLE IF EXISTS `layanan_app_sku`;
CREATE TABLE IF NOT EXISTS `layanan_app_sku` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_sku` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `nik` bigint NOT NULL,
  `nama_usaha` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `jenis_usaha` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `alamat_usaha` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `keterangan` longtext COLLATE utf8mb4_bin NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `id_laporan_id` int NOT NULL,
  `kk` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `ktp` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `pas_foto` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `surat_pengantar` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `layanan_app_sku_id_laporan_id_fafad99a` (`id_laporan_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Dumping data for table `layanan_app_sku`
--

INSERT INTO `layanan_app_sku` (`id`, `id_sku`, `nik`, `nama_usaha`, `jenis_usaha`, `alamat_usaha`, `keterangan`, `created_at`, `updated_at`, `id_laporan_id`, `kk`, `ktp`, `pas_foto`, `surat_pengantar`) VALUES
(1, 'a4cfff8e', 1231231231231, 'dawd', 'dawd', 'dawd', 'dawd', '2023-04-14 12:43:49.448907', '2023-04-14 12:43:49.448907', 8, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `layanan_app_surat_kelahiran`
--

DROP TABLE IF EXISTS `layanan_app_surat_kelahiran`;
CREATE TABLE IF NOT EXISTS `layanan_app_surat_kelahiran` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_surat_kelahiran` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `nik` bigint NOT NULL,
  `nama_bayi` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `ttl` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `jenis_kelamin_anak` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `hari_jam_lahir` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `anak_ke` int NOT NULL,
  `nama_ayah` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `nama_ibu` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `id_laporan_id` int NOT NULL,
  `kk` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `ktp` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `surat_dokter` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `surat_rt_rw` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `layanan_app_surat_kelahiran_id_laporan_id_843d9a56` (`id_laporan_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Dumping data for table `layanan_app_surat_kelahiran`
--

INSERT INTO `layanan_app_surat_kelahiran` (`id`, `id_surat_kelahiran`, `nik`, `nama_bayi`, `ttl`, `jenis_kelamin_anak`, `hari_jam_lahir`, `anak_ke`, `nama_ayah`, `nama_ibu`, `created_at`, `updated_at`, `id_laporan_id`, `kk`, `ktp`, `surat_dokter`, `surat_rt_rw`) VALUES
(1, '0e57e389', 1231231231231, 'dawdawd', '2023-04-14', 'Laki-Laki', '2023-04-14T19:33', 2, 'dawdawd', 'dawdwad', '2023-04-14 12:33:47.400231', '2023-04-14 12:33:47.400231', 5, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `layanan_app_surat_kematian`
--

DROP TABLE IF EXISTS `layanan_app_surat_kematian`;
CREATE TABLE IF NOT EXISTS `layanan_app_surat_kematian` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_surat_kematian` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `nik` bigint NOT NULL,
  `nama_wafat` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `penyebab` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `hari_tanggal_wafat` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `pelapor` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `hubungan_pelapor` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `id_laporan_id` int NOT NULL,
  `ktp_kk` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `ktp_kk_pelapor` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `ktp_pasangan` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `surat_keterangan` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `layanan_app_surat_kematian_id_laporan_id_b5bcd5d2` (`id_laporan_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Dumping data for table `layanan_app_surat_kematian`
--

INSERT INTO `layanan_app_surat_kematian` (`id`, `id_surat_kematian`, `nik`, `nama_wafat`, `penyebab`, `hari_tanggal_wafat`, `pelapor`, `hubungan_pelapor`, `created_at`, `updated_at`, `id_laporan_id`, `ktp_kk`, `ktp_kk_pelapor`, `ktp_pasangan`, `surat_keterangan`) VALUES
(1, '2e8b83cb', 1231231231231, 'dawd', 'dawd', '2023-04-14', 'dawd', 'dawdawd', '2023-04-14 13:07:03.217745', '2023-04-14 13:07:03.217745', 13, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `layanan_app_surat_pindah`
--

DROP TABLE IF EXISTS `layanan_app_surat_pindah`;
CREATE TABLE IF NOT EXISTS `layanan_app_surat_pindah` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_surat_pindah` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `nik` bigint NOT NULL,
  `alamat_asal` longtext COLLATE utf8mb4_bin NOT NULL,
  `pindah_ke` longtext COLLATE utf8mb4_bin NOT NULL,
  `pengikut` longtext COLLATE utf8mb4_bin NOT NULL,
  `keterangan` longtext COLLATE utf8mb4_bin NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `id_laporan_id` int NOT NULL,
  `kk` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `ktp` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `pas_foto` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  `surat_rt_rw` varchar(200) COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `layanan_app_surat_pindah_id_laporan_id_989aa0d4` (`id_laporan_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Dumping data for table `layanan_app_surat_pindah`
--

INSERT INTO `layanan_app_surat_pindah` (`id`, `id_surat_pindah`, `nik`, `alamat_asal`, `pindah_ke`, `pengikut`, `keterangan`, `created_at`, `updated_at`, `id_laporan_id`, `kk`, `ktp`, `pas_foto`, `surat_rt_rw`) VALUES
(1, '7d29c623', 1231231231231, 'dawdawd', 'dawdawd', 'dawdwd', 'dawdawd', '2023-04-14 12:37:04.140801', '2023-04-14 12:37:04.140801', 6, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `layanan_app_user`
--

DROP TABLE IF EXISTS `layanan_app_user`;
CREATE TABLE IF NOT EXISTS `layanan_app_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_bin NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_bin NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_bin NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_bin NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_bin NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `role` smallint UNSIGNED DEFAULT NULL,
  `alamat` longtext COLLATE utf8mb4_bin,
  `jenis_kelamin` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL,
  `nik` bigint DEFAULT NULL,
  `no_hp` bigint DEFAULT NULL,
  `agama` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
  `kewarganegaraan` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
  `pekerjaan` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
  `status` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
  `ttl` varchar(100) COLLATE utf8mb4_bin DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ;

--
-- Dumping data for table `layanan_app_user`
--

INSERT INTO `layanan_app_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `role`, `alamat`, `jenis_kelamin`, `nik`, `no_hp`, `agama`, `kewarganegaraan`, `pekerjaan`, `status`, `ttl`) VALUES
(1, 'pbkdf2_sha256$600000$aDoT37hlVxaG3tMBKInVx6$3uSdXDM0C+L+z0oVTSUYZSpSpDbjN0IvQwB2fPovo0Q=', '2023-04-20 12:21:17.871433', 1, 'aye', 'Aye', 'Shabira', 'aye@aye.com', 1, 1, '2023-04-13 22:23:51.628167', 1, 'dawdawd', 'Laki-Laki', 1231231231231, 1231231232, NULL, NULL, NULL, NULL, NULL),
(2, 'pbkdf2_sha256$600000$8yOUCeZ355vvcuSvtEPS4w$JuyYoNdcdGepCWAJnM6i4XU7pvGwXBM5cQlNGp+F8q8=', '2023-04-16 09:36:05.835171', 0, 'petugas', 'Petugas', 'Desa', '', 0, 1, '2023-04-16 09:29:11.677944', 2, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(3, 'pbkdf2_sha256$600000$6o4desGyFlh8kqKUTTinPt$praF91uA7MHQ0gFZnkGPvXJ8lCcPD8YavPf7/vKyO6c=', '2023-04-19 06:19:22.143418', 0, 'kepala', 'Kepala', 'Desa', '', 0, 1, '2023-04-18 12:02:26.370052', 3, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(4, 'test12345678', NULL, 0, 'test', 'dawdawd', 'dawda', 'test@test.com', 0, 1, '2023-04-20 12:14:18.838829', 1, 'dawdawd', 'Laki-Laki', 123123123, 12312312312, 'dawd', 'WNI', 'awdawd', 'Menikah', '2023-04-20'),
(5, 'pbkdf2_sha256$600000$et37DK7wEZJJcbnvHNlvGf$ud6VjrJ3xclt369RSoZM9hPJS0BRR9digzP8iWpZ0pQ=', NULL, 0, 'dawd', 'dawdawd', 'dawdawd', 'dawd@dawd.com', 0, 1, '2023-04-20 12:16:42.084938', 1, 'dawdawd', 'Laki-Laki', 123123123, 12312312, 'dawd', 'WNI', 'dawd', 'Menikah', '2023-04-20');

-- --------------------------------------------------------

--
-- Table structure for table `layanan_app_user_groups`
--

DROP TABLE IF EXISTS `layanan_app_user_groups`;
CREATE TABLE IF NOT EXISTS `layanan_app_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `layanan_app_user_groups_user_id_group_id_9342ed67_uniq` (`user_id`,`group_id`),
  KEY `layanan_app_user_groups_user_id_6d8f6566` (`user_id`),
  KEY `layanan_app_user_groups_group_id_4869b765` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- --------------------------------------------------------

--
-- Table structure for table `layanan_app_user_user_permissions`
--

DROP TABLE IF EXISTS `layanan_app_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `layanan_app_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `layanan_app_user_user_pe_user_id_permission_id_d230ed60_uniq` (`user_id`,`permission_id`),
  KEY `layanan_app_user_user_permissions_user_id_ab5add74` (`user_id`),
  KEY `layanan_app_user_user_permissions_permission_id_1f8b3ecc` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
