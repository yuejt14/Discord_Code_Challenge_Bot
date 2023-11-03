## Discord_Code_Challenge_Bot

### Description:
The `Discord_Code_Challenge_Bot` is a discord bot designed to facilitate code submission to LeetCode and retrieve results. The bot interacts with LeetCode's API and provides feedback on code submission directly through Discord.

### Table of Contents:

- [Discord\_Code\_Challenge\_Bot](#discord_code_challenge_bot)
  - [Description:](#description)
  - [Table of Contents:](#table-of-contents)
  - [File Overview:](#file-overview)
  - [Setup and Installation:](#setup-and-installation)
  - [Usage:](#usage)
  - [Dependencies:](#dependencies)

### File Overview:

- **`./src/leetcode_api.py`**:
  Contains functions to interact with LeetCode's API such as retrieving problem info, submitting code, and checking submission results. Utilizes GraphQL for specific queries.

- **`./src/common.py`**:
  Provides a language mapping utility function to map between different representations of programming languages.

- **`./src/discord_bot.py`**:
  Contains the main Discord bot logic. It listens to commands from users, processes code submissions, and sends results back to the user.

- **`./src/leetcode_client.py`**:
  Defines the `LeetCodeClient` class which serves as a client to interact with LeetCode's API. It provides methods for submitting code, checking results, and handling cookies.

- **`./docker-compose.yml`**:
  Docker Compose configuration file to manage the bot's Docker container.

- **`./README.md`**:
  This current documentation file.

- **`./test/leetcode_client_test.py`**:
  Contains unit tests for the `LeetCodeClient` class.

- **`./test/solutions/two_sum_python_invalid.txt` & `./test/solutions/two_sum_python_valid.txt`**:
  Contains sample solutions for testing the bot.

- **`./Dockerfile`**:
  Dockerfile for building the bot's Docker image.

- **`./requirements.txt`**:
  List of Python package dependencies required for the bot.

### Setup and Installation:

1. **Docker Setup**:
   Ensure you have Docker and Docker Compose installed on your machine.

2. **Environment Variables**:
   Set up the environment variables for the bot. You will need your `DISCORD_TOKEN`, `CSRF_TOKEN`, and `LEETCODE_SESSION`.

3. **Docker Compose**:
   Run the following command to start the bot's Docker container:
   ```
   docker-compose up --build
   ```

### Usage:

1. **Starting the Bot**:
   Once the bot is online, you can interact with it in your Discord server.

2. **Submitting Code**:
   To submit code to LeetCode, use the following format:
   ```
   ```language
   #your code
   ```
   ```

3. **Other Commands**:
   - **`!start`**: Starts the bot.
   - **`!submit`**: Use this command followed by your code to submit to LeetCode.

### Testing:

Tests are located in the `./test/leetcode_client_test.py` file. To run the tests, execute the following command:

```
python -m unittest discover -s test
```

### Dependencies:

- `python-dotenv`: Load environment variables from a `.env` file.
- `discord`: Discord API library for creating bots.
- `requests`: Library for making HTTP requests.

For a full list of dependencies, refer to the `requirements.txt` file.
