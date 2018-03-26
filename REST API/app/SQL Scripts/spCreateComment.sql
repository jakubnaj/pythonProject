CREATE DEFINER=`root`@`localhost` PROCEDURE `spCreateComment`(
IN p_adviceID INT,
IN p_authorName VARCHAR(50),
IN p_createDate VARCHAR(50),
IN p_content VARCHAR(100),
IN p_likesQuantity INT
)
BEGIN
IF ( select NOT exists (select 1 from users where UserName = p_authorName) ) THEN

    select 'Author not exists.';

ELSEIF ( select NOT exists (select 1 from advices where Id = p_adviceID) ) THEN

    select 'Advice not exists.';
ELSE
BEGIN
insert into comments
(
    AdviceID,
    AuthorName,
    CreateDate,
    Content,
    LikesQuantity
)
values
(
    p_adviceID,
    p_authorName,
    p_createDate,
    p_content,
    p_likesQuantity
);

END;
END IF;
END