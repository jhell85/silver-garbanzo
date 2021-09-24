# Django Rest Framework Examples

## Description

This is a collection of projects built using Django Rest Framework (DRF) it starts with basic
implementation of DRF and adds more and different features to each project.

# _DRF-1_

## Description

This is a sample DRF project using a NewsAPI with Articles and an author
foreignKey field of Journalist.

showing example use cases for:

- Function based Views
- Class based Views
- DRF's Serializer Class
- DRF's ModelSerializer Class
- Simple Validations
  - Validations on a whole Model (check that description and title are different)
  - Validations on individual fields of a Model (check that title is at least 30 chars long)
- Binding foreign fields within serializer

# _DRF-2_

## Description

This is a sample DRF project using an Ebook model with a Review model system for each book
showing example use cases for:

- Authentication
- Authorized User's permissions
  - Only Admin can add Ebooks to the DB
  - Only a user of a review can edit their review
- A User can only review a book once
- Pagination of ebooks
