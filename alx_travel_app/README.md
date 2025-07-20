# Database Modeling and Data Seeding in Django

## Features

- Listings with location, price, and availability
- Booking system with date ranges
- User reviews for listings

## Models

- **Listing**: title, description, location, price_per_night, available
- **Booking**: linked to Listing and User
- **Review**: rating and comment for a listing

## Seeding

Run the following to seed the database with sample listing data:

```bash
python manage.py seed
```
