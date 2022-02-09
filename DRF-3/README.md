# _DRF-3_

## Description

This is a sample DRF project showing use cases for user Authentication
showing example use cases for:

- Change plural names of models
- Use of Django signals to create a profile instance when a new User is created
- Build an api within profiles app to host seperate views and urls utilizing the same model
  - Serializers for Profile, ProfileAvatar, ProfileStatus
  - Build URLs utilizing DRF routers
    - make seperate route for a user to update their profile's avatar
  - View's using DRF viewsets (ModelViewSet, GenericViewSet, UpdateAPIView) and mixins (UpdateModelMixin, ListModelMixin, RetrieveModelMixin)
  - create permissions so anyone can Read but only owners of profiles can Edit their status or profiles
  - create REST URL params for gettin all users status and individual user's status
  - use DRF filters.SearchFilter to search for users.profile by the city
- Write tests for all endpoints using DRF APITestCase class
