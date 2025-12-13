-- Creation of three tables: Assignments, Technologies and Assignment_Technologies --

-- 1. Table for the basic information about the assignments --
CREATE TABLE Assignment (
    AssignmentID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Description TEXT,
    StartDate DATE,
    EndDate DATE
);

-- 2. Table listing of all available technologies --
CREATE TABLE Technologies (
    TechnologyID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL UNIQUE
);


-- 3. Join table for solving M:N relationships --
CREATE TABLE Assignment_Technologies (
    AssignmentID INTEGER,
    TechnologyID INTEGER,

    -- Composite primary key --
    PRIMARY KEY (AssignmentID, TechnologyID),

    -- Foreign keys with references to master tables --
    FOREIGN KEY (AssignmentID) REFERENCES Assignments (AssignmentID),
    FOREIGN KEY (TechnologyID) REFERENCES Technologies (TechnologyID)
);
