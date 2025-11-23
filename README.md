# Student Registration Form

This is a simple web application built using Flask that allows users to register students and view their details. The application uses SQLite as the database to store student information.

## Features

- **Student Registration**: Users can register students by filling out a form.
- **View Registered Students**: Users can view a list of all registered students.
- **Flash Messages**: Provides feedback to users after successful registration.

## Project Structure

```
Student_registration_form/
├── app.py                # Main application file
├── static/
│   └── style.css         # CSS file for styling
├── templates/
│   ├── index.html        # HTML template for the registration form
│   └── view.html         # HTML template for viewing registered students
```

## Prerequisites

- Python 3.7 or higher
- Flask

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dilki-dahanayaka/Student_registration_form.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Student_registration_form
   ```

3. Install the required dependencies:
   ```bash
   pip install flask
   ```

## Usage

1. Run the application:
   ```bash
   python app.py
   ```

2. Open your web browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

3. Use the registration form to add students and view the list of registered students.

## Database

The application uses an SQLite database (`students.db`) to store student information. The database is automatically initialized when the application is run for the first time.

### Database Schema

The `students` table has the following columns:

- `id`: Auto-incremented primary key
- `reg_no`: Registration number
- `date`: Registration date
- `full_name`: Full name of the student
- `dob`: Date of birth
- `gender`: Gender
- `class_name`: Class name
- `religion`: Religion
- `skills`: Skills
- `father_name`: Father's name
- `father_occ`: Father's occupation
- `mother_name`: Mother's name
- `mother_occ`: Mother's occupation

## Templates

- **`index.html`**: Contains the registration form.
- **`view.html`**: Displays the list of registered students.

## Static Files

- **`style.css`**: Contains the CSS styles for the application.

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.