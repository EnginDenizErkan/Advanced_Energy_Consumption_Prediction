# This folder is dedicated towards deployment of model to BentoML and servcie it.
INSTALLATION

To utilize BentoML entegrated with code development environment , we have to serve our model via BentoML

1) Open the Terminal application 

2) Enter the directory where the service.py file is located as follows:

cd C:\Users\your-user-name\path-to-enviroment\

if your environment not active after that here is how you should proceed;

cd C:\Users\your user name\path to enviroment\ > conda activate your-enviroment

3) Start the service with the following command, specifying the path to the service file:

bentoml serve service:svc

    * Note: We use this command because the model is marked as svc in the service.py file, but this is optional and can be changed according to your model.



Use "uvicorn backend_data_serving:app --reload" to run API.