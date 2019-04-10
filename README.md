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

`git commit -m "Your Comments For These Change"` Commits the tracked changes and prepares them to be pushed to a remote repository

`git push -u origin YourBranchName` pushes the changes in your local repository up to github

---

**Ignore idea folders**

       $ git rm -r --cached .idea

---


**Merge a branch into master branch**



        on branch development
        $ git merge master #(resolve any merge conflicts if there are any)

        $ git checkout master
        $ git merge development #(there won't be any conflicts now)
        $ git push origin master
        

-------

error "**Please enter a commit message to explain why this merge is necessary**."  



- If you do not want to enter any message for this pull or merge:

  1. press`Esc`.
  
  2. press`:`+`w`+`q` and then press `Enter`.
  
- If you want to enter a message for it:

  1. Press `i`.
  
  2. Input your message.
  
  3. Press`Esc`.
  
  4. press`:`+`w`+`q` and then press `Enter`.
  
----

error "**The following untracked working tree files would be overwritten by checkout**"


        $ git fetch --all

        $ git reset --hard origin/BranchName

-----

error "**Your local changes to the following files would be overwritten by merge**"


        $ git stash

        $ git pull origin master

        $ git stash pop

-----
