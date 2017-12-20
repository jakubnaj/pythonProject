USE `adwisedb`;
DROP procedure IF EXISTS `spChangePassword`;

DELIMITER $$
USE `adwisedb`$$
CREATE PROCEDURE `spChangePassword` (
IN p_UserId INT(50),
IN p_OldPassword varchar(100),
IN p_NewPassword varchar(100)
)
BEGIN
IF ( select NOT exists (select 1 from users where UserId = p_UserId) ) THEN

    select 'User not exists.';

ELSEIF ( select NOT exists (select 1 from users where UserId = p_UserId AND UserPassword = p_OldPassword) ) THEN

    select 'Incorrect old password.';

ELSE 
BEGIN
UPDATE users SET UserPassword = p_NewPassword
WHERE UserId = p_UserId;
END;
END IF;
END$$

DELIMITER ;

