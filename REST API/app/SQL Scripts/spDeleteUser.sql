USE `adwisedb`;
DROP procedure IF EXISTS `spDeleteUser`;

DELIMITER $$
USE `adwisedb`$$
CREATE PROCEDURE `spDeleteUser` (
IN p_UserId int(20))
BEGIN
IF ( select exists (select 1 from users where UserId = p_UserId) ) THEN
    DELETE FROM users WHERE UserId = p_UserId;
ELSE 
	SELECT 'User not exist';
END IF;
END;$$

DELIMITER ;

