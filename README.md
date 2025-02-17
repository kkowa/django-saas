# Project Overview

This project is built using the following technologies and tools:

## Tech Stack

- **Backend**: Python, Django
- **Deployment**: Docker, Railway
- **Database**: Neon
- **Code Formatting**:
  - Python: `autopep8`
  - Django Templates: `djlint`
- **Utilities**: WhiteNoise (for static files)

## To-Do List

### Deployment & Infrastructure

- [ ] Switch from WhiteNoise to S3 for handling user uploads.

### Email Configuration

- [ ] Investigate and configure email functionality using SMTP.

### Integrations

- [ ] Explore integrating with Plaid for a fun side feature.

### Frontend Improvements

- [ ] Replace `allauth-ui` with Tailwind CSS or custom templates.
  - **Issue**: Custom elements in `allauth-ui` are not rendering correctly due to library and static file rendering problems.
  - **Workaround**: Manually copy over the necessary CSS from the library.



