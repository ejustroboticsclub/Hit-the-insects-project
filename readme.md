# Hit the Insects Project Repository

This repository hosts the "Hit the Insects" project developed by the EJUST Robotics Club.

## Description

The "Hit the Insects" project involves the development of a software application or game focused on the theme of hitting insects. The project may include elements such as gameplay mechanics, user interfaces, and interaction with hardware devices.

## Contributors

### Mentors:

* [Ahmed Anwar](https://github.com/ahmedanwar123)

### Participants:

* [Abdelrahman Salah](https://github.com/Abdelrahman2610)

## Goals

The goals of the project may include:

* Developing an interactive game application.
* Implementing various gameplay mechanics related to hitting insects using computer vision techniques.
* Enhancing user experience through intuitive user interfaces and engaging gameplay.
## Plan

| Category | Item                        | Quantity |
|----------|-----------------------------|----------|
| Hardware | Web camera                  | 1        |
| Software | Text editor or IDE          | ...      |

## Technical Details
###	System Description
This undertaking entails the implementation of hitting the insect game 


## Python Programming :

Understand fundamental programming concepts and syntax.
Proficiency in writing Python code and utilizing libraries.
Ability to design modular and reusable code.
Intermediate-level knowledge of variables, loops, conditionals, functions, and OOP.

## Computer Vision :

Understanding of core computer vision concepts and techniques.
Familiarity with image manipulation and analysis.
Experience with camera calibration.
Knowledge of feature extraction, object detection, and image processing.

## Debugging Skills (Basic Level):

Ability to interpret and analyze error messages.
Basic knowledge of debugging techniques, like print statements and logging.
Troubleshooting common programming mistakes.


# System Description

This document outlines the implementation of the "Hit the Insect" game with two versions: one utilizing the YOLO object detection model and another using pose estimation with MediaPipe.

## YOLO Model Version:

- In this version, the game utilizes the YOLO object detection model to detect the ball within the game environment.
- The YOLO model identifies the position and size of the ball, allowing players to interact with it within the game.
- The distance between the camera and the ball is calculated based on the detected position, enabling players to accurately hit the ball using in-game tools or methods.

## Contours Version:

- Alternatively, There is another version using the property of HSV values to find contours of the ball.
- After detecting the ball it replicates the click on the screen after specific delay for providing more realistic click.
## Technical Implementation:

- **YOLO Model**:
  - The YOLO object detection model will be integrated into the game using relevant libraries or frameworks, such as OpenCV, to perform real-time object detection.
  - The model's output, including the detected ball's position and size, will be processed within the game logic to enable interaction with the ball.
- **Contours Version**:
  - In an alternative implementation, the game can utilize the property of HSV values to find contours of the ball within the game environment.
  - The game logic will process the detected contours to identify the position and size of the ball, enabling interaction with the ball within the game.
  - After detecting the ball using contours, the game will replicate a click on the screen after a specific delay, providing a more realistic interaction experience for the players.
  - This method offers an alternative approach to ball detection, leveraging color-based segmentation techniques, which can complement the YOLO model version or serve as a standalone implementation depending on the game's       requirements and constraints.
- **Pose Estimation**:
  - Uses MediaPipe for hand detection.
  - Controls mouse movements based on the index finger position with PyAutoGUI.
  - Simulates a mouse click when the index finger approaches certain threshold.
## Game Features:

- **Interactive Gameplay**:
  - Both versions of the game offer interactive gameplay experiences where players can hit virtual insects using either the detected ball (YOLO version) or body movements/gestures (MediaPipe version).
  ## Game Modes:

    - **Single Player Mode**:
      - Players can enjoy the game individually, competing against computer-controlled opponents or challenges.
      - Single-player mode offers a solo gaming experience, allowing players to focus on completing objectives or achieving high scores.

    - **Multiplayer Mode** (will be implemented soon):
      - The game also features a multiplayer mode where multiple players can compete against each other in real-time.
      - Multiplayer mode enables social interaction and competition among players, fostering a dynamic and engaging gaming experience.

## Project Scope:

The project's scope includes the development, testing, and deployment of both versions of the "Hit the Insect" game, leveraging either the YOLO object detection model or pose estimation with MediaPipe. The goal is to provide players with immersive and entertaining gameplay experiences while showcasing the team's proficiency in integrating advanced computer vision techniques into game development.
