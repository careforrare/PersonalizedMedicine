# PersonalizedMedicine


to start development you require python. 

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

# Windows
set NEO4J_URI=neo4j://185.112.181.108:7687
set NEO4J_USERNAME=neo4j
set NEO4J_PASSWORD=TUMAIMAKEATHON2024



# Build and push your container by facilitating makefile
make

# run container with
docker run --env-file .env feature-cloud-registry-name/care-for-rare-submission:latest

```
