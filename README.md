# autoloadsystem
## Environment

 `conda create -n env_name python=3.5` create virtual environment by anaconda
 
`conda install -c anaconda mysql-connector-python`

 `activate your_env_name` 
 
 `pip install Django` install Django
 


create our project using pyCharm
 pyCharm->new project->django->existing interpreter->"../anaconda3/env/ env_name/python.exe"

## Git
some git we may use:

`git init`

`git config --global user.name "yourname"`

`git config --global user.email "youremail"`

`git config --global github.user $YOUR_USERNAME$`

`git config --global github.token $YOURTOKEN$` you can find token https://github.com/settings/tokens

`git clone git@github.com:Gdreamlend/autoloadsystem.git`

After we pull the code in our own computer, we can create our own branch in local by excute the code:

`git checkout -b $your name$`

If you make some change to our code, and you have test it in your local environment, you want to push your code to github, the following code can help:

`git add .` add the changed files to repo

`git commit -m $your comments for these change$` Commits the tracked changes and prepares them to be pushed to a remote repository

`git push -u origin $your banch name$` pushes the changes in your local repository up to github

