# Construction Materials Project Documentation

## Table of Contents

1. [Introduction](#introduction)

2. [Getting Started](#getting-started)

- [Prerequisites](#prerequisites)

- [Installation](#installation)

3. [Usage](#usage)

- [Running the Application](#running-the-application)

- [Features](#features)

4. [API Documentation](#api-documentation)

- [Available Endpoints](#available-endpoints)

- [Authentication](#authentication)

5. [Frontend](#frontend)

- [Technologies Used](#technologies-used)

- [Folder Structure](#folder-structure)

- [Redux Setup](#redux-setup)

6. [Loading Materials](#loading-materials)

- [Method 1: Admin Panel](#using-admin-panel)

- [Method 2: Management Command](#using-management-command)

7. [Backend](#backend)

- [Technologies Used](#technologies-used)

- [Database Models](#database-models)

- [API Endpoints](#api-endpoints)

8. [Contributing](#contributing)

9. [License](#license)

## 1. Introduction

The Construction Materials Project is a web-based application designed to facilitate the management and selection of construction materials for various construction projects. This documentation provides an in-depth overview of the project's features, installation instructions, and API documentation.

### Problem Statement:

You are tasked with developing a web page that displays a list of materials for reuse in construction projects. The list should be retrieved from the backend. The frontend and backend should communicate effectively to ensure the list is up-to-date and reflects any changes to the materials.

### Stack: React and Django

### Repos:

- Front End: [https://github.com/sharmanvarun/construction-frontend](https://github.com/sharmanvarun/construction-frontend)
- Back End: [https://github.com/sharmanvarun/construction-backend](https://github.com/sharmanvarun/construction-backend)

### Features:

- Search: Uses debounce in frontend and retrieves the searched materials from backend.

- Filter: Frontend filtering.

- CRUD operations for Materials using Djnago Admin Panel’s User Authentication.

- Increase or decrease the material Amount using buttons. (Updation of Material Amount dynamically using websocket is having bugs right now. Nonetheless, their implementation can be found at [websockets-new](https://github.com/sharmanvarun/construction-backend/tree/websockets-new) branch for material backend, and for front end the branch name is [websockets](https://github.com/sharmanvarun/construction-frontend/tree/websockets)).

## 2. Getting Started

### Prerequisites

Before getting started, ensure that you have the following prerequisites installed:

- [Node.js](https://nodejs.org/) (v14 or higher)

- [Python](https://www.python.org/) (v3.7 or higher)

- [Django](https://www.djangoproject.com/) (v3.2 or higher)

- [Django REST framework](https://www.django-rest-framework.org/)

- [Database system of your choice (e.g., PostgreSQL, SQLite)]

### Installation

Follow these steps to set up and run the project:

1. Clone the repositories to your local machine:

2. Frontend Setup:

```bash

cd frontend

npm install

```

3. Backend Setup: Create a virtual environment and activate it.

```
python3 -m venv venv
source venv/bin/activate
```

Install packages

```bash
pip install packagename
```

Following packages has been used:

channels==4.0.0

- channels-redis==4.1.0

- daphne==4.0.0

- decorator==5.1.1

- Django==4.2.1

- django-cors-headers==4.2.0

- django-filter==23.2

- django-sse==0.4.1

- djangorestframework==3.14.0

- entrypoints==0.4

- pickleshare==0.7.5

- Pillow==10.0.0

- redis==5.0.0

- sse==1.2

4. Database Setup:
   Configure your database settings in `backend/settings.py`. (This mostly won’t be needed. I am pushing my settings.py file unabridged. This file also contains my SECRET_KEY (shouldn’t be of any concern, since it’s a demo project with no sensitive data)

```
python manage.py migrate
```

5. Start the Development Servers:

- Frontend:

```
cd frontend
npm start
```

- Backend:

```
cd backend
python manage.py runserver
```

The project should now be accessible at `http://localhost:3000` for the frontend and `http://localhost:8000` for the backend.

## 4. Usage

### Running the Application

To run the application, follow the installation steps in the previous section. Once the development servers are started, access the application in your web browser.

## 5. API Documentation

### Available Endpoints

The API provides the following endpoints:

- `GET /api/materials/`: Retrieve a list of all construction materials.
  Eg: `curl --location 'http://localhost:8000/api/materials/'`

- `GET/api/materials/?search=Window`: Search for materials containing the word "Window."
  Eg:
  `  curl --location 'http://localhost:8000/api/materials/?search=Window'`

- `GET /api/materials/<material_id>/`: Retrieve a specific material by ID.
  Eg: `curl --location 'http://localhost:8000/api/materials/2/'`

- `PATCH /api/materials/<material_id>/update_amount/`: Update the amount of a material.

  Eg: `curl --location --request PATCH 'http://localhost:8000/api/materials/1/update_amount/' \--header 'Content-Type: application/json' \--data  '{"amount": 3}`

## 6. Loading Materials

Materials can be loaded into our database using 2 ways

### Using Admin Panel

- Access the Django admin panel at `http://localhost:8000/admin/`.
- Log in with your admin credentials. (username:admin, password:admin, for my db)

- Navigate to the "Materials" section to view, create, edit, or delete materials.
- Use the "Add Material" button to create a new material.
- Edit material details.

- #### Uploading Images

- When creating or editing a material, use the `ImageField` to upload an associated image.
- Uploaded images are stored in the `media/material_images/` directory.

### Using Management Command

Materials can also be added from a json file using management command

```
python manage.py load_materials
```

The json file location can be set at: "material_backend/materials/management/commands/load_materials.py

## 7. Frontend

### Technologies Used

The frontend of the Construction Materials Project is built using the following technologies:

- React.js

- Redux for state management

- Thunk middleware for asynchronous actions

### Folder Structure

- `src/`: Contains the frontend source code.

- `src/actions/`: Redux action creators.

- `src/components/`: React components.

  - `FilterBar.js` (To Display the search bar on top)

  - `MaterialList.js` (Filter function, handling amount change, and Display of Materials)

- `src/style/`: Styling css files.

- `src/reducers/`: Redux reducers.

- `src/store.js`: Redux store configuration.

- `src/App.js`: Main application component.

- `src/index.js`: Entry point for the application.

### Redux Setup

Redux is used for state management in the frontend. Actions, reducers, and the Redux store are configured in the appropriate directories. The Api calls are in materialActions.js

## 7. Backend

### Technologies Used

The backend of the Construction Materials Project is built using the following technologies:

- Django and Django REST framework

- sqlLite database (or your preferred database)

### Database Models

#### Materials Model

The core data model for the project is the Material model, defined in the models.py file. It includes fields for material name, description, amount, and an ImageField for storing material images.

#### ImageField Usage

- The `ImageField` is used to store material images in the `material_images/` directory within the `media` directory.
- Images are uploaded via the Django admin panel.

### API Endpoints

The backend provides API endpoints for managing construction materials. Refer to the [API Documentation](#api-documentation) section for a list of available endpoints and their descriptions.

## 8. Contributing

Currently, contributions are not encouraged since it is a personal project intended to display my caliber. Nonetheless, if absolutely needed, contributions can be made by following the given steps:

1. Fork the repository on GitHub.

2. Clone your forked repository to your local machine.

3. Create a new branch for your feature or bug fix.

4. Make your changes and commit them.

5. Push your branch to your forked repository on GitHub.

6. Create a pull request (PR) to the main repository.

This concludes the documentation for the Construction Materials Project. If you have any questions or need further assistance, please feel free to reach out.
