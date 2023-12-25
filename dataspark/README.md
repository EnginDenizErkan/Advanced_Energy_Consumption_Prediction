# Unleashing the Power of Tomorrow's Energy Today: Welcome to DSEnergy

This document is prepared for giving necessary information for the customers and new developers.

&nbsp;

---

Table of contents

- [Information about project](#information-about-project)
- [Development Guidelines](#development-guidelines)
  - [Environment Setup](#environment-setup)
    - [Viewing all available environments](#viewing-all-available-environments)
    - [Creating an environment from scratch](#creating-an-environment-from-scratch)
    - [Creating an environment.yml file](#creating-an-environment.yml-file)
    - [Creating an environment from an environment.yml file](#creating-an-environment-from-an-environment.yml-file)
    - [Updating an environment](#updating-an-environment)
  - [New Branch Creation Rules](#new-branch-creation-rules)
  - [Manage and share code changes between a remote repository](#manage-and-share-code-changes-between-a-remote-repository)
  - [Commit Format](#commit-format)
  - [Merge via Pull Requests](#merge-via-pull-requests)
- [Graphical User Interface](#graphical-user-interface)

---

---

# Information about project

DataSpark is a team established by METU Informatics Institute Data Informatics and Information Systems graduate students, who are the founders of DSEnergy company. DSEnergy offers artificial intelligence and machine learning solutions to its customers in the energy domain since 2023.

- Scope

A predictive model will be developed to forecast hourly and daily energy consumption in the city of London. The outcomes will be presented through a user-friendly interface featuring interactive visualizations, thus facilitating comprehensive data exploration and interpretation.

- Vision

Empowering energy companies with essential insights to facilitate informed and strategic decision-making, thereby enhancing the quality of their services and enabling more effective planning.

- Dataset Name and Link

    Smart Meters in London

    https://data.london.gov.uk/publisher/uk-power-networks

- Used Machine Learning Models

    1- ARIMA
    2- XGBoost
    3- Prophet (Best Performed)

# Development Guidelines    

This document is prepared for giving necessary information for new developers.

## Environment setup

To perform all of the commands below, on Windows open up a **Anaconda Prompt**, on Linux and MacOS open up a **Terminal**.

### Viewing all available environments

    conda env list

### Creating an environment from scratch

If you just want to create an environment without a specific Python version, run

    conda create --name <env_name>

    conda create --name dataspark_env

If you want to create an environment with a specific Python package and multiple packages , run 

    conda create --name <env_name> python=<version> <package1>=<version> <package2>

    conda create --name dataspark_env python=3.10 scipy=0.17.3 pandas

Note: When conda asks you to proceed, type y.

If there is a readily available environment, packages can be installed with the command below:

    conda install -n <myenv> <package1> <package2>

    conda install -n dataspark_env numpy pandas

### Creating an environment.yml file     

If the team is presently working on the same project on various machines and wants to set up the same Conda environment on another machine, it is crucial to generate a single YML file for the specific environment, which will contain all the packages as well as their versions. 
Follow these steps to achieve that:

1- Activate the environment using 

    conda activate <name_of_environment>

    conda activate dataspark_env
    
2- Then export your active environment to a new file using

    conda env export > environment.yml

Note: This command exports the file to path where the environment is stored.

If you want to export the file to Desktop 

Linux or macOS

    conda env export > ~/Desktop/environment.yml

Windows

    conda env export > C:\Users\YourUsername\Desktop\environment.yml

### Creating an environment from an environment.yml file

1- Create the environment using

    conda env create -f environment.yml

Note: Do not forget to use the full path where the environment.yml file is stored

    conda env create -f C:\Users\User\Desktop\DI502_Poject_Repository\dataspark\environment.yml

2- Activate the new environment using

    conda activate dataspark_env

### Updating an environment

You may need to update your environment for a variety of reasons.

-  A new version of one of your key dependencies has just published.
-  For data analysis, you need an extra package.
-  You no longer require the previous package because you've discovered a superior one.

All you have to do is change the environment's contents if any of these things happen. Run the following command after modifying the yml file as necessary:

    conda activate dataspark_env

    conda env update --file environment.yml  --prune

Note: Do not forget to use the full path where the environment.yml file is stored. An example is given below

    conda env update --file C:\Users\User\Desktop\DI502_Poject_Repository\dataspark\environment.yml --prune

## New branch creation rules

1- For every task in Jira, new branch must be created and all the work should be done in that specific branch.

2- When creating a new branch, type of the branch should be selected.

- Bugfix: To address and fix bugs, issues, or defects in a software project

- Feature: To work on a specific new feature or enhancement for a software project

- Hotfix: To address critical issues or defects in a software project

- Release: To manage the codebase for a specific version or release of a software product

3- New branch must be created from development branch.

4- Branch name should include the task number and name.

    Ex: DS-18-development-environment-creation

## Manage and share code changes between a remote repository

In Git and other version control systems, the expression "first pull then push" is frequently used. To avoid accidentally overwriting or clashing with the work of other contributors, it implies that before pushing your modifications to the remote repository, you should first pull the most recent changes from the repository.

- Pull -> Work on Code -> Push

By ensuring that you are working with the most recent version of the code before making your own additions, this procedure promotes code consistency and avoids conflicts.

## Commit format

[TaskNumber] Brief description of what was done 

    Example: [DS-18] Development guidelines are added

## Merge via pull requests

1- At least 2 reviewers must be added for the pull request.

2- Merge cannot be performed without 2 approvals.

3- While developing the project, merge operation should only be performed for development branch. 

4- When it's time to release, the development branch can be merged into the master branch.

# Graphical User Interface

To reach the GUI of the project use the commands below

1- Activate the related environment

    conda activate <env_name>

    conda activate dataspark_env

2- Run the automation_script.py file 

    python automation_script.py

3- After performing all these commands, the GUI will appear on your local computer's web browser.

It is also possible to reach the project's deployed web page from the link below for further insight.

https://dataspark-6bzw2cpa5a-uc.a.run.app/