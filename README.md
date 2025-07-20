# Personal AI Agent

A personal AI agent project using LangChain and Anthropic's Claude model.

## Setup Instructions

### 1. Install Python Dependencies

Create and activate a virtual environment (recommended):

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
# source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

### 2. Set up Anthropic API Key

You'll need an Anthropic API key to use Claude. You can either:

#### Option A: Set it as an environment variable
```bash
# On Windows:
set ANTHROPIC_API_KEY=your_api_key_here

# On macOS/Linux:
export ANTHROPIC_API_KEY=your_api_key_here
```

#### Option B: Let the notebook prompt you
The notebook will automatically prompt you for your API key if it's not set as an environment variable.

### 3. Run the Jupyter Notebook

Start Jupyter:
```bash
jupyter notebook
```

Then open `main.ipynb` and run the cells.

## Project Structure

- `main.ipynb` - Main notebook with the AI agent implementation
- `requirements.txt` - Python dependencies
- `README.md` - This file

## Getting Your Anthropic API Key

1. Go to [Anthropic Console](https://console.anthropic.com/)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key for use in this project 