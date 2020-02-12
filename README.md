# DevOps-Trainee-Recruitment

To build a Docker image go to the folder app in your terminal and use command " docker build -t app:latest . "

To run it use command " docker run -d -p 5000:5000 app "

To test it use curl, for example " curl  http://127.0.0.1:5000/random " or " curl -X POST -H 'Content-Type: application/json' http://127.0.0.1:5000/echo -d '{"name":"Sealia"}' "
 
