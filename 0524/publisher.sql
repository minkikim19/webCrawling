CREATE TABLE `publishers` (
    `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
    `name` varchAr(128) NOT NULL DEFAULT '',
    `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY(`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `publishers` (`id`, `name` )
VALUES
    (1, 'wikibooks'),
    (2, 'hanbit'),
    (3, 'addison-Wesley');

-- SELECT * FROM publishers;