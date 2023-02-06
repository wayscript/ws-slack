![img](https://i.ibb.co/Vgv9nf1/interface3.png)

# Spin Up a Flask Server: Web Server Template
This template is an example of setting up a flask application inside of the WayScript X lair environment. It includes a sample template home page and a sample api response.

## Video Tutorial
Watch the full tutorial for this template on YouTube! https://youtu.be/qON6a6r-TAU 

## Requirements
Inside of your requirements.txt, it is required to include the dependencies of your project. In this example, we have a plain flask server without any other dependencies. That means our requirements.txt file will only include flask

```python
flask
```

## Setup

Flask Applications within WayScript X require three criteria:
- App.py file
- requirements.txt file
- Deploy trigger in .triggers file


### App.py 
The app.py file houses the flask application. This is where you can create routes, or url endpoints, and what response is given to the user when those routes are visited. Here is an example route:

```python
@app.route('/response')
def response():
    return {"Message" : "Success"}
```
In this specific example, the url will be the base url + '/response'. The base url comes from the deploy trigger, an example is included below.

This will return a JSON response which is provided in the return statement.



### Deploy Trigger
A deploy trigger allows easy, seamless deployments of your flask application. Add a deployment trigger to your .triggers file. 
You are able to run your flask application with the following command placed in the command to run blank:
```python
flask run --port 8080 --host 0.0.0.0
```
The flask run command looks for the App.py file by default. This command will need to be modified if your flask application is placed in a file not called App.py 

For the port blank you will need to place the same port number that is included in your flask run command. In this example that is 
```python
8080
```

### WayScript Lair Tools
A WayScript Lair allows you to have two separate environment of your flask application, a development environment and a production environment. Once you are finished developing your application, you can deploy to a separate, production state environment by using the deploy button on the left. 

You can continue to to develop inside the development lair, then redeploy to your production state to reflect those changes in your production state application. 

## Documentation
For full instructions,  please visit the docs: https://docs.wayscript.com/quickstart-spin-up-server/host-a-flask-server
