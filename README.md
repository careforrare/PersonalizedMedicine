# PersonalizedMedicine


to start development you require python and a Docker Setup. If you are using Windows 

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


# Build and push your container by facilitating makefile
make

# run container with
docker run --env-file .env feature-cloud-registry-name/care-for-rare-submission:latest

```