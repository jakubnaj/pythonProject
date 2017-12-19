USE `adwisedb`;
DROP procedure IF EXISTS `spCreateUser`;

DELIMITER $$
USE `adwisedb`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `spCreateUser`(
IN p_Username varchar(100),
IN p_Email varchar(100),
IN p_Password varchar(100)
)
BEGIN
IF ( select exists (select 1 from users where UserName = p_Username) ) THEN

    select 'Username Exists !!';

ELSEIF ( select exists (select 1 from users where UserEmail = p_Email) ) THEN

    select 'Email Exists !!';

ELSE 
BEGIN
insert into users
(
    UserName,
    UserEmail,
    UserPassword
)
values
(
    p_Username,
    p_Email,
    p_Password
);
END;
END IF;
END$$

DELIMITER ;