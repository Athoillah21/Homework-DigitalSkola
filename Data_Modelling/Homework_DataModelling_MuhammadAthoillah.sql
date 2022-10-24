CREATE DATABASE 'homework';

CREATE TABLE `lagu` (
  `id_lagu` VARCHAR(256) NOT NULL,
  `judul_lagu` VARCHAR(256) NOT NULL,
  `id_album` VARCHAR(256) PRIMARY KEY NOT NULL
);

CREATE TABLE `album` (
  `nama_album` VARCHAR(256) NOT NULL,
  `id_musisi` VARCHAR(256) NOT NULL,
  `id_album` VARCHAR(24) NOT NULL
);

CREATE TABLE `musisi` (
  `nama_musisi` VARCHAR(256) NOT NULL,
  `tipe_musisi` ENUM('solo','duo','band'),
  `id_musisi` VARCHAR(256) PRIMARY KEY NOT NULL
);

ALTER TABLE `lagu` ADD FOREIGN KEY (`id_album`) REFERENCES `album` (`id_album`) ON UPDATE SET NULL;

ALTER TABLE `album` ADD FOREIGN KEY (`id_musisi`) REFERENCES `musisi` (`id_musisi`) ON DELETE CASCADE;
