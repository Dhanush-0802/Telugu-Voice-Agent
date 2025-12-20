# TELUGU VOICE-BASED GOVERNMENT SCHEME AGENT

->Overview of the project:

This project is a voice based Telugu service agent that helps users indentify their eligible government or public welfare schemes.
This system interacts fully through the language Telugu(voice), collects requireed user information in a step by step process, and recomends a suitable scheme based on eligiblility rules


->Problem Statement:

Many Users are not aware of which government welfare schemes they are eligible for and face difficulties due to language barriers and complex application processes.
This project aims to simplify the process by providing a voice-based Telugu agent and identifies suitable schemes based on their data.

# System Architecture

The system follows a simple voice-based pipeline which is:

USER (TELUGU VOICE)

->Speech Recognition (Telugu)
->Agent Logic(Planner +Memory)
->Tools (Profile Extraction & Eligibility Check)
->Text-to-Speech(Telugu Response)

## Agent Workflow

The agent follows an proper oder or state-based workflow:

1. The agent listens to the user's Telugu voice input.
2. It checks which user details are missing (age, category, income).
3. Based on the missing information, the agent asks the next appropriate question.
4. The agent uses tools to extract details from the user's speech.
5. Extracted information is stored in memory across turns.
6. Once all required details are collected, the agent determines the eligible scheme.
7. The final result is spoken back to the user in Telugu.

## Tools Used

The agent uses multiple tools to complete the task:

**Age Extraction Tool**: This tool Extracts the user's age from Telugu speech.
**Category Detection Tool**: This tool Identifies whether the user is a student, farmer, or senior citizen.
**Income Detection Tool**: This tool Determines income level (low or high).
**Eligibility Decision Tool**: This tool Recommends a government scheme based on collected details.

Each tool in this project is called independently by the agent during the conversation.

## SETUP AND EXECUTION

### Requirements

-> Python 3.10
-> Microphone access
-> Internet connection (for speech recognition and text to speech)

### Installation

pip install -r requirements.txt

## Run the application

python main.py

Press Ctrl + C to stop the application.

This project demonstrates a voice-first, agentic workflow with tool usage, memory, and failure handling in a native Indian language.
