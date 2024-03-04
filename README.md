# Flashy: A Language Learning Flashcard App

Flashy is a Python-based application designed to aid in language learning through the use of flashcards. Built with Tkinter for the GUI, it provides a visually appealing and interactive way to memorize and recall words in different languages.

## Features

- **Dynamic Flashcard Display**: Showcases words in the language being learned on the front, with translations on the back.
- **Random Word Selection**: Randomly selects words from a dataset, ensuring a varied learning experience.
- **Automated Card Flipping**: Automatically flips the card after a set interval to reveal the translation.
- **Progress Tracking**: Allows users to mark words as known, updating the dataset to focus on words yet to be learned.

## Setup

### Prerequisites

- Python 3.x
- Pandas library
- Tkinter library (usually comes with Python)

### Installation

1. Clone this repository or download the files.
2. Ensure you have the required dependencies:
   ```bash
   pip install pandas
   ```

### Data Files

- `french_words.csv`: Default dataset containing French words and their English translations.
- `words_to_learn.csv`: Dynamically updated dataset with words the user is still learning.

## Usage

Start the application by running:

```bash
python main.py
```

- Click 'Next' to display a new word.
- If you know the word displayed, click 'Known' to remove it from the learning list.
- The application automatically flips the card after 3 seconds to reveal the translation.

## Contributing

Contributions to improve Flashy or add new features are welcome. Feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.