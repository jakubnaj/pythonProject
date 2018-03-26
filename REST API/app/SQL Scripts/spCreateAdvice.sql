CREATE DEFINER=`root`@`localhost` PROCEDURE `spCreateAdvice`(
IN p_adviceTitle varchar(150),
IN p_adviceShortDescription varchar(150),
IN p_adviceCategoryName varchar(50),
IN p_adviceAuthorName varchar(50),
IN p_adviceCreateDate varchar(100),
IN p_adviceBody TEXT
)
BEGIN
IF ( select NOT exists (select 1 from users where UserName = p_adviceAuthorName) ) THEN

    select 'Author not exists.';

ELSE 
BEGIN
insert into advices
(
    Title,
    ShortDescription,
    CategoryName,
    AuthorName,
    CreateDate,
    ViewsQuantity,
    CommentsQuantity,
    Body
    
)
values
(
    p_adviceTitle,
    p_adviceShortDescription,
    p_adviceCategoryName,
    p_adviceAuthorName,
    p_adviceCreateDate,
    0,
    0,
    p_adviceBody
);
END;
END IF;
END