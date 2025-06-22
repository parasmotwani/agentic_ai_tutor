# Agentic AI Tutor

A multi-agent AI tutor system built with FastAPI that specializes in answering math and physics questions. The system uses Google's Gemini API for intelligent question classification and response generation.

## Architecture

The system follows a modular agent-based architecture:

- **TutorAgent**: Main orchestrator that classifies questions using LLM intelligence and routes to specialized agents
- **MathAgent**: Handles mathematical questions and calculations
- **PhysicsAgent**: Handles physics concepts, constants, and calculations
- **Gemini API**: Provides intelligent question classification and complex reasoning

## Features

- Intelligent question classification using LLM
- Specialized agents for math and physics
- Physics constants lookup tool
- Modern web interface
- RESTful API endpoints
- Deployment-ready for serverless platforms

## Local Setup

### Prerequisites

- Python 3.8+
- Gemini API key from Google AI Studio

### Installation

1. Clone the repository:
```bash
git clone https://github.com/parasmotwani/agentic_ai_tutor.git
cd agentic_ai_tutor
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp env.example .env
```

Edit `.env` and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

5. Run the application:
```bash
uvicorn main:app --reload
```

The application will be available at `http://localhost:8000`

## API Endpoints

- `GET /` - Web interface
- `POST /ask` - Ask a question (JSON)
- `POST /ask-form` - Ask a question (form data)
- `GET /health` - Health check

## Usage Examples

### Math Questions
- "What is 2 + 3?"
- "Calculate 15 * 7"
- "Solve the equation x² + 5x + 6 = 0"

### Physics Questions
- "What is Planck's constant?"
- "What is the speed of light?"
- "Explain quantum mechanics"

## Deployment

### Vercel Deployment

1. Install Vercel CLI:
```bash
npm i -g vercel
```

2. Deploy:
```bash
vercel
```

### Railway Deployment

1. Connect your GitHub repository to Railway
2. Set environment variables in Railway dashboard
3. Deploy automatically on push

## Development

The project structure:
```
ai_tutor_agent/
├── agents/          # Agent implementations
├── services/        # External service clients
├── tools/           # Specialized tools
├── static/          # Web interface
├── main.py          # FastAPI application
└── requirements.txt # Dependencies
```

## Challenges and Solutions

- **Question Classification**: Replaced rigid keyword matching with LLM-based classification for better accuracy
- **Error Handling**: Implemented robust error handling for API failures
- **Security**: Removed direct math expression evaluation for security
- **Modularity**: Designed agents as independent modules for easy extension

## License

MIT License - see LICENSE file for details.

## Live Application

[Deployed Application](https://your-deployment-url)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

--- 