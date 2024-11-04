# Technical specification
1. MapGeneration

2. Authors:
    - Team Lead: Lokhmatova Alya Alekseevna
    - Project Developer: Lokhmatova Alya Alekseevna
    - Teacher: Anatolyev Alexey Vladimirovich
3. Description:
    - What will the program do?
        > The program will provide the user with the opportunity to create flat map of some game world.
          The user will be able to choose colors of the map, its size and file extension in case he wants to save it.
    - Program start:
        > The program will start with Cargo help, I think.
    - Necessary forms:
        > The program will need only form of the main menu and a form for interaction with database.
    - Dialogue windows:
        > Window of map settings

        > Window for result

        > Exit asking window
    - Data Base:
        > A database will be used
for saving all generated pics, so the user will be able to get any of generated (or saved if db will be at users
computer).
    - DB size:
        > As the bd will contain pictures, its size can be seriously big after some time of using program.
    - Exiting the program:
        > Program will finish when the user will close it. Will be shown a small dialogue window that asks if the user really want to close the program.

4. Project Description:
    - On the start the user see a window of settings for map. it contains choosing colors, map size, and other. If some input is incorrect, the program will let the user know.
    - Then, after pushing the result button, the user will be shown a new window with the ready picture. In case of emergency, the program will let user know that in previous window. A new one won't be created
    - After pushing the result button the picture will be saved to a DB and if the user wants to see it again he needs just write its name again in a specific pole.
5. Program code plan:
    - logic part - the part of pic generation (currently done)
    - part of form processing. also needs to communicate with logic part
    - part of database
    - part of controlling windows
    - Modules:
      1. PIL
      2. PyQt6 (suddenly)
      3. Random
    - functions:
      1. for summarizing
      2. for randomizing points
    - coming later...
6. Graphical interface:
    - the size of settings window is 900x400. on the left will be color choosing, on the right top will be pic size and name. on the right bottom will be db workspace
7. Deadlines:
    - October 20 - finish forms
    - October 27 - finish part of form processing
    - November 5 - database done
    - November 13 - finish all