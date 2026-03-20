# API with Redis and SQL

A backend API built with **Flask** for product management, using an architecture organized by routes, HTTP request objects, and composers.

This project was developed to study API construction with Flask, following a structured backend pattern and integrating product creation and product lookup features.

---

## Overview

This API provides product-related operations through Flask routes.

Based on the current implementation, the system includes:

- product creation
- product lookup by name

The application uses a modular structure, separating route definitions from business logic through composers and HTTP request abstractions.

---

## Main Features

- Product creation through API requests
- Product search by product name
- Flask-based route handling
- Structured backend organization
- Separation between route layer and business logic

---

## Technologies Used

- **Python**
- **Flask**
- **Redis**
- **SQL**

> The repository name indicates the use of Redis and SQL, while the provided code confirms the use of Flask and a modular API structure.

---

## Project Structure

From the provided code, the project follows an organized structure with components such as:

- **routes**
- **http request abstractions**
- **composers**

Example elements shown in the code:

- `Blueprint`
- `HttpRequest`
- `product_creator_composer`
- `product_finder_composer`

This suggests a design where route handlers delegate business logic to dedicated components.

---

## Available Routes

### Create Product

```http
POST /products
