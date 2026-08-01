CREATE DATABASE `database1`;
SHOW DATABASES;
USE `database1`;

CREATE TABLE `student`(
	`student_id` INT PRIMARY KEY, 
    `name` VARCHAR(20) NOT NULL,
    `major` VARCHAR(20), # UNIQUE; DEFAULT `历史`
    `score` INT
);

DESCRIBE `student`;
# DROP TABLE `student`;

ALTER TABLE `student` ADD gpa DECIMAL(3,2);
ALTER TABLE `student` DROP COLUMN GPA;

INSERT INTO `student` VALUES(1,'小白','历史');
INSERT INTO `student`(`name`, `major`, `student_id`) VALUES('小蓝','英语',4);
INSERT INTO `student`(`major`, `student_id`) VALUES('英语',2);
INSERT INTO `student` VALUES(3,'小绿','数学');
INSERT INTO `student` VALUES(5,'小绿',NULL);
INSERT INTO `student`(`name`, `major`) VALUES('小蓝','语文'); # `student_id` INT AUTO_INCREMENT
SELECT * FROM `student`;  # 搜寻全部资料，*表示全部

# 修改删除资料 -------------------------------------------
SET SQL_SAFE_UPDATE = 0; # 关闭自动更新

UPDATE `student`
SET `major` = '英语文学'
WHERE `major` = '英语'; 

UPDATE `student`
SET `major` = '生化'
WHERE `major` = '生物' OR `major` = '化学'; 

UPDATE `student`
SET `name` = '小灰', `major` = '物理'
WHERE `student_id` = 1; 

UPDATE `student`
SET `major` = '地理';

DELETE FROM `student`
WHERE `student_id` = 4;

DELETE FROM `student`
WHERE `name` = '小灰' AND `major` = '物理';

DELETE FROM `student`
WHERE `score` < 60;

DELETE FROM `student`;

# 取得资料----------------------------------------------
SELECT `name``major` FROM `STUDENT`;
SELECT `name` FROM `STUDENT` ORDER BY `score` DESC; # DESC 由高到低；没有写，默认为ASC，由低到高alter
SELECT * FROM `STUDENT` ORDER BY `score` DESC LIMIT 3;

SELECT * 
FROM `student` 
WHERE `major` = '英语' AND `student_id` = 1; # <> 不等于
 
SELECT * FROM `student`
WHERE `major` IN('历史','英语','生物');
 
# 创建公司资料库表格 ---------------------------------------------
CREATE TABLE `employee`(
	`emp_id` INT PRIMARY KEY,
    `name`VARCHAR(20),
    `birth_date` DATE,
    `sex` VARCHAR(1),
    `salary` INT,
    `branch_id` INT,
    `sup_id` INT
);

CREATE TABLE `branch`(
	`branch_id` INT PRIMARY KEY,
    `branch_name` VARCHAR(20),
    `manager_id` INT,
    FOREIGN KEY(`manager_id`) REFERENCES `employee`(`emp_id`) ON DELETE SET NULL
);

ALTER TABLE `employee` ADD FOREIGN KEY(`branch_id`) REFERENCES `branch`(`branch_id`) ON DELETE SET NULL;
ALTER TABLE `employee` ADD FOREIGN KEY(`sup_id`) REFERENCES `employee`(`emp_id`) ON DELETE SET NULL;

CREATE TABLE `client`(
	`client_id` INT PRIMARY KEY,
    `client_name` VARCHAR(20),
    `phone` VARCHAR(20)	
);

CREATE TABLE `works_with`(
	`emp_id` INT,
    `client_id` INT,
    `total_sales` INT,
    PRIMARY KEY (`emp_id`, `client_id`),
    FOREIGN KEY (`emp_id`) REFERENCES `employee`(`emp_id`) ON DELETE CASCADE,
    FOREIGN KEY (`client_id`) REFERENCES `client`(`client_id`) ON DELETE CASCADE
);
DROP TABLE `work with`;

INSERT INTO `branch` VALUES(1, '研发', NULL);
INSERT INTO `branch` VALUES(2, '行政', NULL);
INSERT INTO `branch` VALUES(3, '资讯', NULL);

INSERT INTO `employee` VALUES(206, '小黄', '1998-10-08', 'F', 50000, 1, NULL);
INSERT INTO `employee` VALUES(207, '小绿', '1985-09-16', 'M', 29000, 2, 206);
INSERT INTO `employee` VALUES(208, '小黑', '2000-12-09', 'M', 35000, 3, 206);
INSERT INTO `employee` VALUES(209, '小白', '1997-01-22', 'F', 39000, 3, 207);
INSERT INTO `employee` VALUES(210, '小兰', '1925-11-10', 'F', 84000, 1, 207);

