CREATE TABLE `books` (
    `id` int(11) unsigned NOT NULL ,
    `publisher_id` int(11) NOT NULL,
    `title` varchar(255) NOT NULL DEFAULT '',
    `language_id` int(11) NOT NULL,
    `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY(`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `books` (`id`, `title`, `publisher_id`, `language_id`)
VALUES
    (34973284, 'HTML WEB PROGRAMING', 2, 1),
    (57555614, 'hello coding python', 2, 1);

-- where is language number