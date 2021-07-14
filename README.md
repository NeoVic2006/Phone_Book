# Polls with questions and Answers 



API requests:

GET: http://127.0.0.1:8000/poll/
Showing all created polls in database

GET: http://127.0.0.1:8000/poll/{poll_name}/      //  poll_name -> Weather (for example)
Showing all questions, all answers and correct answer

POST: http://127.0.0.1:8000/api/token/
Providing authorization Token if admin credentials are correct. (username: Admin, password: admin)