UPDATE `branch` SET `manager_id` = 206 WHERE `branch_id` = 1;
UPDATE `branch` SET `manager_id` = 207 WHERE `branch_id` = 2;
UPDATE `branch` SET `manager_id` = 208 WHERE `branch_id` = 3;

INSERT INTO `client` VALUES(400, 'Alice', '18302830');
INSERT INTO `client` VALUES(401, 'Ace', '18390390');
INSERT INTO `client` VALUES(402, 'Alian', '13889398');
INSERT INTO `client` VALUES(403, 'Amy', '12238330');
INSERT INTO `client` VALUES(404, 'Apollo', '28302830');

INSERT INTO `works_with` VALUES(206, 400, 70000);
INSERT INTO `works_with` VALUES(207, 401, 24000);
INSERT INTO `works_with` VALUES(208, 400, 9800);
INSERT INTO `works_with` VALUES(208, 403, 24000);
INSERT INTO `works_with` VALUES(210, 404, 87940);

# 练习 -------------------------------------------------------------
SELECT * FROM `employee`;
SELECT * FROM `client`;
SELECT * FROM `employee` ORDER BY `salary`;
SELECT `name` FROM `employee` ORDER BY `salary` DESC LIMIT 3;
SELECT `name` FROM `employee`;
SELECT DISTINCT `sex` FROM `employee`; # 返回值不重复

# 聚合函数 aggregate functions -------------------------------------------------
SELECT COUNT(*) FROM `employee`;
SELECT COUNT(`sup_id`) FROM `employee`;

SELECT COUNT(*) 
FROM `employee` 
WHERE `birth_date` > '1970-01-01' AND `sex` = 'F';

SELECT AVG(`salary`) FROM `employee`; # 算平均数
SELECT SUM(`salary`) FROM `employee`;
SELECT MAX(`salary`) FROM `employee`;

# 万用字元 wildcards ----------------------------------------
# %代表多个字元，_代表一个字元
SELECT * 
FROM `client` 
WHERE `phone` LIKE '%335'; # 尾号335

SELECT * 
FROM `client` 
WHERE `client_name` LIKE 'A%';

SELECT * 
FROM `employee`
WHERE `birth_date` LIKE '_____12%'; # 生日在12月

# 并集 union -------------------------------------------
# select后的资料形态一致，比如都是字符串
SELECT `name` FROM `employee` 
UNION
SELECT `client_name` FROM `client`
UNION
SELECT `branch_name` FROM `branch`;

# select后数量一致，返回的是第一个select后的资料名称
SELECT `emp_id`, `name` FROM `employee`
UNION
SELECT `client_id`, `client_name` FROM `client`;

SELECT `emp_id` AS `total_id`, `name` AS `total_name` FROM `employee`
UNION
SELECT `client_id`, `client_name` FROM `client`;

SELECT `salary` FROM `employee`
UNION 
SELECT `total_sales` FROM `works_with`;

# 连接 join --------------------------------------
INSERT INTO `branch` VALUES(4,'偷懒', NULL);
SELECT * FROM `employee` JOIN `branch` ON `emp_id` = `manager_id`;

SELECT `employee`.`emp_id`, `employee`.`name`, `branch`.`branch_name` 
FROM `employee` 
JOIN `branch` 
ON `employee`.`emp_id` = `branch`.`manager_id`; # 防止重名

SELECT `employee`.`emp_id`, `employee`.`name`, `branch`.`branch_name` 
FROM `employee` LEFT JOIN `branch` # 右边表格没有匹配则不返回，左边表格一定返回，同理，RIGHT JOIN与之相反
ON `employee`.`emp_id` = `branch`.`manager_id`; # 防止重名

# 子查询 subquery --------------------------------------------------
SELECT `name` 
FROM `employee`
WHERE `emp_id` = (
	SELECT `manager_id` 
	FROM `branch` 
	WHERE `branch_name` = '研发'
);

SELECT `name`
FROM `employee`
WHERE `emp_id` IN ( # 不止一笔资料时写IN
	SELECT `emp_id` 
	FROM `works_with`
	WHERE `total_sales` > 50000
);

# on delete -----------------------------------
# ON DELETE SET NULL references被删掉后要查询的foreign key设为NULL（注意，主键不能为空）
# ON DELETE CASCADE references被删掉后foreign key那一行跟着一起删掉
DELETE FROM `employee`
WHERE `emp_id` = 207;
SELECT * FROM `branch`;
SELECT * FROM `works_with`;

# python连接mysql ----------------------
INSERT INTO `branch` VALUES(5, 'qq', NULL);