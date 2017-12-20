CREATE DEFINER=`root`@`localhost` PROCEDURE `spCreateAdvice`(
IN p_adviceTitle varchar(150),
IN p_adviceShortDescription varchar(150),
IN p_adviceCategoryID INT,
IN p_adviceAuthorID INT,
IN p_adviceCreateDate varchar(100),
IN p_adviceBody TEXT
)
BEGIN
IF ( select NOT exists (select 1 from users where UserID = p_adviceAuthorID) ) THEN

    select 'Author not exists.';

ELSE 
BEGIN
insert into advices
(
    Title,
    ShortDescription,
    CategoryID,
    AuthorID,
    CreateDate,
    ViewsQuantity,
    CommentsQuantity,
    CommentsID,
    Body
    
)
values
(
    p_adviceTitle,
    p_adviceShortDescription,
    p_adviceCategoryID,
    p_adviceAuthorID,
    p_adviceCreateDate,
    1,
    1,
    1,
    p_adviceBody
);
END;
END IF;
END