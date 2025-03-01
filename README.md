## Sample Gemini Chatbot

Visit [Google AI Studio (Text)](https://makersuite.google.com/app/apikey) to get your API keys.

**To use this code, follow the steps below:**

1.  **Create a virtual environment:** Open your terminal and run the following command:

    ```bash
    python -m venv venv
    ```

2.  **Activate the virtual environment:**  Run the appropriate command for your operating system:

    *   **Windows:**

        ```bash
        venv\Scripts\Activate
        ```

    *   **macOS/Linux:**

        ```bash
        source venv/bin/activate
        ```

3.  **Install dependencies:**  Use pip to install the required packages. Make sure you have a `requirements.txt` file.  Run the following command in your terminal:

    ```bash
    pip install -r requirements.txt
    ```

    *(If you don't have a `requirements.txt` file, you'll need to create one listing the necessary packages.  Likely this will include `streamlit` and `google-generativeai` at a minimum.)*

4.  **Create a `.env` file:** In the same directory as your Python script, create a file named `.env`.  Add your Gemini API key to this file in the following format:

    ```
    GEMINI_API_KEY="YOUR_API_KEY_HERE"
    ```

    *   **Important:** Replace `YOUR_API_KEY_HERE` with your actual Gemini API key.  **Do not commit this file to version control (e.g., Git)** as it contains sensitive information.  Add `.env` to your `.gitignore` file.

5.  **Run the application:**  Use Streamlit to run your Python script.  Replace `<file_name.py>` with the actual name of your Python file.

    ```bash
    streamlit run <file_name.py>
    ```

That's it! You've created your first chatbot using Gemini.

Happy learning!
