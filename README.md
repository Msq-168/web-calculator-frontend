# Web Calculator Frontend
Frontend of separated front-end and back-end calculator.
Only responsible for UI interaction. All math calculation is handled by backend API.

## Tech Stack
HTML5, CSS3, Vanilla JavaScript

## Environment
Modern browser (Chrome recommended). Can be opened via Live Server.

## How to run
Open index.html directly or use Live Server.

## Features
1. Calculator UI, support numbers, decimal point, brackets and four arithmetic operations.
2. Send expression string to backend API `POST /api/calculate`.
3. Fetch history records from `GET /api/history`.
4. Delete single history record or clear all records.

## Backend Connection
Request backend service: `http://127.0.0.1:5000`
Start backend first, otherwise network error will occur.
