# ConveyorBeltProject 

# Electrical Schematic

![Schematic](src/schematic.png)

# Github Sync
I could not get the Raspberry Pi to push to the repo, as I could not give it permissions. Hence, there is no way to merge changes. I would simply edit it and push through my computer and pull through the Raspberry Pi.

## New Folder

    mkdir ConveyorBeltProject
    cd ConveyorBeltProject
    git init
    git branch -M main #rename current branch to main
    git remote add origin https://github.com/flamerten/ConveyorBeltProject
    git pull origin main

## Update Current Folder
Note: Assumes that Git is initialised

    cd ConveyorBeltProject
    git reset --hard
    git pull origin main
