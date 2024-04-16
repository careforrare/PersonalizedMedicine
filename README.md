# PersonalizedMedicine


to start development you require python and a Docker Setup.

The Following example solution is build on https://github.com/FeatureCloud/app-round/

```
pip install virtualenv

python -m venv careforrare

# For Mac Users
source ./careforrare/bin/activate

# For Windows Users (use Powershell)
 ./careforrare/Scripts/Activate.ps1

# Install Requirements
pip install -r requirements.txt

# Develop your application with local environment you have to set local variables
# Please get in touch with the Care-For-Rare Team

# Build and push your container by facilitating makefile. Please change the name of DOCKER_IMAGE_NAME in your file
# if make does not work in your env please utilize statements in Makefile to create same results
make build

# to do a test run of your container with the following statement. In the logs you should see a server starting. When using Windows bases Systems we recognized mounting works better when triggering command directly in WSL System. 
docker run -d -v ./config.yml:/mnt/input/config.yml -v ./data/output:/mnt/output -p 9000:9000 featurecloud.ai/<care-for-rare-submission name>:latest

# Trigger the start of the application states
curl --location 'http://localhost:9000/setup' --header 'Content-Type: application/json' --data '{"id": "0000000000000000","coordinator": false,"coordinatorID": "0000000000000000","clients": []}'

# Look at logs using. Make sure to close container after testing
docker logs <containerID>

# Push the new image to the registry
make push

Alternatively you are free to utilize the full functionalities of the feature-cloud api and Testbed
https://featurecloud.ai/developers

```