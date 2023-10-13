# exarth_learning_task1
 The FLD Django App is a robust Django application integrated with the First Line Of Defence (FLD) project. This app employs AI to measure hand size and recommends suitable guns based on the hand size.


Features
Hand Measurements: Utilizes hand landmarks using the mediapipe library to measure hand size. Offers flexibility by allowing the use of the hand itself as a reference object or providing details of a custom reference object.

Recommendation AI Models: Implements recommendation AI models stored in the machine_learning directory. These models process hand measurements data to provide accurate gun recommendations.

User-Friendly Interface: Users can easily capture hand images, view measurements, and receive gun recommendations through a simple and intuitive interface.

Getting Started
Ensure you have a Django project named FLD set up.
Clone this repository into your Django project directory.
Install required dependencies using pip install -r requirements.txt.
Apply migrations with python manage.py migrate.
Run the development server with python manage.py runserver.
Visit localhost:8000 to explore the app and experience its functionalities.

To-Do List
Notification Functionality: Implement notifications for important updates.
Data Input from Users: Allow users to provide additional data for more accurate recommendations.
Dynamic Model Updates: Implement dynamic model updates based on changes in client requirements for gun recommendations.
