# Meridio - File Hosting Social Media(July 2017)
Meridio is a filehosting and filesharing platform with an inbuilt messaging/chatting application.
### Meridio - A Walkthrough
Merídio(<i>Greek</i>-Share) is a free Filehosting platform where users can host their own repositories of files/videos/images etc and thus make it available for download by any of the registered members of the website.The key aim is to create a network of users who can host items in their repositories and allow other people to access the repository contents and also download stuff from others repositories.Merídio also has an inbuilt chat feature where you can add friends via requests and chat with your friends.
### Signup and Login Page
Meridio prompts you for some user details for sign up. These are the starting steps in the creation of a user profile.
![screenshot from 2017-07-24 01-20-38](https://user-images.githubusercontent.com/24290847/28502475-bbe403d0-6fe2-11e7-88cb-8528037659d6.png)
Once the user signs up they can login and use the features as when they like.If the user doesnt remember their password forgot password prompts a new system generated password to be sent to the user on their registered email.
![imgonline-com-ua-twotoone-xtomipaxzyn](https://user-images.githubusercontent.com/24290847/28502477-c40fbe50-6fe2-11e7-8f32-8f312cc2124c.jpg)
### Profile Page
The profile page has 4 navigational tabs which allow the user to switch between managing their personal info, managing their network of friends and managing the files that they have uploaded to their repositories.
##### Personal Information
This interface allows the user to modify their profile information and their avatar.
![screenshot from 2017-07-24 01-21-46](https://user-images.githubusercontent.com/24290847/28502520-972e8b18-6fe3-11e7-8617-979a13d33239.png)
##### Uploading files to repository and removing current files
User can use the Materials tab to upload files to the repository using the Share button. This interface also consists of a list of the files currently hosted.The user can remove any file required by using the remove button(remove button not visible in the photo illustration)
![materials](https://user-images.githubusercontent.com/24290847/28502541-dbc26362-6fe3-11e7-8a51-3a9191d70858.png)
##### Managing friend requests sent and recieved
The Request tab allows the user to view all the incoming friend requests and sent friend requests and manage these requests.
![screenshot from 2017-07-24 01-22-20](https://user-images.githubusercontent.com/24290847/28502538-d7875da2-6fe3-11e7-9108-ae3ff4e764a9.png)
##### View all Friends
The last tab of the profile section the Network tab allows the user to see all of their current friends.
![screenshot from 2017-07-24 01-22-25](https://user-images.githubusercontent.com/24290847/28502540-d8c612b2-6fe3-11e7-8cad-f165713f0bd1.png)
### Ping:The Meridio Chat Application
On the top navigation panel the Ping tab takes the user to the chat application where the user can. The user can chat with any friend and the most recent chats are pulled to the top automatically. The search bar allows the user to search any of their networks.The search returns a list of closely matched usernames among the user's current networks.
![screenshot from 2017-07-24 01-23-29](https://user-images.githubusercontent.com/24290847/28502622-c1018ee8-6fe5-11e7-8d55-d5dee9570faa.png)
### The Sharing Zone and Repository Structure
The sharing zone contains all the repositories present on the website.The user can click on any of the repositories or use the go to panel to directly go to any repository.
![screenshot from 2017-07-24 01-23-38](https://user-images.githubusercontent.com/24290847/28502623-c3241628-6fe5-11e7-8c89-99545f0aca35.png)
#### Repository internal structure
Each repository has a list of all the files uploaded by the owner of that repository along with information such as the total number of downloads and views tagged along with each file. Each file list element has a preview and a download button. The preview button directs the user to a new page where the preview of the file(music,images,pdfs,vidoes etc) is generated. The download button downloads that file.
![screenshot from 2017-07-24 01-24-04](https://user-images.githubusercontent.com/24290847/28502625-c4e00d50-6fe5-11e7-8921-c09f4a93d53d.png)
Each repository also has a button Send Request to send a friend request from the user to the owner of the repository the user is currently browsing.
![screenshot from 2017-07-24 01-24-26](https://user-images.githubusercontent.com/24290847/28502626-c651de16-6fe5-11e7-9c80-494b02c50fe5.png)
<br><br>
Thats about it all to get you started with meridio,the free file hosting social media.
### Technologies used
1. Django Framework<br>
2. Bootstrap<br>
3. Python<br>
4. JavaScript/JQuery<br>
### Libraries Used
1. Bootstrap<br>
2. Typed.js and animate.css for animations<br>
### How to contribute?
#### Cloning the repo
* Go to the repository you want to clone and click on fork.
* Copy the URL from your forked repo by going to the 'Clone and Download' option.
* Run git/terminal and execute the follwing to clone the repository to your local machine and navigate to the project folder
 ```sh
 $ git clone <THE COPIED URL>
 $ cd <PATH TO THE PROJECT>
 ```
 #### Adding ,Deleting and Editing files
 * Make the necessary changes to project folder. You can add files to the directory and can also edit/delete existing files.
 * Add the files edited/added using the add command
 ```sh
 $ git add <Name of file added/edited>
 ```
 * You can also add all files in a single go by using
 ```sh
 $ git add .
 ``` 
 * You can verify that your files will be added when you commit by checking the status of the current stage
 ```sh
 $ git status
 ```
 * We are ready to commit. Note that the commit action only commits to your local repository.
 ```sh
 $ git commit -m "MESSAGE you want"
 ```
 * Now we are ready to push
```sh
 $ git push <Remote Repositor eg. Origin> <BRANCH eg. master>
 ```
 
 #### Creating a pull request
 * On GitHub, navigate to the main page of the repository.
 * To the right of the Branch menu, click New pull request.
 * On the next page, click compare across forks.
 * Type a title and description for your pull request.
 * Click Create pull request.<br>
   Now you are done.Happy Contribution!!!
### Installation guide
#### Cloning the repo
* Run git/terminal and execute the follwing to clone the repository to your local machine and navigate to the project folder
 ```sh
 $ git clone https://github.com/NJACKWinterOfCode/Meridio.git
 $ cd Meridio
 ```
 #### Installing and activating virtual environment
* Install local environment on your local machine by typing the following in terminal/command prompt
 ```sh
 $ pip install virtualenv
 ```
 ###### Activation of virtual environment on Windows
 * In command prompt type the following to activate the virtual environment
```sh
 $ mkvirtualenv my_project
 ```
 * If you restart the command prompt to run virtual environment again type
```sh
 $ workon my_project
 ```
 ###### Activation of virtual environment on linux/Mac
 * Create a virtual environment for a project
 ```sh
 $ cd my_project_folder
 $ virtualenv my_project
 ```
 * To begin the virtual environment activate it using the following command
 ```sh
 $ source my_project/bin/activate
 ```
#### Install Dependencies
* To install files required to run the project execute the following command
 ```sh
$ pip install -r requirements.txt 
 ```
#### Run the project
* To run the project finally type
 ```sh
$ python manage.py runserver
 ```
 You are done.Cheers!!!

 
