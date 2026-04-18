### Option 5: Library and Loan Management System

#### Assignment

Design and implement a REST API for library management. The system should support the management of authors, books, physical copies, readers, and loans. The application must support tracking book availability and the process of borrowing and returning books.

#### Minimum Domain Scope

The system must contain at least the following entities:

- author
- book
- copy
- reader
- loan

#### Minimum Required Functionality

The application must allow at least:

- managing authors and books
- managing individual book copies
- managing readers
- creating loans
- returning loans
- displaying book availability
- displaying active loans of a specific reader
- filtering loans by status

#### Mandatory Logical Relationships

The design must appropriately capture at least these relationships:

- an author can have multiple books
- a book can have multiple copies
- a reader can have multiple loans
- a loan links a reader with a specific copy

#### Examples of Input Scenarios

The application must work with at least the following inputs:

- creating a book
- adding a copy
- registering a reader
- creating a loan
- returning a loan
- filtering active loans
- getting the details of a book or reader

#### Validation and Error Handling Requirements

The application must handle, for example, the following situations:

- an attempt to borrow a copy that is already loaned out
- an attempt to return a loan that has already been returned
- working with a non-existent book or reader
- an invalid loan or return date
