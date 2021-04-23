----------- SCHEMA FOR THE HOME TASK ORGANIZER DB -------


-- The Tables --

CREATE TABLE Members
(
memberId UNIQUEIDENTIFIER PRIMARY KEY DEFAULT(NEWID()),
memberSquad NVARCHAR(15) NOT NULL,
memberIsAssignedTask BIT NOT NULL DEFAULT(0), -- 0 OR 1 FOR TRUE FALSE
memberName NVARCHAR(15) NOT NULL
);


CREATE TABLE Tasks
(
taskId SMALLINT NOT NULL IDENTITY(1,1) PRIMARY KEY,
taskTitle NVARCHAR(100) NOT NULL,
assignedMember UNIQUEIDENTIFIER NULL FOREIGN KEY references Members (memberId), -- NEEDS an "unassigned" member to be created. 
taskParent SMALLINT NULL,
taskCreatedDateTime DATETIME2 NOT NULL,
taskDeadline DATETIME2 NULL,
taskPriority TINYINT NULL, -- 0 THRU 4
taskHasChild BIT NOT NULL DEFAULT(0), -- 0 OR 1 FOR TRUE FALSE
taskStatus NVARCHAR(15) NOT NULL DEFAULT('backlog'),
taskPercentComplete TINYINT NOT NULL DEFAULT(0)
);


CREATE TABLE taskNotes
(
noteId INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
noteContent NVARCHAR(250) NULL,
taskId SMALLINT NOT NULL FOREIGN KEY references Tasks(TaskId),
memberId UNIQUEIDENTIFIER NOT NULL FOREIGN KEY references Members(memberId),
noteDateTime DATETIME2 NOT NULL

);


CREATE TABLE AssocTaskTeamMember
(
taskId SMALLINT NOT NULL FOREIGN KEY references Tasks(taskId),
memberId UNIQUEIDENTIFIER NOT NULL FOREIGN KEY references Members(memberId),
CONSTRAINT pkAssocTaskTeamMember PRIMARY KEY (taskId, memberId)
);

GO

-- The Initial Values --

INSERT INTO Members (memberSquad, memberName)
Values ('The Lazies','Unassigned');

GO

-- A Trigger or Two --

CREATE TRIGGER assignedMemberShouldBeUnassigned 
ON Tasks AFTER INSERT
AS 
BEGIN
	UPDATE Tasks
	SET assignedMember = (Select memberId FROM Members WHERE Members.memberName LIKE 'Unassigned')
END

GO


-- A Test Value --

INSERT INTO [dbo].[Tasks](taskTitle,taskCreatedDateTime,taskPriority)
VALUES ('Set Up Project Managing Software', SYSDATETIME(), 1);

GO

