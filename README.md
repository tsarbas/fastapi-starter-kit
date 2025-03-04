# FastAPI Starter Kit

A modern FastAPI starter kit with MongoDB integration, comprehensive testing, and best practices for Python development.

## Features

- 🚀 [FastAPI](https://fastapi.tiangolo.com/) for high-performance API development
- 🗃️ [MongoDB](https://www.mongodb.com/) with async support via [Motor](https://motor.readthedocs.io/)
- ✨ Modern Python with type hints and async/await
- 🧪 Testing setup with pytest and async support
- 🛠️ Development tools:
  - Black for code formatting
  - Ruff for fast linting
  - MyPy for static type checking
  - Pre-commit hooks for code quality

## Requirements

- Python 3.12+
- MongoDB 4.0+
- Make (optional, but recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/fastapi-starter-kit.git
cd fastapi-starter-kit
```

2. Install dependencies:
```bash
make install
```

This will:
- Install Python dependencies
- Set up pre-commit hooks

## Development

### Running the Application

Start the development server:
```bash
make run
```

The API will be available at:
- API: http://localhost:8000
- Documentation: http://localhost:8000/api/docs
- ReDoc: http://localhost:8000/api/redoc

### Development Commands

- Format code:
```bash
make format
```

- Run linting:
```bash
make lint
```

- Run tests:
```bash
make test
```

- Run all pre-commit hooks:
```bash
make pre-commit
```

### Docker Support

Start services with Docker:
```bash
make docker-up
```

Stop services:
```bash
make docker-down
```

## Project Structure

```
app/
├── config/          # Configuration modules
│   ├── database.py  # Database configuration
│   └── settings.py  # Application settings
├── features/        # Business logic and domain models
├── integrations/    # External service integrations
├── interfaces/      # Interface adapters
│   └── http/       # HTTP interface (FastAPI routes)
├── schemas/         # Pydantic models and schemas
└── main.py         # Application entry point

tests/              # Test suite
├── conftest.py     # Test configuration and fixtures
└── test_*.py       # Test modules
```

## Testing

The project uses pytest for testing. Run the test suite:

```bash
make test
```

## Code Quality

The project uses several tools to maintain code quality:

- **Black**: Code formatting
- **Ruff**: Fast Python linting
- **MyPy**: Static type checking
- **Pre-commit**: Git hooks for code quality

These checks run automatically on commit, but you can run them manually:

```bash
# Format code
make format

# Run linting
make lint

# Run all checks
make pre-commit
```

## Environment Variables

Create a `.env` file in the root directory:

```env
# Project settings
PROJECT_NAME=FastAPI Starter Kit
VERSION=1.0.0
DESCRIPTION=A modern FastAPI starter kit with best practices

# MongoDB settings
MONGODB_URL=mongodb://localhost:27017
MONGODB_DB_NAME=fastapi_starter

# CORS settings
CORS_ORIGINS=["*"]
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.