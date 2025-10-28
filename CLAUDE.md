# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a 2-day programming course for journalists ("Programmieren für Journalistinnen und Journalisten"), teaching Python, R, and Svelte through practical, journalism-focused examples. The course materials are structured as interactive Jupyter notebooks with progressive lessons, complemented by practical examples for data journalism tasks like web scraping, data analysis, and interactive visualizations.

The repository contains teaching materials in German.

## Project Structure

### Course Materials (Main Lessons)
The numbered notebooks (00-05) form the core curriculum and should be worked through sequentially:

- `00_gude_welt.ipynb` - Introduction to Colab notebooks and basic Python
- `01_erste_schritte.ipynb` - First steps in Python programming
- `02_python_erweitern.ipynb` - Working with Python libraries
- `03_interaktive_widgets.ipynb` - Interactive applications with ipywidgets
- `04_svelte.ipynb` - Introduction to Svelte JavaScript framework
- `05_python_streamlit.ipynb` - Building an AI chatbot with Streamlit

### Examples Directory (`beispiele/`)
Contains practical journalism examples:
- `scrape.py` - Selenium-based web scraper for DSV competition data (German swimming federation)
- `energieverbrauch.ipynb` - Energy consumption data analysis
- `alkoholrechner.svelte` - Alcohol calculator Svelte component
- `PKS_2023.R` - R script for analyzing German crime statistics (Polizeiliche Kriminalstatistik)

### Svelte Application (`src/`)
Simple Svelte app demonstrating the alcohol calculator:
- Entry point: `src/main.js`
- Main component: `src/App.svelte` (imports `alkoholrechner.svelte`)

## Development Commands

### Python/Jupyter Notebooks
Notebooks are designed for Google Colab or local Jupyter environments:
```bash
# Run notebooks locally with Jupyter
jupyter notebook

# Or use VSCode with Jupyter extension (recommended in course)
code .
```

### Svelte/JavaScript
```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## Technology Stack

### Python Environment
- **Python 3.x** (via Miniconda recommended)
- Key libraries used in examples:
  - `selenium` - Web scraping (with ChromeDriver)
  - `pandas` - Data manipulation
  - `openpyxl` - Excel file handling
  - `ipywidgets` - Interactive notebook widgets
  - `streamlit` - Web app framework

### R Environment
- `tidyr`, `dplyr` - Data manipulation
- `ggplot2` - Visualization
- `openxlsx` - Excel integration
- `stringr` - String operations

### JavaScript/Svelte
- **Svelte 5** (latest version with runes)
- **Vite** - Build tool and dev server
- `@sveltejs/vite-plugin-svelte` - Svelte integration

## Course Context

### Target Audience
Journalists learning to code for data journalism tasks. Course assumes:
- No prior programming experience
- Access to install software (not corporate-locked machines)
- Interest in practical data analysis and visualization

### Teaching Philosophy
- Hands-on, example-driven approach
- Real journalism use cases (crime statistics, energy data, sports data)
- Progressive complexity from "Hello World" to AI chatbots
- Mixed language approach (Python for data, Svelte for interactive web)

### Software Setup (from course materials)
Students are guided to install:
1. **Miniconda** - Python environment manager
2. **VSCode** - Code editor with extensions (Python, Jupyter, Continue)
3. **Ollama** (optional) - Local AI model server
4. **Continue VSCode extension** - AI coding assistant

## Working with Notebooks

Jupyter notebooks in this repo combine:
- **Markdown cells** - Explanatory text, instructions, exercises
- **Code cells** - Executable Python code with outputs
- **Teaching elements** - Deliberate errors for learning (e.g., indentation errors in `01_erste_schritte.ipynb`)

When modifying notebooks:
- Preserve the pedagogical structure and progressive difficulty
- Keep explanations in German
- Maintain the conversational, beginner-friendly tone
- Don't "fix" intentional errors that are teaching examples

## Data Journalism Examples

### Web Scraping Pattern (scrape.py)
The scraping example demonstrates:
- Selenium WebDriver setup with Chrome
- Handling dynamic dropdowns and AJAX content
- Retry logic for stale elements
- Exporting to Excel with pandas

ChromeDriver path is configured for macOS (Homebrew): `/opt/homebrew/bin/chromedriver`

### R Data Analysis Pattern (PKS_2023.R)
Shows typical journalism workflow:
- Reading Excel files with complex headers (starting from specific rows)
- Filtering with regex patterns
- Data transformation and reshaping
- Export for visualization in other tools

### Interactive Components (Svelte)
The alcohol calculator demonstrates a simple but practical interactive journalism tool pattern that can be embedded in articles.

## Notes for Development

- Notebooks are designed to run in Google Colab (see Colab badges in headers)
- The `daten/` directory contains course datasets (not tracked in detail here)
- Git branch: `main` is the primary branch for commits and PRs
- Course materials use CC-BY license (Jan Eggers)

## Common Patterns

When adding new examples or lessons, follow these patterns:
- **Notebooks**: Include Colab badge, CC-BY attribution, German text, progressive difficulty
- **Python examples**: Include docstrings, error handling, pandas for output
- **Svelte components**: Keep simple and focused on journalism use cases
- **Data sources**: Prefer German/European data relevant to journalism students
