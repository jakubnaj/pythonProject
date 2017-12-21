CREATE DEFINER=`root`@`localhost` PROCEDURE `spCreateComment`(
IN p_adviceID INT,
IN p_authorID INT,
IN p_createDate VARCHAR(50),
IN p_content VARCHAR(100),
IN p_likesQuantity INT
)
BEGIN
IF ( select NOT exists (select 1 from users where UserID = p_authorID) ) THEN

    select 'Author not exists.';

ELSEIF ( select NOT exists (select 1 from advices where Id = p_adviceID) ) THEN

    select 'Advice not exists.';
ELSE
BEGIN
insert into comments
(
    AdviceID,
    AuthorID,
    CreateDate,
    Content,
    LikesQuantity
)
values
(
    p_adviceID,
    p_authorID,
    p_createDate,
    p_content,
    p_likesQuantity
);

END;
END IF;
END