# Conveyor Monitoring Starter Solution

### Download
Clone this repo: `git clone https://github.com/DigitalShoestringSolutions/ConveyorMonitoring`  
Open the downloaded folder: `cd ConveyorMonitoring`

### Configure & Assemble
- Edit the config file to set machine name `nano Config/Sensing/main.py`
- Check the recipe contains the Modules you desire `nano recipe.txt`
- Assemble the Modules `Modules/Asssembly/get_modules.sh`
- Restart to apply the settings to the downloaded Modules <!-- Namely docker user permissions -->

### Build & Run
- Build the docker containers `docker compose build`
- Start the docker containers `./start.sh`

### Usage
- View the dashboard: navigate to `localhost:3000` in a web browser